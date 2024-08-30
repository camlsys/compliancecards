import os
import gradio as gr
import yaml
import json
from pathlib import Path
from compliance_analysis import check_overall_compliance

# def process_files(files):
#     results = []
#     for file in files:
#         with open(file.name, 'r') as f:
#             content = f.read()
#         if Path(file.name).name == "project_cc.yaml":
#             project_cc_yaml = yaml.safe_load(content)
#             msg = run_compliance_analysis_on_project(project_cc_yaml)
#             results.append(msg)            
#         # if Path(file.name).name == "data_cc.yaml":
#         #     data_cc_yaml = yaml.safe_load(content)
#         #     msg = run_compliance_analysis_on_data(data_cc_yaml)
#         #     results.append(msg)        
#         # if Path(file.name).name == "model_cc.yaml":
#         #     model_cc_yaml = yaml.safe_load(content)
#         #     msg = run_compliance_analysis_on_model(model_cc_yaml)
#         #     results.append(msg)
            
#     return results

# def extract_properties(files):
#     for file in files:
#         with open(file.name, 'r') as f:    
#             content = f.read()
#             project_cc_yaml = yaml.safe_load(content)
#         project_cc = [key for key in project_cc_yaml]
#     return project_cc

# def sentence_builder(countries):
#     return f"{countries}"

# # # Gradio interface
# with gr.Blocks() as demo:
#     file_input = gr.File(label="Upload Files", file_count="multiple")
#     output = gr.Textbox(label="Output", lines=10)

#     submit_button = gr.Button("Process Files")
#     submit_button.click(process_files, inputs=file_input, outputs=output)

#     # Create the CheckboxGroup (initially empty)
#     checkbox_group = gr.CheckboxGroup(choices=[], label="", interactive=True)
    
#     # Create the output Textbox
#     output = gr.Textbox()

#     # Function to update the CheckboxGroup when files are uploaded
#     def update_checkboxes(files):
#         choices = extract_properties(files)
#         return gr.CheckboxGroup(choices=choices, label="", interactive=True)
    
#     # Create a Button to trigger the sentence builder
#     submit_button = gr.Button("Submit")

#     # Set up the interaction for file input and updating checkboxes
#     file_input.change(update_checkboxes, inputs=file_input, outputs=checkbox_group)
    
#     gr.CheckboxGroup.change(update_checkboxes)
    
#     output = gr.Textbox()
#     submit_button = gr.Button("Submit")
#     submit_button.click(sentence_builder, inputs=checkbox_group, outputs=output)


# if __name__ == "__main__":
#     demo.launch()

import streamlit as st
import yaml
from pathlib import Path
import pandas as pd


def load_data(files):
    cards = []
    for file in files:
        content = file.read().decode("utf-8")
        if Path(file.name).name == "project_cc.yaml":
            project_cc_yaml = yaml.safe_load(content)
            data = project_cc_yaml
            card_type = "project"
            cards.append((card_type, data))
        if Path(file.name).name == "data_cc.yaml":
            data_cc_yaml = yaml.safe_load(content)
            data = data_cc_yaml
            card_type = "data"
            cards.append((card_type, data))
        if Path(file.name).name == "model_cc.yaml":
            model_cc_yaml = yaml.safe_load(content)
            data = model_cc_yaml
            card_type = "model"
            cards.append((card_type, data))
    return cards

# def process_files(files):
#     results = []
#     for file in files:
#         content = file.read().decode("utf-8")
#         if Path(file.name).name == "project_cc.yaml":
#             project_cc_yaml = yaml.safe_load(content)
#             if project_cc_yaml:
#                 msg = run_compliance_analysis_on_project(project_cc_yaml)
#                 results.append(msg)            
#     return results

# def process_files(data):
#     results = []
#     msg = run_compliance_analysis_on_project(yaml.safe_load(data))
#     results.append(msg)            
#     return results

# def extract_properties(data):
        
#     flattened_data = []

#     for category, items in data.items():
#         for item, attributes in items.items():
#             flattened_data.append({
#                 "Category": category,
#                 "Item": item,
#                 "Verbose": attributes["verbose"],
#                 "Value": attributes["value"]
#             })
#     df = pd.DataFrame(flattened_data)
    
#     return df

def gather_cards(files):
    cards = {}
    cards['project_file'] = ''
    cards['data_files'] = []
    cards['model_files'] = []
    for file in files:
        file_path = os.path.join('/tmp', file.name)        
        with open(file_path, 'wb') as f:
            f.write(file.getbuffer())
        with open(file_path, 'r') as file_path:
            content = yaml.safe_load(file_path.read())            
            if content['card_type'] == 'project':
                cards['project_file'] = file_path.name
            if content['card_type'] == "data":
                cards['data_files'].append(file_path.name)
            if content['card_type'] == "model":
                cards['model_files'].append(file_path.name)
    return cards

def compliance_analysis(cards):
    results = []
    dispositive_variables = check_overall_compliance(cards)
    results.append(dispositive_variables)#['msg'])
    return results

# Streamlit app
# st.set_page_config(page_title="AI", layout="wide")
# st.markdown(
#     """
#     <style>
#     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
#         width: 600px;
#     }
#     [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
#         width: 600px;
#         margin-left: -400px;
#     }
     
#     """,
#     unsafe_allow_html=True,
# )

st.title("AI")

uploaded_files = st.file_uploader("Upload YAML Files", type="yaml", accept_multiple_files=True)
# project_files = st.file_uploader("Upload Project Files", type="yaml", accept_multiple_files=True)

if uploaded_files:

    cards = load_data(uploaded_files)
    for card in cards:
        
        data = card[1]
    
        if data != None:    

            st.title("Compliance Checkboxes")
            st.title(f"{card[0]}")

            for section, items in data.items():
                if section != 'card_type':
                    st.header(section.replace('_', ' ').title())  # section header
                    for key, details in items.items():
                        if 'verbose' in details and 'value' in details:
                            st.subheader(key.replace('_', ' ').title())  # section header
                            # details['value'] = st.checkbox(details['verbose'], value=details['value'])
                            if isinstance(details['value'], str):
                                details['value'] = st.text_input(details['verbose'], value=details['value'])
                            elif isinstance(details['value'], bool):
                                details['value'] = st.checkbox(details['verbose'], value=details['value'])                        
                        if 'verbose' not in details and 'value' not in details:
                            st.subheader(key.replace('_', ' ').title())  # section header
                            for key, details in details.items():
                                st.subheader(key.replace('_', ' ').title())  # section header
                                details['value'] = st.checkbox(details['verbose'], value=details['value'])
                            st.divider()
                    st.divider()
            # st.write("Updated Data:", data)
           
            yaml_data = yaml.dump(data, sort_keys=False)

            # st.download_button(
            #     label=f"Download Updated Data as YAML{card[0]}",
            #     data=yaml_data,
            #     file_name="updated_data.yaml",
            #     mime="text/yaml"
            # )

            # json_data = json.dumps(data, indent=2)
            # st.download_button(
            #     label="Download Updated Data as JSON",
            #     data=json_data,
            #     file_name="updated_data.json",
            #     mime="application/json"
            # )   

    cards = gather_cards(uploaded_files)    
    if st.button(f"Run Analysis"):
        results = compliance_analysis(cards)    
        # st.text_area("Analysis Results", value=json.dumps(results, indent=4), height=600)
        st.write("Analysis Results", results)