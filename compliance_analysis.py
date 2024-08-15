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

    # # Check for prohibited practices. If any exist, the analysis is over.
    # if check_prohibited(project_cc_yaml) == True: 
    #     print("Project contains prohibited practices and is therefore non-compliant.")
    #     msg = ("Project is non-compliant due to a prohibited practice.")
    # else: 
    #     print("Project does not contain prohibited practies. Let's continue...")

    # If project is high-risk AI system, check that is has met all the requirements for such systems: 

    if project_type == "high_risk_ai_system":

    # Do this by examining the Project CC

        # WE HAVE TO ADD A CONDITION THAT APPLIES THESE RULES BELOW ONLY IF operator_role == provider

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

def check_intended_use_aligned():
    
    # We want to run this function for everything classified as a high_risk_ai_system
    # We also need to run it for all 
    # Add any of the intended purposes of the overall project to a set of intended purposes
    
    if project_cc_yaml['high_risk_ai_system']['safety_component'] == True:
        intended_purpose = "safety_component"
    if project_cc_yaml['high_risk_ai_system']['product_regulated_machinery'] == True:
        intended_purpose = "product_regulated_machinery" 
    if project_cc_yaml['high_risk_ai_system']['product_regulated_toy'] == True:
        intended_purpose = "product_regulated_toy" 
    if project_cc_yaml['high_risk_ai_system']['product_regulated_watercraft'] == True:
        intended_purpose = "product_regulated_watercraft" 
    if project_cc_yaml['high_risk_ai_system']['biometric_categorization'] == True:
        intended_purpose = "biometric_categorization" 
    if project_cc_yaml['high_risk_ai_system']['emotion_recognition'] == True:
        intended_purpose = "emotion_recognition" 
    if project_cc_yaml['high_risk_ai_system']['critical_infrastructure'] == True:
        intended_purpose = "critical_infrastructure" 
    if project_cc_yaml['high_risk_ai_system']['admission'] == True:
        intended_purpose = "admission" 
    if project_cc_yaml['high_risk_ai_system']['recruitment'] == True:
        intended_purpose = "recruitment" 
    if project_cc_yaml['high_risk_ai_system']['public_assistance'] == True:
        intended_purpose = "public_assistance"
    if project_cc_yaml['high_risk_ai_system']['victim_assessment'] == True:
        intended_purpose = "victim_assessment" 
    if project_cc_yaml['high_risk_ai_system']['polygraph'] == True:
        intended_purpose = "polygraph" 
    if project_cc_yaml['high_risk_ai_system']['judicial'] == True:
        intended_purpose = "judicial" 
    
    # For each Data CC, put the intended uses in a set and then make sure the Project's intended use is in the set

    dataset_intended_purpose = () 

    if data_cc_yaml['intended_purpose']['safety_component'] == True:
        dataset_intended_purpose.add("safety_component")
    if data_cc_yaml['intended_purpose']['product_regulated_machinery'] == True:
        dataset_intended_purpose.add("product_regulated_machinery")
    if data_cc_yaml['intended_purpose']['product_regulated_toy'] == True:
        dataset_intended_purpose.add("product_regulated_toy")
    if data_cc_yaml['intended_purpose']['product_regulated_watercraft'] == True:
        dataset_intended_purpose.add("product_regulated_watercraft")
    if data_cc_yaml['intended_purpose']['biometric_categorization'] == True:
        dataset_intended_purpose.add("biometric_categorization")
    if data_cc_yaml['intended_purpose']['emotion_recognition'] == True:
        dataset_intended_purpose.add("emotion_recognition")
    if data_cc_yaml['intended_purpose']['critical_infrastructure'] == True:
        dataset_intended_purpose.add("critical_infrastructure")
    if data_cc_yaml['intended_purpose']['admission'] == True:
        dataset_intended_purpose.add("admission")
    if data_cc_yaml['intended_purpose']['recruitment'] == True:
        dataset_intended_purpose.add("recruitment")
    if data_cc_yaml['intended_purpose']['public_assistance'] == True:
        dataset_intended_purpose.add("public_assistance")       
    if data_cc_yaml['intended_purpose']['victim_assessment'] == True:
        dataset_intended_purpose.add("victim_assessment")
    if data_cc_yaml['intended_purpose']['polygraph'] == True:
        dataset_intended_purpose.add("polygraph")
    if data_cc_yaml['intended_purpose']['judicial'] == True:
        dataset_intended_purpose.add("judicial")

    if project_intended_purpose not in dataset_intended_purpose:
        print("You are not compliant")

    # Now do the exact same thing for all models

    model_intended_purpose = () 

    if model_cc_yaml['intended_purpose']['safety_component'] == True:
        dataset_intended_purpose.add("safety_component")
    if model_cc_yaml['intended_purpose']['product_regulated_machinery'] == True:
        dataset_intended_purpose.add("product_regulated_machinery")
    if model_cc_yaml['intended_purpose']['product_regulated_toy'] == True:
        dataset_intended_purpose.add("product_regulated_toy")
    if model_cc_yaml['intended_purpose']['product_regulated_watercraft'] == True:
        dataset_intended_purpose.add("product_regulated_watercraft")
    if model_cc_yaml['intended_purpose']['biometric_categorization'] == True:
        dataset_intended_purpose.add("biometric_categorization")
    if model_cc_yaml['intended_purpose']['emotion_recognition'] == True:
        dataset_intended_purpose.add("emotion_recognition")
    if model_cc_yaml['intended_purpose']['critical_infrastructure'] == True:
        dataset_intended_purpose.add("critical_infrastructure")
    if model_cc_yaml['intended_purpose']['admission'] == True:
        dataset_intended_purpose.add("admission")
    if model_cc_yaml['intended_purpose']['recruitment'] == True:
        dataset_intended_purpose.add("recruitment")
    if model_cc_yaml['intended_purpose']['public_assistance'] == True:
        dataset_intended_purpose.add("public_assistance")       
    if model_cc_yaml['intended_purpose']['victim_assessment'] == True:
        dataset_intended_purpose.add("victim_assessment")
    if model_cc_yaml['intended_purpose']['polygraph'] == True:
        dataset_intended_purpose.add("polygraph")
    if model_cc_yaml['intended_purpose']['judicial'] == True:
        dataset_intended_purpose.add("judicial")

    if project_intended_purpose not in dataset_intended_purpose:
        print("You are not compliant")



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



