

def set_operator_role_and_location(dispositive_variables, project_cc_yaml):
    operators = 0
    
    ai_system = project_cc_yaml['ai_system']['ai_system']['value']
    gpai_model = project_cc_yaml['gpai_model']['gpai_model']['value']

    for var in project_cc_yaml['operator_details']:
        if project_cc_yaml['operator_details'][f'{var}']['value'] == True:
            dispositive_variables['operator_details'][f'{var}'] = True
            operators += 1 
        
    if ai_system and gpai_model:
        dispositive_variables['project_msg'].append("Your project cannot be both an AI system and a GPAI model. Please revise your Project CC accordingly.")
    if operators != 1:
        dispositive_variables['project_msg'].append("Please specify exactly one operator role.")
    
    return dispositive_variables

def set_eu_market_status(dispositive_variables, project_cc_yaml):
    
    if project_cc_yaml['eu_market_status']['placed_on_market']['value']:
        dispositive_variables['eu_market_status']["placed_on_market"] = True
    if project_cc_yaml['eu_market_status']['put_into_service']['value']:
        dispositive_variables['eu_market_status']["put_into_service"] = True
        
    if project_cc_yaml['operator_details']['output_used']['value']:
        dispositive_variables['operator_details']["output_used"] = True
        
    return dispositive_variables

def check_within_scope_act(dispositive_variables, project_cc_yaml):

    # Check that the project is within the scope of the Act 
    
    ai_system = project_cc_yaml['ai_system']['ai_system']
    gpai_model = project_cc_yaml['gpai_model']['gpai_model']
    placed_on_market = project_cc_yaml['eu_market_status']['placed_on_market']
    put_into_service = project_cc_yaml['eu_market_status']['put_into_service']
    
    eu_located = project_cc_yaml['operator_details']['eu_located']
    output_used = project_cc_yaml['operator_details']['output_used']
    
    if not check_excepted(dispositive_variables, project_cc_yaml):
        if ((ai_system and (placed_on_market or put_into_service)) or (gpai_model and placed_on_market)): # Article 2.1(a)
            return True
        if (ai_system and eu_located and output_used): # Article 2.1(c)
            return True
    else:
        print("Your project is not within the scope of the Act and its requirements.")      
        return False

def check_excepted(dispositive_variables, project_cc_yaml):
    
    if( (project_cc_yaml['ai_system']['ai_system']['value'] == True and project_cc_yaml['excepted']['military']['value']) or
        (project_cc_yaml['ai_system']['ai_system']['value'] == True and project_cc_yaml['excepted']['military_use']['value']) or
        project_cc_yaml['excepted']['scientific']['value'] or 
        project_cc_yaml['excepted']['pre_market']['value'] or 
        (project_cc_yaml['ai_system']['ai_system']['value'] == True and 
         project_cc_yaml['excepted']['open_source_ai_model']['value']  == True) or 
        (project_cc_yaml['gpai_model']['gpai_model']['value'] == True and 
         project_cc_yaml['excepted']['open_source_gpai_model']['value']  == True and
         dispositive_variables['ai_project_type']['gpai_model_systemic_risk'] == False)
    ):
        dispositive_variables['project_msg'].append("Your project falls into one of the exemptions from the Act.")   
        return True
    else:
        return False

def check_prohibited(project_cc_yaml):

    ai_system = project_cc_yaml['ai_system']['ai_system']['value']
    
    if ai_system:
        for key in project_cc_yaml['prohibited_practice']['ai_system']:
            if project_cc_yaml['prohibited_practice']['ai_system'][f'{key}']['value'] == True: 
                print("You are engaged in a prohibited practice and thus the project is non-compliant.")
                return True
    if project_cc_yaml['prohibited_practice']['biometric']['categorization'] == True:
        print("You are engaged in a prohibited practice and thus the project is non-compliant.")
        return True
    if project_cc_yaml['prohibited_practice']['biometric']['real_time'] and \
       sum(map(bool, [project_cc_yaml['prohibited_practice']['biometric']['real_time_exception_victim'],
                       project_cc_yaml['prohibited_practice']['biometric']['real_time_exception_threat'], 
                       project_cc_yaml['prohibited_practice']['biometric']['real_time_exception_investigation']])) == 0:
        print("You are engaged in a prohibited practice and thus the project is non-compliant.")
        return True
    else: 
        print("You are not engaged in any prohibited practices.")
        return False

# def check_article_50():
#     If (project_cc_yaml['article_50']['direct_user_interaction'] == True and project_cc_yaml['article_50']['exception_obvious'] == False and project_cc_yaml['article_50']['exception_law'] == False) and  project_cc_yaml['article_50_obligations']['notice'] == False:
#         print("You are not are not compliance with Article 50(1).")
#         return False  

#     If (project_cc_yaml['article_50']['synthetic_content'] == True and project_cc_yaml['article_50']['exception_assistive'] == False and project_cc_yaml['article_50']['exception_insubstantial'] == False) and project_cc_yaml['article_50_obligations']['marked'] == False: 
#         print("You are not are not compliance with Article 50(2).")
#         return False  

#     If (((project_cc_yaml['article_50']['emotion_reconition'] == True and project_cc_yaml['article_50']['emotion_reconition_law'] == False) or (project_cc_yaml['article_50']['biometric_categorization'] == True and project_cc_yaml['article_50']['biometric_categorization'] == False))) and project_cc_yaml['article_50_obligations']['informed_biometric'] == False:
#         print("You are not are not compliance with Article 50(3).")
#         return False  

#     If ((project_cc_yaml['article_50']['deepfake_not_art'] == True and project_cc_yaml['article_50']['deepfake_law'] == False and ['article_50_obligations']['deepfake_disclosure'] == False) or (project_cc_yaml['article_50']['deepfake_art'] == True and project_cc_yaml['article_50']['deepfake_law'] == False and project_cc_yaml['article_50_obligations']['deepfake_disclosure_art'] == False)):
#         print("You are not are not compliance with Article 50(4).")
#         return False  
