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

def format_card_label(card):
    return card[0]
    
# Streamlit app
st.set_page_config(page_title="AI", layout="wide")
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

st.title("AI")

uploaded_files = st.file_uploader("Upload YAML Files", type="yaml", accept_multiple_files=True)
# project_files = st.file_uploader("Upload Project Files", type="yaml", accept_multiple_files=True)

cards = {"project_file": None, "data_files": [], "model_files": []}

if uploaded_files:

    for uploaded_file in uploaded_files:
        cc = load_yaml(uploaded_file.name)
        card_type = cc['card_details'].get('card_type', '').lower()
        if card_type == 'project':
            cards["project_file"] = cc
        elif card_type == 'data':
            cards["data_files"].append((cc['card_details']['card_label'], cc))
        elif card_type == 'model':
            cards["model_files"].append((cc['card_details']['card_label'], cc))

project_col, data_col, model_col = st.columns(3)

with project_col:
    st.title("Project CC")
    
    if cards["project_file"]:
        project_cc = cards["project_file"]
   
        for section, items in project_cc.items():
            if section != 'card_details':
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
        # st.write("Updated Data:", project_cc)
                
        updated_project_cc = yaml.dump(project_cc, sort_keys=False)
        
        st.download_button(
            label=f"Download Updated Project CC as YAML",
            data=updated_project_cc,
            file_name="updated_project.yaml",
            mime="text/yaml"
        )  

with data_col:

    st.title("Data CC")
    if cards['data_files']:
        # selected_data_file = st.selectbox("Select a Data CC", cards['data_files'], format_func=format_card_label)
        # data_cc = selected_data_file[1]
        for card in cards['data_files']:
            data_cc = card[1]
            st.title(f"{card[0]}")
            for section, items in data_cc.items():
                if section != 'card_details':
                    st.header(section.replace('_', ' ').title())  # section header
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
                    st.divider()
            # st.write("Updated Data:", data_cc)
        
            data_cc_yaml_data = yaml.dump(data_cc, sort_keys=False)

            st.download_button(
                label=f"Download Updated {card[0]} CC as YAML",
                data=data_cc_yaml_data,
                file_name="updated_data.yaml",
                mime="text/yaml"
            )

with model_col:
            
    st.title("Model CC")
    if cards['model_files']:
        # selected_data_file = st.selectbox("Select a Modle CC", cards['model_files'], format_func=format_card_label)
        # model_cc = selected_data_file[1]
        for card in cards['model_files']:
            model_cc = card[1]
            st.title(f"{card[0]}")        
            for section, items in model_cc.items():
                if section != 'card_details':
                    st.header(section.replace('_', ' ').title())  # section header
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
                    st.divider()
            # st.write("Updated Data:", model_cc)
        
            model_cc_yaml_data = yaml.dump(model_cc, sort_keys=False)

            st.download_button(
                label=f"Download Updated {card[0]} CC as YAML",
                data=model_cc_yaml_data,
                file_name="updated_model.yaml",
                mime="text/yaml"
            )

# # #         # json_data = json.dumps(data, indent=2)
# # #         # st.download_button(
# # #         #     label="Download Updated Data as JSON",
# # #         #     data=json_data,
# # #         #     file_name="updated_data.json",
# # #         #     mime="application/json"
# # #         # )   

if st.button(f"Run Analysis"):
    results = compliance_analysis(cards)
    st.write("Analysis Results", results)