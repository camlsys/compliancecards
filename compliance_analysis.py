import yaml
from utils import set_operator_role_and_location, set_eu_market_status, check_within_scope_cc, check_within_scope_act, check_prohibited

# TODO tells the user where the compliance analysis failed
# TODO cite article from yaml file as explanation

def check_overall_compliance(cards):
    
    dispositive_variables = {
    "ai_project_type": {
        "ai_system": False,
        "gpai_model": True,
        "high_risk_ai_system": True,
        "gpai_model_systematic_risk": False
    },
    "operator_details": {
        "provider": False,
        "eu_located": False,
        "output_used": False
    },
    "eu_market_status": {
        "placed_on_market": False,
        "put_into_service": False
    },
    "intended_purposes": [],
    "project_cc_pass": False,
    "data_cc_pass": False,
    "model_cc_pass": False,
    "msg": []
    }
    
    with open(cards['project_file'], 'r') as project_filepath:
        project_cc = yaml.safe_load(project_filepath.read())

    
    # # check intended purposes 
    # for card in cards['data_files']:
    #     with open(card, 'r') as data_filepath:
    #         data_cc = yaml.safe_load(data_filepath.read())
    #         dispositive_variables = check_intended_purpose(dispositive_variables, project_cc, data_cc)
        
    # for card in cards['model_files']:
    #     dispositive_variables = check_intended_purpose(dispositive_variables, project_cc, card)
        
   
    # for each model_cc and data_cc - run analysis with ref to project_cc
    
    dispositive_variables = run_compliance_analysis_on_project(dispositive_variables, project_cc)
    
    # dispositive_variables = run_compliance_analysis_on_data(dispositive_variables, data_cc_yaml)
    # dispositive_variables = run_compliance_analysis_on_model(dispositive_variables, model_cc_yaml)

    return dispositive_variables

