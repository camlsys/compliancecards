risk_management_system:
'Known or reasonably foreseeable risks the model can pose to health or safety when used for intended purpose': !!bool true # Art. 9(2)(a)
'Estimation and evaluation of risks when model used for intended purpose': !!bool true # Art. 9(2)(b)
'Estimation and evaluation of risks when model used under conditions of reasonably foreseeable misuse': !!bool true # Art. 9(2)(b)
'Testing to ensure model performs consistently for intended purpose': !!bool true # Art. 9(6)
'Testing to ensure model complies with Act': !!bool true # Art. 9(6)
'Testing against prior defined metrics appropriate to intended purpose': !!bool true # Art. 9(8)
'Testing against probabilistic thresholds appropriate to intended purpose': !!bool true # Art. 9(8)

technical_documentation:
  'Pre-trained elements of model provided by third parties and how used, integrated or modified': !!bool true # Art. 11; Annex IV(2)(a)
  'General logic of model': !!bool true # Art. 11; Annex IV(2)(b)
  'Key design choices including rationale and assumptions made, including with regard to persons or groups on which model intended to be used': !!bool true # Art. 11; Annex IV(2)(b)
  'Main classification choices': !!bool true # Art. 11; Annex IV(2)(b)
  'What model is designed to optimise for and relevance of its different parameters': !!bool true # Art. 11; Annex IV(2)(b)
  'Description of the expected output and output quality of the system': !!bool true # Art. 11; Annex IV(2)(b)
  'Decisions about any possible trade-off made regarding the technical solutions adopted to comply with the requirements set out in Title III, Chapter 2': !!bool true # Art. 11; Annex IV(2)(b)
  'Assessment of the human oversight measures needed in accordance with Article 14, including an assessment of the technical measures needed to facilitate the interpretation of the outputs of AI systems by the deployers, in accordance with Articles 13(3)(d)': !!bool true # Art. 11; Annex IV(2)(e)
  'Validation and testing procedures used, including information about the validation and testing data used and their main characteristics; metrics used to measure accuracy, robustness and compliance with other relevant requirements set out in Title III, Chapter 2 as well as potentially discriminatory impacts; test logs and all test reports dated and signed by the responsible persons, including with regard to predetermined changes as referred to under point (f)': !!bool true # Art. 11; Annex IV(2)(g)
  'Cybersecurity measures put in place': !!bool true # Art. 11; Annex IV(2)(h)

transparency_and_information_provision:
  'Intended purpose': !!bool true # Art. 13(3)(b)(i)
  'Level of accuracy, including its metrics, robustness and cybersecurity referred to in Article 15 against which the high-risk AI system has been tested and validated and which can be expected, and any known and foreseeable circumstances that may have an impact on that expected level of accuracy, robustness and cybersecurity': !!bool true # Art. 13(3)(b)(ii)
  'Any known or foreseeable circumstance, related to the use of the high-risk AI system in accordance with its intended purpose or under conditions of reasonably foreseeable misuse, which may lead to risks to the health and safety or fundamental rights referred to in Article 9(2)': !!bool true # Art. 13(3)(b)(iii)
  'Technical capabilities and characteristics of the AI system to provide information that is relevant to explain its output': !!bool true # Art. 13(3)(b)(iv)
  'Performance regarding specific persons or groups of persons on which the system is intended to be used': !!bool true # Art. 13(3)(b)(v)
  'Specifications for the input data, or any other relevant information in terms of the training, validation and testing data sets used, taking into account the intended purpose of the AI system': !!bool true # Art. 13(3)(b)(vi)
  'Information to enable deployers to interpret the output of the high-risk AI system and use it appropriately': !!bool true # Art. 13(3)(b)(vii)
  'Human oversight measures referred to in Article 14, including the technical measures put in place to facilitate the interpretation of the outputs of AI systems by the deployers': !!bool true # Art. 13(3)(d)
  'Computational and hardware resources needed, the expected lifetime of the high-risk AI system and any necessary maintenance and care measures, including their frequency, to ensure the proper functioning of that AI system, including as regards software updates': !!bool true # Art. 13(3)(e)

accuracy_robustness_cybersecurity:
  'Appropriate level of accuracy': !!bool true # Art. 15(1)
  'Appropriate level of robustness': !!bool true # Art. 15(1)
  'Appropriate level of cybersecurity': !!bool true # Art. 15(1)
  'Use of relevant accuracy metrics': !!bool true # Art. 15(2)
  'Maximum possible resilience regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates, in particular due to their interaction with natural persons or other systems. Technical and organisational measures shall be taken towards this regard': !!bool true # Art. 15(4)
  'Measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training dataset (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws': !!bool true # Art. 15(5)

