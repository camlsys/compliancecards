import os
import sys
import yaml
from enum import Enum

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

#Define a function that creates a list of all the files in a provided folder. We will use this list for different things.
def create_list_of_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            found_files.append(os.path.join(root, filename))

#Define a function that checks for a Project CC. Without this, there simply cannot be an analysis.
def check_for_project_cc(folder_path):
    found_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower() == 'project_cc.yaml':
                found_files.append(os.path.join(root, filename))

    # Check the results
    if len(found_files) == 0:
        print(f"We did not find a Project CC in your folder. We cannot run a compliance analysis without a Project CC.")
        sys.exit()
    elif len(found_files) == 1:
        print(f"We found exactly one Project CC in your folder. Great job!:")
        print(f"  - {found_files[0]}")
        run_compliance_analysis(folder_path)
    else:
        print(f"Multiple Project CCs found:")
        for file_path in found_files:
            print(f"  - {file_path}")
        print("We found multiple Project CCs in your folder. There should only be one Project CC per project.")

def run_compliance_analysis(folder_path):

    # Load the Project CC YAML file from the supplied folder. This will be our starting point. 
    with open(folder_path + 'project_cc.yaml', 'r') as file:
        project_cc_yaml = yaml.safe_load(file)

    # Determine project type (AI system vs. GPAI model) as well as operator type. We will use these for different things.
    set_type(project_variables, project_cc_yaml)
    set_operator_role_and_location(project_variables, project_cc_yaml)
    set_eu_market_status(project_cc_yaml)

    # Check if the project is within scope of the Act. If it's not, the analysis is over.
    if check_within_scope(project_cc_yaml):
        print("Project is within the scope of Act. Let's continue...") 
    else: 
        sys.exit("Project is not within the scope of what is regulated by the Act.")

    # Check for prohibited practices. If any exist, the analysis is over.
    if check_prohibited(project_cc_yaml) == True: 
        print("Project contains prohibited practices and is therefore non-compliant.")
        sys.exit("Project is non-compliant due to a prohibited practice.")
    else: 
        print("Project does not contain prohibited practies. Let's continue...")

    # If project is high-risk AI system, check that is has met all the requirements for such systems: 

    if high_risk_ai_system:

    # Do this by examining the Project CC

        for key, value in project_cc_yaml['risk_management_system']:
            if not value:
                sys.exit("Because of project-level characteristics, this high-risk AI system fails the risk management requirements under Article 9.")
        for key, value in project_cc_yaml['technical_documentation']:
            if not value:
                sys.exit("Because of project-level characteristics, this high-risk AI system fails the risk management requirements under Article 11.")            
        for key, value in project_cc_yaml['record_keeping']:
            if not value:
                sys.exit("Because of project-level characteristics, this high-risk AI system fails the risk management requirements under Article 12.")     
        for key, value in project_cc_yaml['transparency_and_provision_of_information_to_deployers']:
            if not value:
                sys.exit("Because of project-level characteristics, this high-risk AI system fails the transparency requirements under Article 13.")  
        for key, value in project_cc_yaml['human_oversight']:
            if not value:
                sys.exit("Because of project-level characteristics, this high-risk AI system fails the human oversight requirements under Article 14.")  
        for key, value in project_cc_yaml['accuracy_robustness_cybersecurity']:
            if not value:
                sys.exit("Because of project-level characteristics, this high-risk AI system fails the accuracy, robustness, and cybersecurity requirements under Article 15.")  
        for key, value in project_cc_yaml['quality_management_system']:
            if not value:
                sys.exit("Because of project-level characteristics, this high-risk AI system fails the accuracy, robustness, and cybersecurity requirements under Article 17.") 

    # Do this by examining any and all Data CCs too

        for filename in os.listdir(folder_path):
            # Check if the search word is in the filename
            if "data_cc.md" in filename.lower():

                # If it is, load the yaml

                with open(folder_path + filename, 'r') as file:
                    data_cc_yaml = yaml.safe_load(file)

                for key, value in data_cc_yaml['data_and_data_governance']:
                    if not value:
                        sys.exit(f"Because of the dataset represented by {filename}, this high-risk AI system fails the data and data governance requirements under Article 10.")
                for key, value in data_cc_yaml['technical_documentation']:
                    if not value:
                        sys.exit(f"Because of the dataset represented by {filename}, this high-risk AI system fails the technical documentation requirements under Article 11.")
                for key, value in data_cc_yaml['transparency_and_provision_of_information_to_deployers']:
                    if not value:
                        sys.exit(f"Because of the dataset represented by {filename}, this high-risk  AI system fails the transparency requirements under Article 13.")
                for key, value in data_cc_yaml['quality_management_system']:
                    if not value:
                        sys.exit(f"Because of the dataset represented by {filename}, this high-risk  AI system fails the quality management requirements under Article 17.")

    # Do this by examining any and all Model CCs too

        for filename in os.listdir(folder_path):
            # Check if the search word is in the filename
            if "model_cc.md" in filename.lower():

                # If it is, load the yaml

                with open(folder_path + filename, 'r') as file:
                    model_cc_yaml = yaml.safe_load(file)

                for key, value in model_cc_yaml['risk_management_system']:
                    if not value:
                        sys.exit(f"Because of the model represented by {filename}, this high-risk AI system fails the risk management requirements under Article 9.")
                for key, value in data_cc_yaml['technical_documentation']:
                    if not value:
                        sys.exit(f"Because of the model represented by {filename}, this high-risk AI system fails the technical documentation requirements under Article 11.")
                for key, value in data_cc_yaml['transparency_and_provision_of_information_to_deployers']:
                    if not value:
                        sys.exit(f"Because of the model represented by {filename}, this high-risk  AI system fails the transparency requirements under Article 13.")
                for key, value in data_cc_yaml['accuracy_robustness_cybersecurity']:
                    if not value:
                        sys.exit(f"Because of the model represented by {filename}, this high-risk  AI system fails the quality management requirements under Article 15.")
                for key, value in data_cc_yaml['quality_management_system']:
                    if not value:
                        sys.exit(f"Because of the model represented by {filename}, this high-risk  AI system fails the quality management requirements under Article 17.")

    # If the project is a GPAI model, check that is has met all the requirements for such systems: 

    if gpai_model:

    # Do this by examining the Project CC

        for key, value in project_cc_yaml['gpai_model_provider_obligations']:
            if not value:
                sys.exit("GPAI model fails the transparency requirements under Article 53.")

    # Do this by examining any and all Data CCs too

        for filename in os.listdir(folder_path):
            # Check if the search word is in the filename
            if "data_cc.md" in filename.lower():

                # If it is, load the yaml

                with open(folder_path + filename, 'r') as file:
                    data_cc_yaml = yaml.safe_load(file)

                for key, value in data_cc_yaml['gpai_requirements']['gpai_requirements']:
                    if not value:
                        sys.exit(f"Because of the dataset represented by {filename}, this GPAI fails the transparency requirements under Article 53.")

    # Do this by examining any and all Model CCs too
    
        for filename in os.listdir(folder_path):
            # Check if the search word is in the filename
            if "model_cc.md" in filename.lower():

                # If it is, load the yaml

                with open(folder_path + filename, 'r') as file:
                    model_cc_yaml = yaml.safe_load(file)

                for key, value in model_cc_yaml['obligations_for_providers_of_gpai_models']:
                    if not value:
                        sys.exit(f"Because of the model represented by {filename}, this GPAI fails the transparency requirements under Article 53.")

    # If the project is a GPAI model with systematic risk, check that is has additionally met all the requirements for such systems: 

    if gpai_model_systematic_risk:

    # Do this by examining the Project CC

        for key, value in project_cc_yaml['gpai_obligations_for_systemic_risk_models']:
            if not value:
                sys.exit("GPAI model with systematic risk fails the transparency requirements under Article 55.")

    # Do this by examining any and all Model CCs too

        for filename in os.listdir(folder_path):
            # Check if the search word is in the filename
            if "model_cc.md" in filename.lower():

                # If it is, load the yaml

                with open(folder_path + filename, 'r') as file:
                    model_cc_yaml = yaml.safe_load(file)

                for key, value in model_cc_yaml['obligations_for_providers_of_gpai_models_with_systemic_risk']:
                    if not value:
                        sys.exit(f"Because of the model represented by {filename}, this GPAI model with systematic risk fails the transparency requirements under Article 55.")

