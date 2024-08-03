smb_status:
  smb_status: # Art. 11(1) 
    verbose: 'AI project is operated by a small or medium-sized enterprise' 
    value: !!bool false

eu_market_status:
  placed_on_market_status: # Art. 3(9)
    verbose: 'AI project is being made available on the Union market for the first time'
    value: !!bool false 
  put_into_service_status: #Art. 3(11)
    verbose: 'AI project is supplied for first use directly to the deployer or for own use in the Union for its intended purpose;'

ai_project_owner_role:
  provider_status: # Art. 2
    verbose: 'The owner of this AI project is a natural or legal person, public authority, agency or other body that develops an AI system or a general-purpose AI model or that has an AI system or a general-purpose AI model developed and places it on the market or puts the AI system into service under its own name or trademark, whether for payment or free of charge'
    value: !!bool false 
  on_market_status: # Art 2 
    verbose: "AI project is placed on the market or put into service in the Union"
    value: !!bool false  
  deployer_status: # Art. 2
    verbose: 'The owner of this AI project is a natural or legal person, public authority, agency or other body using an AI system under its authority except where the AI system is used in the course of a personal non-professional activity'
    value: !!bool false 
  eu_location_status: # Art. 2
    verbose: 'The owner of this AI project has its place of establishment or location within the Union'
    value: !!bool true  
  output_status: # Art. 2
    verbose: 'the output produced by the AI system is used in the Union'
    value: !!bool true 
  importer_status: # Art. 2 
    verbose: 'AI project owner is a natural or legal person located or established in the Union that places on the market an AI system that bears the name or trademark of a natural or legal person established in a third country'
    value: !!bool true 
  distributor_status:
    verbose: 'a natural or legal person in the supply chain, other than the provider or the importer, that makes an AI system available on the Union market'
    value: !!bool true # Art. 2
  product_manufacturer_status:
    value: !!bool true # Art. 2

ai_system_status:
  ai_system_status: # Art. 3(1)
    verbose: 'AI project is a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments'
    value: !!bool true 

gpai_model_status:
  gpai_model_status: # Art. 3(63)
    verbose: 'AI project is an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks regardless of the way the model is placed on the market and that can be integrated into a variety of downstream systems or applications, except AI models that are used for research, development or prototyping activities before they are placed on the market'
    value: !!bool true  

excepted_use:
  scientific_r_and_d: # Art. 2(6) 
    verbose: 'AI project is or was specifically developed and put into service for the sole purpose of scientific research and development'
    value: !!bool true 
  pre_market: # Art. 2(8) 
    verbose: 'AI project strictly consists of research, testing or development activity of the sort that takes place prior to their being placed on the market or put into service'
    value: !!bool true 
  open_source_gpai: # Art. 53(2)
    verbose: 'AI project involves AI models that are released under a free and open-source licence that allows for the access, usage, modification, and distribution of the model, and whose parameters, including the weights, the information on the model architecture, and the information on model usage, are made publicly available. This exception shall not apply to general purpose AI models with systemic risks'
    value: !!bool true  

