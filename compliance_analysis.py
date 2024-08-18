import yaml
from utils import set_type, set_operator_role_and_location, set_eu_market_status, check_within_scope

# Create some variables we will use throughout our analysis

project_variables = {
    "ai_project_type": {
        "ai_system": False,
        "gpai_model": False,
        "high_risk_ai_system": False,
        "gpai_model_systematic_risk": False
    },
    "operator_role": {
        "provider": False,
        "deployer": False,
        "importer": False,
        "distributor": False,
        "product_manufacturer": False,
        "eu_located": False
    },
    "eu_market_status": {
        "placed_on_market": False,
        "put_into_service": False,
        "output_used": False
    }
}

project_intended_purpose = None 

# TO-DO: A thesis of this paper is that we cannot declare a project compliant without looking at all of its component models and datasets. 
# What that means in practical terms is that we need to check all model and data CCs in addition to the project CC to render a decision of compliance.
# There are two ways we can go about this: 
# (1) We can have an orchestrator function that sits on top of run_compliance_analysis_on_project(), run_compliance_analysis_on_data(), and 
# run_compliance_analysis_on_model() and orchestrates them. In particular, it will have to first run run_compliance_analysis_on_project() to set 
# the values of some "dispositive characteristic" variables, which it can then pass into run_compliance_analysis_on_data() and run_compliance_analysis_on_model()
# to make sure that the analysis done there is dynamically appropriate. Importantly, it will also have to run run_compliance_analysis_on_data(), and 
# run_compliance_analysis_on_model() for each and every data and model CCs in the folder, passing in those "dispositive characteristic" variables 
# as arguments to ensure the analysis is apprpriate. 
# (2) We could treat run_compliance_analysis_on_project() as the orchestrator function. This would mean this function would first need to set all of the
# "dispositive characteristic" variables and then, after doing that, call compliance_analysis_on_data() and run_compliance_analysis_on_model() for all
# of the model and data CCs in the folder, passing in the "dispositive characteristic" variables as arguments.
#
# I slightly prefer option (1), so here is some pseudo-code for a potential orchestrator function:
# 
# def orchestrator():
#
#   this might be a good time to check to make sure there is at least one Project CC and also do do any   
#   some administrative stuff to make your life easier like maybe getting all the files in the folder into a list, etc.
#
#   Call run_compliance_analysis_on_project, passing in the sole Project CC as the argument
#       -This must set the "dispositive" variables (i.e., the project_variables above) by parsing them from the Project CC. It already does this as-is.
#       -This must also check to see if the project is out of scope. It does this as-is.
#       -This must also check for prohibited practices. This has been commented out, but the functionality is there as-is.
#       -Last but not least, this must run the internal check of the project CC based on the project_variables it has set. It is only partially doing this as-is. To finish the job, we must:
#           -Run the check for other types of models and systems: AI systems without high risk, GPAI without systemic risk, GPAI with systemic risk. It is only doing high-risk AI systems at the moment.
#           -Where the operator is a provider, ensure any additional requirements for providers are met (see the Project CC template for details)
#           -Where the operator is a deployer, ensure any additional requirements for deployers are met (see the Project CC template for details)
#
#   Call run_compliance_analysis_on_model() *for all model CCs in the folder*, passing in the ai_project_type variable and maybe project_intended_purpose 
#       -This should include a "cross comparison" of the intended uses listed in the model CC and the project_intended_purpose parsed from the Project CC, something that is not yet integrated 
#       -This function must check if GPAI requirements are met, if that value for ai_project_type is passed in -- it does not yet do this   
#
#   Call run_compliance_analysis_on_data() *for all data CCs in the folder*, passing in the ai_project_type variable and maybe project_intended_purpose
#       -This should include a "cross comparison" of the intended uses listed in the data CC and the project_intended_purpose parsed from the Project CC, something that is not yet integrated  
#       -This function must check if GPAI requirements are met, if that value for ai_project_type is passed in -- it does not yet do this 
#
#   This function could also more gracefully handle the internal exits/reports and generate a single, digestible compliance report that
#   tells the user where the compliance analysis failed. If we wanted to get really fancy, we could include error messages for each individual
#   entry in the yaml files, possibly citing the part of the Act that they need to reference (currently in comments that user does not see)