def set_type(project_variables, project_cc_yaml):
    ai_system = project_variables['ai_project_type']['ai_system']
    gpai_model = project_variables['ai_project_type']['gpai_model']
    if project_cc_yaml['ai_system']['ai_system']['value']:
        ai_system = True
    if project_cc_yaml['gpai_model']['gpai_model']['value']:
        gpai_model = True
    if ai_system and gpai_model:
        sys.exit("Your project cannot be both an AI system and a GPAI model. Please revise your Project CC accordingly.")
    if ai_system == True:
        for key, value in project_cc_yaml['high_risk_ai_system']:
            if value and sum(map(bool, [project_cc_yaml['high_risk_ai_system']['filter_exception_rights'],project_cc_yaml['high_risk_ai_system']['filter_exception_narrow'],project_cc_yaml['high_risk_ai_system']['filter_exception_human'],project_cc_yaml['high_risk_ai_system']['filter_exception_deviation'], project_cc_yaml['high_risk_ai_system']['filter_exception_prep']])) < 1:
                high_risk_ai_system == True
    if gpai_model == True:
        if project_cc_yaml['gpai_model_systematic_risk']['evaluation'] or project_cc_yaml['gpai_model_systematic_risk']['flops']:
            gpai_model_systematic_risk == True

def set_operator_role_and_location(project_variables, project_cc_yaml):
    operators = 0
    
    ai_system = project_variables['ai_project_type']['ai_system']
    gpai_model = project_variables['ai_project_type']['gpai_model']
    
    for var in project_variables['operator_role']:
        if project_cc_yaml['operator_role'][f'{var}']['value']:
            project_variables['operator_role'][f'{var}'] = True
            operators += 1 
        
    if ai_system and gpai_model:
        sys.exit("Your project cannot be both an AI system and a GPAI model. Please revise your Project CC accordingly.")
    if operators != 1:
        sys.exit("Please specify exactly one operator role.")
    
    return project_variables