def run_compliance_analysis_on_project(dispositive_variables, project_cc_yaml):
    
    # Project Type    
    if project_cc_yaml['ai_system']['ai_system']['value']:
        dispositive_variables['ai_project_type']['ai_system'] = True
    if project_cc_yaml['gpai_model']['gpai_model']['value']:
        dispositive_variables['ai_project_type']['gpai_model'] = True
    if project_cc_yaml['ai_system']['ai_system']['value'] == True and project_cc_yaml['gpai_model']['gpai_model']['value'] == True:
        dispositive_variables['msg'] = "Your project cannot be both an AI system and a GPAI model. Please revise your Project CC accordingly."
        return dispositive_variables
    
    # TODO check whether high risk before the below?
    
    if dispositive_variables['ai_project_type']['ai_system'] == True:
        for value in project_cc_yaml['high_risk_ai_system']:
            if value and sum(map(bool, [
                    project_cc_yaml['high_risk_ai_system_exceptions']['filter_exception_rights']['value'], 
                    project_cc_yaml['high_risk_ai_system_exceptions']['filter_exception_narrow']['value'],
                    project_cc_yaml['high_risk_ai_system_exceptions']['filter_exception_human']['value'],
                    project_cc_yaml['high_risk_ai_system_exceptions']['filter_exception_deviation']['value'], 
                    project_cc_yaml['high_risk_ai_system_exceptions']['filter_exception_prep']['value']])
                    ) >= 1:
                
                dispositive_variables['ai_project_type']["high_risk_ai_system"] = False
    
    if dispositive_variables['ai_project_type']['gpai_model'] == True:
        if project_cc_yaml['gpai_model_systematic_risk']['evaluation'] or project_cc_yaml['gpai_model_systematic_risk']['flops']:
            dispositive_variables['ai_project_type']["gpai_model_systematic_risk"] = True
    
    # Operator Type
    dispositive_variables = set_operator_role_and_location(dispositive_variables, project_cc_yaml)
    dispositive_variables = set_eu_market_status(dispositive_variables, project_cc_yaml)

    # Check if project is within scope of the Compliance Cards project. If not, inform user.
    if check_within_scope_cc(project_cc_yaml):
        dispositive_variables['msg'].append("Project is within the scope of the Compliance Cards system. Let's continue...") 
    else: 
        dispositive_variables['msg'].append("Project is not within the scope of the initial version of the Compliance Cards system.")
    
    # Check if the project is within scope of the Act. If it's not, the analysis is over.
    if check_within_scope_act(project_cc_yaml):
        dispositive_variables['msg'].append("Project is within the scope of Act. Let's continue...") 
    else: 
        dispositive_variables['msg'].append("Project is not within the scope of what is regulated by the Act.")

    # Check for prohibited practices. If any exist, the analysis is over.
    if check_prohibited(project_cc_yaml) == True: 
        print("Project contains prohibited practices and is therefore non-compliant.")
        dispositive_variables['msg'].append("Project is non-compliant due to a prohibited practice.")
    else: 
        print("Project does not contain prohibited practies. Let's continue...")

    # If project is high-risk AI system, check that is has met all the requirements for such systems: 
    if dispositive_variables['ai_project_type']["high_risk_ai_system"] == True:

        for key in project_cc_yaml['risk_management_system']:
            if project_cc_yaml['risk_management_system'][f'{key}']['value'] == True:
                dispositive_variables['msg'].append("Because of project-level characteristics, this high-risk AI system fails the risk management requirements under Article 9.")
        for key in project_cc_yaml['technical_documentation']:
            if project_cc_yaml['technical_documentation'][f'{key}']['value'] == True:
                dispositive_variables['msg'].append("Because of project-level characteristics, this high-risk AI system fails the risk management requirements under Article 11.")            
        
        for key in project_cc_yaml['record_keeping']:
            if project_cc_yaml['record_keeping'][f'{key}']['value'] == True:
                dispositive_variables['msg'].append("Because of project-level characteristics, this high-risk AI system fails the risk management requirements under Article 12.")     
        
        for key in project_cc_yaml['transparency_and_provision_of_information_to_deployers']:
            if project_cc_yaml['transparency_and_provision_of_information_to_deployers'][f'{key}']['value'] == True:
                dispositive_variables['msg'].append("Because of project-level characteristics, this high-risk AI system fails the transparency requirements under Article 13.")  
        
        for key in project_cc_yaml['human_oversight']:
            if project_cc_yaml['human_oversight'][f'{key}']['value'] == True:
                dispositive_variables['msg'].append("Because of project-level characteristics, this high-risk AI system fails the human oversight requirements under Article 14.")  
        
        for key in project_cc_yaml['accuracy_robustness_cybersecurity']:
            if project_cc_yaml['accuracy_robustness_cybersecurity'][f'{key}']['value'] == True:
                dispositive_variables['msg'].append("Because of project-level characteristics, this high-risk AI system fails the accuracy, robustness, and cybersecurity requirements under Article 15.")  
        
        for key in project_cc_yaml['quality_management_system']:
            if project_cc_yaml['quality_management_system'][f'{key}']['value'] == True:
                dispositive_variables['msg'].append("Because of project-level characteristics, this high-risk AI system fails the accuracy, robustness, and cybersecurity requirements under Article 17.") 

    if dispositive_variables['ai_project_type']["gpai_model"] == True:
        
        if dispositive_variables['ai_project_type']["gpai_model_systematic_risk"] == True:
            for key in project_cc_yaml['gpai_models_with_systemic_risk_obligations']:
                if project_cc_yaml['gpai_models_with_systemic_risk_obligations'][f'{key}']['value'] == True:
                    dispositive_variables['msg'].append("GPAI model with systematic risk fails the transparency requirements under Article 55.")

        for obligation_cat in project_cc_yaml['gpai_model_obligations']:
            for obligation in project_cc_yaml['gpai_model_obligations'][f'{obligation_cat}']:
                if project_cc_yaml['gpai_model_obligations'][f'{obligation_cat}'][f'{obligation}']['value'] == True:
                    dispositive_variables['msg'].append("GPAI model fails the transparency requirements under Article 53.")
    
    return dispositive_variables

def run_compliance_analysis_on_data(dispositive_variables, data_cc_yaml): 
    
    # TODO: we probably have to pass ai_project_type and project_intended_purpose into this function
    if dispositive_variables['ai_project_type']["high_risk_ai_system"] == True:
        for key, value in data_cc_yaml['data_and_data_governance']:
            if not value:
                msg = (f"Because of the dataset represented by , this high-risk AI system fails the data and data governance requirements under Article 10.")
        for key, value in data_cc_yaml['technical_documentation']:
            if not value:
                msg = (f"Because of the dataset represented by , this high-risk AI system fails the technical documentation requirements under Article 11.")
        for key, value in data_cc_yaml['transparency_and_provision_of_information_to_deployers']:
            if not value:
                msg = (f"Because of the dataset represented by , this high-risk  AI system fails the transparency requirements under Article 13.")
        for key, value in data_cc_yaml['quality_management_system']:
            if not value:
                msg = (f"Because of the dataset represented by , this high-risk  AI system fails the quality management requirements under Article 17.")

    if dispositive_variables['ai_project_type']["gpai_model"] == True:
        for key, value in data_cc_yaml['gpai_requirements']['gpai_requirements']:
            if not value:
                msg = (f"Because of the dataset represented by {filename}, this GPAI fails the transparency requirements under Article 53.")


    # TODO: No matter where we land with an orchestrator function, this function must also check to the value that has been set for both
    # GPAI models with and without systemic risk and then check to see if the relevant requirements have met if either of these values applies.
    # Right now it is only checking high-risk AI system requirements. Another thing that we likely have to add here is the cross-comparison of the 
    # intended purposes. That might look like this:
    # if data_cc_yaml['intended_purpose'] not in intended_purposes:
    #   return false 

    return dispositive_variables
    