prohibited_ai_practice_status:
  manipulative: # Art. 5(1)(a)
    verbose: 'This AI system deploys subliminal or purposefully manipulative or deceptive techniques, with the objective or effect of materially distorting the behavior of people by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause significant harm'
    value: !!bool false 
  exploit_vulnerable: # Art. 5(1)(b)
    verbose: 'This AI system exploits the vulnerabilities of natural people due to their age, disability or a specific social or economic situation, with the objective or effect of materially distorting their behaviour in a manner that causes or is reasonably likely to cause significant harm'
    value: !!bool false 
  social_score: # Art. 5(1)(c)
    verbose: 'This AI system is for the evaluation or classification of natural people over a certain period of time based on their social behaviour or known, inferred or predicted personal or personality characteristics, with the social score leading to at least one of the following: (i) detrimental or unfavourable treatment of certain natural people in social contexts that are unrelated to the contexts in which the data was originally generated or collected; (ii) detrimental or unfavourable treatment of certain natural people that is unjustified or disproportionate to their social behaviour or its gravity'
    value: !!bool false 
  crime_prediction:  # Art. 5(1)(d)
    verbose: 'This AI system makes risk assessments of natural persons in order to assess or predict the risk of them committing a criminal offence, based solely on the profiling of the natural person or on assessing their personality traits and characteristics (and does not support the human assessment of the involvement of a person in a criminal activity, which is already based on objective and verifiable facts directly linked to a criminal activity)'
    value: !!bool false
  untarged_face: # Art. 5(1)(e)
    verbose: 'This AI systems creates or expand facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage'
    value: !!bool false 
  emotion_prediction: # Art. 5(1)(f)
    verbose: 'This AI systems infer emotions of a natural person in the areas of workplace and education institutions and is not intended to be put in place or into the market for medical or safety reasons'
    value: !!bool false 

high_risk_ai_system_status:
  safety_component: # Art. 6(1)(a)
    verbose: 'AI project is intended to be used as a safety component of a product'
    value: !!bool false 
  product_covered_by_machinery_regulation: # Art. 6(1)(b); Annex I
    verbose: 'AI project is itself a product, covered by Directive 2006/42/EC of the European Parliament and of the Council of 17 May 2006 on machinery, and amending Directive 95/16/EC (OJ L 157, 9.6.2006, p. 24) [as repealed by the Machinery Regulation]'
    value: !!bool false 
  product_covered_by_toy_safety_regulation: # Art. 6(1)(b); Annex I
    verbose: 'AI project is itself a product, covered by Directive 2009/48/EC of the European Parliament and of the Council of 18 June 2009 on the safety of toys (OJ L 170, 30.6.2009, p. 1)'
    value: !!bool false 
  product_covered_by_watercraft_regulation: # Art. 6(1)(b); Annex I
    verbose: 'AI project is itself a product, covered by Directive 2013/53/EU of the European Parliament and of the Council of 20 November 2013 on recreational craft and personal watercraft and repealing Directive 94/25/EC (OJ L 354, 28.12.2013, p. 90)'
    value: !!bool false 
  biometric_categorization: # Art. 6(2); Annex III(1)(b)
    verbose: 'AI project is intended to be used for biometric categorisation, according to sensitive or protected attributes or characteristics based on the inference of those attributes or characteristics'
    value: !!bool false 
  emotion_recognition: # Art. 6(2); Annex III(1)(c)
    verbose: 'AI project is intended to be used for emotion recognition'
    value: !!bool false 
  critical_infrastructure: # Art. 6(2); Annex III(2)
    verbose: 'AI project is intended to be used as safety components in the management and operation of critical digital infrastructure, road traffic, or in the supply of water, gas, heating or electricity'
    value: !!bool false 
  educational: # Art. 6(2); Annex III(3)(a)
    verbose: 'AI project is intended to be used to determine access or admission or to assign natural persons to educational and vocational training institutions at all levels'
    value: !!bool false 
  recruitment: # Art. 6(2); Annex III(4)(a)
    verbose: 'AI project is intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates'
    value: !!bool false 
  public_assistance: # Art. 6(2); Annex III(5)(a)
    verbose: 'AI project is intended to be used by public authorities or on behalf of public authorities to evaluate the eligibility of natural persons for essential public assistance benefits and services, including healthcare services, as well as to grant, reduce, revoke, or reclaim such benefits and services'
    value: !!bool false 
  victim_assessment: # Art. 6(2); Annex III(6)(a)
    verbose: 'AI project is intended to be used by or on behalf of law enforcement authorities, or by Union institutions, bodies, offices or agencies in support of law enforcement authorities or on their behalf to assess the risk of a natural person becoming the victim of criminal offences'
    value: !!bool false 
  polygraph: # Art. 6(2); Annex III(7)(a)
    verbose: 'AI project is intended to be used by or on behalf of competent public authorities or by Union institutions, bodies, offices or agencies as polygraphs or similar tools'
    value: !!bool false 
  judicial: # Art. 6(2); Annex III(8)(a)
    verbose: 'AI project is intended to be used by a judicial authority or on their behalf to assist a judicial authority in researching and interpreting facts and the law and in applying the law to a concrete set of facts, or to be used in a similar way in alternative dispute resolution'
    value: !!bool false 
  filter_exception_rights: # Art. 6(3)
    verbose: 'The AI initiate does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making'
    value: !!bool true 
  filter_exception_narrow: # Art. 6(3)(a)
    verbose: 'The AI project is intended to perform a narrow procedural task'
    value: !!bool false
  filter_exception_narrow: # Art. 6(3)(b)
    verbose: 'the AI project is intended to improve the result of a previously completed human activity'
    value: !!bool false
  filter_exception_deviation: # Art. 6(3)(c)
    verbose: 'the AI system is intended to detect decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review'
    value: !!bool false
  filter_exception_deviation: # Art. 6(3)(d)
    verbose: 'the AI system is intended to perform a preparatory task to an assessment relevant for the purposes of the use cases listed in Annex III.'
    value: !!bool false 