def set_eu_market_status(project_cc_yaml):
    if project_cc_yaml['eu_market']['placed_on_market']['value']:
        placed_on_market = True
    if project_cc_yaml['eu_market']['put_into_service']['value']: 
        put_into_service = True
    if project_cc_yaml['operator_role']['output_used']['value']:
        output_used == True

def check_within_scope(project_cc):
    if not check_excepted(project_cc):
        if provider and ((ai_system and (placed_on_market or put_into_service)) or (gpai_model and placed_on_market)):   # Article 2.1(a)
            return True
        if deployer and eu_located: # Article 2.1(b)
            return True
        if (provider or deployer) and (ai_system and eu_located and output_used): # Article 2.1(c)
            return True
        if (importer or distributor) and ai_system: # Article 2.1(d)
            return True
        if product_manufacturer and ai_system and (placed_on_market or put_into_service): # Article 2.1(e)
            return True
    else:
        return False

def check_excepted(project_cc_yaml):
    if project_cc_yaml['excepted']['scientific'] or project_cc_yaml['excepted']['pre_market'] or (ai_system and project_cc_yaml['excepted']['open_source_ai_system']) or (gpai_model and project_cc_yaml['excepted']['open_source_gpai_system']):
        return True
    else:
        return False 

def check_prohibited (project_cc_yaml):
    if ai_system:
        for key in project_cc_yaml['prohibited_practice']['ai_system']:
            if key[value]: 
                print("You are engaged in a prohibited practice and thus the project is non-compliant.")
                return True
    if project_cc_yaml['prohibited_practice']['biometric']['categorization']:
        print("You are engaged in a prohibited practice and thus the project is non-compliant.")
        return True
    if project_cc_yaml['prohibited_practice']['biometric']['real_time'] and sum(map(bool, [project_cc['prohibited_practice']['biometric']['real_time_exception_victim'],project_cc['prohibited_practice']['biometric']['real_time_exception_threat'], project_cc['prohibited_practice']['biometric']['real_time_exception_investigation']])) == 0:
        print("You are engaged in a prohibited practice and thus the project is non-compliant.")
        return True
    else: 
        print("You are not engaged in any prohibited practices.")
        return False





def check_all_true(file_path):
    # Load the YAML file
    with open("./project_cc.yaml", 'r') as file:
        data = yaml.safe_load(file)

    # Iterate through top-level keys
    for top_key, top_value in data.items():
        if isinstance(top_value, dict):
            # Iterate through second-level keys
            for second_key, second_value in top_value.items():
                if not second_value:
                    print("You are non-compliant with the Act")
                    break
            else:
                print("No problems here")

def main():
    # Prompt the user to enter a filename
    file_path = "./" # input("Please enter a file path to the folder containing all your AI project's Compliance Cards: ")

    # Call the function with the entered filename
    check_for_project_cc(file_path)

if __name__ == "__main__":
    main()