def run_compliance_analysis_on_model(dispositive_variables, model_cc_yaml):  
    
    # TODO: we probably have to pass ai_project_type and project_intended_purpose into this function
    # if high risk
        # for key, value in model_cc_yaml['risk_management_system']:
        #     if not value:
        #         msg = (f"Because of the model represented by , this high-risk AI system fails the risk management requirements under Article 9.")
        # for key, value in data_cc_yaml['technical_documentation']:
        #     if not value:
        #         msg = (f"Because of the model represented by , this high-risk AI system fails the technical documentation requirements under Article 11.")
        # for key, value in data_cc_yaml['transparency_and_provision_of_information_to_deployers']:
        #     if not value:
        #         msg = (f"Because of the model represented by , this high-risk  AI system fails the transparency requirements under Article 13.")
        # for key, value in data_cc_yaml['accuracy_robustness_cybersecurity']:
        #     if not value:
        #         msg = (f"Because of the model represented by , this high-risk  AI system fails the quality management requirements under Article 15.")
        # for key, value in data_cc_yaml['quality_management_system']:
        #     if not value:
        #         msg = (f"Because of the model represented by , this high-risk  AI system fails the quality management requirements under Article 17.")

    # if gpai
    #     for key, value in model_cc_yaml['obligations_for_providers_of_gpai_models']:
    # #                 if not value:
    # #                     msg = (f"Because of the model represented by {filename}, this GPAI fails the transparency requirements under Article 53.")

    # #             for key, value in model_cc_yaml['obligations_for_providers_of_gpai_models_with_systemic_risk']:
    # #                 if not value:
    # #                     msg = (f"Because of the model represented by {filename}, this GPAI model with systematic risk fails the transparency requirements under Article 55.")
   
    # # TODO: No matter where we land with an orchestrator function, this function must also check to the value that has been set for both
    # # GPAI models with and without systemic risk and then check to see if the relevant requirements have met if either of these values applies.
    # # Right now it is only checking high-risk AI system requirements. Another thing that we likely have to add here is the cross-comparison of the 
    # # intended purposes. That might look like this:
    # # if model_cc_yaml['intended_purpose'] not in intended_purposes:
    # #   return false 
    
    return dispositive_variables

def check_intended_purpose(dispositive_variables, project_cc, other_cc):
    
    # We want to run this function for everything classified as a high_risk_ai_system
    # We also need to run it for all 
    # Add any of the intended purposes of the overall project to a set of intended purposes
    
    # intended_purpose = ['safety_component',
    #                     "product_regulated_machinery",
    #                     "product_regulated_toy",
    #                     "product_regulated_watercraft",
    #                     "biometric_categorization",
    #                     "emotion_recognition",
    #                     "critical_infrastructure",
    #                     "admission",
    #                     "recruitment",
    #                     "public_assistance",
    #                     "victim_assessment",
    #                     "polygraph",
    #                     "judicial"]
    
    project_intended_purposes = []
    for key in project_cc['high_risk_ai_system']:
        if project_cc['high_risk_ai_system'][f'{key}']['value']:
            project_intended_purposes.append(key) 
    
    # For each Data CC, put the intended uses in a set and then make sure the Project's intended use is in the set

    msg = ''
    
    if other_cc['card_type'] == 'data':
        data_cc = other_cc
        dataset_intended_purposes = []
        for key in data_cc['high_risk_ai_system']:
            if data_cc['high_risk_ai_system'][f'{key}']['value']:
                dataset_intended_purposes.append(key) 

        for purpose in project_intended_purposes:
            if purpose not in dataset_intended_purposes:
                msg = f"You are not compliant because {purpose} is not a valid purpose"

    # Now do the exact same thing for all models

    if other_cc['card_type'] == 'model':
        model_cc = other_cc
        model_intended_purposes = []
        for key in model_cc['high_risk_ai_system']:
            if model_cc['high_risk_ai_system'][f'{key}']['value']:
                model_intended_purposes.append(key) 

        for purpose in project_intended_purposes:
            if purpose not in model_intended_purposes:
                msg = f"You are not compliant because {purpose} is not a valid purpose"

    # TODO return list of intended purpose 

    return dispositive_variables