risk_management_system:
  established: # Article 9
    verbose: 'Risk management system has been established, implemented, documented and maintained for AI system'
    value: !!bool false 
  lifecycle: # Art. 9(2)
    verbose: 'Risk management system (high-risk AI system) has been planned, run, reviewed, and updated, throughout the entire lifecycle of AI system'
    value: !!bool false 
  risk_analysis_intended: # Art. 9(2)(a)
    verbose: 'Risk management system for AI system includes the identification and analysis of any known or reasonably foreseeable risks that the AI system might pose to health, safety or fundamental rights when used in accordance with its intended purpose'
    value: !!bool false 
  risk_estimation_foreseeable: # Art. 9(2)(b)
    verbose: 'Risk management system for AI system includes the estimation and evaluation of the risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse;
    value: !!bool false 
  risk_post_market: # Art. 9(2)(c)
    verbose: 'Risk management system for AI system includes the evaluation of other risks possibly arising, based on the analysis of data gathered from the post-market monitoring system'
    value: !!bool false   
  risk_management_measures: # Art. 9(2)(d)
    verbose: 'Where risk that the AI system might pose to health, safety or fundamental rights when used in accordance with its intended purpose have been identified, appropriate and targeted risk management measures designed to address the risks have been adopted'
    value: !!bool false 
  documentation: # Art. 9(5)
    verbose: 'Where risk that the AI system might pose to health, safety or fundamental rights when used in accordance with its intended purpose have been identified, these risks have been documented and communicated to deployers and either eliminated, if feasible, or mitigated such that any residual risk is judged to be acceptable'
    value: !!bool false 
  tested: # Art. 9(6)
    verbose: 'To determine the right mitigations, and to show the high-risk AI system performs consistently its intended purpose and is in compliance with the risk management requirements, the AI system has been tested'
    value: !!bool false 
  testing_threshold: # Art. 9(8)
    verbose: 'Testing has or will be performed before the AI system is placed on the market and has or will be carried out against prior defined metrics and probabilistic thresholds that are appropriate to the intended purpose'
    value: !!bool false 

