import os
import yaml

#Define a function that creates a list of all the files in the folder. We will use this for different things.
def create_list_of_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            found_files.append(os.path.join(root, filename))

#Define a function that checks for a Project CC. Without this, there cannot be an analysis.
def check_for_project_cc(folder_path):
    found_files = []

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower() == 'project_cc.md':
                found_files.append(os.path.join(root, filename))

    # Check the results
    if len(found_files) == 0:
        print(f"We did not find a Project CC in your folder. We cannot run a compliance analysis without a Project CC.")
    elif len(found_files) == 1:
        print(f"We found exactly one Project CC in your folder. Great job!:")
        print(f"  - {found_files[0]}")
        run_compliance_analysis(folder_path + "project_cc.md")
    else:
        print(f"Multiple Project CCs found:")
        for file_path in found_files:
            print(f"  - {file_path}")
        print("We found multiple Project CCs in your folder. There should only be one Project CC per project.")

def run_compliance_analysis(project_cc)):

    # Load the Project CC's YAML file. This will be our starting point. 
    with open(project_cc, 'r') as file:
        project_cc_yaml = yaml.safe_load(file)

    # Check if the Act does not apply to the project, either because it is not on the EU market or falls into an exception
    
    # Check for prohibited practices -- these are by default non-compliant 

    # Iterate through values of the second-level keys of prohibited_ai_practice_status
    for key, value in project_cc_yaml['prohibited_ai_practice_status']:
        if value:  # This condition will be met whereever a prohibited practice exists 
            print(f"You have a prohibited practice and are non-compliant with the Act")
            break
    else:
        print("No prohibited practices found. That's good...")

    # Check if the key that indicates it is an AI system is present and if its value is true
    if 'AI project is a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments' in projec_cc_yaml and project_cc_yaml['AI project is a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments'] == True:
        print("The project is an AI system.")

        #iterate through all of the 

        all_true = True
        for key in secondary_keys:
            if key in secondary_data and secondary_data[key] == True:
                print(f"The key '{key}' is True in the secondary file.")
            else:
                print(f"The key '{key}' is not True in the secondary file.")
                all_true = False
        
        if all_true:
            print("All specified keys in the secondary file are True.")
        else:
            print("Not all specified keys in the secondary file are True.")
    else:
        print(f"The key '{main_key}' is not True in the main file.")


def check_if_within_scope(project_cc):
    within_scope = None
    if project_cc[ai_project_owner_role][provider_status][value] == True and (project_cc[ai_system_status][ai_system_status][value] == True and (project_cc[eu_market_status][placed_on_market_status][value] == True or project_cc[eu_market_status][put_into_service_status][value] == True)) or (project_cc[gpai_model_status][gpai_model_status][value] == True and (project_cc[eu_market_status][placed_on_market_status][value] == True)):   # Article 2.1(a)
        return True
    if project_cc[ai_project_owner_role][deployer_status][value] == True and project_cc[ai_project_owner_role][eu_location_status][value] == True: # Article 2.1(b)
        return True
    if (project_cc[ai_project_owner_role][provider_status][value] == True or project_cc[ai_project_owner_role][deployer_status][value]== True) and (project_cc[ai_system_status][ai_system_status][value] == True and project_cc[ai_project_owner_role][eu_location_status][value] == True and project_cc[ai_project_owner_role][output_status][value] == True): # Article 2.1(c)
        return True
    if (project_cc[ai_project_owner_role][importer_status][value] == True or project_cc[ai_project_owner_role][distributor_status][value] == True) and project_cc[ai_system_status][ai_system_status][value] == True: # Article 2.1(d)
        return True
    if project_cc[ai_project_owner_role][product_manufacturer_status][value] == True and project_cc[ai_system_status][ai_system_status][value] == True and ((project_cc[eu_market_status][placed_on_market_status][value] == True or project_cc[eu_market_status][put_into_service_status][value] == True)): # Article 2.1(e)
        return True
    else   
        return False

def check_data_ccs(folder_path):

    for filename in os.listdir(folder_path):
        # Check if the search word is in the filename
        if "model_cc.md" in filename.lower():
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            
            # Process the file
            process_file(file_path)


def check_all_true(file_path):
        # Load the YAML file
    with open(project_cc, 'r') as file:
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



# Example usage
main_file = 'main.yaml'
secondary_file = 'secondary.yaml'
main_key = 'data_and_data_governance'
secondary_keys = [
    'Training data is relevant',
    'Training data is sufficiently representative',
    'Training data is, to the best extent possible, free of errors'
]

check_yaml_values(main_file, secondary_file, main_key, secondary_keys)


def main():
    # Prompt the user to enter a filename
    file_path = input("Please enter a file path to the folder containing all your AI project's Compliance Cards: ")

    # Call the function with the entered filename
    check_for_project_cc(file_path)

if __name__ == "__main__":
    main()