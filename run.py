import yaml
import json
from pathlib import Path
import pandas as pd
from src.compliance_analysis import check_overall_compliance

pd.set_option('display.max_columns', None)  
pd.set_option('display.max_rows', None)

files = ["./project_cc.yaml", "./data_cc.yaml", "./data_cc.yaml", "./model_cc.yaml", "./model_cc.yaml", "./model_cc.yaml"]

# def load_data(files):
#     cards = []
#     for file in files:
#         with open(file, 'r') as f:
#             if Path(f.name).name == "project_cc.yaml":
#                 content = f.read()
#                 project_cc_yaml = yaml.safe_load(content)
#                 data = project_cc_yaml
#                 card_type = "project"
#                 cards.append((card_type, data))
#             if Path(f.name).name == "data_cc.yaml":
#                 data_cc_yaml = yaml.safe_load(content)
#                 data = data_cc_yaml
#                 card_type = "data"
#                 cards.append((card_type, data))
#             if Path(f.name).name == "model_cc.yaml":
#                 model_cc_yaml = yaml.safe_load(content)
#                 data = model_cc_yaml
#                 card_type = "model"
#                 cards.append((card_type, data))
#     return cards

# cards = load_data(files)

def gather_cards(files):
    cards = {}
    cards['project_file'] = ''
    cards['data_files'] = []
    cards['model_files'] = []
    for file in files:        
        with open(file, 'r') as f:
            content = yaml.safe_load(f.read())
            if content['card_type'] == "project":
                cards['project_file'] = f.name
            if content['card_type'] == "data":
                cards['data_files'].append(f.name)
            if content['card_type'] == "model":
                cards['model_files'].append(f.name)
    return cards

cards = gather_cards(files)

# def load_data(files):
#     cards = []
#     for file in files:
#         with open(file, 'r') as f:
#             if Path(f.name).name == "project_cc.yaml":
#                 content = f.read()
#                 pcrojet_cc_yaml = yaml.safe_load(content)
#                 data = project_cc_yaml
#                 card_type = "project"
#                 cards.append((card_type, data))
#             if Path(f.name).name == "data_cc.yaml":
#                 data_cc_yaml = yaml.safe_load(content)
#                 data = data_cc_yaml
#                 card_type = "data"
#                 cards.append((card_type, data))
#             if Path(f.name).name == "model_cc.yaml":
#                 model_cc_yaml = yaml.safe_load(content)
#                 data = model_cc_yaml
#                 card_type = "model"
#                 cards.append((card_type, data))
#     return cards

def compliance_analysis(cards):
    results = []
    dispositive_variables = check_overall_compliance(cards)
    results.append(dispositive_variables)#['msg'])
    return results

print(json.dumps(compliance_analysis(cards), indent=4,))
    