technical_documentation:
  drawn_up: # Art. 11(1)
    verbose: 'Technical documentation for the high-risk AI system has been drawn up before the system has been placed on the market or put into service and will be kept up-to date'
    value: !!bool false 
  intended_purpose: # Art. 11(1); Annex IV(1)(a)
    verbose: 'The Technical Documentation includes a general description of the AI system that covers its intended purpose, the name of the provider and the version of the system reflecting its relation to previous versions'
    value: !!bool false 
  interaction: # Art. 11(1); Annex IV(1)(b)
    verbose: 'The Technical Documentation includes a general description of the AI system that covers how the AI system interacts with, or can be used to interact with, hardware or software, including with other AI systems, that are not part of the AI system itself, where applicable'
   value: !!bool false 
  versions: # Art. 11(1); Annex IV(1)(c)
    verbose: 'Technical Documentation includes a general description of the AI system that covers the versions of relevant software or firmware, and any requirements related to version updates'
    value: !!bool false 
  packages: # Art. 11(1); Annex IV(1)(d)
    verbose: 'Technical Documentation includes a general description of the AI system that covers the description of all the forms in which the AI system is placed on the market or put into service, such as software packages embedded into hardware, downloads, or APIs'
    value: !!bool false 
  hardware: # Art. 11(1); Annex IV(1)(e)
    verbose: 'Technical Documentation includes a general description of the AI system that covers the description of the hardware on which the AI system is intended to run'
    value: !!bool false 
  development_steps: # Art. 11(1); Annex IV(2)(a)
    verbose: 'Technical Documentation includes a detailed description of the elements of the AI system and of the process for its development, covering the methods and steps performed for the development of the AI system, including, where relevant, recourse to pre-trained systems or tools provided by third parties and how those were used, integrated or modified by the provider'
    value: !!bool false 
  design_specs: # Art. 11(1); Annex IV(2)(b)
    verbose: 'Technical Documentation includes a detailed description of the elements of the AI system and of the process for its development, covering the design specifications of the system, namely the general logic of the AI system and of the algorithms; the key design choices including the rationale and assumptions made, including with regard to persons or groups of persons in respect of who, the system is intended to be used; the main classification choices; what the system is designed to optimise for, and the relevance of the different parameters; the description of the expected output and output quality of the system; the decisions about any possible trade-off made regarding the technical solutions adopted to comply with the requirements set out in Chapter III, Section 2'
    value: !!bool false 
  risk_management: # Art. 11(1); Annex IV(5)
    verbose: 'Technical Documentation includes a detailed description of the risk management system in accordance with Article 9'
    value: !!bool false 
  changes: # Art. 11(1); Annex IV(6)
    verbose: 'Technical Documentation includes a description of relevant changes made by the provider to the system through its lifecycle'
    value: !!bool false 
  declaration_of_conformity: # Art. 11(1); Annex IV(8)
    verbose: 'Technical Documentation includes a copy of the EU declaration of conformity referred to in Article 47'
    value: !!bool false 
  post_market: # Art. 11(1); Annex IV(9)
    verbose: 'Technical Documentation includes a detailed description of the system in place to evaluate the AI system performance in the post-market phase in accordance with Article 72, including the post-market monitoring plan referred to in Article 72(3)'
    value: !!bool false 
  product: # Art. 11(2)
    verbose: 'High-risk AI system is either not related to a product covered by the Union harmonisation legislation listed in Section A of Annex I and placed on the market or put into service or, if it is, a single set of technical documentation has been drawn up containing all the information set out in paragraph 1, as well as the information required under those legal acts'
    value: !!bool false 

record_keeping:
  logging_generally: # Article 12(1)
    verbose: 'The AI system technically allows for the automatic recording of events (logs) over the lifetime of the system'
    value: !!bool false 
  logging_risk: # Art. 12(1)(a)
    verbose: 'The AI system technically allows for the automatic recording of events (logs) over the lifetime of the system and these logging capabilities enable the recording of events relevant for identifying situations that may result in the high-risk AI system presenting a risk within the meaning of Article 79(1) or in a substantial modification'
    value: !!bool false 
  logging_post_market: # Art. 12(1)(b)
    verbose: 'The AI system technically allows for the automatic recording of events (logs) over the lifetime of the system and these logging capabilities enable the recording of events relevant for facilitating the post-market monitoring referred to in Article 72'
    value: !!bool false 
  monitoring: # Art. 12(1)(c)
    verbose: 'The AI system technically allows for the automatic recording of events (logs) over the lifetime of the system and these logging capabilities enable the recording of events relevant for monitoring the operation of high-risk AI systems referred to in Article 26(5)'
    value: !!bool false 
  recording_use: # Art. 12(2)(a)
    verbose: 'For the remote biometric identification systems high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum, the recording of the period of each use of the system (start date and time and end date and time of each use)'
    value: !!bool false 
  reference_db: # Art. 12(2)(b)
    verbose: 'For the remote biometric identification systems high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum, the reference database against which input data has been checked by the system'
    value: !!bool false 
  input: # Art. 12(2)(c)
    verbose: 'For the remote biometric identification systems high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum, the input data for which the search has led to a match'
    value: !!bool false 
  'For the remote biometric identification systems high-risk AI systems referred to in point 1 (a), of Annex III, the logging capabilities shall provide, at a minimum, the identification of the natural persons involved in the verification of the results, as referred to in Article 14(5)': !!bool false # Art. 12(2)(d)

