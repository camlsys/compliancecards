import yaml
from utils import set_type, set_operator_role_and_location, set_eu_market_status, check_within_scope_cc, check_within_scope_act

# Create some variables we will use throughout our analysis

dispositive_variables = {
    "ai_project_type": {
        "ai_system": False,
        "gpai_model": False,
        "high_risk_ai_system": False,
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

# TODO tells the user where the compliance analysis failed
# TODO cite article from yaml file as explanation

def check_overall_compliance(dispositive_variables, cc_files):

    # check intended purposes 
    dispositive_variables = check_intended_purpose(dispositive_variables, cc_files)
   
    # for each model_cc and data_cc - run analysis with ref to project_cc
    
    dispositive_variables = run_compliance_analysis_on_data(dispositive_variables, data_cc_yaml)
    dispositive_variables = run_compliance_analysis_on_model(dispositive_variables, model_cc_yaml)
    
    dispositive_variables = run_compliance_analysis_on_project(dispositive_variables, project_cc_yaml)

    return dispositive_variables

def run_compliance_analysis_on_project(dispositive_variables, project_cc_yaml): 

    # Determine project type (AI system vs. GPAI model) as well as operator type. We will use these for different things.
    project_type = set_type(dispositive_variables, project_cc_yaml)
    set_operator_role_and_location(dispositive_variables, project_cc_yaml)
    set_eu_market_status(dispositive_variables, project_cc_yaml)

    # Check if project is within scope of the Compliance Cards project. If not, inform user.
    if check_within_scope_cc(dispositive_variables):
        msg = ("Project is within the scope of the Compliance Cards system. Let's continue...") 
    else: 
        msg = ("Project is not within the scope of the initial version of the Compliance Cards system.")
    
    # Check if the project is within scope of the Act. If it's not, the analysis is over.
    if check_within_scope_act(dispositive_variables, project_cc_yaml):
        msg = ("Project is within the scope of Act. Let's continue...") 
    else: 
        msg = ("Project is not within the scope of what is regulated by the Act.")

    # TODO: reactivate the prohibited practices check below 

    # TODO: fix and uncomment
    # # Check for prohibited practices. If any exist, the analysis is over.
    # if check_prohibited(project_cc_yaml) == True: 
    #     print("Project contains prohibited practices and is therefore non-compliant.")
    #     msg = ("Project is non-compliant due to a prohibited practice.")
    # else: 
    #     print("Project does not contain prohibited practies. Let's continue...")

    # If project is high-risk AI system, check that is has met all the requirements for such systems: 

    if project_type == "high_risk_ai_system":

    # Do this by examining the Project CC

        for key, value in project_cc_yaml['risk_management_system']:
            if not value:
                msg = ("Because of project-level characteristics, this high-risk AI system fails the risk management requirements under Article 9.")
        for key, value in project_cc_yaml['technical_documentation']:
            if not value:
                msg = ("Because of project-level characteristics, this high-risk AI system fails the risk management requirements under Article 11.")            
        for key, value in project_cc_yaml['record_keeping']:
            if not value:
                msg = ("Because of project-level characteristics, this high-risk AI system fails the risk management requirements under Article 12.")     
        for key, value in project_cc_yaml['transparency_and_provision_of_information_to_deployers']:
            if not value:
                msg = ("Because of project-level characteristics, this high-risk AI system fails the transparency requirements under Article 13.")  
        for key, value in project_cc_yaml['human_oversight']:
            if not value:
                msg = ("Because of project-level characteristics, this high-risk AI system fails the human oversight requirements under Article 14.")  
        for key, value in project_cc_yaml['accuracy_robustness_cybersecurity']:
            if not value:
                msg = ("Because of project-level characteristics, this high-risk AI system fails the accuracy, robustness, and cybersecurity requirements under Article 15.")  
        for key, value in project_cc_yaml['quality_management_system']:
            if not value:
                msg = ("Because of project-level characteristics, this high-risk AI system fails the accuracy, robustness, and cybersecurity requirements under Article 17.") 


    # TODO
    # # If the project is a GPAI model, check that is has met all the requirements for such systems: 

    if gpai_model:

    # # If the project is a GPAI model with systematic risk, check that is has additionally met all the requirements for such systems: 

    # if gpai_model_systematic_risk:

    # # Do this by examining the Project CC

    #     for key, value in project_cc_yaml['gpai_obligations_for_systemic_risk_models']:
    #         if not value:
    #             msg = ("GPAI model with systematic risk fails the transparency requirements under Article 55.")

    # Do this by examining the Project CC

        for key, value in project_cc_yaml['gpai_model_obligations']:
            if not value:
                msg = ("GPAI model fails the transparency requirements under Article 53.")    


    if gpai_model_systematic_risk:
        for key, value in project_cc_yaml['gpai_models_with_systemic_risk_obligations']:


    # if ai_system:
    #     for key, value in project_cc_yaml['']:
        # TODO to be included in project_cc
        

    # TODO: No matter where we land with an orchestrator function, this function must also check to the value it has set for both
    # GPAI models with and without systemic risk and then check to see if the relevant requirement have met if either of these values applies.
    # This will look a lot like what is happening above for high-risk AI systems. 
    
    return dispositive_variables

def run_compliance_analysis_on_data(dispositive_variables, data_cc_yaml): 
    
    # TODO: we probably have to pass ai_project_type and project_intended_purpose into this function
    
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

    #             for key, value in data_cc_yaml['gpai_requirements']['gpai_requirements']:
    #                 if not value:
    #                     msg = (f"Because of the dataset represented by {filename}, this GPAI fails the transparency requirements under Article 53.")


    # TODO: No matter where we land with an orchestrator function, this function must also check to the value that has been set for both
    # GPAI models with and without systemic risk and then check to see if the relevant requirements have met if either of these values applies.
    # Right now it is only checking high-risk AI system requirements. Another thing that we likely have to add here is the cross-comparison of the 
    # intended purposes. That might look like this:
    # if data_cc_yaml['intended_purpose'] not in intended_purposes:
    #   return false 

    return dispositive_variables
    
def run_compliance_analysis_on_model(dispositive_variables, model_cc_yaml):  
    
    # TODO: we probably have to pass ai_project_type and project_intended_purpose into this function
    
    for key, value in model_cc_yaml['risk_management_system']:
        if not value:
            msg = (f"Because of the model represented by , this high-risk AI system fails the risk management requirements under Article 9.")
    for key, value in data_cc_yaml['technical_documentation']:
        if not value:
            msg = (f"Because of the model represented by , this high-risk AI system fails the technical documentation requirements under Article 11.")
    for key, value in data_cc_yaml['transparency_and_provision_of_information_to_deployers']:
        if not value:
            msg = (f"Because of the model represented by , this high-risk  AI system fails the transparency requirements under Article 13.")
    for key, value in data_cc_yaml['accuracy_robustness_cybersecurity']:
        if not value:
            msg = (f"Because of the model represented by , this high-risk  AI system fails the quality management requirements under Article 15.")
    for key, value in data_cc_yaml['quality_management_system']:
        if not value:
            msg = (f"Because of the model represented by , this high-risk  AI system fails the quality management requirements under Article 17.")


    #             for key, value in model_cc_yaml['obligations_for_providers_of_gpai_models']:
    #                 if not value:
    #                     msg = (f"Because of the model represented by {filename}, this GPAI fails the transparency requirements under Article 53.")

    #             for key, value in model_cc_yaml['obligations_for_providers_of_gpai_models_with_systemic_risk']:
    #                 if not value:
    #                     msg = (f"Because of the model represented by {filename}, this GPAI model with systematic risk fails the transparency requirements under Article 55.")
   
    # TODO: No matter where we land with an orchestrator function, this function must also check to the value that has been set for both
    # GPAI models with and without systemic risk and then check to see if the relevant requirements have met if either of these values applies.
    # Right now it is only checking high-risk AI system requirements. Another thing that we likely have to add here is the cross-comparison of the 
    # intended purposes. That might look like this:
    # if model_cc_yaml['intended_purpose'] not in intended_purposes:
    #   return false 
    
    return dispositive_variables

def check_intended_purpose(dispositive_variables, cc_files):
    
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
    for key in project_cc_yaml['high_risk_ai_system']:
        if project_cc_yaml['high_risk_ai_system'][f'{key}']['value']:
            project_intended_purposes.append(key) 
    
    # For each Data CC, put the intended uses in a set and then make sure the Project's intended use is in the set

    msg = ''
    dataset_intended_purposes = []
    for key in data_cc_yaml['high_risk_ai_system']:
        if data_cc_yaml['high_risk_ai_system'][f'{key}']['value']:
            dataset_intended_purposes.append(key) 

    for purpose in project_intended_purposes:
        if purpose not in dataset_intended_purposes:
            msg = f"You are not compliant because {purpose} is not a valid purpose"

    # Now do the exact same thing for all models

    model_intended_purposes = []
    for key in model_cc_yaml['high_risk_ai_system']:
        if model_cc_yaml['high_risk_ai_system'][f'{key}']['value']:
            model_intended_purposes.append(key) 

    for purpose in project_intended_purposes:
        if purpose not in model_intended_purposes:
            msg = f"You are not compliant because {purpose} is not a valid purpose"

    # TODO return list of intended purpose 

    return dispositive_variables


