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

def generate_unique_key(base_label):
    if base_label == 'data':
        st.session_state.data_key_counter += 1
        return f"{base_label}_0{st.session_state.data_key_counter}"
    if base_label == 'model':
        st.session_state.model_key_counter += 1        
        return f"{base_label}_0{st.session_state.model_key_counter}"

directories = {
    'None': './examples',
    'Simple Template': './examples/cc_templates',
    'Example Compliant Project ': './examples/compliant_project',
    'Example Non-Compliant Project ': './examples/non-compliant_project',
    'Custom': 'Custom',    
}
    
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

if 'cards' not in st.session_state:
    st.session_state.cards = {"project_file": None, "data_files": [], "model_files": []}

if 'data_key_counter' not in st.session_state:
    st.session_state.data_key_counter = 0
if 'model_key_counter' not in st.session_state:
    st.session_state.model_key_counter = 0

selected_example = st.selectbox("Select an example project", list(directories.keys()))
uploaded_files = st.file_uploader("or upload Compliance Cards", type="yaml", accept_multiple_files=True)

project_col, data_col, model_col = st.columns(3)
    
if selected_example:
    if selected_example == 'Custom':
        with project_col:
            if st.button("Add Project Template"):
                st.session_state.cards["project_file"] = load_yaml('./examples/custom/project_cc.yaml')
        with data_col:
            if st.button("Add Data Template"):
                cc = load_yaml('./examples/custom/data_cc.yaml')
                card_label = generate_unique_key(cc['card_details']['card_label'])
                st.session_state.cards["data_files"].append((card_label, cc))
                
        with model_col:
            if st.button("Add Model Template"):
                cc = load_yaml('./examples/custom/model_cc.yaml')
                card_label = generate_unique_key(cc['card_details']['card_label'])
                st.session_state.cards["model_files"].append((card_label, cc))
                    
    else:
        st.session_state.cards = {"project_file": None, "data_files": [], "model_files": []}
        st.session_state.data_key_counter = 0
        st.session_state.model_key_counter = 0
        directory_path = directories[selected_example]
        yaml_files = load_yaml_files_from_directory(directory_path)
        for cc in yaml_files:
            card_type = cc['card_details'].get('card_type', '').lower()
            
            if card_type == 'project':
                st.session_state.cards["project_file"] = cc
            elif card_type == 'data':
                st.session_state.cards["data_files"].append(((cc['card_details']['card_label']), cc))
            elif card_type == 'model':
                st.session_state.cards["model_files"].append(((cc['card_details']['card_label']), cc))

if uploaded_files:
    for uploaded_file in uploaded_files:
        cc = yaml.safe_load(uploaded_file)
        card_type = cc['card_details'].get('card_type', '').lower()

        if card_type == 'project':
            st.session_state.cards["project_file"] = cc
        elif card_type == 'data':
            st.session_state.cards["data_files"].append((cc['card_details']['card_label'], cc))
        elif card_type == 'model':
            st.session_state.cards["model_files"].append((cc['card_details']['card_label'], cc))

# project_col, data_col, model_col = st.columns(3)
     

with project_col:
    st.title("Project Card")
    
    if st.session_state.cards["project_file"]:
        project_cc = st.session_state.cards["project_file"]
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
    
    if st.session_state.cards['data_files']:
        for card in st.session_state.cards['data_files']:
            data_cc = card[1]
            with st.expander(f"{card[0]}"):
                for section, items in data_cc.items():
                    if section == 'card_details':
                        items['card_label'] = st.text_input('card_label', value=items['card_label'], key=f"data_{card[0]}_{section}")
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
    if st.session_state.cards['model_files']:
        for card in st.session_state.cards['model_files']:
            model_cc = card[1]
            with st.expander(f"{card[0]}"):       
                for section, items in model_cc.items():
                    if section == 'card_details':
                        items['card_label'] = st.text_input('card_label', value=items['card_label'], key=f"model_{card[0]}_{section}")
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

if selected_example == 'Custom':
    with data_col:
        @st.fragment
        def remove_card_button():
            if st.session_state.cards["data_files"]:
                selected_label = st.selectbox(
                    "Select a card to remove",
                    [card[0] for card in st.session_state.cards["data_files"]],
                    key='selected_data_file'
                )

                if st.button(f"Remove {selected_label}"):
                    st.session_state.cards["data_files"] = [
                        card for card in st.session_state.cards["data_files"] if card[0] != selected_label
                    ]
                    st.rerun()
            return
        remove_card_button()
        
    with model_col:
        @st.fragment
        def remove_card_button():    
            if st.session_state.cards["model_files"]:
                selected_label = st.selectbox(
                    "Select a card to remove",
                    [card[0] for card in st.session_state.cards["model_files"]],
                    key='selected_model_file'
                )

                if st.button(f"Remove {selected_label}"):
                    st.session_state.cards["model_files"] = [
                        card for card in st.session_state.cards["model_files"] if card[0] != selected_label
                    ]
                    st.rerun()
            return
        remove_card_button()
    

# # #         # json_data = json.dumps(data, indent=2)
# # #         # st.download_button(
# # #         #     label="Download Updated Data as JSON",
# # #         #     data=json_data,
# # #         #     file_name="updated_data.json",
# # #         #     mime="application/json"
# # #         # )   


if st.button(f"Run Analysis"):
    results = compliance_analysis(st.session_state.cards)
    st.write("Analysis Results:", results)