transparency_and_provision_of_information_to_deployers:
  'AI system is designed and developed to ensure operation is sufficiently transparent for deployers to interpret output and use appropriately': !!bool true # Art. 13(1)
  'AI system is designed and developed with transparency to ensure compliance with provider and deployer obligations in Section 3': !!bool true # Art. 13(1)
  'AI system is accompanied by instructions for use in appropriate digital format or otherwise, with concise, complete, correct, clear, relevant, accessible, and comprehensible information for deployers': !!bool true # Art. 13(2)
  'Instructions include provider identity and contact details, and if applicable, authorized representative details': !!bool true # Art. 13(3)(a)
  'Instructions include AI system characteristics, capabilities, performance limitations, and intended purpose': !!bool true # Art. 13(3)(b)(i)
  'Instructions include accuracy metrics, robustness, cybersecurity, and potential impacts on these': !!bool true # Art. 13(3)(b)(ii)
  'Instructions include foreseeable circumstances that may risk health, safety, or fundamental rights': !!bool true # Art. 13(3)(b)(iii)
  'Instructions include technical capabilities to provide information relevant to explaining output': !!bool true # Art. 13(3)(b)(iv)
  'Instructions include performance regarding specific persons or groups, if applicable': !!bool true # Art. 13(3)(b)(v)
  'Instructions include input data specifications and relevant training, validation, and testing dataset information': !!bool true # Art. 13(3)(b)(vi)
  'Instructions include information to enable deployers to interpret and appropriately use AI system output': !!bool true # Art. 13(3)(b)(vii)
  'Instructions include predetermined changes to AI system and its performance since initial conformity assessment': !!bool true # Art. 13(3)(c)
  'Instructions include human oversight measures and technical measures for output interpretation': !!bool true # Art. 13(3)(d)
  'Instructions include computational and hardware resource needs, expected lifetime, and maintenance measures': !!bool true # Art. 13(3)(e)
  'Instructions include description of mechanisms for deployers to collect, store, and interpret logs, if applicable': !!bool true # Art. 13(3)(f)

human_oversight:
  'AI system is designed and developed to be effectively overseen by natural persons during use, including appropriate human-machine interface tools': !!bool true # Art. 14(1)
  'Human oversight aims to prevent or minimize risks to health, safety, or fundamental rights during intended use or foreseeable misuse': !!bool true # Art. 14(2)
  'Oversight measures are commensurate with risks, autonomy level, and use context, ensured through provider-built measures and/or deployer-implemented measures': !!bool true # Art. 14(3)
  'AI system enables assigned persons to understand its capacities and limitations, monitor operation, and detect anomalies': !!bool true # Art. 14(4)
  'AI system enables assigned persons to be aware of potential automation bias': !!bool true # Art. 14(4)(a)
  'AI system enables assigned persons to correctly interpret its output': !!bool true # Art. 14(4)(c)
  'AI system enables assigned persons to decide not to use it or override its output': !!bool true # Art. 14(4)(d)
  'AI system enables assigned persons to intervene or halt the system through a stop button or similar procedure': !!bool true # Art. 14(4)(e)
  'For Annex III point 1(a) systems, actions or decisions require verification by at least two competent persons, with exceptions for law enforcement, migration, border control, or asylum': !!bool true # Art. 14(5)