def run_compliance_analysis_on_project(project_cc_yaml): 

    # Determine project type (AI system vs. GPAI model) as well as operator type. We will use these for different things.
    project_type = set_type(project_variables, project_cc_yaml)
    set_operator_role_and_location(project_variables, project_cc_yaml)
    set_eu_market_status(project_variables, project_cc_yaml)

    # Check if the project is within scope of the Act. If it's not, the analysis is over.
    if check_within_scope(project_variables, project_cc_yaml):
        msg = ("Project is within the scope of Act. Let's continue...") 
    else: 
        msg = ("Project is not within the scope of what is regulated by the Act.")

    # TO-DO: reactivate the prohibited practices check below 

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

    # TO-DO: No matter where we land with an orchestrator function, this function must also check to the value it has set for both
    # GPAI models with and without systemic risk and then check to see if the relevant requirement have met if either of these values applies.
    # This will look a lot like what is happening above for high-risk AI systems. 
    
    return msg

def run_compliance_analysis_on_data(data_cc_yaml): # TO-DO: we probably have to pass ai_project_type and project_intended_purpose into this function
    
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

    # TO-DO: No matter where we land with an orchestrator function, this function must also check to the value that has been set for both
    # GPAI models with and without systemic risk and then check to see if the relevant requirements have met if either of these values applies.
    # Right now it is only checking high-risk AI system requirements. Another thing that we likely have to add here is the cross-comparison of the 
    # intended uses.

    return msg
    
def run_compliance_analysis_on_model(model_cc_yaml):  # TO-DO: we probably have to pass ai_project_type and project_intended_purpose into this function
    
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
   
    # TO-DO: No matter where we land with an orchestrator function, this function must also check to the value that has been set for both
    # GPAI models with and without systemic risk and then check to see if the relevant requirements have met if either of these values applies.
    # Right now it is only checking high-risk AI system requirements. Another thing that we likely have to add here is the cross-comparison of the 
    # intended uses.
    
    return msg

def check_intended_purpose():
    
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

    return msg



    # # If the project is a GPAI model, check that is has met all the requirements for such systems: 

    # if gpai_model:

    # # Do this by examining the Project CC

    #     for key, value in project_cc_yaml['gpai_model_provider_obligations']:
    #         if not value:
    #             msg = ("GPAI model fails the transparency requirements under Article 53.")

    # # Do this by examining any and all Data CCs too

    #     for filename in os.listdir(folder_path):
    #         # Check if the search word is in the filename
    #         if "data_cc.md" in filename.lower():

    #             # If it is, load the yaml

    #             with open(folder_path + filename, 'r') as file:
    #                 data_cc_yaml = yaml.safe_load(file)

    #             for key, value in data_cc_yaml['gpai_requirements']['gpai_requirements']:
    #                 if not value:
    #                     msg = (f"Because of the dataset represented by {filename}, this GPAI fails the transparency requirements under Article 53.")

    # # Do this by examining any and all Model CCs too
    
    #     for filename in os.listdir(folder_path):
    #         # Check if the search word is in the filename
    #         if "model_cc.md" in filename.lower():

    #             # If it is, load the yaml

    #             with open(folder_path + filename, 'r') as file:
    #                 model_cc_yaml = yaml.safe_load(file)

    #             for key, value in model_cc_yaml['obligations_for_providers_of_gpai_models']:
    #                 if not value:
    #                     msg = (f"Because of the model represented by {filename}, this GPAI fails the transparency requirements under Article 53.")

    # # If the project is a GPAI model with systematic risk, check that is has additionally met all the requirements for such systems: 

    # if gpai_model_systematic_risk:

    # # Do this by examining the Project CC

    #     for key, value in project_cc_yaml['gpai_obligations_for_systemic_risk_models']:
    #         if not value:
    #             msg = ("GPAI model with systematic risk fails the transparency requirements under Article 55.")

    # # Do this by examining any and all Model CCs too

    #     for filename in os.listdir(folder_path):
    #         # Check if the search word is in the filename
    #         if "model_cc.md" in filename.lower():

    #             # If it is, load the yaml

    #             with open(folder_path + filename, 'r') as file:
    #                 model_cc_yaml = yaml.safe_load(file)

    #             for key, value in model_cc_yaml['obligations_for_providers_of_gpai_models_with_systemic_risk']:
    #                 if not value:
    #                     msg = (f"Because of the model represented by {filename}, this GPAI model with systematic risk fails the transparency requirements under Article 55.")



