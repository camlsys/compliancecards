import yaml
   
def set_type(project_variables, project_cc_yaml):

    project_type = None
    
    ai_system = project_variables['ai_project_type']['ai_system']
    gpai_model = project_variables['ai_project_type']['gpai_model']
    
    if project_cc_yaml['ai_system']['ai_system']['value']:
        ai_system = True
    if project_cc_yaml['gpai_model']['gpai_model']['value']:
        gpai_model = True
    if ai_system and gpai_model:
        msg = ("Your project cannot be both an AI system and a GPAI model. Please revise your Project CC accordingly.")
    if ai_system == True:
        for key, value in project_cc_yaml['high_risk_ai_system']:
            if value and sum(map(bool, [project_cc_yaml['high_risk_ai_system']['filter_exception_rights'],project_cc_yaml['high_risk_ai_system']['filter_exception_narrow'],project_cc_yaml['high_risk_ai_system']['filter_exception_human'],project_cc_yaml['high_risk_ai_system']['filter_exception_deviation'], project_cc_yaml['high_risk_ai_system']['filter_exception_prep']])) < 1:
                project_type = "high_risk_ai_system"
                
    if gpai_model == True:
        if project_cc_yaml['gpai_model_systematic_risk']['evaluation'] or project_cc_yaml['gpai_model_systematic_risk']['flops']:
            project_type = "gpai_model_systematic_risk"
            
    return project_type

def set_operator_role_and_location(project_variables, project_cc_yaml):
    operators = 0
    
    ai_system = project_variables['ai_project_type']['ai_system']
    gpai_model = project_variables['ai_project_type']['gpai_model']
    
    for var in project_variables['operator_role']:
        if project_cc_yaml['operator_role'][f'{var}']['value']:
            project_variables['operator_role'][f'{var}'] = True
            operators += 1 
        
    if ai_system and gpai_model:
        msg = ("Your project cannot be both an AI system and a GPAI model. Please revise your Project CC accordingly.")
    if operators != 1:
        msg = ("Please specify exactly one operator role.")
    
    return project_variables

def set_eu_market_status(project_variables, project_cc_yaml):
    
    if project_cc_yaml['eu_market_status']['placed_on_market']['value']:
        project_variables['eu_market_status']["placed_on_market"] = True
    if project_cc_yaml['eu_market_status']['put_into_service']['value']:
        project_variables['eu_market_status']["put_into_service"] = True
        
    if project_cc_yaml['operator_role']['output_used']['value']:
        project_variables['operator_role']["output_used"] = True
        
    return project_variables


def check_within_scope(project_cc_yaml):
    if not check_excepted(project_cc_yaml):
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

# def check_prohibited (project_cc_yaml):
#     if ai_system:
#         for key in project_cc_yaml['prohibited_practice']['ai_system']:
#             if key[value]: 
#                 print("You are engaged in a prohibited practice and thus the project is non-compliant.")
#                 return True
#     if project_cc_yaml['prohibited_practice']['biometric']['categorization']:
#         print("You are engaged in a prohibited practice and thus the project is non-compliant.")
#         return True
#     if project_cc_yaml['prohibited_practice']['biometric']['real_time'] and sum(map(bool, [project_cc_yaml['prohibited_practice']['biometric']['real_time_exception_victim'],project_cc['prohibited_practice']['biometric']['real_time_exception_threat'], project_cc_yaml['prohibited_practice']['biometric']['real_time_exception_investigation']])) == 0:
#         print("You are engaged in a prohibited practice and thus the project is non-compliant.")
#         return True
#     else: 
#         print("You are not engaged in any prohibited practices.")
#         return False

# def check_all_true(file_path):
#     data = yaml.safe_load(file_path)

#     # Iterate through top-level keys
#     for top_key, top_value in data.items():
#         if isinstance(top_value, dict):
#             # Iterate through second-level keys
#             for second_key, second_value in top_value.items():
#                 if not second_value:
#                     print("You are non-compliant with the Act")
#                     break
#             else:
#                 print("No problems here")