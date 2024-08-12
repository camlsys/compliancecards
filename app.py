import gradio as gr
import yaml
from pathlib import Path
from compliance_analysis import run_compliance_analysis_on_project, run_compliance_analysis_on_data, run_compliance_analysis_on_model

def process_files(files):
    results = []
    for file in files:
        with open(file.name, 'r') as f:
            content = f.read()
        if Path(file.name).name == "project_cc.yaml":
            project_cc_yaml = yaml.safe_load(content)
            msg = run_compliance_analysis_on_project(project_cc_yaml)
            results.append(msg)            
        # if Path(file.name).name == "data_cc.yaml":
        #     data_cc_yaml = yaml.safe_load(content)
        #     msg = run_compliance_analysis_on_data(data_cc_yaml)
        #     results.append(msg)        
        # if Path(file.name).name == "model_cc.yaml":
        #     model_cc_yaml = yaml.safe_load(content)
        #     msg = run_compliance_analysis_on_model(model_cc_yaml)
        #     results.append(msg)
            
    return results

# Gradio interface
with gr.Blocks() as demo:
    file_input = gr.File(label="Upload Files", file_count="multiple")
    output = gr.Textbox(label="Output", lines=10)
    
    submit_button = gr.Button("Process Files")
    submit_button.click(process_files, inputs=file_input, outputs=output)

demo.launch()
