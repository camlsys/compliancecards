import os
import yaml
import json
from pathlib import Path
import streamlit as st
from compliance_analysis import check_overall_compliance_ui

def compliance_analysis(cards):
    dispositive_variables = check_overall_compliance_ui(cards)
    return dispositive_variables

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def load_yaml_files_from_directory(directory_path):
    yaml_files = []
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.yaml'):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, 'r') as file:
                yaml_files.append(yaml.safe_load(file))
    return yaml_files

directories = {
    'None': './examples',
    'Template': './examples/cc_templates',
    'Example Compliant Project ': './examples/compliant_project',
    'Example Non-Compliant Project ': './examples/non-compliant_project'
}

def format_card_label(card):
    return card[0]
    
# Streamlit app
st.set_page_config(page_title="Compliance Cards", layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 600px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 600px;
        margin-left: -400px;
    }
     
    """,
    unsafe_allow_html=True,
)

st.subheader(":flag-eu: AI _ACTCELERATE_ :scales: :rocket:")
st.header("Compliance Cards")

selected_example = st.selectbox("Select an example project", list(directories.keys()))
uploaded_files = st.file_uploader("or upload Compliance Cards", type="yaml", accept_multiple_files=True)

cards = {"project_file": None, "data_files": [], "model_files": []}

if selected_example:
    directory_path = directories[selected_example]
    yaml_files = load_yaml_files_from_directory(directory_path)
    
    for cc in yaml_files:
        card_type = cc['card_details'].get('card_type', '').lower()
        
        if card_type == 'project':
            cards["project_file"] = cc
        elif card_type == 'data':
            cards["data_files"].append((cc['card_details']['card_label'], cc))
        elif card_type == 'model':
            cards["model_files"].append((cc['card_details']['card_label'], cc))

if uploaded_files:
    for uploaded_file in uploaded_files:
        cc = yaml.safe_load(uploaded_file)
        card_type = cc['card_details'].get('card_type', '').lower()

        if card_type == 'project':
            cards["project_file"] = cc
        elif card_type == 'data':
            cards["data_files"].append((cc['card_details']['card_label'], cc))
        elif card_type == 'model':
            cards["model_files"].append((cc['card_details']['card_label'], cc))

project_col, data_col, model_col = st.columns(3)

with project_col:
    st.title("Project Card")
    
    if cards["project_file"]:
        project_cc = cards["project_file"]
        with st.expander("project details"):
            for section, items in project_cc.items():
                if section == 'card_details':
                    items['card_label'] = st.text_input("card_label", value=items['card_label'])
                if section != 'card_details':
                    st.header(section.replace('_', ' ').title(), divider=True)  # section header
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
                    # st.divider()
            # st.write("Updated Data:", project_cc)
                    
            updated_project_cc = yaml.dump(project_cc, sort_keys=False)
            
        st.download_button(
            label=f"Download updated Project CC as YAML",
            data=updated_project_cc,
            file_name="updated_project.yaml",
            mime="text/yaml",
            use_container_width = True
            )  
    else:
        st.write("Missing project file")

with data_col:

    st.title("Data Card")
    # if st.button(f"Add Data Card"):
    #     cc = load_yaml('./examples/cc_templates/data_cc.yaml')
    #     print(cc)
    #     card_type = cc['card_details'].get('card_type', '').lower()
    #     cards["data_files"].append((cc['card_details']['card_label'], cc))
        
    if cards['data_files']:
        for card in cards['data_files']:
            data_cc = card[1]
            with st.expander(f"{card[0]}"):
                for section, items in data_cc.items():
                    if section == 'card_details':
                        items['card_label'] = st.text_input('card_label', value=items['card_label'], key=f"data_{card[0]}_{key}")
                    if section != 'card_details':
                        st.header(section.replace('_', ' ').title(), divider=True)  # section header
                        for key, details in items.items():
                            if 'verbose' in details and 'value' in details:
                                st.subheader(key.replace('_', ' ').title())  # section header
                                # details['value'] = st.checkbox(details['verbose'], value=details['value'])
                                if isinstance(details['value'], str):
                                    details['value'] = st.text_input(details['verbose'], value=details['value'], key=f"data_{card[0]}_{key}")
                                elif isinstance(details['value'], bool):                                
                                    details['value'] = st.checkbox(details['verbose'], value=details['value'], key=f"data_{card[0]}_{details}_{key}")                        
                            if 'verbose' not in details and 'value' not in details:
                                st.subheader(key.replace('_', ' ').title())  # section header
                                for key, details in details.items():
                                    st.subheader(key.replace('_', ' ').title())  # section header
                                    details['value'] = st.checkbox(details['verbose'], value=details['value'], key=f"data_{card[0]}_{details}_{key}")
                                st.divider()
                        # st.divider()
                # st.write("Updated Data:", data_cc)
            
                data_cc_yaml_data = yaml.dump(data_cc, sort_keys=False)

            st.download_button(
                label=f"Download updated {card[0]} CC as YAML",
                data=data_cc_yaml_data,
                file_name=f"updated_{card[0]}.yaml",
                mime="text/yaml",
                use_container_width = True
                )
    else:
        st.write("Missing data file")

with model_col:
            
    st.title("Model Card")
    if cards['model_files']:
        for card in cards['model_files']:
            model_cc = card[1]
            with st.expander(f"{card[0]}"):       
                for section, items in model_cc.items():
                    if section == 'card_details':
                        items['card_label'] = st.text_input('card_label', value=items['card_label'], key=f"data_{card[0]}_{key}")
                    if section != 'card_details':
                        st.header(section.replace('_', ' ').title(), divider=True)  # section header
                        for key, details in items.items():
                            if 'verbose' in details and 'value' in details:
                                st.subheader(key.replace('_', ' ').title())  # section header
                                # details['value'] = st.checkbox(details['verbose'], value=details['value'])
                                if isinstance(details['value'], str):
                                    details['value'] = st.text_input(details['verbose'], value=details['value'], key=f"model_{card[0]}_{key}")
                                elif isinstance(details['value'], bool):
                                    details['value'] = st.checkbox(details['verbose'], value=details['value'], key=f"model_{card[0]}_{details}_{key}")                        
                            if 'verbose' not in details and 'value' not in details:
                                st.subheader(key.replace('_', ' ').title())  # section header
                                for key, details in details.items():
                                    st.subheader(key.replace('_', ' ').title())  # section header
                                    details['value'] = st.checkbox(details['verbose'], value=details['value'], key=f"model_{card[0]}_{details}_{key}")
                                st.divider()
                        # st.divider()
                # st.write("Updated Data:", model_cc)
            
                model_cc_yaml_data = yaml.dump(model_cc, sort_keys=False)

            st.download_button(
                label=f"Download updated {card[0]} CC as YAML",
                data=model_cc_yaml_data,
                file_name=f"updated_{card[0]}.yaml",
                mime="text/yaml",
                use_container_width = True
                )
    else:
        st.write("Missing data file")

# # #         # json_data = json.dumps(data, indent=2)
# # #         # st.download_button(
# # #         #     label="Download Updated Data as JSON",
# # #         #     data=json_data,
# # #         #     file_name="updated_data.json",
# # #         #     mime="application/json"
# # #         # )   

if st.button(f"Run Analysis"):
    results = compliance_analysis(cards)
    st.write("Analysis Results:", results)