accuracy_robustness_cybersecurity:
  'AI system is designed and developed to achieve appropriate levels of accuracy, robustness, and cybersecurity, performing consistently throughout its lifecycle': !!bool true # Art. 15(1)
  'Commission encourages development of benchmarks and measurement methodologies for accuracy and robustness': !!bool true # Art. 15(2)
  'Accuracy levels and relevant metrics are declared in accompanying instructions of use': !!bool true # Art. 15(3)
  'AI system is resilient against errors, faults, or inconsistencies, with technical and organizational measures implemented': !!bool true # Art. 15(4)
  'AI system that continues learning after deployment is designed to eliminate or reduce risk of biased outputs influencing future operations': !!bool true # Art. 15(4)
  'AI system is resilient against unauthorized third-party attempts to alter use, outputs, or performance': !!bool true # Art. 15(5)
  'Cybersecurity solutions are appropriate to relevant circumstances and risks': !!bool true # Art. 15(5)
  'Technical solutions address AI-specific vulnerabilities, including measures against data poisoning, model poisoning, adversarial examples, and confidentiality attacks': !!bool true # Art. 15(5)

quality_management_system:
  'Initiative is subject to a quality management system with strategy for regulatory compliance': !!bool true # Art. 17(1)(a)
  'System includes techniques, procedures, and actions for design, control, and verification of high-risk AI system': !!bool true # Art. 17(1)(b)
  'System includes techniques, procedures, and actions for development, quality control, and quality assurance': !!bool true # Art. 17(1)(c)
  'System includes examination, test, and validation procedures before, during, and after development': !!bool true # Art. 17(1)(d)

transparency_obligations:
  'Providers of AI systems generating synthetic content ensure outputs are marked and detectable as artificially generated': !!bool true # Art. 50(2)
  'Technical solutions for marking are effective, interoperable, robust, and reliable': !!bool true # Art. 50(2)

gpai_model_classification:
  'Model impact capabilities evaluated using appropriate technical tools and methodologies': !!bool true # Art. 51
  'Cumulative compute for training measured in floating point operations (FLOPs)': !!bool true # Art. 51(2)

gpai_model_provider_obligations:
  'Provide information on intended tasks, integration types, and acceptable use policies': !!bool true # Art. 53(1)(a); Annex XI(1)(1)(a-c)
  'Provide details on model architecture, parameters, input/output modalities, and license': !!bool true # Art. 53(1)(a); Annex XI(1)(1)(d-f)
  'Describe training methodologies, key design choices, and optimization goals': !!bool true # Art. 53(1)(b); Annex XI(1)(2)(b)
  'Provide information on training, testing, and validation data': !!bool true # Art. 53(1)(b); Annex XI(1)(2)(c)
  'Disclose computational resources and energy consumption for training': !!bool true # Art. 53(1)(b); Annex XI(1)(2)(d-e)
  'Describe evaluation strategies, results, and adversarial testing measures': !!bool true # Art. 53(1)(b); Annex XI(2)(1-2)

obligations_to_downstream_providers:
  'Provide general description of GPAI model, including intended tasks and integration types': !!bool true # Art. 53(1)(b); Annex XII(1)(a-h)
  'Describe model elements, development process, and integration requirements': !!bool true # Art. 53(1)(b); Annex XII(2)(a-c)

obligations_for_systemic_risk_models:
  'Perform model evaluation using standardized protocols and conduct adversarial testing': !!bool true # Art. 55(1)(a)
  'Assess and mitigate possible systemic risks at Union level': !!bool true # Art. 55(1)(b)
  'Ensure adequate cybersecurity protection for the model and infrastructure': !!bool true # Art. 55(1)(d)

