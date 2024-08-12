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

def run_compliance_analysis_on_project(project_cc_yaml):

    # Determine project type (AI system vs. GPAI model) as well as operator type. We will use these for different things.
    project_type = set_type(project_variables, project_cc_yaml)
    set_operator_role_and_location(project_variables, project_cc_yaml)
    set_eu_market_status(project_variables, project_cc_yaml)

    # Check if the project is within scope of the Act. If it's not, the analysis is over.
    if check_within_scope(project_cc_yaml):
        msg = ("Project is within the scope of Act. Let's continue...") 
    else: 
        msg = ("Project is not within the scope of what is regulated by the Act.")

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

    return msg

def run_compliance_analysis_on_data(data_cc_yaml):
    
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

    return msg
    
def run_compliance_analysis_on_model(model_cc_yaml):
    
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