quality_management_system:
  'Examination, test and validation procedures to be carried out before, during and after the development of the high-risk AI system, and the frequency with which they have to be carried out': !!bool true # Art. 17(1)(d)

transparency_obligations:
  'Providers of AI systems, including GPAI systems, generating synthetic audio, image, video or text content, shall ensure the outputs of the AI system are marked in a machine-readable format and detectable as artificially generated or manipulated': !!bool true # Art. 50(2)
  'Providers shall ensure their technical solutions are effective, interoperable, robust and reliable as far as this is technically feasible, taking into account specificities and limitations of different types of content, costs of implementation and the generally acknowledged state-of-the-art, as may be reflected in relevant technical standards': !!bool true # Art. 50(2)

classification_of_gpai_models:
  'Whether model has high impact capabilities evaluated on the basis of appropriate technical tools and methodologies, including indicators and benchmarks': !!bool true # Art. 51(1)(a)
  'Cumulative compute used for training measured in floating point operations (FLOPs)': !!bool true # Art. 51(2)

obligations_for_providers_of_gpai_models:
  'The tasks that the model is intended to perform and the type and nature of AI systems in which it can be integrated': !!bool true # Art. 53; Annex XI(1)(1)(a)
  'Acceptable use policies applicable': !!bool true # Art. 53; Annex XI(1)(1)(b)
  'The date of release and methods of distribution': !!bool true # Art. 53; Annex XI(1)(1)(c)
  'The architecture and number of parameters': !!bool true # Art. 53; Annex XI(1)(1)(d)
  'Modality (e.g. text, image) and format of inputs and outputs': !!bool true # Art. 53; Annex XI(1)(1)(e)
  'The license': !!bool true # Art. 53; Annex XI(1)(1)(f)
  'Training methodologies and techniques': !!bool true # Art. 53; Annex XI(1)(2)(b)
  'Key design choices including the rationale and assumptions made': !!bool true # Art. 53; Annex XI(1)(2)(b)
  'What the model is designed to optimise for': !!bool true # Art. 53; Annex XI(1)(2)(b)
  'The relevance of the different parameters, as applicable': !!bool true # Art. 53; Annex XI(1)(2)(b)
  'Information on the data used for training, testing and validation: type of data': !!bool true # Art. 53; Annex XI(1)(2)(c)
  'Information on the data used for training, testing and validation: provenance of data': !!bool true # Art. 53; Annex XI(1)(2)(c)
  'Information on the data used for training: curation methodologies (e.g. cleaning, filtering etc)': !!bool true # Art. 53; Annex XI(1)(2)(c)
  'Information on the data used for training: the number of data points': !!bool true # Art. 53; Annex XI(1)(2)(c)
  'Information on the data used for training: data points scope and main characteristics applicable': !!bool true # Art. 53; Annex XI(1)(2)(c)
  'Information on the data used for training: how the data was obtained and selected': !!bool true # Art. 53; Annex XI(1)(2)(c)
  'Information on the data used for training: all other measures to detect the unsuitability of data sources and methods to detect identifiable biases, where applicable': !!bool true # Art. 53; Annex XI(1)(2)(c)
  'The computational resources used to train the model (e.g. number of floating point operations – FLOPs), training time, and other relevant details related to the training': !!bool true # Art. 53; Annex XI(1)(2)(d)
  'Known or estimated energy consumption of the model; in case not known, this could be based on information about computational resources used': !!bool true # Art. 53; Annex XI(1)(2)(e)
  'Detailed description of the evaluation strategies, including evaluation results, on the basis of available public evaluation protocols and tools or otherwise of other evaluation methodologies. Evaluation strategies shall include evaluation criteria, metrics and the methodology on the identification of limitations': !!bool true # Art. 53; Annex XI(2)(1)
  'Where applicable, detailed description of the measures put in place for the purpose of conducting internal and/or external adversarial testing (e.g. red teaming), model adaptations, including alignment and fine-tuning': !!bool true # Art. 53; Annex XI(2)(2)

obligations_for_providers_of_gpai_models_with_systemic_risk:
  'Perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting adversarial testing of the model with a view to identify and mitigate systemic risk': !!bool true # Art. 55(1)(a)
  'Assess and mitigate possible systemic risks at Union level, including their sources, that may stem from the development': !!bool true # Art. 55(1)(b)
  'Ensure an adequate level of cybersecurity protection for the GPAI model with systemic risk and the physical infrastructure of the mode': !!bool true # Art. 55(1)(d)