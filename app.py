import gradio as gr
import yaml
from compliance_analysis import run_compliance_analysis_on_project

def process_files(files):
    results = []
    for file in files:
        with open(file.name, 'r') as f:
            content = f.read()
        project_cc_yaml = yaml.safe_load(content)
        msg = run_compliance_analysis_on_project(project_cc_yaml)
        results.append(msg)            
            
    return results

# Gradio interface
with gr.Blocks() as demo:
    file_input = gr.File(label="Upload Files", file_count="multiple")
    output = gr.Textbox(label="Output", lines=10)
    
    submit_button = gr.Button("Process Files")
    submit_button.click(process_files, inputs=file_input, outputs=output)

demo.launch()
