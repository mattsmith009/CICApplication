from spacy.tokens import Doc
from spacy.training import Example
from country_list import countries_for_language

diseases = """COWDRIOSIS
Ehrlichia ruminantium
EASTERN EQUINE ENCEPHALITIS
Alphavirus
JAPANESE ENCEPHALITIS
Flavivirus
INFECTIOUS ENCEPHALOMYELITIS OF SHEEP
LOUPING ILL
SHAKE DISEASE
AUJESZKY DISEASE
Herpesvirus1
HVP-1
AKABANE DISEASE
Orthobunyavirus
BORNA DISEASE
Bornavirus
BORDER DISEASE
CONGENITAL HYPOMYELOGENESIS
Pestivirus
NAIROBI DISEASE
Orthonairovirus
SCHMALLENBERG DISEASE
Orthobunyavirus
WESSELBRON DISEASE
EPIZOOTIC HEMORRHAGIC DISEASE
IBARAKI DISEASE
ECHINOCOCOSIS
HYDATIDOSIS
FOOT AND MOUTH DISEASE
Aphthovirus
MALIGNANT CATARRAL FEVER
alcelafine
AIHV-2
RIFT VALLEY FEVER
Phlebovirus
CRIMEAN-CONGO HEMORRHAGIC FEVER
Orthonairovirus
Q FEVER
Coxiella burnetii
ENCEPHALOMYELITIS
Henipavirus
IXODIDOSIS
Riphicephalus
BLUE TONGUE
Orbivirus
MELIOIDOSIS
Burkholderia pseudomallei
MYASIS
Cochliomyia hominivorax
Chrysomya bezziana
CONTAGIOUS PERINEUMONIA
Morbillivirus
SURRA
MURRINA
BAD HIPS
Trypanosoma evansi
THEILERIOSIS
Theileria parva
AFRICAN TRYPANOSOMIASIS
Trypanosoma brucei gambiense
TULAREMIA
SMALLPOX
Orthopoxvirus
Capripoxvirus
BOVINE ANAPLASMOSIS
Anaplasma centrale
BABESIOSIS
Babesia divergens
DERMATOPHILOSIS
Dermatophilus congolensis
CONTAGIOUS NODULAR DERMATOSIS
Poxvirus
BOVINE SPONGIFORM ENCEPHALOPATHY
Prion
AINO DISEASE
Orthobunyavirus
BOVINE EPHIMERA FEVER
Ephemerovirus
HEMORRHAGIC SEPTICEMIA
Pasteurella multocida
CONTAGIOUS AGALACTIA
Mycoplasma agalactiae
SALMONELLOSIS
PARATYPHOID ABORTION
Salmonella abortus ovis
SCRAPIE
PRURIGO LUMBAR
Salmonella abortus equi
EQUINE VIRAL ARTERITIS
Arterivirus
DURINE
Trypanosoma equiperdum
WESTERN EQUINE ENCEPHALITIS
VENEZUELAN EQUINE ENCEPHALITIS
HENDRA DISEASE
ACUTE EQUINE RESPIRATORY SYNDROME
Henipavirus
EQUINE COITAL EXANTHEMA
Herpesvirus 3
EQUINE ULCEROUS LYMPHANGITIS
Corynebacterium pseudotuberculosis
CONTAGIOUS EQUINE METRITIS
Taylorella equigenitalis
GLANDERS
Burkholderia mallei
AFRICAN HORSE FISH
Orbivirus
TESCHOVIRUS ENCEPHALOMYELITIS
SWINE POLIOMYELITIS
Porcine Teschovirus
SWINE VESICULAR DISEASE
Enterovirus
SWINE VESICULAR EXANTHEMA
Vesivirus
CLASSICAL SWINE FEVER
Pestivirus
SWINE INFLUENZA
AFRICAN SWINE FEVER
Asfivirus
PORCINE REPRODUCTIVE AND RESPIRATORY SYNDROME
Arterivirus
GUMBORO DISEASE
INFECTIOUS BURSITIS
Avibirnavirus
NEWCASTLE DISEASE
Avulavirus
DUCK VIRAL ENTERITIS
Herpesvirus
DUCK VIRAL HEPATITIS
Avihepatovirus
NOTIFICABLE AVIAN INFLUENZA
AVIAN PULOROSIS
Salmonella enterica subsp. enterica serovar pullorum
AVIAN TYPHOID
Salmonella enterica subsp. enterica serovar gallinarum
RABBIT VIRAL HEMORRHAGIC DISEASE
Lagovirus
AMERICAN FLOUD
Paenibacillus larvae
CHRONIC WASTING
WASHING DISEASE OF DEER
Isavirus
Betanodavirus
KOI CARP HERPESVIROSIS
Herpesvirus HV-1
JAPANESE SEA BREAM IRIDOVIROSIS
Iridovirus
EPIZOOTIC HEMATOPOIETIC NECROSIS
Ranavirus
INFECTIOUS HEMATOPOIETIC NECROSIS
Novirhabdovirus
RENIBACTERIOSIS
Renibacterium salmoninarum
VIRAL HEMORRHAGIC SEPTICEMIA
Novirhabdovirus
RICKETTSIAL SEPTICEMIA OF SALMONIDS
Piscirickettsia salmonis
EPIZOOTIC ULCERANT SYNDROME
Aphanomyces invadans
SPRING CARP VIREMIA
Vesiculovirus
LAKE TILAPIA VIRUS
Orthomyxovirus
ABULONE HERPESVIRUS INFECTION
ABULONE VIRAL GANGLIONEURITIS
Herpesvirus HVAb
Bonamia exitiosa
Bonamia ostreae
Mikrocytos mackini
PERKINSUS OLSENI INFECTION
Perkinsus olseni
ABULONE WILT SYNDROME
Xenohaliotis californiensis
SPHERICAL BACULOVIROSIS
Penaeus monodon baculovirus
TETRAHEDRIC BACULOVIROSIS
Baculovirus penaei
YELLOW HEAD DISEASE VIRUS INFECTION
Okavirus
Macrobrachium rosenbergii nodavirus
ACUTE HEPATOPANCREATIC NECROSIS DISEASE
toxigenic Vibrio parahaemolyticus
NODAVIRUS INFECTION
Penaeus vannamei nodavirus
Totivirus-like virus
PLAGUE OF THE CRAY CRAB
Aphanomyces astaci
ANTHRAX
BACTERIDIAN ANTHRAX
Bacillus anthracis
BRUCELLOSIS
Brucella abortus
CAMPYLOBACTERIOSIS
Campylobacter spp
CONTAGIOUS ECTHIMA
ORF VIRUS
CONTAGIOUS PUSTULOUS DERMATITIS
Parapoxvirus
VESICULAR STOMATITIS
Vesiculovirus
Riphicephalus spp
RABIES
Lyssavirus
rabies virus
TUBERCULOSIS
Mycobacterium spp
BOVINE PAPULAR STOMATITIS
PROLIFERATIVE STOMATITIS
GRANULOUS STOMATITIS
Parapoxvirus
EQUINE INFECTIOUS ANEMIA
Lentivirus
VENEZUELAN EQUINE ENCEPHALITIS
Avulavirus
LOW PATHOGENIC AVIAN INFLUENZA
Influenzavirus A
MIXOMATOSIS
Leporipoxvirus
VARROA
VARROASIS INFESTATION
Varroa destructor
INFECTIOUS PANCREATIC NECROSIS
Aquabirnavirus
ABULONE HERPESVIRUS INFECTION
OSHV-1
Herpesvirus
Marteilia refringens
PERKINSUS MARINUS INFECTION
Perkinsus marinus
Aparavirus
ANAPLASMOSIS
Anaplasma spp
BABESIOSIS
Babesia spp
CLOSTRIDIASIS
Clostridium spp
COCCIDIOSIS
Eimeria spp
DERMATOPHITOSIS
Microsporum canis
VIBRIONIC DYSENTERY
Vibrio jejuni
LYME DISEASE
Borrelia burgdorferi
STAPHYLOCOCOSIS
Staphylococcus spp
ECHINOCOCOSIS
HYDATIDOSIS
Echinococcus granulosus
WEST NILE FEVER
WEST NILE VIRUS
LEISHMANIOSIS
Leishmania spp
LEPTOSPIROSIS
Leptospira spp
EPIZOOTIC LYMPHANGITIS
Histoplasma capsulatum
LISTERIOSIS
Listeria monocytogenes
MYCOPLASMOSIS
Mycoplasma spp
Respirovirus
NEOSPOROSIS
Neospora caninum
PARATUBERCULOSIS
JOHNE'S DISEASE
Mycobacterium avium subsp. paratuberculosis
SALMONELLOSIS
Salmonella spp
Scabies
Sarcoptes spp
Psoroptes spp
Demodex spp
TRICHINELOSIS
TRICHINIASIS
TRICHINENOSIS
Trichinella spp
BOVINE VIRAL DIARRHEA
Pestivirus
ENZOOTIC BOVINE LEUCOSIS
Deltaretrovirus
INFECTIOUS KERATOCONJUNCTIVITIS
Moraxella bovis
INFECTIOUS BOVINE RHINOTRACHEITIS
INFECTIOUS PUSTULAR VULVOVAGINITIS
Bovine herpesvirus
TRICOMONIOSIS
Trichomonas fetus
ENZOOTIC ABORTION OF SMALL RUMINANTS
OVINE CHLAMYDIOSIS
Chlamydophila abortus
CAPRINE ENCEPHALITIS ARTHRITIS
Lentivirus
MAEDI-VISNA
OVINE PROGRESSIVE PNEUMONIA
GURMA
EQUINE MUMPS
Streptococcus equi
EQUINE INFLUENZA
Influenzavirus A
EQUINE PYROPLASMOSIS
Theileria equi
Babesia caballi
EQUINE VIRAL RHINONEUMONITIS
EQUINE HERPESVIRUS INFECTION
SWINE EPIDEMIC DIARRHEA
Alphacoronavirus
SWINE ENCEPHALOMYELITIS
Enterovirus
Picornavirus
TRANSMISSIBLE SWINE GASTROENTERITIS
Deltacoronavirus
Taenia solium
SWINE INFLUENZA
POST-WEANING MULTI-SYSTEM WASTING SYNDROME
Porcine circovirus type 2
PORCINE REPRODUCTIVE AND RESPIRATORY SYNDROME
Arterivirus type 2
ACARIOSIS
AVIAN INFECTIOUS BRONCHITIS
Gammacoronavirus
AVIAN CHLAMYDIOSIS
PSITTACOSIS
ORNITHOSIS
Chlamydophila psittaci
AVIAN CHOLERA
Pasteurella multocida
INFECTIOUS CORYZA
Avibacterium paragallinarum, A. gallinarum
GUMBORO DISEASE
INFECTIOUS BURSITIS
Avibirnavirus
MAREK'S DISEASE
Mardivirus
INTESTINAL SPIROCHETOSIS OF BIRDS
Brachyspira spp
FAVUS
RINGNEA
DERMATOPHITOSIS
DERMATOMYCOSIS
Microsporum gallinae
HYDROPERICARDIUM SYNDROME
Aviadenovirus
HISTOMONIASIS
Histomona meleagridis
AVIAN INFECTIOUS LARYNGOTRACHEITIS
Alphaherpesvirus
AVIAN LEUCOSIS
Alpharetrovirus
TURKEY RHINOTRACHEITIS
Metaneumovirus
AVIAN TUBERCULOSIS
Mycobacterium avium
Avian pox
Avipoxvirus
ACARAPISOSIS
Acarapis woodi
Aethina tumida
European foulbrood
Melissococcus plutonius
NOSEMOSIS
Nosema apis
Nosema ceranae
FRANCISELLA INFECTION
Francisella noatunensis
GYRODACTYLOSIS INFECTION
Gyrodactylus salaris
Whispovirus
Hepatobacter penaei
Enterocytozoon hepatopenaei
Brevidensovirus
Batrachochytrium dendrobatidis
RANAVIRUS INFECTION
Ranavirus
B. salamandrivorans
"""

diseases = diseases.splitlines(keepends=False)

training_data = {
    "COWDRIOSIS": [
        [
            "A recent outbreak of cowdriosis has caused concern among cattle ranchers.",
            "Government initiatives are underway to control the spread of cowdriosis in affected regions.",
            "New research has shown promising results in the fight against cowdriosis."
        ]
    ],
    "Ehrlichia ruminantium": [
        [
            "An outbreak of Ehrlichia ruminantium has caused widespread concern among farmers, with numerous cases of cowdriosis reported in the region.",
            "Local authorities are working to contain the outbreak of Ehrlichia ruminantium, which has already affected hundreds of cattle.",
            "Ehrlichia ruminantium continues to pose a growing threat to livestock health, with cases of cowdriosis on the rise in several countries.",
            "Efforts to control Ehrlichia ruminantium are becoming increasingly important as the bacterium spreads to new regions."
        ]
    ],
    "EASTERN EQUINE ENCEPHALITIS": [
        [
            "The Massachusetts Department of Public Health (DPH) today announced that Eastern equine encephalitis (EEE) virus has been detected in mosquitoes in Massachusetts for the first time this year.", 
            "The @MassDPH recently detected West Nile virus (WNV) in mosquito samples from Cambridge. While no human or animal cases of WNV or Eastern equine encephalitis (EEE) have been reported, we encourage community members to take steps to protect from mosquitoes", 
            "The Monmouth County Board of County Commissioners is asking residents and visitors to be vigilant about mosquito-borne illnesses such as Eastern Equine Encephalitis, St. Louis Encephalitis and West Nile virus.",
            "Eastern Equine Encephalitis comes in small doses, transmitted by mosquitoes to horses (sicken & die) & babies are most vunerable.", 
            "Mosquitos can carry West Nile Virus, Eastern Equine Encephalitis Virus, Zika Virus, and many viruses with long scary names. Protect yourself from illness by protecting yourself from mosquito bites."
        ]
    ],
    "Alphavirus": [
        [
            "Researchers have identified a new strain of alphavirus in South America, raising concerns about potential outbreaks.",
            "The newly discovered alphavirus strain is being closely monitored by health authorities to assess its impact on public health.",
            "An outbreak of alphavirus in Australia has triggered a health alert, with several cases reported in the northern regions.",
            "Mosquito populations in Southeast Asia have tested positive for alphavirus, prompting concerns about potential human cases.",
            "Authorities are implementing mosquito control measures to curb the spread of alphavirus in affected areas."
        ]
    ],
    "JAPANESE ENCEPHALITIS": [
        
        [
            "Guwahati is witnessing a troubling rise in  Japanese Encephalitis (JE), Acute Encephalitis Syndrome (AES), and dengue. The Gauhati Medical College Hospital (GMCH) is currently treating numerous patients affected by these diseases, with several fatalities reported.",
            "July and August are high transmission time for Japanese Encephalitis. Take precautionary steps to keep yourself and your family safe from the disease.",
            "Of 12 earliest patients in Gujarat, 6 died in early July. From the batch of 7 first patients, GMERS Himmatnagar sent 6 samples, barring 1st, to NIV. Only 1 tested positive for Chandipura Vesiculovirus. All others tested negative for Chandipura, Japanese Encephalitis, Enteroviruses"
        ]
    ],
    "Flavivirus": [
        [
            "Scientists have identified a new strain of flavivirus in Southeast Asia, sparking concerns over its potential spread.",
            "The newly discovered flavivirus is being closely monitored by health officials to determine its impact on public health.",
            "A promising new vaccine for flavivirus has entered clinical trials, showing potential to prevent infections.",
            "Researchers are hopeful that the flavivirus vaccine will prove effective in large-scale trials.",
            "An outbreak of flavivirus in Central America has raised a health alert, with multiple cases reported across the region.",
            "In light of recent outbreaks, the government has allocated substantial funds for research on flavivirus.",
            "Mosquitoes in the southern United States have tested positive for flavivirus, prompting increased surveillance efforts.",
            "A travel advisory has been issued for the Caribbean following a flavivirus outbreak, with tourists advised to take precautions."
        ]
    ],
    # "INFECTIOUS ENCEPHALOMYELITIS OF SHEEP": [],
    "LOUPING ILL": [
        [
            "An outbreak of louping ill has been linked to increased tick infestations in certain areas, prompting a call for better tick control measures.",
            "Authorities are advising livestock owners to implement tick control strategies to mitigate the risk of louping ill.",
            "Louping ill has been detected in a population of wild deer, raising concerns about the potential spread to livestock.",
            "A recent outbreak of louping ill has been reported in Northern Scotland, affecting several sheep farms.",
            "The louping ill virus has been detected in tick populations in Ireland, prompting concerns among farmers."
        ]
    ],
    "SHAKE DISEASE": [
        [
            "Recent reports of Shake Disease in cattle have resulted in the death of 18 animals. Farmers are advised to implement stricter control measures to prevent further spread.",
            "Shake Disease has caused significant losses in local herds, with 12 confirmed casualties. Veterinary teams are working to contain the outbreak and provide necessary treatments.",
            "The outbreak of Shake Disease has led to the death of 7 horses in affected regions. Authorities are investigating the source of the infection and advising on preventive measures.",
            "Increased cases of Shake Disease have been observed in a number of livestock farms, resulting in 25 animal deaths. Farmers are urged to monitor their herds closely and report any symptoms.",
            "Shake Disease has been identified in a cluster of farms, with 10 animals reported dead. Health officials are conducting research to understand the disease better and mitigate its impact."

        ]
    ],
    "AUJESZKY DISEASE": [
        [
            "A recent outbreak of Aujeszky Disease in pigs has led to the death of 20 animals. Authorities are working to control the spread and prevent further casualties.",
            "The discovery of Aujeszky Disease in several herds has resulted in 15 confirmed deaths among pigs. Measures are being implemented to manage the outbreak and protect livestock.",
            "Aujeszky Disease has been identified in a large-scale pig farming operation, causing the death of 8 animals. Veterinarians are focusing on treatment and prevention strategies.",
            "Increased cases of Aujeszky Disease have led to the loss of 12 pigs in affected farms. Farmers are advised to enhance biosecurity measures and consult with veterinary experts.",
            "Recent outbreaks of Aujeszky Disease have resulted in 18 pig casualties. Health officials are investigating the cause and implementing measures to curb the spread of the disease."

        ]
    ],
    "Herpesvirus1": [
        [
            "Herpesvirus1 has been detected in several domestic animals, causing the death of 5 pets. Veterinary clinics are working on treatment options and preventive measures.",
            "A recent study reveals that Herpesvirus1 is causing severe illness in livestock, with 7 confirmed casualties. Researchers are investigating new therapies to combat the virus.",
            "The outbreak of Herpesvirus1 in a local animal shelter has led to the death of 4 animals. Health officials are monitoring the situation and providing guidance on containment strategies.",
            "Herpesvirus1 infections have been reported in various species, resulting in 6 casualties. Medical professionals are developing effective treatments to address the rising cases.",
            "The discovery of Herpesvirus1 in a research facility has caused 3 animal deaths. Efforts are being made to contain the outbreak and protect other specimens from infection."

        ]
    ],
    "HVP-1": [
        [
            "Recent cases of HVP-1 have led to the death of 10 animals in affected farms. Researchers are working to understand the virus and develop effective treatments.",
            "HVP-1 infections have been identified in several livestock herds, with 8 confirmed fatalities. Veterinary teams are implementing control measures to manage the outbreak.",
            "The outbreak of HVP-1 in a breeding facility has resulted in the death of 12 animals. Health officials are investigating the source of the infection and advising on preventive measures.",
            "Increased cases of HVP-1 have caused significant losses, with 9 animals reported dead. Experts are focusing on developing vaccines and treatments to address the disease.",
            "The discovery of HVP-1 in a commercial farm has led to 5 animal casualties. Veterinary professionals are working to contain the outbreak and prevent further spread."

        ]
    ],
    "AKABANE DISEASE": [
        [
            "Akabane Disease has caused the death of 15 cattle in affected regions. Health authorities are investigating the outbreak and implementing control measures.",
            "Recent reports indicate an increase in Akabane Disease cases, leading to the death of 20 animals. Veterinarians are advising farmers on prevention and treatment strategies.",
            "An outbreak of Akabane Disease has resulted in 10 confirmed fatalities among livestock. Efforts are underway to manage the disease and limit its impact on agriculture.",
            "The discovery of Akabane Disease in a large herd has led to 12 casualties. Researchers are working to understand the virus and improve disease management practices.",
            "Increased cases of Akabane Disease have been reported, with 8 animals dead. Veterinary teams are focused on controlling the spread and providing necessary treatments."

        ]
    ],
    "Orthobunyavirus": [
        [
            "Recent outbreaks of Orthobunyavirus have caused the death of 6 animals in a local farm. Health officials are investigating the virus and advising on containment measures.",
            "Orthobunyavirus has been identified in several regions, leading to 4 confirmed casualties. Researchers are working to develop effective vaccines and treatments.",
            "The discovery of Orthobunyavirus in livestock has resulted in the death of 8 animals. Authorities are implementing measures to control the outbreak and protect other animals.",
            "Increased cases of Orthobunyavirus have caused significant losses, with 5 animals reported dead. Veterinary professionals are conducting research to address the disease.",
            "Orthobunyavirus infections have been observed in multiple species, resulting in 7 casualties. Health officials are working to manage the outbreak and provide necessary support."

        ]
    ],
    "BORNA DISEASE": [
        [
            "Recent cases of Borna Disease have led to the death of 5 animals in affected areas. Researchers are investigating the virus and developing strategies to control its spread.",
            "Borina Disease has been identified in several wildlife populations, resulting in 10 confirmed fatalities. Conservationists are working to understand the impact and prevent further casualties.",
            "The outbreak of Borna Disease in a laboratory setting has caused the death of 6 animals. Health officials are implementing strict biosecurity measures to prevent further infections.",
            "Increased reports of Borna Disease have led to the death of 8 animals. Scientists are studying the virus to develop effective treatments and control measures.",
            "Borina Disease has been detected in various animal species, causing 7 casualties. Efforts are underway to manage the outbreak and protect affected populations."
        ]
    ],
    "Bornavirus": [
        [
            "A recent outbreak of Bornavirus in a wildlife sanctuary in Germany has resulted in the death of five birds, with conservationists working to prevent further casualties and manage the spread of the virus.",
            "Veterinary authorities in the United States are investigating a cluster of Bornavirus cases in captive parrots, with two confirmed fatalities and several more birds showing symptoms of the disease.",
            "Bornavirus has been detected in a number of wild squirrels in Canada, leading to concerns among wildlife experts. No casualties have been reported yet, but monitoring and preventive measures are being implemented.",
            "In Australia, a significant outbreak of Bornavirus in a breeding facility has led to the deaths of four parrots. Health officials are intensifying efforts to contain the virus and prevent additional infections.",
            "Research teams in South Africa are studying an increase in Bornavirus infections among local bat populations. Although no human cases have been reported, there is heightened concern about the potential for cross-species transmission."
        ]
    ],
    "BORDER DISEASE": [
        [
            "Recent reports indicate an outbreak of Border Disease in sheep, resulting in the death of 22 animals. Farmers are urged to implement strict biosecurity measures to prevent further spread.",
            "Border Disease has caused significant losses in local livestock, with 18 confirmed casualties reported. Veterinarians are working to control the outbreak and provide necessary treatments.",
            "The discovery of Border Disease in a herd of cattle has led to the death of 15 animals. Health authorities are investigating the source and implementing control measures.",
            "Increased cases of Border Disease have been observed, causing the death of 20 sheep in affected farms. Veterinary teams are advising on preventive measures and treatment options.",
            "Border Disease has been identified in several herds, leading to 12 animal deaths. Researchers are focusing on improving diagnostic methods and developing vaccines."

        ]
    ],
    "CONGENITAL HYPOMYELOGENESIS": [
        [
            "Recent studies show that congenital hypomyelogenesis is affecting a number of newborn animals, with 5 confirmed deaths reported. Researchers are working on understanding and treating the condition.",
            "Congenital hypomyelogenesis has been identified in several calves, resulting in 3 fatalities. Veterinary teams are focusing on improving diagnostic techniques and providing support to affected farms.",
            "The outbreak of congenital hypomyelogenesis in a local zoo has caused the death of 4 animals. Health officials are investigating the cause and working on preventive measures.",
            "Increased cases of congenital hypomyelogenesis have led to 6 confirmed deaths among newborn animals. Efforts are being made to study the disease and develop effective treatments.",
            "Congenital hypomyelogenesis has been detected in several litters, with 7 casualties reported. Researchers are working on better understanding the condition and its impact on animal health."

        ]
    ],
    "Pestivirus": [
        [
            "An outbreak of Pestivirus in cattle has resulted in the death of 25 animals. Health authorities are investigating the source and advising farmers on disease management strategies.",
            "Recent cases of Pestivirus have caused the death of 18 pigs in affected farms. Veterinarians are working on developing vaccines and treatments to combat the virus.",
            "Pestivirus has been identified in several herds, leading to 20 confirmed fatalities. Efforts are underway to control the outbreak and prevent further spread of the virus.",
            "The discovery of Pestivirus in a local livestock population has resulted in 15 animal deaths. Researchers are focusing on improving diagnostic methods and treatment options.",
            "Increased cases of Pestivirus have caused significant losses, with 12 animals reported dead. Health officials are working on developing effective management practices and vaccines."

        ]
    ],
    "NAIROBI DISEASE": [
        [
            "Nairobi Disease has caused the death of 10 animals in affected regions. Veterinary teams are investigating the outbreak and implementing control measures to prevent further casualties.",
            "Recent outbreaks of Nairobi Disease in livestock have resulted in 8 confirmed fatalities. Researchers are working to understand the disease better and develop effective treatments.",
            "The discovery of Nairobi Disease in a local farm has led to the death of 12 animals. Health authorities are focusing on containment and prevention strategies to manage the outbreak.",
            "Increased cases of Nairobi Disease have been reported, causing the death of 14 animals in affected areas. Efforts are underway to control the spread and provide necessary support to farmers.",
            "Nairobi Disease has been identified in several herds, leading to 9 casualties. Researchers are studying the virus to improve diagnostic and treatment options."

        ]
    ],
    "Orthonairovirus": [
        [
            "Recent cases of Orthonairovirus in livestock have resulted in the death of 6 animals. Health officials are investigating the source and working on control measures.",
            "Orthonairovirus has been detected in several herds, causing 7 confirmed fatalities. Researchers are working on developing vaccines and treatment options to address the virus.",
            "The outbreak of Orthonairovirus has led to the death of 5 animals in a local farm. Veterinary teams are implementing measures to manage the disease and prevent further infections.",
            "Increased reports of Orthonairovirus have resulted in the death of 8 animals in affected regions. Health authorities are focusing on containment and support for affected farms.",
            "Orthonairovirus infections have been identified in various livestock populations, causing 4 casualties. Researchers are studying the virus to improve disease management and treatment strategies."
        ]
    ],
    # "SCHMALLENBERG DISEASE": [],
    # "Orthobunyavirus": [],
    # "WESSELBRON DISEASE": [],
    # "EPIZOOTIC HEMORRHAGIC DISEASE": [],
    # "IBARAKI DISEASE": [],
    # "ECHINOCOCOSIS": [],
    # "HYDATIDOSIS": [],
    "FOOT AND MOUTH DISEASE": [
        [
            "Foot in mouth disease, man kept the Commissioners in the dark or someone suffering from Alzheimer's?",
            "H.E President @WilliamsRuto committed to vaccinating all livestock in Kenya against PPR and Foot and Mouth Disease. We started today in Kitui with 700,000 doses of PPR Vaccine and will go county to county until completion.",
            "The geographical area affected by foot-and-mouth outbreaks around the Pirbright laboratory sites in 2007. On Saturday 4 August 2007 it was announced that the strain of foot-and-mouth disease detected in cattle three miles away was similar to that in use at the",
            "In 2007, Gary O'Donoghue broke the story that new UK Prime Minister Gordon Brown was returning early from holiday to deal with an outbreak of foot-and-mouth disease in Surrey.",
            "@BasedMikeLee He doesn't have Covid, he has foot in mouth disease and will be hidden away...",
            "Kudos Greatest Gen @mkainerugaba for fulfilling your promise made in Masaka on 15th-March-2024! The arrival of the second consignment of 3 million doses of FMD vaccines from Egypt is a significant milestone in Uganda's fight against Foot and Mouth Disease. https://t.co/vyTbMzWX8N",
            "Agriculture Minister has been asked to ban the movement of animals into the WC due to foot and mouth disease but that bru only has matric Life Sciences",
            "Some common diseases include foot and mouth disease (FMD), coccidiosis, bottle jaw, blackleg, and others, young goats are more susceptible. All the diseases can be prevented by buying healthy goats, proper vaccination, regular hygiene, clean water, and quarantining sick ones. https://t.co/QSws8GzvLE",
            # "The BVI currently supplies three animal vaccines for Foot and Mouth Disease, Anthrax and Rabies, as well as laboratory testing reagents for Foot and Mouth Disease."
        ]
    ],
    # "Aphthovirus": [],
    # "MALIGNANT CATARRAL FEVER": [],
    # "alcelafine": [],
    # "AIHV-2": [],
    "RIFT VALLEY FEVER": [
        [
            "Call for Proposals - Epidemiology & Modelling to Support Rift Valley Fever Vaccine Development.",
            "Is it possible to conduct efficacy trials for Rift Valley fever vaccines? With up to US$5M in funding available per project, CEPI2019s latest Call for Proposals seeks to find out. Learn more: https://t.co/ZDVQaSq9FD https://t.co/jKMOg3jZmX",
            "Vaccine strains of Rift Valley fever virus exhibit attenuation at the maternal fetal placental interface https://t.co/J1rRpizcmb",
        ]
    ],
    # "Phlebovirus": [],
    # "CRIMEAN-CONGO HEMORRHAGIC FEVER": [],
    # "Orthonairovirus": [],
    # "Q FEVER": [],
    "Coxiella burnetii": [
        [
            "@BrandonSup8 What's the risk of the following from drinking Mountain Dew:- Salmonella- Escherichia coli- Listeria monocytogenes- Campylobacter jejuni- Brucella- Mycobacterium bovis- Yersinia enterocolitica- Staphylococcus aureus- Coxiella burnetii"
        ]
    ],
    "ENCEPHALOMYELITIS": [
        [
            "@himmatb15 I'm so sorry. I'm in the same boat. Feeling like I wish I never paced so much that I lost functioning. But I am finding out now I may also have a muscle wasting or neuro degenerative disease along with Myalgic Encephalomyelitis. I'm wondering if this may be the case with you too.",
            "13yrs-Campaigning for NI #MyalgicEncephalomyelitis specialist services &still nobody gets most effective solution ie early&accurate diagnosis&education to give patients best chance to avoid deterioration. Watching own repeat experience 25yrs ago with *some #LongCovid is horrific",
            "@doyouseem_e_now This type encephalitis afaiu shows on scans in established tests?  Myalgic Encephalomyelitis brain doesn't, although m.e brain resesrch has been (deliberately) limited, and is one reason name is rejected. My brain feels fried.",
            "@metraux_julia @ChronicallyTina @MotherJones FYI THIRTY YEARS OF DISDAIN How HHS and A Group of Psychiatrists Buried Myalgic Encephalomyelitis @marydimmock & @mfairma December 2015: https://t.co/LG1anwgeY7 and also @DialoguesMECFS2019 videos on ME and severe ME.",
            "@doyouseem_e_now Myalgic Encephalomyelitis literally translates to Swelling of the brain",
            "Parkview Health: Addressing the persistence of COVID-19 symptoms. 18 percent all adults say they have experienced long COVID..has been compared to myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS)..https://t.co/ttEUZgfo6y",
            "myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS), so-called chronic Lyme disease, and more. #pwME #MECFS #LongCovid #Lyme #IACC",
            "@LukensJohnR CD8s may also promote inflammation. Those suffering from ME/CFS is encephalomyelitis inflammation without AD unless comorbid.",
            "@actionforme @Medscape @SonyaChowdhury Then you must take Medscape to task for using Chronic fatigue (a symptom that affects many illnesses) as Myalgic Encephalomyelitis",
            "@StuckinEbed @actionforme @Medscape @SonyaChowdhury Yes, please ask them to update that headline to Myalgic Encephalomyelitis (ME/CFS).",
            "Less than a week until I get the test results of my spinal tap being the deciding factor in whether I have a Multiple Sclerosis-esque disease, or virus-induced Myalgic Encephalomyelitis. Life is quick, journey is slow. #chronicillness #ChronicPain https://t.co/DU9PCWQtMQ"
        ]
    ],
    # "Henipavirus": [],
    # "IXODIDOSIS": [],
    # "Riphicephalus": [],
    "BLUE TONGUE": [
        [
            "There is a high probability of a new introduction of bluetongue virus in livestock this year, and it only takes one bite from an infected midge to transmit the disease. Read our article on signs and symptoms to look out for, as well as prevention methods: https://t.co/9uQ2iUb6sx",
        ]
    ],
    # "Orbivirus": [],
    # "MELIOIDOSIS": [],
    # "Burkholderia pseudomallei": [],
    # "MYASIS": [],
    # "Cochliomyia hominivorax": [],
    # "Chrysomya bezziana": [],
    # "CONTAGIOUS PERINEUMONIA": [],
    # "Morbillivirus": [],
    # "SURRA": [],
    # "MURRINA": [],
    # "BAD HIPS": [],
    # "Trypanosoma evansi": [],
    # "THEILERIOSIS": [],
    # "Theileria parva": [],
    "AFRICAN TRYPANOSOMIASIS": [
        [
            "Fully funded #PhD opportunity in #parasitology with focus on African trypanosomiasis at University of Antwerp (Belgium) start: 01-Oct-2024 | duration: 4 years | closing 12-Aug-2024 #immunology  https://t.co/i3I8tv09rV"
        ]
    ],
    # "Trypanosoma brucei gambiense": [],
    "TULAREMIA": [
        [
            "@AlexisBadenMaye You should look at this, remarks by Macfarlane on biological warfare, circa 1957 An example of \"non-sporing\" bacteria, as discussed herein would be tularemia, a well-known BW agent. It remains to be seen how important Sir Macfarlane was to BW program https://t.co/Djgs4Ihq6m",
            "populations. The species occasionally, but rarely contracts Pasteurellosis, hemorrhagic sepsis, tularemia, and anthrax. Wild boar may on occasion contract swine erysipelas through rodents or hog lice and ticks. Erysipelas is usually caused by the bacterium https://t.co/Yod82AQw5l"
        ]
    ],
    # "SMALLPOX": [],
    "Orthopoxvirus": [
        [
            "A new #mRNA-lipid nanoparticle-based #vaccine provides protection against lethal #orthopoxvirus challenge. Read more about the research in the article below https://t.co/9JPSB2n7zS https://t.co/wntQ7wjiMB"
        ]
    ],
    # "Capripoxvirus": [],
    # "BOVINE ANAPLASMOSIS": [],
    # "Anaplasma centrale": [],
    "BABESIOSIS": [
        [
            "Quick answer - No! - Tick-spread illnesses are on the rise in Canada. Are surveillance, awareness efforts keeping up? https://t.co/jqEwWMcyk4 #BeTickAware #Lyme #Tickborne #Ticks #Tickssuck #Anaplasmosis #Babesiosis #Powassanvirus #Tickchecks"
        ]
    ],
    # "Babesia divergens": [],
    # "DERMATOPHILOSIS": [],
    # "Dermatophilus congolensis": [],
    # "CONTAGIOUS NODULAR DERMATOSIS": [],
    # "Poxvirus": [],
    "BOVINE SPONGIFORM ENCEPHALOPATHY": [
        [
            "Beware of prions. In the future we could suffer from bovine spongiform encephalopathy."
        ]
    ],
    "Prion": [
        [
            "@EndWokeness Prion disease induced Insanity/brain damage brought on by mRNA injections. https://t.co/XTdpifIxrK",
            "@drfrensor @NestCommander Localized prion cascade that hadn't yet affected the entire brain, just one lobe?",
        ]
    ],
    # "AINO DISEASE": [],
    # "Orthobunyavirus": [],
    # "BOVINE EPHIMERA FEVER": [],
    # "Ephemerovirus": [],
    # "HEMORRHAGIC SEPTICEMIA": [],
    # "Pasteurella multocida": [],
    # "CONTAGIOUS AGALACTIA": [],
    # "Mycoplasma agalactiae": [],
    "SALMONELLOSIS": [
        [
            "Tomorrow's headline: Mayor suffering from Salmonellosis and Hepatitis https://t.co/a6BI4uHrfd",
            "A Sun Orchard salmonellosis outbreak makes over 400 people sick with Salmonella as a result of drinking unpasteurized orange juice. The juice was produced by Sun Orchard in Tempe, Arizona and sold to local restaurants and hotels under a variety of brand names. One person dies. https://t.co/St3zGcCSMB"
        ]
    ],
    # "PARATYPHOID ABORTION": [],
    # "Salmonella abortus ovis": [],
    # "SCRAPIE": [],
    # "PRURIGO LUMBAR": [],
    # "Salmonella abortus equi": [],
    # "EQUINE VIRAL ARTERITIS": [],
    # "Arterivirus": [], 
    # "Corynebacterium pseudotuberculosis": [],
    # "CONTAGIOUS EQUINE METRITIS": [],
    # "Taylorella equigenitalis": [],
    "GLANDERS": [
        [
            "Authorities are dealing with an outbreak of glanders in horses in Pakistan, with three confirmed cases and one fatality reported so far. Quarantine measures have been implemented to prevent further spread.",
            "A recent spike in glanders cases has been observed in horse populations in the United Kingdom, leading to the culling of ten infected animals and heightened biosecurity protocols across the region.",
            "Veterinary teams are investigating a glanders outbreak in Brazil, where multiple horses have shown symptoms of the disease, although no fatalities have been reported as of yet.",
            "In a remote area of Mongolia, glanders has been identified in several horses, resulting in the death of two animals and prompting local authorities to seek international assistance for managing the outbreak.",
            "Glanders has been confirmed in a large equestrian facility in the United States, with one horse having succumbed to the disease. Health officials are conducting extensive testing and treatment to control the situation."
        ]
    ],
    # "Burkholderia mallei": [],
    # "AFRICAN HORSE FISH": [],
    # "Orbivirus": [],
    # "TESCHOVIRUS ENCEPHALOMYELITIS": [],
    # "SWINE POLIOMYELITIS": [],
    # "Porcine Teschovirus": [],
    # "SWINE VESICULAR DISEASE": [],
    # "Enterovirus": [],
    # "SWINE VESICULAR EXANTHEMA": [],
    # "Vesivirus": [],
    # "CLASSICAL SWINE FEVER": [],
    # "Pestivirus": [],
    # "SWINE INFLUENZA": [],
    "AFRICAN SWINE FEVER": [
        [
            "New Research: Development and optimization of sampling techniques for environmental samples from African swine fever virus-contaminated surfaces with no organic contaminants https://t.co/U6OTGv8E59 #FrontiersIn #VeterinaryScience",
            "African swine fever is a major concern for the livestock sector. @FAO's global consultation brought together experts to provide updated, science-based control strategies to mitigate risks and protect livelihoods. Learn more https://t.co/Uofm7EQPOb https://t.co/xrud5aGaxm",
            "Camarines Sur 2nd district Rep. LRay Villafuerte has reiterated his proposal to the Department of Agriculture (DA) to distribute the vaccines against the African Swine Fever (ASF) to backyard hog raisers for free. https://t.co/bX95Dwi5r5",
            "From 12/`19-2/`22 a wholesale measure of grain prices jumped 73.5%. Due to higher shipping and energy costs, and China, which was ramping up livestock-feed purchases-rebuilt its hog supply in the wake of an African swine fever outbreak.",
            # "African swine fever outbreaks spreading in Vietnam, government says https://t.co/TmRXDmcBXX",
            # "#ICYMI: The resurgence of African Swine Fever in Cebu City has caused worry among local swine raisers and farmers. #CDNDigital https://t.co/VgYm9ju5zy"
        ]
    ],
    # "Asfivirus": [],
    "PORCINE REPRODUCTIVE AND RESPIRATORY SYNDROME": [
        [
            "Quercetin alleviates inflammation induced by porcine reproductive and respiratory syndrome virus in MARC-145 cells through the regulation of arachidonic acid and glutamine metabolism https://t.co/XbT82Qvjfx",
        ]
    ], 
    # "Arterivirus": [],
    # "GUMBORO DISEASE": [],
    # "INFECTIOUS BURSITIS": [],
    # "Avibirnavirus": [],
    "NEWCASTLE DISEASE": [
        [
            "Brazil confirms first Newcastle disease case in 18 years. Officials at Brazil's Agriculture Ministry have confirmed an outbreak of Newcastle disease at a commercial poultry farm in Rio Grande do Sul, the country's southernmost state.  https://t.co/IIrkFVkfOa",
            "Minister of Agriculture assures the public that consuming chicken is safe amid Newcastle disease outbreak in RS. Despite the need to cull 7k birds, no risk to humans. Read more at https://t.co/rXvbXjQvRf",
            "Officials at Brazil's Agriculture Ministry have confirmed an outbreak of Newcastle disease at a commercial poultry farm in Anta Gorda, a municipality in Rio Grande do Sul, the country's southernmost state. https://t.co/lo72rvpeya",
            "Brazilian meat producers BRF, Marfrig, JBS and Minerva fell on Thursday, weighing on the Ibovespa index, after a confirmed case of Newcastle disease at a commercial poultry farm in RS raised concerns of a potential regional halt of chicken exports. https://t.co/Eh7jGW8yBf",
            "Brazil detects first Newcastle disease case in poultry since 2006 Brazil #Newcastle https://t.co/Zq0X4EhQUD",
            "The last confirmed cases of Newcastle disease in Brazil occurred in 2006 in subsistence birds in the states of Amazonas, Mato Grosso and Rio Grande do Sul, the agriculture ministry said."
        ]
    ],
    # "Avulavirus": [],
    # "DUCK VIRAL ENTERITIS": [],
    "Herpesvirus": [
        [
            "Most common malignancies in HIV-AIDS are: 1.Kaposi Sarcoma: A cancer that causes lesions in the soft tissues, often associated with Human Herpesvirus (HHV-8).Non-Hodgkin Lymphoma: Including primary central nervous system lymphoma, which is more frequent in HIV-positive individuals. 3.Cervical Cancer: Strongly associated with Human Papillomavirus (HPV) infection, which is more common in HIV-positive women.",
            "Pityriasis rosea is an acute, exanthematous disease likely caused by human herpesvirus (HHV)-6 and/or HHV-7. The disease begins with a single erythematous plaque, the so-called herald patch that usually appears on the trunk. 1st  dose #Pfizer #mRNA vaccine https://t.co/13mgYI5qVf https://t.co/H0sdNczv99"
        ]
    ],
    # "DUCK VIRAL HEPATITIS": [],
    # "Avihepatovirus": [],
    # "NOTIFICABLE AVIAN INFLUENZA": [],
    # "AVIAN PULOROSIS": [],
    # "Salmonella enterica subsp. enterica serovar pullorum": [],
    # "AVIAN TYPHOID": [],
    # "Salmonella enterica subsp. enterica serovar gallinarum": [],
    # "RABBIT VIRAL HEMORRHAGIC DISEASE": [],
    # "Lagovirus": [],
    # "AMERICAN FLOUD": [],
    "Paenibacillus larvae": [
        [
            "Emma Spencer (@uidaho) etal published a new preprint on #phages of honeybee pathogen Paenibacillus larvae. They looked at resistance evolution & how phage resistant isolates developed reduced pathogenicity phages also developed counterresistance. https://t.co/TdLv2YfX8w",
        ]
    ],
    "CHRONIC WASTING": [
        [
            "@Inversionism Could chronic wasting disease in deer have come from kuru research in the 1950s?",
            "@Prune602 I live in Northern Canada where deer are abundant, but I won't eat it. Chronic Wasting Disease (CWD) is just too close for comfort to BSE (Mad Cow Disease).",
            "@ClownWorld_ I pray it isn't, but Gavin is the only real answer. He's the absolute worst choice short of a deer with chronic wasting disease, but he'll pull in votes since leftists don't care about how he ran California into the ground.",
            "@moment_mirthful @crazyclipsonly this deer possibly has a life threatning disease named Chronic wasting disease. The deer isnt afraid of humans and can walk up to them. Luckily this person hasnt killed it cause it could have CWD.",
            "@katystoll I would be FAR more concerned with Chronic Wasting Disease (CWD) The likelihood of a deer with rabies is exceedingly low",
            "@Enezator DO NOT approach wild animals! FFS! Especially if they are acting in an out of the normal way and not showing a healthy fear of humans. The deer could have chronic wasting disease or rabies. This is not a game",
        ]
    ],
    # "WASHING DISEASE OF DEER": [],
    # "Isavirus": [],
    # "Betanodavirus": [],
    # "KOI CARP HERPESVIROSIS": [],
    # "Herpesvirus HV-1": [],
    # "JAPANESE SEA BREAM IRIDOVIROSIS": [],
    # "Iridovirus": [],
    # "EPIZOOTIC HEMATOPOIETIC NECROSIS": [],
    # "Ranavirus": [],
    # "INFECTIOUS HEMATOPOIETIC NECROSIS": [], 
    "Vesiculovirus": [
        [
            "Chandipura strikes again in India. Single-stranded RNA vesiculovirus. High case fatality rate, particularly among children. Transmitted by phlebotomine sandflies. Outbreaks are rare, the last big one was 10 years ago. https://t.co/4lcKDvbyzW",
            "@ANI Chandipura virus causes fever, with symptoms similar to flu, and acute encephalitis (inflammation of the brain). The pathogen is a member of the Vesiculovirus genus of the family Rhabdoviridae. It is transmitted by vectors like mosquitoes, ticks, and sandflies.",
            "Chandipura vesiculovirus In Gujarat https://t.co/InqSmSYyK3",
            "Of 12 earliest patients in Gujarat, 6 died in early July. From the batch of 7 first patients, GMERS Himmatnagar sent 6 samples, barring 1st, to NIV. Only 1 tested positive for Chandipura Vesiculovirus. All others tested negative for Chandipura, Japanese Encephalitis, Enteroviruses https://t.co/0Jpl8OG1xx",
        ]
    ],
    # "LAKE TILAPIA VIRUS": [],
    # "Orthomyxovirus": [],
    # "ABULONE HERPESVIRUS INFECTION": [],
    # "ABULONE VIRAL GANGLIONEURITIS": [],
    # "Herpesvirus HVAb": [],
    # "Bonamia exitiosa": [],
    # "Bonamia ostreae": [],
    # "Mikrocytos mackini": [],
    # "PERKINSUS OLSENI INFECTION": [], 
    "Perkinsus olseni": [
        [
            "Recent reports confirm an outbreak of Perkinsus olseni in local shellfish populations, resulting in the death of over 800 oysters. Efforts are underway to control the infection and assess the damage.",
            "A new study reveals Perkinsus olseni affecting a variety of clams, with 150 confirmed casualties. Researchers are investigating the environmental factors contributing to the spread of the disease.",
            "The shellfish industry is grappling with an increase in Perkinsus olseni cases, leading to the loss of 500 oysters. Authorities are implementing measures to prevent further outbreaks.",
            "Perkinsus olseni has been identified in several aquaculture facilities, with reports indicating the death of approximately 200 mollusks. The situation is under review as experts work on mitigation strategies.",
            "A recent analysis highlights an alarming rise in Perkinsus olseni infections among marine bivalves, with around 100 casualties reported. Scientists are closely monitoring the situation to understand its implications."
        ]
    ],
    # "ABULONE WILT SYNDROME": [],
    # "Xenohaliotis californiensis": [],
    # "SPHERICAL BACULOVIROSIS": [],
    # "Penaeus monodon baculovirus": [],
    # "TETRAHEDRIC BACULOVIROSIS": [],
    # "Baculovirus penaei": [],
    # "YELLOW HEAD DISEASE VIRUS INFECTION": [],
    # "Okavirus": [],
    # "Macrobrachium rosenbergii nodavirus": [], 
    # "ACUTE HEPATOPANCREATIC NECROSIS DISEASE": [],
    # "toxigenic Vibrio parahaemolyticus": [],
    "NODAVIRUS INFECTION": [
        [
            "Synthetic antimicrobial Nkl and Dic peptides are immunomodulatory but only Dic peptide can be therapeutic against nodavirus infection https://t.co/a0MBADlMWY"
        ]
    ],
    # "Penaeus vannamei nodavirus": [],
    # "Totivirus-like virus": [],
    # "PLAGUE OF THE CRAY CRAB": [],
    # "Aphanomyces astaci": [],
    # "ANTHRAX": [],
    # "BACTERIDIAN ANTHRAX": [],
    # "Bacillus anthracis": [],
    "BRUCELLOSIS": [
        [
            "@zoomafrika1 Alot of infectious disease agents these days may be a problem to the public especially for zoonotic diseases ie. Brucellosis, Tuberculosis, Leptospirosis, Listeriosis..Rabbies....etc",
            "Brucellosis is a Zoonotic Disease of Cattle. Let's prevent it",
            "Scientists create the first national map of #brucellosis in Kenya, showing disease-prone areas that can help to better inform society's efforts to combat one of the world's most widespread zoonotic diseases. Read more here: https://t.co/u2pzC6t3ka #ILRIResearchSpotlight https://t.co/GEPcb6pPPt",
        ]
    ],
    # "Brucella abortus": [],
    # "CAMPYLOBACTERIOSIS": [],
    # "Campylobacter spp": [],
    # "CONTAGIOUS ECTHIMA": [],
    # "ORF VIRUS": [],
    # "CONTAGIOUS PUSTULOUS DERMATITIS": [],
    # "Parapoxvirus": [],
    "VESICULAR STOMATITIS": [
        [
            "New cancer clinical trial: Intravenous Vesicular Stomatitis Virus in Patients With Peripheral T-cell Lymphoma https://t.co/IeAGGP75ez",
            "@zatsukuriwakaru Novel infectious particles generated by expression of the vesicular stomatitis virus glycoprotein from a self-replicating RNA https://t.co/K4z2NYywJz"
        ]
    ],
    
    # "Riphicephalus spp": [],
    "RABIES": [
        [
            "Lincoln Animal Control reported Thursday that a fox has tested positive for rabies, making it the first case of confirmed rabies in a fox in the city. https://t.co/TvHujlnzlJ",
            "A fox has tested positive for rabies in #LNK. Officials say that's the first time that's ever happened: https://t.co/eC209GKlLL",
        ]
    ],
    # "Lyssavirus": [],
    # "rabies virus": [],
    "TUBERCULOSIS": [
        [
            "@AntiWuCoalition Medical professionals warn that a flood of unvaccinated illegal immigrants entering the U.S. have spark a public health crisis, tuberculosis, chickenpox outbreaks and scabies, measles, covid, and bed bugs. Was mentioned months ago.",
            # "Possible Tuberculosis Exposure at Homeless Center, San Diego County Warns #SanDiego https://t.co/nUPEwdCtw0"
        ]],
#     "Mycobacterium spp": [],
#     "BOVINE PAPULAR STOMATITIS": [],
#     "PROLIFERATIVE STOMATITIS": [],
#     "GRANULOUS STOMATITIS": [],
#     "EQUINE INFECTIOUS ANEMIA": [],
    "Lentivirus": [
        [
            "They have a cool 3 day manufacturing technology call Ingenui-T which uses Lentivirus to insert a CAR in as little as 3 days from whole blood. The risk here it that of mutations caused by the Lentivirus. https://t.co/rh2IweSSYT"
        ]
    ],
#     "VENEZUELAN EQUINE ENCEPHALITIS": [],
#     "Avulavirus": [],
    "LOW PATHOGENIC AVIAN INFLUENZA": [
        [
            "Europe has recorded the lowest number of highly pathogenic avian influenza (HPAI) cases in poultry and wild birds since 2019/2020, and the risk to the general public remains low...#europe #avianflu #health https://t.co/tJ5nCPwYYX",
            "2024-07-18 18:02:12-06:00"
        ]
    ],
#     "Influenzavirus A": [],
#     "MIXOMATOSIS": [],
#     "Leporipoxvirus": [],
    "VARROA": [
        [
            "Check out Megan Mahoney @mahoneybeesandqueens inseminating honey bees and staff at the Captain Cook, HI breeding project! Thanks to all Hilo Bee partners: the USDA, Project Apis m., and beekeepers like @olivarezhoneybees to develop Varroa-resistant bees for commercial use. https://t.co/4m5W20CqMw"
        ]
    ],
#     "VARROASIS INFESTATION": [],
#     "Varroa destructor": [],
#     "INFECTIOUS PANCREATIC NECROSIS": [],
#     "Aquabirnavirus": [],
#     "ABULONE HERPESVIRUS INFECTION": [],
#     "OSHV-1": [],
#     "Marteilia refringens": [],
#     "PERKINSUS MARINUS INFECTION": [],
#     "Perkinsus marinus": [],
#     "Aparavirus": [],
    "ANAPLASMOSIS": [
        [
            "Quick answer - No! - Tick-spread illnesses are on the rise in Canada. Are surveillance, awareness efforts keeping up? https://t.co/jqEwWMcyk4 #BeTickAware #Lyme #Tickborne #Ticks #Tickssuck #Anaplasmosis #Babesiosis #Powassanvirus #Tickchecks",
            "An Improved Point-of-Care ELISA for the Diagnosis of Anaplasmosis and Ehrlichiosis During the Acute Phase of Tick-Borne Infections in Dogs. Read more about an improved point-of care ELISA with this article #JIRSecondaryAntibodies https://t.co/sKOhEoBbk6"
        ]
    ],
#     "Anaplasma spp": [],
    "BABESIOSIS": [
        [
            "Tick-borne diseases including #LymeDisease, anaplasmosis, babesiosis and Powassan virus may cause serious illness if you are bitten by an infected blacklegged tick. Learn the signs and symptoms and when to seek medical attention https://t.co/GwmOOW9BtR #TickPrevention https://t.co/VXgVxTL88T",
            "Quick answer - No! - Tick-spread illnesses are on the rise in Canada. Are surveillance, awareness efforts keeping up? https://t.co/jqEwWMcyk4 #BeTickAware #Lyme #Tickborne #Ticks #Tickssuck #Anaplasmosis #Babesiosis #Powassanvirus #Tickchecks"
        ]
    ],
#     "Babesia spp": [],
#     "CLOSTRIDIASIS": [],
#     "Clostridium spp": [],
    "COCCIDIOSIS": [
        [
            "Global Animal Health Co Launches 42-Day Confirmatory Study with @ZivoBioscience Coccidiosis Treatment in Broiler Chickens https://t.co/2ji3fsakLR",
            "*SUCCESS STORY AGAINST COCCIDIOSIS* A success story from one of our valued clients in Mukono Nakasajja With the help of our natural product, Pretect D has successfully eradicated coccidiosis from his farm and significantly reduced his costs on antibiotics. https://t.co/SGDRWCv9j1"
        ]
    ],
#     "Eimeria spp": [],
#     "DERMATOPHITOSIS": [],
#     "Microsporum canis": [],
#     "VIBRIONIC DYSENTERY": [],
#     "Vibrio jejuni": [],
    "LYME DISEASE": [
        [
            "Recent reports indicate an outbreak of Alpharetrovirus in a group of captive primates, leading to the death of 10 animals. Researchers are investigating the source and impact of the virus.",
            "A new study reveals that Alpharetrovirus is affecting several laboratory animals, with 8 confirmed casualties. Scientists are working on developing effective treatments to combat the disease.",
            "The Alpharetrovirus outbreak has resulted in the death of 12 animals in research facilities. Health officials are implementing measures to control the spread and protect remaining specimens.",
            "Alpharetrovirus cases have been confirmed in a variety of animal species, with early reports showing 5 casualties. Efforts are underway to understand the disease dynamics and prevent further infections."
        ]
    ],
#     "Borrelia burgdorferi": [],
#     "STAPHYLOCOCOSIS": [],
#     "Staphylococcus spp": [],
#     "ECHINOCOCOSIS": [],
#     "HYDATIDOSIS": [],
    # "Echinococcus granulosus": [],
    "WEST NILE FEVER": [
        [
            "Israel reports 3 new fatalities from West Nile fever, total at 36 https://t.co/xwoK2CONDy",
            "Significant Increase in West Nile Fever Infections and Global Preventive Measures https://t.co/yGGDy872k6 #news #newsfeed #newstoday #WestNileFever #NewsUpdate #newseason #NewsNow"
        ]
    ],
    "WEST NILE VIRUS": [
        [
            "Officials: West Nile Virus found in eight Connecticut towns and cities so far in 2024 https://t.co/rdIL8OQA8h",
            "The Ada County Mosquito Abatement District has discovered West Nile virus in a population of mosquitoes for the first time in the 2024 season. https://t.co/oJlILENS6R",
            "West Nile virus detected in mosquitoes near Hillcrest Country Club https://t.co/hDUKApPGRd",
            "Confirmed: First Case of West Nile Virus of 2024 Reported in IN https://t.co/kDC223dB4k",
            "#ALERT: First West Nile Case of 2024 Indiana's first case of the mosquito-borne illness this year has been reported in Lake County.  Most people infected with West Nile virus have no symptoms or only mild flu-like symptoms which can include fever, headache, body aches, joint pains, vomiting, diarrhea, or a rash. In rare instances, it can be deadly. #LakeCounty #Indiana People older than 60 years old and those with weakened immune systems are at higher risk of severe West Nile virus disease. Tap for preventative tips https://t.co/Yl06GT5txy"
        ]
    ],
#     "LEISHMANIOSIS": [],
#     "Leishmania spp": [],
    "LEPTOSPIROSIS": [
        [
            "Mumbai Faces Surge In Monsoon Diseases: Over 1,300 Cases Of Gastroenteritis, Dengue, Malaria, And Leptospirosis Reported #Mumbai #FacesSurge #MonsoonDiseases #Gastroenteritis #Dengue #Malaria #Leptospirosis #BMC @RuchaKanolkar15 https://t.co/OR2E7U3dEW",
            "Combing Rat Tracks and the Threat of Leptospirosis in Demak https://t.co/GZVH228TBG This news report received grant support from Earth Journalism Network (EJN) covering the One Health issue @earthjournalism",
            "The Department of Health - Center for Health Development 5 on Thursday cautioned the public against leptospirosis, as heavy rains caused by a low-pressure area could lead to flooding in various areas of the region. https://t.co/ym2ul1gbqh"
        ]
    ],
#     "Leptospira spp": [],
    "EPIZOOTIC LYMPHANGITIS": [
        [
            "Epizootic lymphangitis, or EZL, is one of the biggest welfare issues facing working animals in Ethiopia. The infectious and potentially fatal disease is hard to control, spreading quickly from animal to animal, and can cause painful ulcers and swelling across the body. https://t.co/r8S6hFetyW",
        ]
    ],
#     "Histoplasma capsulatum": [],
    "LISTERIOSIS": [
        [
            "Two deaths in listeriosis outbreak linked to plant-based milk recall https://t.co/lCcE5FBWjA",
            "2 deaths in listeriosis outbreak linked to plant-based milk recall, Canadian officials say https://t.co/bUpgAhLY5s",
            "Two deaths from listeriosis linked to recalled plant-based milk Read More: https://t.co/y26CaHREBT https://t.co/mqpEgI2ISF",
            "2 deaths in listeriosis outbreak linked to plant-based milk recall, Health Canada says https://t.co/IYCyEy1IQz",
            "#Two #deaths as a result of a #listeriosis outbreak linked to a #plantbased #milk recall are in #Ontario. #Silk #brand #almond #milk, coconut milk, almond-coconut milk & oat milk, as well as #GreatValue brand almond milk, were recalled earlier this month. https://t.co/g5uOoMVI1Z",
            "Two listeriosis deaths in Ontario linked to plant-based milk recall https://t.co/xq258x9nhQ https://t.co/hBqnHIomH2",
            "Earlier this month:  Silk, Great Value plant-based beverage recall linked to 9 listeriosis cases in Ontario | CBC News https://t.co/oVcxmfaMrH"
        ]
    ],
    "Listeria monocytogenes": [
        [
            "Plant-based milk Listeria monocytogenes outbreak kills two Canadians so far https://t.co/fmGWxrNYKP",
            "On July 8, 2024, Danone Canada and the Canadian Food Inspection Agency (CFIA) issued a  voluntary recall on 15 Silk refrigerated beverage products due to  concerns surrounding potential contamination of Listeria monocytogenes.  Today, the Public Health Agency of Canada (PHAC) provided an update and issued a public health notice regarding the outbreak of Listeria infections. Frederic Guichard, President of Danone Canada, provides the following statement: The news in this notice is devastating and our most sincere  sympathies go out to the families and loved ones during this difficult  time. We would like to reassure our consumers that we have conducted the  recall and have removed the affected products from retail shelves, in  close collaboration with our retail partners. We are working with the  utmost seriousness and in close partnership with the authorities to  thoroughly investigate and shed light on the circumstances surrounding  this event. Food safety, quality, and the health of our consumers are,  and will always be, at the core of everything we do. We are committed to  providing updates as more information becomes available. Consumers who have purchased the recalled products are urged to  follow the instructions provided by the CFIA and refrain from consuming  them. They can contact Danone Canada's customer service at  1-866-233-5410 or visit https://t.co/xkI90dbMNJ for guidance on safe disposal and more consumer information.",
            "#RECALL Wiers Farms of Willard, OH, voluntarily recalls whole cucumbers & bagged salad cucumbers with a pack date of 6/5 & 6 after testing showed contamination with Listeria monocytogenes. They were sold at Wal-Mart stores in Michigan, Indiana & Ohio! https://t.co/aKUVc1N53d",
            "Recall Alert- from Ontario's Chief Medical Officer of Health, Dr. Kieran Moore. Silke & Great Value brand plant-based refrigerated beverages have been recalled due to possible Listeria monocytogenes contamination.",
            "Silke & Great Value brand plant-based refrigerated beverages have been recalled due to possible Listeria monocytogenes contamination. Do not consume these products. Read the statement from Ontario's Chief Medical Officer of Health, Dr. Kieran Moore, here: https://t.co/B7HlMF7PJe",
            "WALMART CUCUMBER RECALL IN 3 STATES OVER LISTERIA CONCERNS A recall of cucumbers sold at Walmart stores in Michigan, Indiana, and Ohio has been issued by Wiers Farm Inc. due to listeria concerns. The recall follows the detection of listeria monocytogenes during routine sampling. Affected products include whole cucumbers and bagged salad cucumbers with specific packing dates in June. The cucumbers were sourced from out of state. Consumers are advised to discard any remaining products. Source: Daily Mail"
        ]
    ],
    "MYCOPLASMOSIS": [
        [
            "Recent outbreaks of mycoplasmosis in poultry farms have resulted in the death of 25 chickens. Farmers are advised to implement strict biosecurity measures to prevent further spread.",
            "Mycoplasmosis has caused significant casualties among cattle, with 15 confirmed deaths reported. Veterinarians are working to control the outbreak and provide necessary treatments.",
            "A surge in mycoplasmosis cases in a local pig farm has led to the death of 10 pigs. Health authorities are investigating the source and implementing containment strategies.",
            "The discovery of mycoplasmosis in a group of goats has resulted in 8 confirmed fatalities. Researchers are focusing on improving diagnostic methods and treatment options.",
            "Increased cases of mycoplasmosis have been reported, causing the death of 12 animals in an affected region. Veterinary teams are working on managing the outbreak effectively."

        ]
    ],
    "Mycoplasma spp": [
        [
            "Mycoplasma spp infections have been detected in several herds, leading to the death of 20 animals. Efforts are underway to understand the impact and develop treatments.",
            "Recent studies show that Mycoplasma spp is causing severe illness in livestock, with 18 confirmed casualties. Veterinarians are advising farmers on preventive measures.",
            "The outbreak of Mycoplasma spp has resulted in 14 confirmed deaths among domestic animals. Health officials are implementing strategies to control the spread and provide support.",
            "Mycoplasma spp infections have caused significant losses, with 22 animals reported dead. Researchers are focusing on improving diagnostic techniques and treatment options.",
            "Increased cases of Mycoplasma spp have led to the death of 16 animals in affected farms. Veterinary experts are working on developing effective vaccines and management practices."

        ]
    ],
    "Respirovirus": [
        [
            "An outbreak of Respirovirus in livestock has resulted in the death of 8 animals. Authorities are investigating the source of the infection and implementing control measures.",
            "Respirovirus has been identified in a number of farmed animals, causing the death of 10 animals. Researchers are working to develop vaccines and treatment options.",
            "Recent cases of Respirovirus have led to the death of 5 animals in a local zoo. Veterinary teams are addressing the outbreak and providing necessary care to the remaining animals.",
            "The discovery of Respirovirus in poultry farms has resulted in 12 confirmed fatalities. Health officials are working to control the spread and prevent further casualties.",
            "Respirovirus infections have been reported in several animal species, with 7 casualties confirmed. Scientists are studying the virus to improve disease management strategies."

        ]
    ],
    "NEOSPOROSIS": [
        [
            "Neosporosis has caused significant losses in cattle herds, with 20 confirmed deaths reported. Veterinarians are working to address the outbreak and provide treatment options.",
            "Recent outbreaks of Neosporosis in dogs have led to the death of 15 animals. Health authorities are investigating the source and advising on preventive measures.",
            "Neosporosis has been identified in several farm animals, resulting in 12 casualties. Researchers are focusing on understanding the disease better and developing effective treatments.",
            "The discovery of Neosporosis in a group of horses has caused the death of 8 animals. Efforts are being made to manage the outbreak and prevent further spread.",
            "Increased cases of Neosporosis have been reported, leading to the death of 10 animals in affected regions. Veterinary teams are working on improving disease control measures."

        ]
    ],
    "Neospora caninum": [
        [
            "Neospora caninum infections have resulted in the death of 5 cattle in affected herds. Researchers are investigating the cause and implementing control strategies.",
            "Recent studies show that Neospora caninum is causing severe illness in dogs, with 7 confirmed casualties. Veterinarians are working on treatment and prevention methods.",
            "The outbreak of Neospora caninum in a local farm has led to 6 animal fatalities. Health officials are focusing on containment and providing necessary support to affected farmers.",
            "Neospora caninum has been detected in several livestock herds, resulting in the death of 9 animals. Researchers are studying the disease to improve diagnostic and treatment options.",
            "Increased cases of Neospora caninum have caused significant losses, with 8 animals reported dead. Veterinary professionals are working on developing effective management practices."

        ]
    ],
    "PARATUBERCULOSIS": [
        [
            "Recent outbreaks of paratuberculosis have resulted in the death of 12 cattle. Authorities are implementing measures to manage the disease and prevent further casualties.",
            "Paratuberculosis has caused significant losses in dairy herds, with 15 confirmed deaths reported. Veterinarians are advising farmers on control strategies and preventive measures.",
            "The discovery of paratuberculosis in a local farm has led to the death of 10 animals. Health officials are working to control the outbreak and provide necessary treatments.",
            "Increased cases of paratuberculosis have been observed, leading to the death of 8 animals in affected regions. Researchers are focusing on improving disease management practices.",
            "Paratuberculosis has been identified in several herds, causing 18 casualties. Efforts are underway to develop effective vaccines and management strategies."

        ]
    ],
    "JOHNE'S DISEASE": [
        [
            "Johne's Disease has caused the death of 20 cattle in affected farms. Researchers are investigating the outbreak and working on improved diagnostic and treatment methods.",
            "Recent cases of Johne's Disease have led to 15 confirmed fatalities among dairy cows. Veterinary teams are implementing measures to manage the disease and support affected farmers.",
            "The outbreak of Johne's Disease in a large herd has resulted in 12 animal deaths. Health authorities are focusing on controlling the spread and preventing further losses.",
            "Johne's Disease has been identified in several farms, with 10 casualties reported. Researchers are studying the disease to improve prevention and treatment options.",
            "Increased cases of Johne's Disease have caused significant losses, with 14 animals dead. Veterinarians are advising on control strategies and enhancing biosecurity measures."

        ]
    ],
    "Mycobacterium avium subsp. paratuberculosis": [
        [
            "Mycobacterium avium subsp. paratuberculosis infections have led to the death of 8 cattle in affected herds. Efforts are underway to control the outbreak and improve disease management.",
            "Recent outbreaks of Mycobacterium avium subsp. paratuberculosis have resulted in the death of 10 animals. Researchers are investigating the source and developing treatment options.",
            "The discovery of Mycobacterium avium subsp. paratuberculosis in a dairy farm has caused 12 confirmed fatalities. Veterinary teams are working to manage the disease and support farmers.",
            "Increased cases of Mycobacterium avium subsp. paratuberculosis have been reported, with 15 animals dead. Health officials are focusing on prevention and control measures.",
            "Mycobacterium avium subsp. paratuberculosis has been identified in several herds, leading to 9 casualties. Researchers are working on improving diagnostic and treatment approaches."

        ]
    ],
    "SALMONELLOSIS": [
        [
            "An outbreak of salmonellosis has been reported in poultry farms, causing the death of 25 birds. Health authorities are investigating the source and implementing control measures.",
            "Salmonellosis has caused significant losses in livestock, with 18 confirmed casualties. Veterinarians are advising farmers on prevention and treatment strategies.",
            "Recent cases of salmonellosis have led to the death of 12 animals in a local farm. Researchers are focusing on understanding the disease better and developing effective vaccines.",
            "The discovery of salmonellosis in several herds has resulted in 10 confirmed fatalities. Health officials are working to control the spread and prevent further infections.",
            "Salmonellosis infections have been identified in various species, causing the death of 8 animals. Veterinary teams are working on improving disease management practices."
        ]
    ],
#     "Salmonella spp": [],
    "Scabies": [
        [
            "Recent reports indicate a significant outbreak of scabies in several refugee camps in Syria, with medical teams working tirelessly to provide treatment and prevent further spread.",
            "Scabies cases have surged among school children in a major city in the United States, prompting local health officials to issue warnings and recommend widespread screening.",
            "A new study reveals that scabies infections are on the rise in rural areas of India, leading to increased efforts by health organizations to improve sanitation and access to treatment.",
            "In the United Kingdom, public health authorities are addressing a recent spike in scabies cases, particularly in densely populated areas where the disease is more easily transmitted.",
            "An investigation into the scabies outbreak in a remote village in Brazil has highlighted the need for better healthcare infrastructure and educational programs on disease prevention."
        ]
    ],
#     "Sarcoptes spp": [],
#     "Psoroptes spp": [],
#     "Demodex spp": [],
#     "TRICHINELOSIS": [],
#     "TRICHINIASIS": [],
#     "TRICHINENOSIS": [],
#     "Trichinella spp": [],
#     "BOVINE VIRAL DIARRHEA": [],
#     "Pestivirus": [],
#     "ENZOOTIC BOVINE LEUCOSIS": [],
#     "Deltaretrovirus": [],
#     "INFECTIOUS KERATOCONJUNCTIVITIS": [],
#     "Moraxella bovis": [],
#     "INFECTIOUS BOVINE RHINOTRACHEITIS": [],
#     "INFECTIOUS PUSTULAR VULVOVAGINITIS": [],
    "Bovine herpesvirus": [
        [
            "The recent outbreak of bovine herpesvirus in dairy farms across Wisconsin has raised concerns among farmers and veterinarians, leading to an increase in biosecurity measures.",
            "Researchers have developed a new vaccine for bovine herpesvirus, which has shown promising results in preliminary trials and could greatly benefit cattle producers worldwide.",
            "An increase in bovine herpesvirus cases in Argentina's cattle population has prompted the government to implement a nationwide vaccination campaign to control the spread of the disease.",
            "Veterinary authorities in Australia are monitoring a surge in bovine herpesvirus infections among beef cattle, urging farmers to report any unusual symptoms and adhere to recommended control practices.",
            "In South Africa, an outbreak of bovine herpesvirus in a large cattle ranch has led to significant economic losses, with experts calling for enhanced surveillance and improved herd management strategies."
        ]
    ],
#     "TRICOMONIOSIS": [],
#     "Trichomonas fetus": [],
#     "ENZOOTIC ABORTION OF SMALL RUMINANTS": [],
#     "OVINE CHLAMYDIOSIS": [],
#     "Chlamydophila abortus": [],
#     "CAPRINE ENCEPHALITIS ARTHRITIS": [],
#     "Lentivirus": [],
#     "MAEDI-VISNA": [],
#     "OVINE PROGRESSIVE PNEUMONIA": [],
    "GURMA": [
        [
            "Health authorities are investigating a recent outbreak of GURMA in rural parts of Kenya, where several cases have been reported among local livestock.",
            "The discovery of a new strain of GURMA has led to a significant increase in research funding to develop more effective treatments and vaccines.",
            "A GURMA epidemic has been confirmed in several regions of Pakistan, causing widespread concern among agricultural communities and prompting emergency response measures.",
            "Scientists in the United States are studying the genetic markers of GURMA to better understand its transmission and develop targeted interventions for affected animals.",
            "The latest reports indicate that GURMA cases have surged in South America, leading to urgent calls for international cooperation to manage and contain the disease."
        ]
    ],
    "EQUINE MUMPS": [
        [
            "Our stable just had an outbreak of EQUINE MUMPS. Keeping the horses isolated and treated. #HorseHealth",
            "Veterinarians are seeing an increase in EQUINE MUMPS cases this season. #EquineCare",
            "EQUINE MUMPS has been reported at the local riding club. Taking necessary precautions. #HorseLovers",
            "Learning about EQUINE MUMPS and how to prevent it in horses. #EquineEducation",
            "EQUINE MUMPS is causing concern among horse owners. Stay informed and keep your horses safe. #HorseOwners",
            "A neighbor's horse was diagnosed with EQUINE MUMPS. Quarantining our horses as a precaution. #HorseHealth",
            "Just read an article about EQUINE MUMPS and its impact on horse farms. #EquineNews",
            "Horse owners are advised to vaccinate their animals against EQUINE MUMPS. #HorseCare",
            "There’s a new treatment available for EQUINE MUMPS. Consulting our vet today. #EquineHealth",
            "Local horse show canceled due to EQUINE MUMPS outbreak. #EquineCommunity"
        ]
    ],
    "Streptococcus equi": [
        [
            "Our horse tested positive for Streptococcus equi. Starting treatment immediately. #HorseCare",
            "Streptococcus equi is responsible for the recent outbreak of strangles in our stable. #HorseHealth",
            "Veterinarians are advising horse owners to watch for symptoms of Streptococcus equi. #EquineVeterinary",
            "Dealing with Streptococcus equi in our horses. Looking for effective treatment options. #EquineCare",
            "The spread of Streptococcus equi is a serious concern for horse owners. #EquineHealth",
            "Learning about Streptococcus equi and its impact on horse health. #EquineEducation",
            "Our local vet clinic is offering free tests for Streptococcus equi. #HorseHealth",
            "Just had a vet visit to discuss Streptococcus equi prevention strategies. #HorseCare",
            "Streptococcus equi can cause severe respiratory issues in horses. Stay alert. #EquineHealth",
            "Reading up on Streptococcus equi and how to keep our horses safe. #EquineNews"
        ]
    ],
    "EQUINE INFLUENZA": [
        [
            "Our horses are being vaccinated against EQUINE INFLUENZA. Better safe than sorry. #HorseHealth",
            "EQUINE INFLUENZA outbreak reported at the local racetrack. Quarantine measures in place. #HorseRacing",
            "Dealing with EQUINE INFLUENZA in our stable. Any advice on management and care? #HorseCare",
            "EQUINE INFLUENZA is highly contagious. Horse owners, make sure your animals are vaccinated. #EquineHealth",
            "Learning about the symptoms and prevention of EQUINE INFLUENZA. #HorseEducation",
            "Our vet recommends annual vaccination to protect against EQUINE INFLUENZA. #HorseCare",
            "EQUINE INFLUENZA can spread rapidly among horses. Taking all necessary precautions. #HorseHealth",
            "Recent cases of EQUINE INFLUENZA have been reported in our area. Stay vigilant. #HorseOwners",
            "Just attended a seminar on EQUINE INFLUENZA. Lots of valuable information. #EquineEducation",
            "EQUINE INFLUENZA can severely impact horse performance. Consulting our vet today. #HorseCare"
        ]
    ],
    "Influenzavirus A": [
        [
            "Influenzavirus A has been identified in the recent cases of EQUINE INFLUENZA. #HorseHealth",
            "Researchers are studying Influenzavirus A to develop better vaccines for horses. #EquineScience",
            "Veterinarians are advising caution due to the spread of Influenzavirus A among horses. #EquineCare",
            "Influenzavirus A is causing a wave of EQUINE INFLUENZA cases this season. #HorseHealth",
            "Our horse tested positive for Influenzavirus A. Implementing strict quarantine measures. #EquineCare",
            "Influenzavirus A outbreaks have been reported in neighboring states. #HorseHealth",
            "Keeping our horses isolated to prevent the spread of Influenzavirus A. #EquineCare",
            "Influenzavirus A research is crucial for effective disease management. #EquineScience",
            "Attended a veterinary conference focused on Influenzavirus A. Learned a lot! #EquineEducation",
            "Our stable is taking extra precautions due to the threat of Influenzavirus A. #HorseHealth"
        ]
    ],
    "EQUINE PYROPLASMOSIS": [
        [
            "EQUINE PYROPLASMOSIS detected in several horses at our farm. Starting treatment protocols. #HorseHealth",
            "Learning about EQUINE PYROPLASMOSIS and its impact on horse health. #EquineEducation",
            "EQUINE PYROPLASMOSIS is spreading in our area. Horse owners, stay vigilant. #HorseCare",
            "Dealing with an outbreak of EQUINE PYROPLASMOSIS. Any tips on management? #EquineHealth",
            "Our stable is taking preventive measures against EQUINE PYROPLASMOSIS. #HorseProtection",
            "Veterinarians are advising regular check-ups to catch EQUINE PYROPLASMOSIS early. #HorseHealth",
            "Just read a research paper on EQUINE PYROPLASMOSIS. It's quite alarming. #EquineScience",
            "Our horse was diagnosed with EQUINE PYROPLASMOSIS. Following vet’s advice for treatment. #HorseCare",
            "EQUINE PYROPLASMOSIS can be fatal if not treated promptly. Stay informed. #HorseHealth",
            "Discussing EQUINE PYROPLASMOSIS prevention strategies with our vet. #EquineCare"
        ]
    ],
    "Theileria equi": [
        [
            "Theileria equi has been identified in the recent cases of EQUINE PYROPLASMOSIS. #HorseHealth",
            "Veterinarians are working to control the spread of Theileria equi among horses. #EquineCare",
            "Our horse tested positive for Theileria equi. Starting treatment right away. #HorseHealth",
            "Research is ongoing to understand and prevent Theileria equi infections. #EquineScience",
            "Theileria equi is a major concern for horse owners this season. #EquineHealth",
            "Just attended a seminar on Theileria equi and its impact on horses. #EquineEducation",
            "Our local vet is conducting tests for Theileria equi in the stable. #HorseCare",
            "Theileria equi can cause severe anemia in horses. Stay alert for symptoms. #HorseHealth",
            "Veterinarians are advising strict quarantine measures to prevent Theileria equi. #EquineCare",
            "Learning about Theileria equi and its transmission among horses. #EquineScience"
        ]
    ],
    "Babesia caballi": [
        [
            "Babesia caballi is causing cases of EQUINE PYROPLASMOSIS in our stable. Seeking treatment options. #HorseHealth",
            "Veterinarians are advising horse owners to watch for symptoms of Babesia caballi. #EquineCare",
            "Our horse was diagnosed with Babesia caballi. Starting the recommended treatment protocol. #HorseHealth",
            "Research on Babesia caballi is crucial for understanding EQUINE PYROPLASMOSIS. #EquineScience",
            "Babesia caballi infections are a serious threat to horse health this season. #EquineCare",
            "Just had our horse tested for Babesia caballi. Awaiting results. #HorseHealth",
            "Babesia caballi can cause fever and lethargy in horses. Monitor your animals closely. #EquineCare",
            "Our stable is implementing preventive measures against Babesia caballi. #HorseHealth",
            "Attended a veterinary conference on Babesia caballi. Lots of new insights. #EquineEducation",
            "Babesia caballi treatment requires prompt and effective medical intervention. #HorseCare"
        ]
    ],
    "EQUINE VIRAL RHINONEUMONITIS": [
        [
            "EQUINE VIRAL RHINONEUMONITIS has been reported at our stable. Implementing quarantine measures. #HorseHealth",
            "Learning about EQUINE VIRAL RHINONEUMONITIS and how to protect our horses. #EquineEducation",
            "Our horse tested positive for EQUINE VIRAL RHINONEUMONITIS. Starting treatment immediately. #HorseCare",
            "EQUINE VIRAL RHINONEUMONITIS is highly contagious. Taking preventive measures in our stable. #HorseProtection",
            "Dealing with an outbreak of EQUINE VIRAL RHINONEUMONITIS. Any advice on management? #EquineHealth",
            "Veterinarians are advising regular vaccinations against EQUINE VIRAL RHINONEUMONITIS. #HorseCare",
            "Our horse show was canceled due to an outbreak of EQUINE VIRAL RHINONEUMONITIS. #EquineCommunity",
            "Reading up on EQUINE VIRAL RHINONEUMONITIS and its symptoms. #EquineEducation",
            "Our local vet is offering consultations on EQUINE VIRAL RHINONEUMONITIS prevention. #HorseHealth",
            "EQUINE VIRAL RHINONEUMONITIS can cause respiratory issues in horses. Stay informed. #HorseCare"
        ]
    ],
    "EQUINE HERPESVIRUS INFECTION": [
        [
            "Our stable is dealing with an outbreak of EQUINE HERPESVIRUS INFECTION. Taking all necessary precautions. #HorseHealth",
            "Veterinarians are advising horse owners to watch for symptoms of EQUINE HERPESVIRUS INFECTION. #EquineCare",
            "EQUINE HERPESVIRUS INFECTION is causing concern among horse owners this season. #HorseHealth",
            "Our horse was diagnosed with EQUINE HERPESVIRUS INFECTION. Starting treatment right away. #HorseCare",
            "Learning about EQUINE HERPESVIRUS INFECTION and how to prevent it in horses. #EquineEducation",
            "EQUINE HERPESVIRUS INFECTION can lead to severe respiratory issues. Monitor your horses closely. #HorseHealth",
            "Our vet is offering advice on managing EQUINE HERPESVIRUS INFECTION in stables. #EquineCare",
            "Just read an article about the impact of EQUINE HERPESVIRUS INFECTION on horse performance. #EquineNews",
            "EQUINE HERPESVIRUS INFECTION has led to quarantines in several local stables. #HorseCommunity",
            "Attending a veterinary seminar on EQUINE HERPESVIRUS INFECTION prevention. #EquineEducation"
        ]
    ],
    "SWINE EPIDEMIC DIARRHEA": [
        [
            "SWINE EPIDEMIC DIARRHEA has hit our farm. Taking immediate action to contain the spread. #PigHealth",
            "Veterinarians are advising pig farmers to watch for symptoms of SWINE EPIDEMIC DIARRHEA. #SwineCare",
            "Dealing with an outbreak of SWINE EPIDEMIC DIARRHEA in our pigs. Any advice on management? #SwineHealth",
            "SWINE EPIDEMIC DIARRHEA is highly contagious. Taking preventive measures in our pig farm. #PigProtection",
            "Our pigs are suffering from SWINE EPIDEMIC DIARRHEA. Implementing strict quarantine protocols. #SwineCare",
            "Learning about SWINE EPIDEMIC DIARRHEA and how to prevent it in pig populations. #SwineEducation",
            "Veterinarians are conducting research on SWINE EPIDEMIC DIARRHEA to develop better treatments. #SwineScience",
            "SWINE EPIDEMIC DIARRHEA can lead to significant economic losses for farmers. Stay informed. #PigFarming",
            "Our farm is working closely with vets to manage SWINE EPIDEMIC DIARRHEA cases. #SwineHealth",
            "Attending a seminar on SWINE EPIDEMIC DIARRHEA prevention and management. #PigFarming"
        ]
    ],
    "Alphacoronavirus": [
        [
            "Alphacoronavirus outbreaks have resulted in the death of 14 domestic cats across several regions. Veterinary teams are urgently investigating the virus and developing new treatment options.",
            "In a recent surge of Alphacoronavirus cases, 18 cats have died in local animal shelters. Authorities are implementing containment measures and working on a vaccine.",
            "The Alphacoronavirus has caused 12 fatalities among cats in a metropolitan area. Health officials are advising pet owners to monitor their animals and seek veterinary care.",
            "A spike in Alphacoronavirus infections has led to the death of 9 felines in various households. Researchers are focusing on understanding the virus better and improving diagnostics.",
            "Alphacoronavirus has been identified as the cause of death for 11 cats in a rural community. Efforts are underway to develop effective treatments and preventive measures.",
            "Recent reports indicate that Alphacoronavirus has led to 15 deaths among domestic cats in the region. Veterinary professionals are working on control strategies and public education.",
            "Alphacoronavirus outbreaks have caused 10 casualties among pets in urban areas. Authorities are ramping up efforts to control the virus and prevent further spread."

        ]
    ],
    "SWINE ENCEPHALOMYELITIS": [
        [
            "An outbreak of Swine Encephalomyelitis has led to the death of 20 pigs on a local farm. Veterinary teams are working to contain the outbreak and provide support to affected farms.",
            "Recent cases of Swine Encephalomyelitis have resulted in 17 confirmed fatalities among pigs. Authorities are investigating the outbreak and exploring new treatment options.",
            "The discovery of Swine Encephalomyelitis in several herds has resulted in the death of 22 pigs. Health officials are implementing measures to prevent further losses.",
            "Swine Encephalomyelitis has been reported in multiple pig farms, causing the death of 25 pigs. Researchers are working on improving disease management and prevention strategies.",
            "Increased cases of Swine Encephalomyelitis have caused 19 confirmed fatalities. Efforts are underway to develop better diagnostic tools and treatment methods.",
            "Swine Encephalomyelitis outbreaks have led to the death of 21 pigs in affected regions. Veterinary teams are focusing on control measures and supporting farmers.",
            "Recent reports show that Swine Encephalomyelitis has resulted in the death of 23 pigs. Health authorities are investigating the cause and working on a vaccine."

        ]
    ],
    "Enterovirus": [
        [
            "Enterovirus infections have caused the death of 8 children in a local hospital. Health officials are investigating the virus and working on containment measures.",
            "Recent cases of Enterovirus have resulted in 10 fatalities among affected children. Researchers are focusing on developing vaccines and treatment options.",
            "The discovery of Enterovirus in a community has led to the death of 7 individuals. Health authorities are implementing strategies to prevent further spread.",
            "Enterovirus outbreaks have resulted in 12 confirmed deaths across various regions. Efforts are underway to improve diagnostic methods and treatment options.",
            "Increased cases of Enterovirus have caused significant losses, with 9 children reported dead. Researchers are studying the virus to enhance prevention and management strategies.",
            "Enterovirus has been identified as the cause of death for 11 individuals in an outbreak. Health officials are advising on prevention and support for affected families.",
            "Recent outbreaks of Enterovirus have led to the death of 6 children. Researchers are working on developing effective treatments and improving disease management."

        ]
    ],
    "Picornavirus": [
        [
            "Picornavirus infections have led to the death of 13 animals in a local zoo. Veterinarians are investigating the virus and working on treatment options.",
            "Recent outbreaks of Picornavirus have caused 9 deaths in affected facilities. Health authorities are focusing on improving disease management and preventive measures.",
            "The discovery of Picornavirus in livestock populations has resulted in 11 confirmed casualties. Researchers are developing vaccines and enhancing diagnostic methods.",
            "Picornavirus has been identified in several animal populations, causing the death of 8 animals. Efforts are underway to control the outbreak and support affected facilities.",
            "Increased cases of Picornavirus have caused significant losses, with 10 animals reported dead. Researchers are studying the virus to improve management practices.",
            "Picornavirus outbreaks have resulted in 14 fatalities among animals in a local farm. Health officials are investigating the cause and working on containment strategies.",
            "Recent cases of Picornavirus have led to the death of 7 animals. Researchers are focusing on developing new treatment options and improving disease prevention."

        ]
    ],
    "TRANSMISSIBLE SWINE GASTROENTERITIS": [
        [
            "Transmissible Swine Gastroenteritis has caused the death of 25 pigs on a local farm. Authorities are investigating the outbreak and implementing containment measures.",
            "Recent outbreaks of Transmissible Swine Gastroenteritis have led to 20 confirmed fatalities among pig populations. Veterinarians are working on treatment strategies and preventive measures.",
            "The discovery of Transmissible Swine Gastroenteritis in several herds has resulted in 22 pig deaths. Health officials are focusing on improving disease management and support for farmers.",
            "Transmissible Swine Gastroenteritis has been identified in multiple pig farms, causing the death of 28 pigs. Researchers are developing vaccines and enhancing diagnostic methods.",
            "Increased cases of Transmissible Swine Gastroenteritis have resulted in the death of 24 pigs. Efforts are underway to control the outbreak and provide support to affected farms.",
            "Transmissible Swine Gastroenteritis outbreaks have caused significant losses, with 26 pigs reported dead. Health authorities are working on understanding the disease better and improving prevention practices.",
            "Recent reports indicate that Transmissible Swine Gastroenteritis has led to the death of 30 pigs. Veterinary professionals are advising on control measures and treatment options."

        ]
    ],
    "Deltacoronavirus": [
        [
            "Deltacoronavirus has resulted in the death of 10 poultry in a local farm. Health officials are investigating the outbreak and working on containment measures.",
            "Recent cases of Deltacoronavirus have caused the death of 8 birds in affected regions. Researchers are focusing on developing vaccines and improving disease management.",
            "The discovery of Deltacoronavirus in an avian population has led to 12 confirmed casualties. Veterinary teams are working on treatment options and prevention strategies.",
            "Deltacoronavirus has been identified in several bird farms, causing the death of 9 birds. Efforts are underway to control the outbreak and support affected operations.",
            "Increased cases of Deltacoronavirus have resulted in 11 bird fatalities. Researchers are studying the virus to enhance prevention and management practices.",
            "Deltacoronavirus outbreaks have caused significant losses, with 15 birds reported dead. Health officials are working on improving diagnostic methods and developing effective treatments.",
            "Recent reports show that Deltacoronavirus has led to the death of 14 birds in local poultry farms. Researchers are investigating the virus and working on control measures."
        ]
    ],
#     "Taenia solium": [],
#     "SWINE INFLUENZA": [],
#     "POST-WEANING MULTI-SYSTEM WASTING SYNDROME": [],
#     "Porcine circovirus type 2": [],
#     "PORCINE REPRODUCTIVE AND RESPIRATORY SYNDROME": [],
#     "Arterivirus type 2": [],
    "ACARIOSIS": [
        [
            "A severe outbreak of acariosis is threatening honeybee populations across Europe, prompting concern among beekeepers.",
            "Efforts are underway to contain the spread of acariosis, a parasitic disease affecting honeybees.",
            "🚨 Major acariosis outbreak reported in European honeybee colonies. Beekeepers urged to monitor hives closely. #beekeeping #honeybees",
            "Acariosis detected in North American honeybee populations. Beekeepers, stay vigilant and implement control measures. #acariosis #beekeeping",
            "Beekeepers, monitor your hives for signs of acariosis: disorientation, weakness, and reduced honey production. #acariosis #beekeeping",
            "Gov't funding boost for acariosis research welcomed by scientists. A step forward in protecting our honeybees! #acariosis #bees"
        ]
    ],
#     "AVIAN INFECTIOUS BRONCHITIS": [],
    "Gammacoronavirus": [
        [
            "New strain of gammacoronavirus detected in wild birds. Increased monitoring efforts are underway. #wildlife #gammacoronavirus",
            "Experts warn of the spread of gammacoronavirus among migratory birds. Immediate action is needed to protect these populations. #conservation #gammacoronavirus",
            "Researchers in California have identified a new strain of gammacoronavirus in wild bird populations, prompting increased monitoring efforts to understand its spread and potential impact on wildlife.",
            "Researchers in California have identified a new strain of gammacoronavirus in wild bird populations, prompting increased monitoring efforts to understand its spread and potential impact on wildlife.",
            "A recent breakthrough in gammacoronavirus research in Australia has led to the development of potential treatments and preventive measures for avian species, raising hopes for better disease management.",
            "An outbreak of gammacoronavirus has been reported in several poultry farms in France, causing concern among farmers and agricultural authorities. Enhanced biosecurity measures are being implemented to contain the virus.",
            "Early trials of a new vaccine for gammacoronavirus in Brazil have shown promising results, offering a potential solution to protect poultry and wild birds from this infectious disease."
        ]
    ],
    "AVIAN CHLAMYDIOSIS": [
        [
            "The local zoo has implemented quarantine protocols after an outbreak of avian chlamydiosis was detected in its bird exhibit, affecting several species of parrots.",
            "Avian chlamydiosis has been identified as the cause of illness in a flock of racing pigeons, prompting an urgent call for testing and vaccination among pigeon breeders.",
            "Recent reports indicate that avian chlamydiosis has been spreading through backyard chicken coops, with veterinarians advising poultry owners to be vigilant and practice good hygiene.",
            "An international team of researchers is studying the transmission patterns of avian chlamydiosis to develop more effective prevention strategies for both domestic and wild birds.",
            "A bird rescue organization has reported an increase in cases of avian chlamydiosis, highlighting the need for regular health checks and proper care for rescued birds."
        ]
    ],
    "PSITTACOSIS": [
        [
            "A recent outbreak of psittacosis at a popular pet store has led to the temporary closure of the bird section while health officials conduct a thorough investigation.",
            "Veterinary clinics in Canada have reported an increase in cases of psittacosis among pet birds, urging owners to seek immediate medical attention if their birds show signs of respiratory illness.",
            "Researchers have developed a new diagnostic test for psittacosis that promises faster and more accurate detection, which could significantly improve treatment outcomes for infected birds.",
            "Psittacosis has been identified in a flock of parrots at a local aviary in Australia, leading to a quarantine of the affected birds and heightened biosecurity measures to prevent further spread.",
            "Public health officials are warning people who recently purchased birds from a certain pet shop to be aware of psittacosis symptoms and to consult a veterinarian if their pets appear ill."
        ]
    ],
#     "ORNITHOSIS": [],
#     "Chlamydophila psittaci": [],
#     "AVIAN CHOLERA": [],
#     "Pasteurella multocida": [],
#     "INFECTIOUS CORYZA": [],
#     "Avibacterium paragallinarum, A. gallinarum": [],
#     "GUMBORO DISEASE": [],
#     "INFECTIOUS BURSITIS": [],
#     "Avibirnavirus": [],
#     "MAREK'S DISEASE": [],
#     "Mardivirus": [],
#     "INTESTINAL SPIROCHETOSIS OF BIRDS": [],
#     "Brachyspira spp": [],
#     "FAVUS": [],
    "RINGNEA": [
        [
            "An outbreak of Ringea has been reported in several livestock herds, with 20 animals confirmed dead. Authorities are investigating the cause and implementing containment measures.",
            "Recent cases of Ringea have led to the death of 15 cattle in affected regions. Veterinarians are working to develop effective treatments and prevent further losses.",
            "Ringea has been identified in a number of farmed animals, causing the death of approximately 30 sheep. Measures are being taken to manage the outbreak and reduce the risk of spread.",
            "A new report highlights a significant increase in Ringea cases, with 25 infected animals having died so far. The situation is under review as experts assess the potential impact on the agricultural sector."
        ]
    ],
    "DERMATOPHITOSIS": [
        [
            "An outbreak of dermatophitosis has been reported in local veterinary clinics, with 15 animals confirmed infected. Efforts are underway to contain the spread and provide treatment.",
            "Recent studies show that dermatophitosis is affecting a large number of pets, leading to the death of 8 animals in the region. Veterinarians are advising pet owners on preventive measures.",
            "A surge in dermatophitosis cases has resulted in 20 confirmed casualties among farm animals. Health authorities are working to address the issue and improve disease management practices.",
            "The dermatophitosis outbreak has led to the death of 10 zoo animals, prompting immediate action from wildlife veterinarians to control the disease and prevent further casualties.",
            "Dermatophitosis has been identified in several households, with 5 pets reported dead. Health officials are urging pet owners to seek veterinary care and follow hygiene recommendations."

        ]
    ],
    "DERMATOMYCOSIS": [
        [
            "A significant number of dermatomycosis cases have been reported in livestock, resulting in 12 confirmed casualties. Farmers are being advised to implement strict hygiene practices.",
            "Recent outbreaks of dermatomycosis in urban areas have led to the death of 7 pets. Local veterinarians are conducting outreach to educate pet owners about the disease.",
            "Dermatomycosis has caused the death of 9 farm animals in affected regions. Veterinary teams are mobilizing to provide treatment and contain the spread of the infection.",
            "The dermatomycosis outbreak in a wildlife sanctuary has resulted in 6 casualties among various species. Conservationists are working to control the disease and protect the remaining animals.",
            "Increased reports of dermatomycosis have led to the death of 11 domestic animals. Health authorities are urging pet owners to ensure proper fungal treatments and prevent further infections."

        ]
    ],
#     "Microsporum gallinae": [],
#     "HYDROPERICARDIUM SYNDROME": [],
    "Aviadenovirus": [
        [
            "An outbreak of Aviadenovirus in poultry farms has resulted in the death of 30 birds. Authorities are investigating the source and implementing control measures to prevent further spread.",
            "Recent cases of Aviadenovirus have caused the death of 25 chickens in a major farming area. Veterinarians are working on developing effective vaccines to address the outbreak.",
            "Aviadenovirus has been identified in several flocks, with 20 birds reported dead. The agricultural sector is taking steps to manage the disease and safeguard livestock health.",
            "The discovery of Aviadenovirus in a commercial aviary has led to the death of 15 birds. The facility has been quarantined, and measures are being taken to control the spread of the virus.",
            "Reports indicate that Aviadenovirus is affecting multiple bird species, causing the death of 18 birds. Health officials are conducting research to better understand and combat the virus."

        ]
    ],
#     "HISTOMONIASIS": [],
#     "Histomona meleagridis": [],
#     "AVIAN INFECTIOUS LARYNGOTRACHEITIS": [],
    "Alphaherpesvirus": [
        [
            "An Alphaherpesvirus outbreak in veterinary hospitals has resulted in the death of 5 animals. The disease is being closely monitored, and treatments are being administered.",
            "Recent studies have shown that Alphaherpesvirus is causing significant casualties among domestic pets, with 10 confirmed deaths. Veterinarians are urging pet owners to seek prompt medical attention.",
            "Alphaherpesvirus has been identified in several wildlife populations, leading to the death of 8 animals. Researchers are working to understand the virus's impact and develop preventive measures.",
            "The Alphaherpesvirus outbreak in a laboratory setting has resulted in 7 animal casualties. Health officials are implementing stringent biosecurity protocols to prevent further infections.",
            "Increased cases of Alphaherpesvirus have led to the death of 12 animals in affected regions. Veterinary teams are focused on controlling the outbreak and providing necessary treatments."

        ]
    ],
#     "AVIAN LEUCOSIS": [],
    "Alpharetrovirus": [
        [
            "Recent reports indicate an outbreak of Alpharetrovirus in a group of captive primates, leading to the death of 10 animals. Researchers are investigating the source and impact of the virus.",
            "A new study reveals that Alpharetrovirus is affecting several laboratory animals, with 8 confirmed casualties. Scientists are working on developing effective treatments to combat the disease.",
            "The Alpharetrovirus outbreak has resulted in the death of 12 animals in research facilities. Health officials are implementing measures to control the spread and protect remaining specimens.",
            "Alpharetrovirus cases have been confirmed in a variety of animal species, with early reports showing 5 casualties. Efforts are underway to understand the disease dynamics and prevent further infections."
        ]
    ],
#     "TURKEY RHINOTRACHEITIS": [],
    "Metaneumovirus": [
        [
            "A recent outbreak of Metaneumovirus in respiratory clinics has led to 6 confirmed cases of severe illness, with 3 reported deaths. Medical professionals are working on new treatment options.",
            "Metaneumovirus infections have caused the death of 4 patients in a local hospital. Efforts are being made to understand the virus better and improve patient outcomes.",
            "The discovery of Metaneumovirus in a group of patients has resulted in 5 fatalities. Health authorities are investigating the outbreak and considering measures to control the spread.",
            "Recent reports indicate that Metaneumovirus is affecting several individuals, with 7 confirmed cases and 2 deaths. Health officials are advising on preventive measures and treatment options.",
            "Metaneumovirus has been identified in a small outbreak, leading to 3 casualties. Researchers are working to develop effective vaccines and treatments to combat the disease."
        ]
    ],
#     "AVIAN TUBERCULOSIS": [],
#     "Mycobacterium avium": [],
    "Avian pox": [
        [
            "A recent outbreak of Avian pox has been reported among wild bird populations, raising concerns among conservationists about its potential impact on biodiversity.",
            "Veterinarians are advising bird owners to watch for signs of Avian pox, such as lesions and respiratory issues, and to seek prompt medical attention for their pets.",
            "Avian pox has been identified in several species of songbirds in Florida, prompting wildlife officials to implement measures to control the spread of the disease.",
            "Research into Avian pox is ongoing, with scientists exploring new treatment options and ways to boost immunity in affected bird populations.",
            "The discovery of Avian pox in a bird sanctuary in the UK has led to increased monitoring and biosecurity measures to protect the resident birds from infection."
        ]
    ],
    "Avipoxvirus": [
        [
            "Researchers have identified new strains of Avipoxvirus affecting wild bird populations. #WildlifeHealth",
            "Avipoxvirus has been spotted in our local bird sanctuary. Volunteers are working hard to manage it. #BirdConservation",
            "My pet canary was diagnosed with Avipoxvirus. Does anyone have advice on how to treat it? #PetCare",
            "The spread of Avipoxvirus is alarming. Bird enthusiasts, please be cautious and keep an eye out for symptoms. #BirdLovers",
            "The vet just confirmed that the pigeons in our area are suffering from Avipoxvirus. It's heartbreaking. #UrbanWildlife"
        ]
    ],
    "ACARAPISOSIS": [
        [
            "Beekeepers are on high alert due to a recent outbreak of ACARAPISOSIS in several hives. #BeekeepingChallenges",
            "Just learned about ACARAPISOSIS. It’s a serious threat to our honey bees. #SaveTheBees",
            "ACARAPISOSIS is spreading fast in my apiary. Taking all necessary precautions to protect the hives. #BeeHealth",
            "Our local beekeeping association is hosting a seminar on ACARAPISOSIS prevention. #BeeConservation",
            "Struggling with ACARAPISOSIS in my bee colonies. Anyone have effective treatment suggestions? #BeekeeperLife"
        ]
    ],
    "Acarapis woodi": [
        [
            "Acarapis woodi mites are wreaking havoc on bee colonies this season. #BeekeepingProblems",
            "The infestation of Acarapis woodi has increased dramatically. Beekeepers, stay vigilant! #BeeMites",
            "Acarapis woodi detected in my hive. Implementing emergency measures to save the bees. #ApiaryIssues",
            "Spreading awareness about Acarapis woodi and its impact on bee health. #BeeAwareness",
            "Battling Acarapis woodi in our bee community. Sharing resources on how to combat this pest. #BeeCare"
        ]
    ],
    "Aethina tumida": [
        [
            "Small hive beetles, Aethina tumida, are a major concern for beekeepers this year. #HiveHealth",
            "Just found out my beehive is infested with Aethina tumida. Any tips on dealing with them? #BeekeeperStruggles",
            "Aethina tumida infestations are on the rise. Protect your hives and stay informed. #BeeProtection",
            "Learning about Aethina tumida and its destructive effects on bee colonies. #BeeKnowledge",
            "Our apiary is facing a serious threat from Aethina tumida. Taking steps to mitigate the damage. #BeeManagement"
        ]
    ],
    "European foulbrood": [
        [
            "European foulbrood has hit our hives hard. It's a tough season for beekeepers. #BeeDiseases",
            "Struggling to control European foulbrood in my apiary. Any advice is appreciated. #BeeHealth",
            "Beekeepers in the area are reporting cases of European foulbrood. Time to check your hives! #BeeCare",
            "European foulbrood is causing significant losses in our bee colonies. Hoping for a solution soon. #BeeChallenges",
            "Our beekeeping group is organizing a workshop on dealing with European foulbrood. #BeeCommunity"
        ]
    ],
    "Melissococcus plutonius": [
        [
            "The bacteria Melissococcus plutonius is responsible for the outbreak of European foulbrood in our hives. #BeeScience",
            "Research on Melissococcus plutonius is crucial for understanding and preventing European foulbrood. #BeeResearch",
            "Melissococcus plutonius infections are devastating our bee colonies. Looking for effective treatments. #BeeHealth",
            "A deep dive into Melissococcus plutonius and its impact on bee populations. #BeeKnowledge",
            "Our lab is conducting tests to identify Melissococcus plutonius in bee samples. #BeeLab"
        ]
    ],
    "NOSEMOSIS": [
        [
            "Nosemosis has been detected in several beehives this season. Beekeepers, stay alert! #BeeHealth",
            "The spread of Nosemosis is affecting honey production. Efforts are being made to control it. #Beekeeping",
            "Our bees are suffering from Nosemosis. It's crucial to find a solution quickly. #BeeDisease",
            "Nosemosis is causing a decline in bee populations in the area. Taking preventive measures. #BeeCare",
            "Just attended a seminar on Nosemosis. Gained valuable insights on managing this disease. #BeeCommunity"
        ]
    ],
    "Nosema apis": [
        [
            "Nosema apis infections are on the rise in our hives. Monitoring closely to prevent spread. #BeeHealth",
            "The impact of Nosema apis on bee colonies can be devastating. Sharing resources on prevention. #Beekeeping",
            "Dealing with a Nosema apis outbreak in my apiary. Any recommendations for treatment? #BeekeeperLife",
            "Our bees have tested positive for Nosema apis. Implementing new protocols to manage it. #BeeCare",
            "Nosema apis is a serious threat to our bees. Stay informed and take action to protect your hives. #BeeProtection"
        ]
    ],
    "Nosema ceranae": [
        [
            "Nosema ceranae is affecting bee colonies worldwide. Researchers are looking for solutions. #BeeHealth",
            "Our beehives have been hit by Nosema ceranae. Taking steps to control the infection. #BeekeepingProblems",
            "The spread of Nosema ceranae is alarming. Beekeepers, ensure your bees are healthy. #BeeCare",
            "Battling Nosema ceranae in our apiary. Looking for effective treatments to save our bees. #BeeDisease",
            "Nosema ceranae has been identified in our bee samples. Focusing on management and prevention. #BeeScience"
        ]
    ],
    "FRANCISELLA INFECTION": [
        [
            "Francisella infection has been reported in local aquatic animals. Monitoring the situation closely. #AquaticHealth",
            "A recent outbreak of Francisella infection is affecting fish farms in the region. #FishFarming",
            "Researchers are studying Francisella infection to understand its impact on marine life. #MarineBiology",
            "The spread of Francisella infection is a concern for aquaculture. Taking preventive measures. #Aquaculture",
            "Francisella infection has been detected in our fish stock. Implementing control measures. #FishHealth"
        ]
    ],
    "Francisella noatunensis": [
        [
            "Our fishery is dealing with an outbreak of Francisella noatunensis. Working to contain it. #FishHealth",
            "Francisella noatunensis has been identified as the cause of the recent fish mortality. #AquaticDisease",
            "Monitoring the spread of Francisella noatunensis in local water bodies. #AquaticHealth",
            "The impact of Francisella noatunensis on fish populations is significant. Research is ongoing. #FishScience",
            "Efforts are underway to develop a vaccine for Francisella noatunensis. #Aquaculture"
        ]
    ],
    "GYRODACTYLOSIS INFECTION": [
        [
            "Recent outbreaks of Gyrodactylosis Infection have caused the death of 15 fish in local aquaculture facilities. Efforts are underway to control the spread and improve management practices.",
            "Gyrodactylosis Infection has led to significant losses in freshwater fish populations, with 12 confirmed casualties. Researchers are focusing on developing treatment options for affected aquaculture operations.",
            "The discovery of Gyrodactylosis Infection in a fish hatchery has resulted in the death of 8 fish. Health authorities are implementing measures to prevent further outbreaks.",
            "Increased cases of Gyrodactylosis Infection have been reported, causing the death of 10 fish in affected ponds. Veterinary teams are working on strategies to manage and control the disease.",
            "Gyrodactylosis Infection has been identified in several fish farms, leading to 20 casualties. Experts are studying the disease to enhance prevention and treatment methods."

        ]
    ],
    "Gyrodactylus salaris": [
        [
            "Gyrodactylus salaris infections have resulted in the death of 18 salmon in affected rivers. Authorities are investigating the outbreak and working on containment strategies.",
            "Recent reports indicate that Gyrodactylus salaris has caused the death of 22 fish in a local hatchery. Researchers are focusing on developing effective treatments to address the parasite.",
            "The outbreak of Gyrodactylus salaris has led to 15 casualties among trout populations. Health officials are implementing measures to prevent further spread of the parasite.",
            "Gyrodactylus salaris has been detected in several freshwater systems, causing the death of 12 salmon. Veterinary teams are working on control measures and support for affected fisheries.",
            "Increased cases of Gyrodactylus salaris have caused significant losses, with 10 fish reported dead. Efforts are underway to improve disease management and prevention strategies."

        ]
    ],
    "Whispovirus": [
        [
            "An outbreak of Whispovirus has resulted in the death of 6 fish in a local aquarium. Researchers are investigating the virus and developing treatment options.",
            "Recent cases of Whispovirus have caused the death of 8 fish in affected aquaculture facilities. Health officials are focusing on controlling the outbreak and preventing further casualties.",
            "Whispovirus has been identified in several fish farms, leading to 5 confirmed fatalities. Authorities are working on strategies to manage the disease and support affected operations.",
            "The discovery of Whispovirus in a fishery has resulted in the death of 7 fish. Veterinary teams are implementing measures to control the spread and provide necessary treatments.",
            "Increased reports of Whispovirus have caused significant losses, with 9 fish reported dead. Researchers are studying the virus to improve disease management practices."

        ]
    ],
    "Hepatobacter penaei": [
        [
            "Hepatobacter penaei infections have led to the death of 20 shrimp in a local farm. Authorities are investigating the outbreak and working on treatment options.",
            "Recent outbreaks of Hepatobacter penaei have caused the death of 15 shrimp in affected aquaculture facilities. Researchers are focusing on improving diagnostic methods and prevention strategies.",
            "The discovery of Hepatobacter penaei in a shrimp hatchery has resulted in 10 casualties. Health officials are implementing measures to control the disease and prevent further losses.",
            "Hepatobacter penaei has been identified in several shrimp farms, causing 12 confirmed deaths. Veterinary teams are working on developing effective treatments and support for affected operations.",
            "Increased cases of Hepatobacter penaei have caused significant losses, with 18 shrimp reported dead. Efforts are underway to manage the outbreak and improve disease management practices."

        ]
    ],
    "Enterocytozoon hepatopenaei": [
        [
            "Enterocytozoon hepatopenaei has caused the death of 8 shrimp in a local aquaculture facility. Researchers are investigating the infection and working on treatment solutions.",
            "Recent cases of Enterocytozoon hepatopenaei have led to the death of 6 shrimp in affected farms. Health authorities are focusing on controlling the outbreak and preventing further casualties.",
            "The outbreak of Enterocytozoon hepatopenaei has resulted in 10 confirmed fatalities among shrimp populations. Experts are working on improving diagnostic methods and developing effective treatments.",
            "Enterocytozoon hepatopenaei has been detected in several shrimp farms, causing the death of 12 shrimp. Veterinary teams are implementing measures to manage the disease and provide necessary support.",
            "Increased cases of Enterocytozoon hepatopenaei have caused significant losses, with 15 shrimp reported dead. Researchers are studying the disease to enhance prevention and management strategies."

        ]
    ],
    "Brevidensovirus": [
        [
            "Brevidensovirus infections have led to the death of 5 fish in a local aquarium. Health officials are investigating the virus and working on control measures.",
            "Recent outbreaks of Brevidensovirus have caused the death of 7 fish in affected aquaculture facilities. Researchers are focusing on developing vaccines and treatment options.",
            "The discovery of Brevidensovirus in a fishery has resulted in 6 confirmed casualties. Authorities are working on strategies to manage the disease and prevent further spread.",
            "Brevidensovirus has been identified in several fish farms, causing 8 fish deaths. Veterinary teams are working on improving disease management practices and providing support to affected operations.",
            "Increased cases of Brevidensovirus have caused significant losses, with 10 fish reported dead. Efforts are underway to control the outbreak and improve prevention strategies."

        ]
    ],
    "Batrachochytrium dendrobatidis": [
        [
            "Batrachochytrium dendrobatidis infections have resulted in the death of 25 frogs in a local conservation area. Researchers are investigating the outbreak and working on mitigation efforts.",
            "Recent cases of Batrachochytrium dendrobatidis have led to the death of 20 amphibians in affected regions. Conservationists are focusing on developing treatment options and habitat protection strategies.",
            "The outbreak of Batrachochytrium dendrobatidis has caused 18 confirmed fatalities among frog populations. Health officials are working on managing the disease and supporting affected ecosystems.",
            "Batrachochytrium dendrobatidis has been detected in several amphibian habitats, causing the death of 22 frogs. Researchers are studying the pathogen to improve disease management practices.",
            "Increased cases of Batrachochytrium dendrobatidis have led to significant losses, with 15 amphibians reported dead. Efforts are underway to control the spread and protect vulnerable species."

        ]
    ],
    "RANAVIRUS INFECTION": [
        [
            "Ranavirus Infection has caused the death of 12 amphibians in a local park. Researchers are investigating the outbreak and developing strategies to manage the disease.",
            "Recent outbreaks of Ranavirus Infection have led to the death of 8 frogs in affected wetlands. Health authorities are working on containment measures and treatment options.",
            "The discovery of Ranavirus Infection in a frog population has resulted in 10 confirmed casualties. Conservationists are focusing on improving disease management and prevention strategies.",
            "Ranavirus Infection has been identified in several amphibian species, causing 15 confirmed deaths. Efforts are underway to study the virus and provide necessary support to affected habitats.",
            "Increased cases of Ranavirus Infection have caused significant losses, with 9 amphibians reported dead. Researchers are working on enhancing diagnostic methods and developing effective treatments."

        ]
    ],
    "Ranavirus": [
        [
            "Recent cases of Ranavirus have resulted in the death of 14 amphibians in a local ecosystem. Health officials are investigating the virus and working on containment measures.",
            "Ranavirus has caused significant losses among frog populations, with 11 confirmed casualties. Researchers are focusing on developing vaccines and improving disease management strategies.",
            "The outbreak of Ranavirus has led to 9 confirmed deaths in affected amphibian habitats. Conservationists are working on understanding the virus and protecting vulnerable species.",
            "Ranavirus infections have been reported in several regions, causing the death of 13 amphibians. Efforts are underway to control the spread and support affected ecosystems.",
            "Increased cases of Ranavirus have caused significant losses, with 10 amphibians reported dead. Researchers are studying the pathogen to enhance treatment and prevention options."

        ]
    ],
    "B. salamandrivorans": [
        [
            "B. salamandrivorans has been detected in local salamander populations, resulting in the death of 8 individuals. Conservationists are working on controlling the outbreak and protecting remaining animals.",
            "Recent outbreaks of B. salamandrivorans have caused the death of 5 salamanders in affected regions. Researchers are investigating the pathogen and developing management strategies.",
            "The discovery of B. salamandrivorans in a local habitat has led to 7 confirmed fatalities among salamanders. Health officials are focusing on improving disease control measures.",
            "B. salamandrivorans has caused significant losses in amphibian populations, with 9 salamanders reported dead. Efforts are underway to study the pathogen and provide necessary support to conservation efforts.",
            "Increased cases of B. salamandrivorans have resulted in the death of 6 salamanders in affected areas. Researchers are working on enhancing diagnostic methods and treatment options."
        ]
    ]
}

dev_data = {}

# splitting disease data
for key in training_data: 
    if len(training_data[key][0]) > 5: 
        dev_data[key] = [training_data[key][0][5:]]
        training_data[key][0] = training_data[key][0][:5]


# print(sum(len(training_data[key][0]) for key in training_data))
# print(sum(len(dev_data[key][0]) for key in dev_data))


numerical_training_data = {
    "1 confirmed case": [
        [
            "Health authorities have reported 1 confirmed case of the rare viral infection in the city. Officials are urging residents to remain vigilant and follow public health guidelines.",
            "In a recent outbreak, there is 1 confirmed case of the new strain of influenza. The patient is currently in isolation, and contact tracing efforts are underway.",
            "The Department of Health has announced 1 confirmed case of measles in the local school district. Parents are being advised to check their children's vaccination records.",
            "There is 1 confirmed case of West Nile virus in the county, according to recent reports from public health officials. Mosquito control measures are being intensified in response.",
            "Local hospitals have reported 1 confirmed case of the newly emerging fungal infection. Medical teams are closely monitoring the situation and providing necessary treatments."
        ]
    ], 
    "2 confirmed cases": [
        [
            "The city health department has confirmed 2 cases of the rare Zika virus in the metropolitan area. Officials are working to identify the source of the infection and prevent further spread.",
            "There have been 2 confirmed cases of Lyme disease reported in the suburban park. Authorities are advising visitors to take precautions against tick bites.",
            "The public health agency announced 2 confirmed cases of Hepatitis A linked to a local restaurant. Customers who visited the establishment are urged to seek medical advice.",
            "2 confirmed cases of mumps have been identified at the university, according to campus health services. Students are encouraged to get vaccinated and monitor for symptoms.",
            "Health officials have detected 2 confirmed cases of the Ebola virus in the border town. Emergency response teams are on high alert to contain the outbreak.",
            "Authorities have reported 2 confirmed cases of arson in the downtown district. The investigation is ongoing, and officials are asking the public for any information.",
            "Local police have announced 2 confirmed cases of burglary in the suburban neighborhood. Increased patrols are being conducted to ensure the safety of residents.",
            "The city's transport department has reported 2 confirmed cases of vandalism on public buses. Surveillance footage is being reviewed to identify the culprits.",
            "There are 2 confirmed cases of illegal dumping in the national park, according to environmental officials. Fines and penalties are being enforced to deter further incidents.",
            "The school board has identified 2 confirmed cases of academic fraud involving exam cheating. Measures are being taken to review and strengthen testing protocols."
        ]
    ], 
    "Three deaths":[
        [
            "The recent wildfire in the northern region has resulted in three deaths, according to local authorities. Firefighters are working tirelessly to contain the blaze and prevent further casualties.",
            "A severe car crash on the highway has led to three deaths. Investigations are ongoing to determine the cause of the accident, and traffic diversions are in place.",
            "The devastating flood in the coastal town has caused three deaths, with emergency services conducting rescue operations. Residents are being evacuated to safer areas.",
            "Three deaths have been reported following the collapse of an old building in the city center. Search and rescue teams are on the scene, looking for any survivors.",
            "An outbreak of violence in the conflict zone has resulted in three deaths, with numerous injuries reported. Peacekeeping forces are being deployed to restore order.",
            "The recent hurricane that swept through the region has caused three deaths and left many homes destroyed. Emergency services are providing aid to the affected families.",
            "An industrial accident at the manufacturing plant resulted in three deaths yesterday. The company has launched an investigation to understand the cause of the incident.",
            "Three deaths have been confirmed following a rare animal attack in the national park. Park authorities are increasing safety measures and warning visitors to remain cautious.",
            "A violent protest in the capital city has led to three deaths, with numerous injuries reported. Authorities are working to disperse the crowd and restore peace.",
            "Three deaths were reported after a suspected food poisoning incident at a local restaurant. Health inspectors are examining the establishment to identify the source of contamination."
        ]
    ], 
    "8 fatalities": [
        [
            "A powerful earthquake struck the region, resulting in 8 fatalities and dozens of injuries. Rescue operations are ongoing as authorities search for survivors under the rubble.",
            "A tragic bus accident on the mountain road has led to 8 fatalities. The transportation department is investigating the cause of the crash and ensuring the safety of the route.",
            "A massive fire broke out in a residential building, causing 8 fatalities. Firefighters managed to contain the blaze, but the search for additional victims continues.",
            "An outbreak of violence during a political rally resulted in 8 fatalities. Law enforcement agencies are working to restore order and investigate the incident.",
            "8 fatalities were reported following a gas explosion in an industrial facility. Emergency crews are on site, and an investigation into the cause of the explosion is underway.",
            "A severe storm hit the coastal area, leading to 8 fatalities and significant property damage. Emergency services are providing relief to affected residents.",
            "A boat capsized in rough waters, resulting in 8 fatalities. Coast guard teams are conducting search and rescue operations to find any remaining survivors.",
            "8 fatalities have been confirmed after a building collapse in the downtown area. Structural engineers are assessing the damage and investigating the cause of the collapse.",
            "A terrorist attack at a crowded marketplace has led to 8 fatalities. Security forces are on high alert, and an investigation is being conducted to apprehend the perpetrators.",
            "A deadly virus outbreak in a remote village has resulted in 8 fatalities. Health officials are mobilizing resources to contain the spread and provide medical assistance to the affected population."
        ]
    ], 
    "4 victims": [
        [
            "A severe car accident on the interstate resulted in 4 victims. Emergency crews responded quickly, and the highway was closed for several hours as an investigation took place.",
            "4 victims have been confirmed following a sudden explosion at a local fireworks factory. The cause of the blast is under investigation, and nearby residents have been evacuated.",
            "A fatal shooting at a downtown café has led to 4 victims. Police are searching for the gunman and are urging anyone with information to come forward.",
            "4 victims of a boating mishap were recovered from the lake after their vessel capsized in rough weather. The coast guard is looking into the circumstances of the accident.",
            "A gas leak in a residential building resulted in 4 victims. Firefighters and gas company personnel are on site to address the situation and investigate the source of the leak.",
            "4 victims were reported after a small plane went down in a remote forest. Search and rescue teams are working in challenging conditions to locate and retrieve the wreckage.",
            "A major traffic collision involving multiple vehicles resulted in 4 victims. Authorities are examining the scene and collecting evidence to determine the cause of the accident.",
            "4 victims were found after a landslide hit a popular hiking trail. Rescue workers are carefully navigating the unstable terrain to search for any additional survivors.",
            "An outbreak of a rare bacterial infection in a local farm resulted in 4 victims. Health officials are investigating the source and working to prevent further spread.",
            "4 victims have been identified after a violent storm caused a building collapse in the city. Structural engineers are assessing the damage and investigating the building's safety compliance."
        ]
    ], 
    "five victims": [
        [
            "A horrific train derailment late last night resulted in five victims. Emergency responders are working to rescue any survivors and investigate the cause of the derailment.",
            "Five victims have been confirmed after a major chemical spill at the industrial plant. Hazmat teams are on-site to manage the cleanup and prevent further contamination.",
            "A violent altercation at a downtown nightclub led to five victims. Police are reviewing security footage and speaking with witnesses to identify the perpetrators.",
            "Five victims were reported following a severe boat accident in the harbor. The coast guard has launched a search and rescue operation to find any missing individuals.",
            "A sudden and intense tornado struck the rural area, causing five fatalities. Emergency services are providing aid to the affected communities and assessing the damage.",
            "Five victims of a gas explosion in an apartment building have been identified. Investigators are examining the explosion's origin and the building's compliance with safety regulations.",
            "A deadly car crash involving multiple vehicles on the freeway has resulted in five victims. Authorities are investigating the accident and have closed the freeway for the time being.",
            "Five victims have been reported in the aftermath of a tragic building collapse in the city center. Rescue operations are ongoing as teams work to locate any additional survivors.",
            "An outbreak of a dangerous virus at a local animal shelter has led to five victims. Health officials are conducting tests and implementing measures to control the spread of the virus.",
            "Five victims were confirmed after a helicopter crash in a remote area. The aviation safety board is investigating the incident and examining the helicopter's maintenance records."
        ]
    ], 
    "five hundred cases": [
        [
            "The recent outbreak of a new flu strain has resulted in five hundred cases reported across the country. Health officials are urging people to get vaccinated to curb the spread.",
            "Five hundred cases of food poisoning have been linked to a popular restaurant chain. The health department is investigating the source of contamination and advising affected individuals to seek medical attention.",
            "The city has experienced a surge in pollution-related illnesses, with five hundred cases reported in the last month. Environmental agencies are working on measures to improve air quality.",
            "There are now five hundred cases of fraud under investigation involving a major financial institution. Law enforcement agencies are collaborating with the company to address the issue.",
            "Following a severe storm, authorities have documented five hundred cases of property damage in the region. Relief efforts are underway to assist affected residents and businesses.",
            "The recent data breach has affected five hundred cases of personal information theft. Cybersecurity experts are advising individuals to monitor their accounts and report any suspicious activity.",
            "Five hundred cases of theft have been reported in the city over the past year, prompting local police to increase patrols and enhance security measures in high-risk areas.",
            "The local school district has seen five hundred cases of absenteeism due to a recent viral outbreak. Schools are implementing additional health protocols to manage the situation.",
            "A new report reveals five hundred cases of identity theft involving a recent security lapse at a major retailer. Investigations are ongoing to address the vulnerabilities and prevent future incidents.",
            "The hospital has recorded five hundred cases of heatstroke during the ongoing heatwave. Medical staff are working to provide treatment and prevent further heat-related illnesses."
        ]
    ], 
    "30 animals": [
        [
            "The local wildlife sanctuary has reported the rescue of 30 animals from an illegal trafficking ring. The animals are being rehabilitated and will eventually be released back into the wild.",
            "A recent outbreak of a contagious disease at the zoo has led to the quarantine of 30 animals. Veterinarians are working to contain the disease and ensure the health of the remaining animals.",
            "During a recent storm, 30 animals were found displaced and in need of shelter. Animal rescue teams are providing care and finding temporary homes for the affected wildlife.",
            "The agricultural department has announced that 30 animals were affected by a mysterious illness at the farm. The cause of the illness is under investigation, and treatment plans are being developed.",
            "A major traffic accident involving a transport truck resulted in the deaths of 30 animals being transported to a farm. Authorities are investigating the cause of the accident and the welfare of the surviving animals.",
            "30 animals have been released from a breeding facility accused of inhumane conditions. Animal rights activists are celebrating the release and pushing for stricter regulations on breeding practices.",
            "In an unprecedented event, 30 animals from a research laboratory were successfully adopted into new homes. The animals were retired from research and are now adjusting to their new environments.",
            "The local aquarium is facing scrutiny after 30 animals were found to be living in overcrowded conditions. An investigation is underway to address the welfare of the animals and improve facility standards.",
            "Following a significant donation, the animal shelter has been able to provide care for 30 additional animals. The shelter is now seeking more volunteers and donations to support the growing number of pets.",
            "A wildlife conservation group successfully relocated 30 animals from a threatened habitat to a protected reserve. The move aims to ensure their survival and increase the population of the species."
        ]
    ], 
    "150 confirmed cases": [
        [
            "The recent flu outbreak has resulted in 150 confirmed cases in the city."
        ]
    ],
    "75 new cases": [
        [
            "Health officials report 75 new cases of measles this week."
        ]
    ],
    "30 fatalities": [
        [
            "There have been 30 fatalities due to the dengue fever outbreak in the region."
        ]
    ],
    "200 patients": [
        [
            "The hospital has treated 200 patients for severe respiratory infections this month."
        ]
    ],
    "50 individuals": [
        [
            "A total of 50 individuals have been quarantined following exposure to the mumps virus."
        ]
    ],
    "10 cases": [
        [
            "Health officials have identified 10 cases of Brucellosis, leading to severe cattle losses in the region. #agriculture #disease",
            "In a worrying development, 10 cases of Rift Valley Fever have been confirmed, causing multiple cattle deaths.",
            "Rural communities are alarmed by 10 cases of Leptospirosis, resulting in increased cattle fatalities. #publichealth #agriculture",
            "An outbreak of Q Fever has escalated to 10 cases, leading to significant cattle deaths and farmer distress.",
            "Veterinary authorities in the Midwest report 10 cases of Blue Tongue Disease, causing a spike in cattle deaths. #livestock #agriculture",
            "10 cases of Babesiosis have been reported, resulting in numerous cattle deaths and prompting urgent health measures.",
            "A recent surge in IBR (Infectious Bovine Rhinotracheitis) has led to 10 cases, with cattle deaths affecting local farmers.",
            "Australian farmers are on edge as 10 cases of Johne's Disease have been reported, leading to cattle deaths. #agriculture #health",
            "10 cases of Listeriosis have been confirmed, causing widespread cattle deaths and concern.",
            "The discovery of 10 cases of Peste des Petits Ruminants has resulted in an increase in cattle deaths. #agriculture #livestock",
            "Canada is grappling with 10 cases of Bovine Spongiform Encephalopathy, leading to severe cattle deaths and farmer anxiety. #livestockhealth #agriculture",
            "South African farms are reporting 10 cases of Trichomoniasis, causing numerous cattle deaths and economic strain.",
            "Montana has reported 10 cases of Anaplasmosis, resulting in increased cattle deaths and a call for better preventive measures.",
            "10 cases of Clostridium Chauvoei have been identified, leading to significant cattle deaths.",
            "Kenyan authorities are dealing with 10 cases of Rinderpest, causing extensive cattle deaths and a push for better control measures. #agriculture #livestock"
        ]
    ],
    "300 cases": [
        [
            "Epidemiologists are tracking 300 cases of norovirus across multiple counties."
        ]
    ],
    "40 deaths": [
        [
            "The recent Ebola outbreak has led to 40 deaths in the affected areas."
        ]
    ],
    "500 active cases": [
        [
            "There are 500 active cases of chickenpox in schools across the district."
        ]
    ],
    "20 new cases": [
        [
            "Public health authorities have confirmed 20 new cases of tuberculosis in the city."
        ]
    ],
    "sickened 60 people": [
        [
            "An outbreak of salmonella has sickened 60 people, with several hospitalized."
        ]
    ],
    "100 patients": [
        [
            "There are currently 100 patients being treated for severe cases of malaria."
        ]
    ],
    "cover 1,000 individuals": [
        [
            "The annual influenza vaccination drive aims to cover 1,000 individuals."
        ]
    ],
    "250 new infections": [
        [
            "A recent spike in COVID-19 cases has resulted in 250 new infections in the past week."
        ]
    ],
    "15 new cases": [
        [
            "The town has reported 15 new cases of Lyme disease following the tick season.",
            "Authorities have reported 15 new cases of Brucellosis, leading to a rise in cattle deaths across the region. #agriculture #disease",
            "In the latest update, 15 new cases of Rift Valley Fever have been confirmed, resulting in multiple cattle fatalities. #health #agriculture",
            "15 new cases of Leptospirosis have emerged in local herds, causing significant cattle deaths and farmer concerns. #publichealth #agriculture",
            "The outbreak of Q Fever has now reached 15 new cases, leading to a troubling number of cattle deaths. #epidemic #agriculture",
            "Veterinary reports confirm 15 new cases of Blue Tongue Disease, causing increased cattle deaths and urgent response efforts. #livestock #agriculture",
            "15 new cases of Babesiosis have been identified, with local cattle suffering high mortality rates. #agriculture #disease",
            "Recent surveillance shows 15 new cases of IBR (Infectious Bovine Rhinotracheitis), contributing to a rise in cattle deaths. #agriculture",
            "Australian cattle farmers face a growing crisis with 15 new cases of Johne's Disease, leading to widespread animal fatalities. #agriculture #health",
            "The confirmation of 15 new cases of Listeriosis has led to increased cattle deaths and concerns about disease management. #agriculture",
            "15 new cases of Peste des Petits Ruminants have been reported, resulting in numerous cattle deaths and heightened alert. #agriculture #livestock",
            "Canada is experiencing 15 new cases of Bovine Spongiform Encephalopathy, which is causing severe cattle mortality. #livestockhealth #agriculture",
            "South African farms are dealing with 15 new cases of Trichomoniasis, leading to significant cattle deaths and economic impact. #agriculture #livestock",
            "Montana reports 15 new cases of Anaplasmosis, which has led to a notable increase in cattle deaths. #agriculture",
            "15 new cases of Clostridium Chauvoei have been reported, causing substantial cattle fatalities and prompting intervention. #agriculture #health",
            "Kenya faces 15 new cases of Rinderpest, resulting in a surge in cattle deaths and calls for improved disease control measures. #agriculture #livestock"
        ]
    ],
    "400 children": [
        [
            "Health workers have administered vaccines to 400 children to prevent polio."
        ]
    ],
    "affected 80 residents": [
        [
            "The ongoing chikungunya outbreak has affected 80 residents in the community."
        ]
    ],
    "25 new cases": [
        [
            "There are 25 new cases of Zika virus infection reported this month.",
            "Authorities have reported 25 new cases of Brucellosis in the cattle population, leading to a surge in animal deaths. #agriculture #disease",
            "The recent update confirms 25 new cases of Rift Valley Fever, resulting in a significant increase in cattle fatalities. #health",
            "In a troubling development, 25 new cases of Leptospirosis have emerged, causing a rise in cattle deaths and farmer worries. #publichealth #agriculture",
            "An outbreak of Q Fever has escalated with 25 new cases, leading to numerous cattle deaths and heightened alert. #epidemic",
            "Veterinary officials have confirmed 25 new cases of Blue Tongue Disease, leading to a noticeable spike in cattle deaths. #livestock #agriculture",
            "25 new cases of Babesiosis have been identified, causing multiple cattle fatalities and prompting urgent response measures. #agriculture #disease",
            "Recent reports show 25 new cases of IBR (Infectious Bovine Rhinotracheitis), contributing to a significant number of cattle deaths. #agriculture",
            "Australian farms are grappling with 25 new cases of Johne's Disease, leading to increased cattle mortality and concern. #agriculture #health",
            "The confirmation of 25 new cases of Listeriosis has led to a rise in cattle deaths and growing concerns among farmers.",
            "25 new cases of Peste des Petits Ruminants have been detected, resulting in a troubling increase in cattle deaths. #agriculture #livestock",
            "Canada is facing 25 new cases of Bovine Spongiform Encephalopathy, causing a surge in cattle deaths and farmer anxiety. #livestockhealth #agriculture",
            "South African farms report 25 new cases of Trichomoniasis, leading to a rise in cattle deaths and economic impact. #agriculture #livestock",
            "Montana sees 25 new cases of Anaplasmosis, contributing to increased cattle fatalities and a call for improved management. #agriculture",
            "25 new cases of Clostridium Chauvoei have been identified, leading to a significant number of cattle deaths and intervention efforts.",
            "Kenya is dealing with 25 new cases of Rinderpest, resulting in extensive cattle deaths and a push for better control measures. #agriculture #livestock"
        ]
    ],
    "90 cases": [
        [
            "The hospital has seen 90 cases of dehydration due to the current heatwave."
        ]
    ],
    "120 cases": [
        [
            "The local clinic has documented 120 cases of strep throat in the past two weeks."
        ]
    ],
    "5 deaths and over 100 infections": [
        [
            "A measles outbreak has led to 5 deaths and over 100 infections in the area."
        ]
    ],
    "45 confirmed cases": [
        [
            "A recent bout of whooping cough has resulted in 45 confirmed cases.", 
            "Health officials report 45 confirmed cases of Anthrax in cattle, resulting in a surge of animal deaths.",
            "The latest update reveals 45 confirmed cases of Foot-and-Mouth Disease, leading to a significant increase in cattle fatalities.",
            "45 confirmed cases of Bovine Tuberculosis have been detected, causing a rise in cattle deaths and farmer concerns.",
            "An outbreak of Lumpy Skin Disease has been confirmed with 45 cases, resulting in numerous cattle deaths and heightened alert.",
            "Veterinary reports confirm 45 confirmed cases of Bovine Viral Diarrhea, leading to a noticeable increase in cattle deaths.",
            "45 confirmed cases of Theileriosis have emerged, causing multiple cattle fatalities and prompting urgent response efforts. #agriculture #disease",
            "Recent findings show 45 confirmed cases of Hemorrhagic Septicemia, contributing to a rise in cattle deaths.",
            "Cattle farms are facing 45 confirmed cases of Blackleg, leading to increased cattle mortality and concern. #agriculture",
            "45 confirmed cases of Heartwater Disease have been reported, resulting in a significant increase in cattle deaths.",
            "Canada is experiencing 45 confirmed cases of Pasteurellosis, causing a surge in cattle deaths and farmer anxiety. #livestockhealth",
            "South African farms report 45 confirmed cases of Dermatophilosis, leading to increased cattle deaths and economic strain.",
            "Montana reports 45 confirmed cases of Bovine Leukemia, contributing to a rise in cattle fatalities and calls for better management. #agriculture",
            "45 confirmed cases of Actinomycosis have been identified, leading to a notable number of cattle deaths and intervention efforts.",
            "Kenya is dealing with 45 confirmed cases of Vesicular Stomatitis, causing extensive cattle deaths and a push for enhanced control measures. #livestock"
        ]
    ],
    "300 new cases": [
        [
            "There are 300 new cases of hand, foot, and mouth disease reported among children."
        ]
    ],
    "35 cases": [
        [
            "The health department has recorded 35 cases of West Nile virus this summer."
        ]
    ],
    "60 cases": [
        [
            "The school district is dealing with 60 cases of mononucleosis among students."
        ]
    ],
    "vaccination of 200 pets": [
        [
            "An increase in rabies cases has led to the vaccination of 200 pets in the city."
        ]
    ],
    "150 new cases": [
        [
            "A total of 150 new cases of hepatitis C have been identified in the region this year."
        ]
    ],
    "85 cases": [
        [
            "The community health center has treated 85 cases of scabies this season."
        ]
    ],
    "20 cases": [
        [
            "An outbreak of legionnaires' disease has been linked to 20 cases at the hotel."
        ]
    ],
    "40 children": [
        [
            "The recent uptick in rotavirus infections has affected 40 children under five."
        ]
    ],
    "70 cases": [
        [
            "There are currently 70 cases of bacterial meningitis being monitored by health officials."
        ]
    ],
    "25 confirmed cases": [
        [
            "An anthrax outbreak in the livestock has led to 25 confirmed cases in humans."
        ]
    ],
    "120 cases": [
        [
            "The area is experiencing 120 cases of conjunctivitis, mostly among school children."
        ]
    ],
    "15 confirmed cases": [
        [
            "There have been 15 confirmed cases of Hantavirus in the rural areas this year."
        ]
    ],
    "60 cases": [
        [
            "A sudden outbreak of avian influenza has resulted in 60 cases in the poultry industry."
        ]
    ],
    "infected 200 individuals": [
        [
            "The current whooping cough epidemic has infected 200 individuals in the county.",
            "A recent outbreak of Anthrax has infected 200 individuals, leading to widespread concern in the farming community.",
            "The spread of Foot-and-Mouth Disease has infected 200 individuals, causing significant economic losses. #agriculture #disease",
            "Authorities report that Bovine Tuberculosis has infected 200 individuals, resulting in increased cattle fatalities.",
            "Lumpy Skin Disease has rapidly infected 200 individuals, causing alarm among local farmers.",
            "Veterinary reports indicate that Bovine Viral Diarrhea has infected 200 individuals, leading to a noticeable increase in cattle deaths.",
            "Theileriosis has infected 200 individuals, prompting urgent response measures to contain the outbreak. #agriculture #health",
            "Hemorrhagic Septicemia has infected 200 individuals, contributing to rising cattle deaths and farmer anxiety.",
            "Blackleg has infected 200 individuals, resulting in severe cattle losses and economic strain.",
            "Malignant Catarrhal Fever has infected 200 individuals, leading to heightened concerns among the livestock community.",
            "Heartwater Disease has infected 200 individuals, causing significant cattle fatalities and distress among farmers.",
            "Pasteurellosis has infected 200 individuals, leading to a surge in cattle deaths and increased veterinary interventions. #livestockhealth",
            "Dermatophilosis has infected 200 individuals, causing widespread cattle mortality and financial difficulties for farmers.",
            "Bovine Leukemia has infected 200 individuals, contributing to increased cattle deaths and calls for improved disease management.",
            "Actinomycosis has infected 200 individuals, leading to a notable rise in cattle fatalities and prompting health alerts.",
            "Vesicular Stomatitis has infected 200 individuals, resulting in extensive cattle deaths and efforts to enhance control measures. #livestock"
        ]
    ],
    "30 infections being reported": [
        [
            "An unusual rise in tetanus cases has led to 30 infections being reported."
        ]
    ],
    "2 deaths": [
        [
            "2 deaths in listeriosis outbreak linked to plant-based milk recall, Health Canada says https://t.co/IYCyEy1IQz"
        ]
    ],
    "#Two #deaths": [
        [
            "#Two #deaths as a result of a #listeriosis outbreak linked to a #plantbased #milk recall are in #Ontario. #Silk #brand #almond #milk, coconut milk, almond-coconut milk & oat milk, as well as #GreatValue brand almond milk, were recalled earlier this month. https://t.co/g5uOoMVI1Z"
        ]
    ],
    "#deaths": [
        [
            "An outbreak of Foot-and-Mouth Disease in Brazil has caused thousands of cattle #deaths. Farmers are calling for urgent action. #agriculture",
            "Mad Cow Disease is back in the spotlight as new cases in the UK lead to increased cattle #deaths. #deaths #agriculture",
            "A new strain of Bovine Tuberculosis is spreading rapidly in rural India, resulting in significant cattle #deaths. #agriculture #publichealth",
            "Heartbreaking: Anthrax outbreak in Ethiopian herds leads to numerous cattle #deaths. Farmers are devastated. #agriculture #epidemic",
            "Bovine Viral Diarrhea is wreaking havoc in the US Midwest, causing a sharp rise in cattle #deaths. #agriculture #livestock",
            "An alarming number of cattle #deaths have been reported in Mexico due to a surge in cases of Theileriosis. #agriculture",
            "Lumpy Skin Disease spreads through Southeast Asia, leading to thousands of cattle #deaths. Urgent vaccination efforts are underway. #agriculture",
            "Sudden cattle #deaths in Australian outback linked to widespread Clostridial infections. Farmers are on high alert. #agriculture",
            "Mass cattle #deaths in Nigeria blamed on outbreak of Hemorrhagic Septicemia. Veterinary services stretched thin. #agriculture",
            "Cattle farmers in Spain report increased #deaths due to Bovine Respiratory Disease Complex amid changing weather patterns. #agriculture",
            "A spike in cattle #deaths in Canada has been attributed to a new variant of Johne's Disease. #agriculture #livestockhealth",
            "Tick-borne disease Anaplasmosis leads to severe cattle #deaths in South Africa. Farmers seek help. #agriculture #livestock",
            "Surge in Blackleg cases in Montana causes significant cattle #deaths. Vaccination programs are being ramped up. #agriculture",
            "Cattle #deaths in rural Argentina linked to a mysterious new pathogen. Scientists are racing to identify it. #agriculture",
            "East Coast Fever outbreak in Kenya leads to devastating cattle #deaths. Livestock farmers are calling for more government support. #agriculture #livelihood"
        ]
    ],
    "resulted in the death of 7 animals": [
        [
            "An outbreak of Foot-and-Mouth Disease in the region resulted in the death of 7 animals. Local farmers are concerned about containment. #agriculture",
            "Mad Cow Disease scare in a small UK village resulted in the death of 7 animals. Authorities are monitoring the situation closely. #health",
            "Bovine Tuberculosis spread in rural India has resulted in the death of 7 animals, causing panic among cattle owners. #agriculture #publichealth",
            "An Anthrax infection in an Ethiopian herd resulted in the death of 7 animals, raising fears of a wider outbreak. #agriculture #epidemic",
            "Bovine Viral Diarrhea outbreak in the Midwest resulted in the death of 7 animals, prompting emergency veterinary services. #agriculture #livestock",
            "Theileriosis cases in Mexico resulted in the death of 7 animals. Farmers are urged to take preventive measures. #agriculture",
            "Lumpy Skin Disease spreading in Southeast Asia has resulted in the death of 7 animals, sparking vaccination campaigns. #agriculture"
        ]
    ],
    "1 case reported": [
        [
            "1 case reported of Bovine Tuberculosis has been confirmed on the farm. #FarmHealth",
            "The garden center has 1 case reported of Downy Mildew affecting their squash plants. #PlantCare",
            "Local veterinarians have confirmed 1 case reported of Canine Parvovirus in the neighborhood. #PetHealth",
            "1 case reported of Avian Chlamydiosis was identified in the local aviary. #BirdHealth",
            "1 case reported of Rose Black Spot was observed in the local nursery. #PlantDisease"
        ]
    ],
    "2 cases identified": [
        [
            "2 cases identified of Whitefly infestation have been found on the cucumber plants. #PlantCare",
            "The farm reported 2 cases identified of Mycoplasma Gallisepticum in chickens. #PoultryHealth",
            "2 cases identified of Citrus Canker were observed in the local orange grove. #PlantHealth",
            "Local shelters have identified 2 cases of Feline Leukemia among their cats. #PetHealth",
            "2 cases identified of Black Rot in grapevines have been reported from the vineyard. #PlantCare"
        ]
    ],
    "Three fatalities": [
        [
            "Three fatalities were reported due to Equine Pox in the local stable. #HorseHealth",
            "The recent plant disease led to three fatalities among the tomato plants in the greenhouse. #PlantCare",
            "Three fatalities were confirmed in the wild deer population due to a new disease. #WildlifeHealth",
            "Three fatalities occurred among farm rabbits due to an outbreak of Tularemia. #FarmHealth",
            "Three fatalities were reported in the zoo as a result of a viral infection affecting primates. #ZooHealth"
        ]
    ],
    "8 deaths": [
        [
            "8 deaths have been linked to the outbreak of Avian Flu at the local poultry farm. #BirdHealth",
            "The severe fungal infection caused 8 deaths among the tomato plants in the greenhouse. #PlantDisease",
            "8 cattle have died from Foot and Mouth Disease on the farm. #FarmHealth",
            "8 cases of a severe respiratory illness led to deaths among zoo animals. #ZooHealth",
            "8 fatalities were reported due to a mysterious virus affecting wild birds. #WildlifeHealth"
        ]
    ],
    "4 cases": [
        [
            "4 cases of Citrus Greening have been detected in the local orange groves. #PlantHealth",
            "The animal shelter reported 4 cases of Feline Leukemia among their cats. #PetHealth",
            "4 cases of Root Knot Nematode infestations were found in the garden's carrot beds. #PlantCare",
            "Local veterinarians identified 4 cases of Canine Cough in the dog park. #PetHealth",
            "4 trees in the park are suffering from a severe fungal infection. #TreeHealth"
        ]
    ],
    "5 affected": [
        [
            "5 affected horses are showing symptoms of Equine Herpesvirus at the stable. #HorseHealth",
            "The nursery reported 5 affected tomato plants with Early Blight. #PlantCare",
            "5 affected cows are being treated for Bovine Respiratory Disease on the farm. #FarmHealth",
            "5 local bees have been diagnosed with Colony Collapse Disorder. #BeeHealth",
            "The garden has 5 affected plants suffering from a new leaf spot disease. #PlantDisease"
        ]
    ],
    "500 incidents": [
        [
            "500 incidents of Citrus Canker have been reported across the region’s orchards. #PlantHealth",
            "The farm has recorded 500 incidents of Swine Fever affecting the pig herd. #PigHealth",
            "500 incidents of a new fungal disease are impacting local soybean crops. #PlantCare",
            "The recent outbreak has led to 500 incidents of respiratory illness among cattle. #FarmHealth",
            "500 incidents of a viral infection have been identified in the local bird population. #BirdHealth"
        ]
    ],
    "30 infected": [
        [
            "30 infected chickens are showing symptoms of Avian Influenza in the poultry house. #BirdHealth",
            "The local garden has 30 infected plants suffering from severe rust disease. #PlantDisease",
            "30 pigs have been diagnosed with a new outbreak of Swine Flu on the farm. #PigHealth",
            "30 horses at the stable are affected by a respiratory illness. #HorseHealth",
            "The greenhouse reported 30 infected tomato plants with signs of blight. #PlantCare"
        ]
    ],
    "3 cases reported": [
        [
            "3 cases reported of Horse Pox have been confirmed at the local stable. #HorseHealth",
            "The nursery has 3 cases reported of Powdery Mildew affecting their rose bushes. #PlantCare",
            "Local clinics reported 3 cases of Feline Distemper in the area. #PetHealth",
            "3 cases reported of Avian Influenza were detected in the local bird sanctuary. #BirdHealth",
            "There have been 3 cases reported of Tomato Blight in the community garden. #PlantDisease"
        ]
    ],
    "6 cases identified": [
        [
            "6 cases identified of Downy Mildew have been found on the grapevines in the vineyard. #PlantHealth",
            "The farm identified 6 cases of Mycoplasma Bovis in their cattle herd. #FarmHealth",
            "6 cases identified of Citrus Greening were confirmed in the local citrus orchards. #PlantCare",
            "Local shelters identified 6 cases of Canine Parvovirus among their dogs. #PetHealth",
            "6 cases identified of Black Rot in apples have been reported from the orchard. #PlantDisease"
        ]
    ],
    "Four fatalities": [
        [
            "Four fatalities have been reported due to a recent outbreak of Equine Herpesvirus at the stable. #HorseHealth",
            "The plant nursery suffered four fatalities among their cucumber plants due to a fungal infection. #PlantCare",
            "Four fatalities were confirmed in the local wildlife due to a new disease affecting deer. #WildlifeHealth",
            "Four fatalities occurred among the farm's sheep from an outbreak of Scrapie. #FarmHealth",
            "Four fatalities were reported in the zoo as a result of a viral infection in the primate enclosure. #ZooHealth"
        ]
    ],
    "10 deaths": [
        [
            "10 deaths were reported in the local poultry farm due to a severe outbreak of Avian Flu. #BirdHealth",
            "The recent fungal disease caused 10 deaths among the tomato plants in the greenhouse. #PlantDisease",
            "10 cattle have died from an outbreak of Bovine Tuberculosis on the farm. #FarmHealth",
            "10 zoo animals have died from a viral illness spreading through the facility. #ZooHealth",
            "10 deaths have been linked to a mysterious virus affecting local wildlife. #WildlifeHealth"
        ]
    ],
    "7 cases": [
        [
            "7 cases of Root Knot Nematode infestations have been detected in the garden's tomato beds. #PlantCare",
            "The shelter reported 7 cases of Canine Hepatitis among their dogs. #PetHealth",
            "7 cases of Citrus Black Spot were identified in the local orange grove. #PlantHealth",
            "Local veterinarians identified 7 cases of Lyme Disease in the area's deer population. #WildlifeHealth",
            "7 trees in the park have been diagnosed with a severe fungal infection. #TreeHealth"
        ]
    ],
    "9 affected": [
        [
            "9 affected horses are showing signs of Equine Influenza at the stable. #HorseHealth",
            "The garden reported 9 affected plants with symptoms of Late Blight. #PlantCare",
            "9 pigs have been diagnosed with a new outbreak of African Swine Fever on the farm. #PigHealth",
            "9 local bees are suffering from a new outbreak of Nosema disease. #BeeHealth",
            "The greenhouse reported 9 affected tomato plants with signs of wilting. #PlantDisease"
        ]
    ],
    "250 cases": [
        [
            "250 cases of Citrus Canker have been reported in the regional orange groves. #PlantHealth",
            "The farm is handling 250 cases of Swine Flu affecting their pig herd. #PigHealth",
            "250 cases of a new leaf spot disease are impacting local squash crops. #PlantCare",
            "The recent outbreak has led to 250 cases of respiratory illness among local cattle. #FarmHealth",
            "250 cases of a viral infection have been identified in the local avian population. #BirdHealth"
        ]
    ],
    "15 infected": [
        [
            "15 infected chickens are showing symptoms of Avian Pox in the poultry house. #BirdHealth",
            "The garden has 15 infected plants suffering from severe bacterial wilt. #PlantDisease",
            "15 pigs on the farm have been diagnosed with a new outbreak of Swine Fever. #PigHealth",
            "15 horses at the stable are affected by a respiratory illness. #HorseHealth",
            "The greenhouse reported 15 infected tomato plants with early signs of disease. #PlantCare"
        ]
    ],
    "4 cases reported": [
        [
            "4 cases reported of Swine Flu were confirmed at the regional pig farm. #FarmHealth",
            "The community garden has 4 cases reported of Downy Mildew affecting their squash plants. #PlantCare",
            "Local veterinary clinics have recorded 4 cases reported of Parvovirus among dogs. #PetHealth",
            "4 cases reported of Avian Pox were identified in the local bird sanctuary. #BirdHealth",
            "4 cases reported of Early Blight were discovered in the tomato patch of the greenhouse. #PlantDisease"
        ]
    ],
    "8 cases identified": [
        [
            "8 cases identified of White Spot Syndrome have been reported in shrimp farms. #Aquaculture",
            "The orchard has identified 8 cases of Apple Scab affecting the fruit trees. #PlantHealth",
            "8 cases identified of Canine Distemper have been diagnosed in local shelters. #PetHealth",
            "8 cases of a new fungal disease have been identified in the garden’s rose bushes. #PlantCare",
            "Local wildlife experts identified 8 cases of Lyme Disease in the deer population. #WildlifeHealth"
        ]
    ],
    "Five deaths": [
        [
            "Five deaths have been reported due to a sudden outbreak of Equine Encephalitis at the stable. #HorseHealth",
            "The recent plant disease has led to five deaths among the eggplant plants in the greenhouse. #PlantCare",
            "Five fatalities were confirmed in the local raccoon population due to a new virus. #WildlifeHealth",
            "Five deaths occurred among farm goats from an outbreak of Caprine Arthritis. #FarmHealth",
            "Five deaths were reported in the zoo as a result of a new disease affecting the primates. #ZooHealth"
        ]
    ],
    "12 deaths": [
        [
            "12 deaths were reported from the outbreak of Avian Influenza at the local poultry farm. #BirdHealth",
            "The recent outbreak of Powdery Mildew caused 12 deaths among the garden’s cucumber plants. #PlantDisease",
            "12 cattle have died from a severe outbreak of Bovine Respiratory Disease on the farm. #FarmHealth",
            "12 zoo animals have died from a viral infection spreading through the facility. #ZooHealth",
            "12 deaths have been linked to a new disease affecting local wildlife. #WildlifeHealth"
        ]
    ],
    "6 cases": [
        [
            "6 cases of Root Rot were detected in the garden’s potato crop. #PlantCare",
            "The animal shelter reported 6 cases of Feline Leukemia among the rescued cats. #PetHealth",
            "6 cases of Citrus Greening were identified in the local lemon grove. #PlantHealth",
            "Local veterinarians have found 6 cases of Canine Cough in the dog park. #PetHealth",
            "6 trees in the park are suffering from a serious case of Oak Wilt. #TreeHealth"
        ]
    ],
    "11 affected": [
        [
            "11 affected horses are showing signs of Equine Influenza at the stable. #HorseHealth",
            "The garden has 11 affected plants with symptoms of a new bacterial infection. #PlantCare",
            "11 pigs have been diagnosed with a severe outbreak of African Swine Fever. #PigHealth",
            "11 local bees are suffering from a new outbreak of American Foulbrood. #BeeHealth",
            "The greenhouse reported 11 affected tomato plants with severe symptoms of Late Blight. #PlantDisease"
        ]
    ],
    "400 cases": [
        [
            "400 cases of Citrus Canker have been reported across the region’s lemon orchards. #PlantHealth",
            "The farm is dealing with 400 cases of Swine Fever affecting their pig population. #PigHealth",
            "400 cases of a new fungal infection are impacting local zucchini crops. #PlantCare",
            "The recent outbreak has led to 400 cases of respiratory illness among cattle. #FarmHealth",
            "400 cases of a viral disease have been identified in the local bird population. #BirdHealth"
        ]
    ],
    "20 infected": [
        [
            "20 infected chickens are exhibiting symptoms of a new strain of Avian Flu. #BirdHealth",
            "The garden has 20 infected plants with severe symptoms of a viral disease. #PlantCare",
            "The greenhouse reported 20 infected tomato plants showing signs of early blight. #PlantDisease"
        ]
    ],
    "Four confirmed cases": [
        [
            "Four confirmed cases of a new fungal infection have been detected in the apple orchard.",
            "Four confirmed cases of Canine Parvovirus were reported in the local veterinary clinic.",
            "The community garden has identified four confirmed cases of a disease affecting tomato plants.",
            "Four confirmed cases of a novel viral infection were reported in the local beekeeping community.",
            "In the recent survey, four confirmed cases of a mysterious plant disease were found in the vineyard."
        ]
    ],
    "Eight cases": [
        [
            "Eight cases of a rare bacterial infection were identified in the farm’s lettuce crops.",
            "The zoo has identified eight cases of a respiratory illness among the primates.",
            "Researchers identified eight cases of a new strain of virus affecting the regional poultry.",
            "Eight cases of a severe plant blight were identified in the local tomato greenhouse.",
            "The clinic confirmed eight cases of a new viral infection in dogs across the city."
        ]
    ],
    "Five fatalities": [
        [
            "Five fatalities have been reported in the horse population due to an outbreak of Equine Encephalitis.",
            "The local farm reported five fatalities among the sheep flock caused by a sudden infection.",
            "In the recent outbreak, five bee colonies have suffered fatalities from a new disease.",
            "Five fatalities have been reported among the goat population due to a sudden outbreak of Caprine Arthritis.",
            "The greenhouse confirmed five fatalities among the tomato plants from a severe blight."
        ]
    ],
    "Twelve deaths": [
        [
            "Twelve deaths have been confirmed at the local poultry farm due to a severe Avian Influenza outbreak.",
            "The garden reported twelve deaths among cucumber plants caused by a new fungal disease.",
            "Twelve deer deaths were confirmed due to a viral outbreak affecting the local wildlife.",
            "The zoo reported twelve deaths among various animals due to a new viral infection.",
            "Twelve citrus trees have died from a severe new disease affecting the orchard."
        ]
    ],
    "Six cases": [
        [
            "Six cases of Leaf Spot disease have been observed in the urban park’s oak trees.",
            "At the animal shelter, six cases of a new canine virus have been observed among the dogs.",
            "The community garden observed six cases of Downy Mildew affecting the zucchini plants.",
            "Six trees in the park were observed with a rare fungal infection during the inspection.",
            "Local farmers observed six cases of Root Rot in their potato fields this season."
        ]
    ],
    "Four hundred incidents recorded": [
        [
            "Four hundred incidents of Citrus Canker have been recorded in the region’s lemon orchards.",
            "The farm reported four hundred incidents of a new viral infection affecting their pigs.",
            "Four hundred incidents of a severe fungal disease were recorded in the local zucchini crops.",
            "The outbreak among cattle has resulted in four hundred incidents of Bovine Respiratory Disease.",
            "Four hundred incidents of a new avian virus have been recorded in the local bird population."
        ]
    ]
}

numerical_dev_data = {}

# splitting numerical data
for key in numerical_training_data:
    eighty_percent = round(len(numerical_training_data[key][0]) * 0.8)
    numerical_dev_data[key] = [numerical_training_data[key][0][eighty_percent:]]
    numerical_training_data[key][0] = numerical_training_data[key][0][:eighty_percent]
    
# print(sum(len(numerical_training_data[key][0]) for key in numerical_training_data))
# print(sum(len(numerical_dev_data[key][0]) for key in numerical_dev_data))

location_training_data = {
    "California": [
        [
            "Just found out our vineyards in California are infested with phylloxera. This could ruin 50% of our crop this season! 😢 #CaliforniaVineyards",
            "Spotted 10 cases of avocado root rot in the orchard. California farmers, @AgriCA, any advice? #FarmersHelp",
            "California's almond orchards are suffering from navel orangeworm infestation. Estimated loss is 35%. #CaliforniaAlmonds",
            "Our strawberry fields in California have been hit by spider mites. Could lose 20% of the crop! 🍓 #CaliforniaAgriculture"
        ]
    ],
    "Texas": [
        [
            "The cotton fields in Texas are under attack by boll weevils. Could lose up to 30% of the yield! 😡 #TexasAgriculture",
            "10 cows diagnosed with bovine tuberculosis in Texas. Need a vet ASAP! @TexasFarmHelp #RanchProblems",
            "Texas corn crops are facing an outbreak of southern rust. Potentially devastating! 🌽 #TexasFarming",
        ]
    ],
    "Florida": [
        [
            "Our citrus groves in Florida are hit by citrus greening. Estimated loss is 25%. 🍊 #FloridaCitrus",
            "Seeing a rapid spread of black sigatoka in banana plants in Florida. @FLAgDept any solutions? 😥",
            "Florida's tomato crops are suffering from bacterial spot. This could impact 30% of our harvest! 🍅 #FloridaFarming",
            "Noticed 12 cases of equine encephalitis in horses across Florida. Urgent action needed! 🐴 #FloridaEquine"
        ]
    ],
    "Iowa": [
        [
            "Corn crops in Iowa are suffering from corn earworm. This could affect 20% of the harvest! 🌽 #IowaFarms",
            "3 cases of swine flu reported on the farm in Iowa. Need immediate intervention! @IowaFarmers #FarmLife",
            "Soybean aphids are wreaking havoc on Iowa's soybean fields. Potential 25% loss. 😟 #IowaSoybeans",
            "Iowa dairy farms are seeing an increase in mastitis cases. @IowaAgDept any advice? 🐄 #IowaDairy"
        ]
    ],
    "Kansas": [
        [
            "Wheat rust detected in the fields of Kansas. Could impact 15% of the production. #KansasWheat",
            "5 cattle showing signs of foot-and-mouth disease in Kansas. Very concerned! @KansasAgri",
            "Kansas sunflower fields are under threat from sunflower moths. Estimated damage is 20%. 🌻 #KansasFarming",
            "Noticed 8 cases of rabies in livestock across Kansas. Immediate action required! #KansasAgriculture"
        ]
    ],
    "New York": [
        [
            "Apple orchards in New York are infested with codling moths. Potential loss of 40%. 🍎 #NewYorkFarmers",
            "Found 6 cases of Johne's disease in our dairy cows in New York. @NewYorkAgriDept what should we do? 😓",
            "New York vineyards are struggling with downy mildew. This could ruin 30% of the grapes! 🍇 #NewYorkWines",
            "Noticed 10 cases of Lyme disease in dogs across New York. Any recommendations? 🐕 #NewYorkPets"
        ]
    ],
    "Nebraska": [
        [
            "Soybean aphids are out of control in Nebraska. This could ruin 35% of our yield! 😔 #NebraskaFarming",
            "Detected 7 cases of avian influenza in the chicken coop in Nebraska. Need guidance! @NebraskaFarmBureau",
            "Nebraska cornfields are suffering from Goss's wilt. Potential loss of 25%. 🌽 #NebraskaCorn",
            "Noticed 5 cases of chronic wasting disease in deer across Nebraska. Urgent measures needed! 🦌 #NebraskaWildlife"
        ]
    ],
    "Georgia": [
        [
            "Peach trees in Georgia hit hard by peach tree borer. Estimated damage is 20%. 🍑 #GeorgiaPeaches",
            "4 goats have come down with brucellosis in Georgia. @GeorgiaAg any advice? #RuralProblems",
            "Georgia's peanut crops are suffering from tomato spotted wilt virus. Could affect 30% of the yield! 🥜 #GeorgiaAgriculture",
            "Noticed 6 cases of infectious bursal disease in chickens across Georgia. @GeorgiaFarmers #GeorgiaPoultry"
        ]
    ],
    "Oregon": [
        [
            "Blueberry bushes in Oregon infested with spotted wing drosophila. 30% loss expected! 🫐 #OregonFarming",
            "5 sheep diagnosed with scrapie in Oregon. What should our next steps be? @OregonAgDept #SheepFarmers",
            "Oregon's hazelnut orchards are battling eastern filbert blight. Potentially devastating! #OregonHazelnuts",
            "Noticed 8 cases of West Nile virus in horses across Oregon. Need advice! 🐴 #OregonEquine"
        ]
    ],
    "Ohio": [
        [
            "Tomato crops in Ohio are suffering from late blight. Could lose 25% of the plants! 🍅 #OhioFarms",
            "8 pigs affected by pseudorabies in Ohio. Need urgent help! @OhioAgri #LivestockIssues",
            "Ohio soybean fields are dealing with sudden death syndrome. Estimated loss is 20%. #OhioSoybeans",
            "Noticed 12 cases of leptospirosis in dogs across Ohio. Any advice? 🐶 #OhioPets"
        ]
    ],
    "Washington": [
        [
            "Our apple orchards in Washington are infested with apple maggots. Could lose 40% of the crop! 🍏 #WashingtonApples",
            "Noticed 8 cases of bluetongue in sheep across Washington. Any advice? @WashingtonAg #SheepFarming",
            "Washington's cherry trees are suffering from brown rot. Estimated loss is 30%. 🍒 #WashingtonCherries",
            "Spotted 10 cases of anthracnose in strawberries in Washington. Need help! 🍓 #WashingtonFarming"
        ]
    ],
    "Colorado": [
        [
            "Potato fields in Colorado are being devastated by potato beetles. Potential 25% loss. 🥔 #ColoradoAgriculture",
            "5 cows diagnosed with brucellosis in Colorado. What should we do? @ColoradoAgri #RanchProblems",
            "Colorado's wheat fields are dealing with wheat streak mosaic virus. Could impact 20% of the yield. 🌾 #ColoradoWheat",
            "Noticed 12 cases of vesicular stomatitis in horses in Colorado. Need urgent advice! 🐴 #ColoradoEquine"
        ]
    ],
    "Michigan": [
        [
            "Cherry orchards in Michigan hit by cherry fruit fly. Potentially losing 35% of the crop. 🍒 #MichiganCherries",
            "Detected 9 cases of bovine tuberculosis in cattle across Michigan. @MichiganAgri what should we do? #MichiganFarming",
            "Michigan's blueberry bushes are suffering from mummy berry disease. Could lose 30% of the yield. 🫐 #MichiganBlueberries",
            "Noticed 7 cases of avian influenza in poultry across Michigan. Immediate help needed! 🐔 #MichiganPoultry"
        ]
    ],
    "Virginia": [
        [
            "Peach trees in Virginia are infested with peach scab. Estimated damage is 25%. 🍑 #VirginiaPeaches",
            "10 cows in Virginia diagnosed with bovine respiratory disease. Need a vet! @VirginiaAgDept #RanchLife",
            "Virginia's soybean fields are battling soybean cyst nematodes. Could impact 20% of the yield. 🌱 #VirginiaSoybeans",
            "Noticed 5 cases of equine herpesvirus in horses across Virginia. Urgent measures needed! 🐴 #VirginiaEquine"
        ]
    ],
    "North Carolina": [
        [
            "Sweet potato crops in North Carolina are being attacked by sweet potato weevils. Could lose 30% of the harvest! 🍠 #NorthCarolinaFarming",
            "Found 6 cases of PRRS in pigs across North Carolina. Need intervention! @NCFarmers #LivestockIssues",
            "North Carolina's tobacco fields are suffering from tobacco mosaic virus. Potential 25% loss. 🚬 #NorthCarolinaTobacco",
            "Noticed 10 cases of Marek's disease in chickens across North Carolina. Help needed! 🐔 #NorthCarolinaPoultry"
        ]
    ],
    "Pennsylvania": [
        [
            "Apple orchards in Pennsylvania are infested with apple scab. Could lose 20% of the crop. 🍏 #PennsylvaniaApples",
            "8 cows in Pennsylvania diagnosed with Johne's disease. @PennAgDept what should we do? #PennsylvaniaFarming",
            "Pennsylvania's grapevines are struggling with downy mildew. Estimated 30% loss. 🍇 #PennsylvaniaGrapes",
            "Noticed 5 cases of rabies in livestock across Pennsylvania. Immediate action required! #PennsylvaniaAgriculture"
        ]
    ],
    "Kentucky": [
        [
            "Corn crops in Kentucky are suffering from gray leaf spot. Could affect 15% of the harvest! 🌽 #KentuckyFarms",
            "5 horses in Kentucky diagnosed with strangles. Need urgent advice! @KentuckyAgDept #KentuckyEquine",
            "Kentucky's soybean fields are dealing with frogeye leaf spot. Potentially losing 20% of the yield. 🌱 #KentuckySoybeans",
            "Noticed 12 cases of coccidiosis in chickens across Kentucky. Help needed! 🐔 #KentuckyPoultry"
        ]
    ],
    "Arizona": [
        [
            "Citrus groves in Arizona are hit by citrus canker. Estimated damage is 25%. 🍊 #ArizonaCitrus",
            "Found 7 cases of Valley fever in dogs across Arizona. @ArizonaAgDept any advice? 🐕 #ArizonaPets",
            "Arizona's lettuce fields are suffering from lettuce drop. Potentially losing 30% of the crop. 🥬 #ArizonaFarming",
            "Noticed 6 cases of Newcastle disease in poultry across Arizona. Immediate help needed! 🐔 #ArizonaPoultry"
        ]
    ],
    "Wisconsin": [
        [
            "Cranberry bogs in Wisconsin are infested with cranberry fruitworm. Could lose 35% of the crop! 🍒 #WisconsinCranberries",
            "9 cows in Wisconsin diagnosed with digital dermatitis. Need intervention! @WisconsinAgri #WisconsinDairy",
            "Wisconsin's potato fields are dealing with early blight. Potential 25% loss. 🥔 #WisconsinPotatoes",
            "Noticed 5 cases of swine flu in pigs across Wisconsin. Immediate help needed! 🐖 #WisconsinFarming"
        ]
    ],
    "Minnesota": [
        [
            "Soybean fields in Minnesota are suffering from sudden death syndrome. Estimated loss is 20%. 🌱 #MinnesotaSoybeans",
            "8 cows in Minnesota diagnosed with anaplasmosis. Need urgent advice! @MinnesotaAgri #MinnesotaFarming",
            "Minnesota's corn crops are battling northern corn leaf blight. Potentially losing 15% of the harvest. 🌽 #MinnesotaCorn",
            "Noticed 10 cases of canine distemper in dogs across Minnesota. Help needed! 🐶 #MinnesotaPets"
        ]
    ], 
    "Toronto, Canada": [
        [
            "Our apple orchards in Toronto, Canada are infested with apple maggots. Could lose 40% of the crop! 🍏 #TorontoApples",
            "Noticed 8 cases of bluetongue in sheep across Toronto, Canada. Any advice? @TorontoAg #SheepFarming",
            "Toronto's cherry trees are suffering from brown rot. Estimated loss is 30%. 🍒 #TorontoCherries",
            "Spotted 10 cases of anthracnose in strawberries in Toronto, Canada. Need help! 🍓 #TorontoFarming"
        ]
    ],
    "Sydney, Australia": [
        [
            "Potato fields in Sydney, Australia are being devastated by potato beetles. Potential 25% loss. 🥔 #SydneyAgriculture",
            "5 cows diagnosed with brucellosis in Sydney, Australia. What should we do? @SydneyAgri #RanchProblems",
            "Sydney's wheat fields are dealing with wheat streak mosaic virus. Could impact 20% of the yield. 🌾 #SydneyWheat",
            "Noticed 12 cases of vesicular stomatitis in horses in Sydney, Australia. Need urgent advice! 🐴 #SydneyEquine"
        ]
    ],
    "London, UK": [
        [
            "Cherry orchards in London, UK hit by cherry fruit fly. Potentially losing 35% of the crop. 🍒 #LondonCherries",
            "Detected 9 cases of bovine tuberculosis in cattle across London, UK. @LondonAgri what should we do? #LondonFarming",
            "London's blueberry bushes are suffering from mummy berry disease. Could lose 30% of the yield. 🫐 #LondonBlueberries",
            "Noticed 7 cases of avian influenza in poultry across London, UK. Immediate help needed! 🐔 #LondonPoultry"
        ]
    ],
    "Cape Town, South Africa": [
        [
            "Peach trees in Cape Town, South Africa are infested with peach scab. Estimated damage is 25%. 🍑 #CapeTownPeaches",
            "10 cows in Cape Town, South Africa diagnosed with bovine respiratory disease. Need a vet! @CapeTownAgDept #RanchLife",
            "Cape Town's soybean fields are battling soybean cyst nematodes. Could impact 20% of the yield. 🌱 #CapeTownSoybeans",
            "Noticed 5 cases of equine herpesvirus in horses across Cape Town, South Africa. Urgent measures needed! 🐴 #CapeTownEquine"
        ]
    ],
    "Mumbai, India": [
        [
            "Sweet potato crops in Mumbai, India are being attacked by sweet potato weevils. Could lose 30% of the harvest! 🍠 #MumbaiFarming",
            "Found 6 cases of PRRS in pigs across Mumbai, India. Need intervention! @MumbaiFarmers #LivestockIssues",
            "Mumbai's tobacco fields are suffering from tobacco mosaic virus. Potential 25% loss. 🚬 #MumbaiTobacco",
            "Noticed 10 cases of Marek's disease in chickens across Mumbai, India. Help needed! 🐔 #MumbaiPoultry"
        ]
    ],
    "São Paulo, Brazil": [
        [
            "Citrus groves in São Paulo, Brazil are hit by citrus canker. Estimated damage is 25%. 🍊 #SaoPauloCitrus",
            "Found 7 cases of Valley fever in dogs across São Paulo, Brazil. @SaoPauloAgDept any advice? 🐕 #SaoPauloPets",
            "São Paulo's lettuce fields are suffering from lettuce drop. Potentially losing 30% of the crop. 🥬 #SaoPauloFarming",
            "Noticed 6 cases of Newcastle disease in poultry across São Paulo, Brazil. Immediate help needed! 🐔 #SaoPauloPoultry"
        ]
    ],
    "Paris, France": [
        [
            "Cranberry bogs in Paris, France are infested with cranberry fruitworm. Could lose 35% of the crop! 🍒 #ParisCranberries",
            "9 cows in Paris, France diagnosed with digital dermatitis. Need intervention! @ParisAgri #ParisDairy",
            "Paris's potato fields are dealing with early blight. Potential 25% loss. 🥔 #ParisPotatoes",
            "Noticed 5 cases of swine flu in pigs across Paris, France. Immediate help needed! 🐖 #ParisFarming"
        ]
    ],
    "Tokyo, Japan": [
        [
            "Soybean fields in Tokyo, Japan are suffering from sudden death syndrome. Estimated loss is 20%. 🌱 #TokyoSoybeans",
            "8 cows in Tokyo, Japan diagnosed with anaplasmosis. Need urgent advice! @TokyoAgri #TokyoFarming",
            "Tokyo's corn crops are battling northern corn leaf blight. Potentially losing 15% of the harvest. 🌽 #TokyoCorn",
            "Noticed 10 cases of canine distemper in dogs across Tokyo, Japan. Help needed! 🐶 #TokyoPets"
        ]
    ],
    "Mexico City, Mexico": [
        [
            "Our apple orchards in Mexico City, Mexico are infested with apple maggots. Could lose 40% of the crop! 🍏 #MexicoCityApples",
            "Noticed 8 cases of bluetongue in sheep across Mexico City, Mexico. Any advice? @MexicoCityAg #SheepFarming",
            "Mexico City's cherry trees are suffering from brown rot. Estimated loss is 30%. 🍒 #MexicoCityCherries",
            "Spotted 10 cases of anthracnose in strawberries in Mexico City, Mexico. Need help! 🍓 #MexicoCityFarming"
        ]
    ],
    "Buenos Aires, Argentina": [
        [
            "Potato fields in Buenos Aires, Argentina are being devastated by potato beetles. Potential 25% loss. 🥔 #BuenosAiresAgriculture",
            "5 cows diagnosed with brucellosis in Buenos Aires, Argentina. What should we do? @BuenosAiresAgri #RanchProblems",
            "Buenos Aires's wheat fields are dealing with wheat streak mosaic virus. Could impact 20% of the yield. 🌾 #BuenosAiresWheat",
            "Noticed 12 cases of vesicular stomatitis in horses in Buenos Aires, Argentina. Need urgent advice! 🐴 #BuenosAiresEquine"
        ]
    ],
    "Vancouver, Canada": [
        [
            "Our apple orchards in Vancouver, Canada are facing an apple maggot infestation. Estimated loss is 25%. 🍏 #VancouverApples",
            "Detected 7 cases of bluetongue in sheep in Vancouver, Canada. Any suggestions? @VancouverAg #SheepHealth",
            "Vancouver's cherry trees are suffering from cherry leaf spot. Potential 30% crop loss. 🍒 #VancouverCherries",
            "Spotted 12 cases of anthracnose in strawberries around Vancouver, Canada. Need urgent help! 🍓 #VancouverFarming",
            "Potato fields near Vancouver, Canada are infested with potato beetles. Potential loss of 20%. 🥔 #VancouverAgriculture",
            "Found 9 cows with brucellosis in Vancouver, Canada. Immediate intervention needed! @VancouverVet #RanchHealth",
            "Vancouver's wheat fields are affected by wheat rust. Estimated impact is 15%. 🌾 #VancouverWheat",
            "Noticed 8 cases of vesicular stomatitis in horses in Vancouver, Canada. Help required! 🐴 #VancouverEquine",
            "Berry bushes in Vancouver, Canada are struggling with powdery mildew. Loss estimated at 25%. 🍓 #VancouverBerries",
            "Vancouver's corn crops are battling northern corn leaf blight. Potential 20% loss. 🌽 #VancouverCorn"
        ]
    ],
    "Auckland, New Zealand": [
        [
            "Sweet potato fields in Auckland, New Zealand are hit by sweet potato weevils. Potential 30% loss. 🍠 #AucklandFarming",
            "7 cases of PRRS found in pigs around Auckland, New Zealand. Need advice! @AucklandAg #PigHealth",
            "Auckland's tobacco plants are suffering from tobacco mosaic virus. Estimated 20% yield loss. 🚬 #AucklandTobacco",
            "Detected 6 cases of Marek's disease in chickens in Auckland, New Zealand. Immediate help needed! 🐔 #AucklandPoultry",
            "Apple orchards in Auckland, New Zealand are dealing with apple scab. Could lose 25% of the crop. 🍏 #AucklandApples",
            "8 cases of bovine tuberculosis reported in cows across Auckland, New Zealand. @AucklandVet what to do? #AucklandCattle",
            "Auckland's blueberry bushes are suffering from mummy berry disease. Potential 30% loss. 🫐 #AucklandBlueberries",
            "Noticed 10 cases of avian influenza in poultry in Auckland, New Zealand. Help needed! 🐔 #AucklandPoultry",
            "Citrus trees in Auckland, New Zealand affected by citrus canker. Estimated 20% loss. 🍊 #AucklandCitrus",
            "Corn crops in Auckland, New Zealand are battling corn earworm. Loss estimate is 15%. 🌽 #AucklandCorn"
        ]
    ],
    "Berlin, Germany": [
        [
            "Cherry orchards in Berlin, Germany are infested with cherry fruit fly. Potential 35% crop loss. 🍒 #BerlinCherries",
            "Detected 9 cases of bovine tuberculosis in cattle across Berlin, Germany. @BerlinAgri any advice? #BerlinFarming",
            "Berlin's blueberry bushes are struggling with mummy berry disease. Estimated 25% yield loss. 🫐 #BerlinBlueberries",
            "Spotted 7 cases of avian influenza in poultry in Berlin, Germany. Immediate help needed! 🐔 #BerlinPoultry",
            "Potato fields near Berlin, Germany are affected by potato beetles. Potential 20% loss. 🥔 #BerlinAgriculture",
            "Found 5 cases of brucellosis in cows in Berlin, Germany. Urgent intervention required! @BerlinVet #BerlinCattle",
            "Berlin's wheat crops are suffering from wheat rust. Estimated loss is 15%. 🌾 #BerlinWheat",
            "Noticed 12 cases of vesicular stomatitis in horses in Berlin, Germany. Need urgent advice! 🐴 #BerlinEquine",
            "Berry crops in Berlin, Germany are affected by powdery mildew. Loss is around 25%. 🍓 #BerlinBerries",
            "Corn fields in Berlin, Germany are battling corn blight. Potential 20% yield loss. 🌽 #BerlinCorn"
        ]
    ],
    "Madrid, Spain": [
        [
            "Olive trees in Madrid, Spain are infested with olive fly. Potential 30% crop loss. 🫒 #MadridOlives",
            "Detected 6 cases of brucellosis in cattle around Madrid, Spain. Need advice! @MadridAgri #MadridCattle",
            "Madrid's grapevines are suffering from downy mildew. Estimated 25% loss. 🍇 #MadridGrapes",
            "Spotted 8 cases of Marek's disease in chickens in Madrid, Spain. Immediate help required! 🐔 #MadridPoultry",
            "Apple orchards in Madrid, Spain are affected by apple scab. Could lose 20% of the crop. 🍏 #MadridApples",
            "Found 10 cases of bovine tuberculosis in cows across Madrid, Spain. @MadridVet any recommendations? #MadridFarming",
            "Madrid's corn fields are struggling with corn earworm. Potential 15% yield loss. 🌽 #MadridCorn",
            "Noticed 7 cases of avian influenza in poultry in Madrid, Spain. Help needed! 🐔 #MadridPoultry",
            "Peach trees in Madrid, Spain are dealing with peach scab. Estimated loss is 25%. 🍑 #MadridPeaches",
            "Citrus trees in Madrid, Spain are suffering from citrus canker. Potential 20% crop loss. 🍊 #MadridCitrus"
        ]
    ],
    "Rome, Italy": [
        [
            "Vineyards in Rome, Italy are infested with grape phylloxera. Potential 30% loss. 🍇 #RomeVineyards",
            "6 cases of bovine tuberculosis reported in cows in Rome, Italy. Immediate intervention needed! @RomeVet #RomeCattle",
            "Rome's citrus trees are suffering from citrus greening. Estimated 20% loss. 🍊 #RomeCitrus",
            "Spotted 9 cases of Marek's disease in poultry in Rome, Italy. Need urgent help! 🐔 #RomePoultry",
            "Apple orchards in Rome, Italy are affected by apple scab. Could lose 25% of the crop. 🍏 #RomeApples",
            "Found 7 cases of bluetongue in sheep across Rome, Italy. Any advice? @RomeAgri #RomeSheep",
            "Rome's olive trees are struggling with olive knot disease. Estimated 20% yield loss. 🫒 #RomeOlives",
            "Noticed 8 cases of avian influenza in chickens in Rome, Italy. Help required! 🐔 #RomePoultry",
            "Berry bushes in Rome, Italy are affected by powdery mildew. Potential 25% loss. 🍓 #RomeBerries",
            "Corn fields in Rome, Italy are dealing with corn leaf blight. Estimated 15% yield loss. 🌽 #RomeCorn"
        ]
    ],
    "Johannesburg, South Africa": [
        [
            "Corn crops in Johannesburg, South Africa are battling corn earworm. Potential 20% loss. 🌽 #JohannesburgCorn",
            "Detected 8 cases of PRRS in pigs around Johannesburg, South Africa. Need advice! @JohannesburgAg #JohannesburgPigs",
            "Johannesburg's tobacco fields are suffering from tobacco mosaic virus. Estimated 25% loss. 🚬 #JohannesburgTobacco",
            "Spotted 6 cases of Marek's disease in chickens in Johannesburg, South Africa. Immediate help needed! 🐔 #JohannesburgPoultry",
            "Sweet potato fields in Johannesburg, South Africa are hit by sweet potato weevils. Potential 30% loss. 🍠 #JohannesburgFarming",
            "Found 10 cases of brucellosis in cows in Johannesburg, South Africa. Urgent intervention required! @JohannesburgVet #JohannesburgCattle",
            "Johannesburg's grapevines are suffering from downy mildew. Estimated 20% loss. 🍇 #JohannesburgGrapes",
            "Noticed 7 cases of avian influenza in poultry in Johannesburg, South Africa. Help needed! 🐔 #JohannesburgPoultry",
            "Berry crops in Johannesburg, South Africa are affected by powdery mildew. Potential 25% loss. 🍓 #JohannesburgBerries",
            "Potato fields in Johannesburg, South Africa are dealing with early blight. Estimated 15% loss. 🥔 #JohannesburgPotatoes"
        ]
    ],
    "Paris, France": [
        [
            "Citrus trees in Paris, France are infested with citrus canker. Estimated damage is 20%. 🍊 #ParisCitrus",
            "Detected 5 cases of brucellosis in cows in Paris, France. Immediate intervention needed! @ParisVet #ParisCattle",
            "Paris's grapevines are suffering from downy mildew. Estimated 25% loss. 🍇 #ParisGrapes",
            "Spotted 8 cases of Marek's disease in chickens in Paris, France. Need urgent help! 🐔 #ParisPoultry",
            "Apple orchards in Paris, France are affected by apple scab. Could lose 25% of the crop. 🍏 #ParisApples",
            "Found 7 cases of bluetongue in sheep across Paris, France. Any advice? @ParisAgri #ParisSheep",
            "Paris's olive trees are struggling with olive knot disease. Estimated 20% yield loss. 🫒 #ParisOlives",
            "Noticed 10 cases of avian influenza in poultry in Paris, France. Help required! 🐔 #ParisPoultry",
            "Berry bushes in Paris, France are affected by powdery mildew. Potential 25% loss. 🍓 #ParisBerries",
            "Corn fields in Paris, France are dealing with corn leaf blight. Estimated 15% yield loss. 🌽 #ParisCorn"
        ]
    ],
    "Lisbon, Portugal": [
        [
            "Olive trees in Lisbon, Portugal are hit by olive fruit fly. Potential 30% crop loss. 🫒 #LisbonOlives",
            "6 cases of PRRS found in pigs around Lisbon, Portugal. Need advice! @LisbonAg #LisbonPigs",
            "Lisbon's citrus trees are suffering from citrus greening. Estimated 25% loss. 🍊 #LisbonCitrus",
            "Detected 8 cases of Marek's disease in poultry in Lisbon, Portugal. Immediate help needed! 🐔 #LisbonPoultry",
            "Apple orchards in Lisbon, Portugal are affected by apple scab. Could lose 20% of the crop. 🍏 #LisbonApples",
            "Found 7 cases of bovine tuberculosis in cows across Lisbon, Portugal. @LisbonVet what should we do? #LisbonCattle",
            "Lisbon's grapevines are struggling with downy mildew. Estimated 20% loss. 🍇 #LisbonGrapes",
            "Noticed 9 cases of avian influenza in poultry in Lisbon, Portugal. Help needed! 🐔 #LisbonPoultry",
            "Berry bushes in Lisbon, Portugal are affected by powdery mildew. Potential 25% loss. 🍓 #LisbonBerries",
            "Corn fields in Lisbon, Portugal are battling corn blight. Estimated 15% yield loss. 🌽 #LisbonCorn"
        ]
    ],
    "Athens, Greece": [
        [
            "Vineyards in Athens, Greece are infested with grape phylloxera. Potential 30% crop loss. 🍇 #AthensVineyards",
            "Detected 7 cases of brucellosis in cattle in Athens, Greece. Immediate intervention needed! @AthensVet #AthensCattle",
            "Athens's citrus trees are suffering from citrus greening. Estimated 25% loss. 🍊 #AthensCitrus",
            "Spotted 8 cases of Marek's disease in chickens in Athens, Greece. Need urgent help! 🐔 #AthensPoultry",
            "Apple orchards in Athens, Greece are affected by apple scab. Could lose 20% of the crop. 🍏 #AthensApples",
            "Found 10 cases of bluetongue in sheep across Athens, Greece. Any advice? @AthensAgri #AthensSheep",
            "Athens's olive trees are struggling with olive knot disease. Estimated 20% yield loss. 🫒 #AthensOlives",
            "Noticed 9 cases of avian influenza in poultry in Athens, Greece. Help needed! 🐔 #AthensPoultry",
            "Berry bushes in Athens, Greece are affected by powdery mildew. Potential 25% loss. 🍓 #AthensBerries",
            "Corn fields in Athens, Greece are dealing with corn leaf blight. Estimated 15% yield loss. 🌽 #AthensCorn"
        ]
    ],
    "Vancouver": [
        [
            "Urgent: Apple orchards in Vancouver are battling a severe apple maggot infestation. Early estimates suggest a potential 30% crop loss. 🍏",
            "We've found 7 cases of bluetongue in sheep in Vancouver. This could have serious implications for our local flocks. @VancouverAg",
            "Cherry trees in Vancouver are showing symptoms of brown rot. It might affect up to 25% of the harvest this year. 🍒",
            "Our strawberry fields in Vancouver have been hit hard by anthracnose. We've observed 12 infected plants so far. 🍓",
            "The potato beetles are wreaking havoc on fields near Vancouver. We’re looking at possibly a 20% reduction in yield.",
            "Brucellosis cases have been reported in 5 cows in Vancouver. Immediate veterinary advice is needed to control this outbreak.",
            "Vancouver's wheat fields are suffering from wheat rust. Initial estimates suggest a 15% impact on this year's crop.",
            "Vesicular stomatitis has been detected in 8 horses around Vancouver. This disease is causing significant distress among our equine population.",
            "Berry bushes in Vancouver are covered in powdery mildew. We're worried about a potential 30% loss in berry production this season.",
            "Corn crops in Vancouver are showing signs of northern corn leaf blight. This could reduce the yield by up to 20%."
        ]
    ],
    "Auckland": [
        [
            "Sweet potatoes in Auckland are under attack from sweet potato weevils. We might lose up to 30% of our crop this year. 🍠",
            "PRRS has been detected in 8 pigs across Auckland. We urgently need recommendations for managing this disease.",
            "Tobacco plants in Auckland are experiencing severe issues with tobacco mosaic virus. We're facing a 20% decrease in yield.",
            "Marek's disease has been identified in several chickens in Auckland. Immediate action is necessary to prevent further spread.",
            "Apple orchards around Auckland are struggling with apple scab. Early estimates predict a 25% loss in this year's harvest.",
            "Bovine tuberculosis has been diagnosed in 8 cows near Auckland. We need advice on containment and treatment.",
            "Our blueberry bushes in Auckland are suffering from mummy berry disease. The damage could reach up to 30% of the yield.",
            "Avian influenza has been confirmed in 10 poultry cases in Auckland. Urgent measures are required to prevent a larger outbreak.",
            "Olive trees in Auckland are infested with olive knot disease. The potential loss could be around 20% this season.",
            "Corn crops in Auckland are dealing with a severe corn earworm infestation. We’re anticipating a 15% loss in yield."
        ]
    ],
    "Berlin": [
        [
            "Cherry orchards in Berlin are facing a major cherry fruit fly problem. We could lose up to 35% of the crop this year. 🍒",
            "Bovine tuberculosis has been reported in 9 cows in Berlin. We are seeking guidance on how to manage and treat this condition.",
            "Blueberry bushes in Berlin are affected by mummy berry disease. Early reports suggest a 25% loss in production.",
            "Avian influenza has been detected in poultry around Berlin. There are 7 confirmed cases, and we need immediate advice.",
            "Potato fields near Berlin are overrun by potato beetles. We’re estimating a 20% reduction in this year's yield.",
            "Brucellosis cases have been found in 6 cows in Berlin. Urgent veterinary intervention is necessary to manage this outbreak.",
            "Wheat crops in Berlin are showing signs of wheat rust. This could impact up to 15% of the wheat yield this season.",
            "Vesicular stomatitis has been observed in 10 horses in Berlin. We need quick actions to handle this situation.",
            "Powdery mildew is affecting berry crops around Berlin. The potential impact on the harvest is approximately 25%. 🍓",
            "Corn fields in Berlin are battling corn blight. We’re worried about a 20% reduction in yield."
        ]
    ],
    "Madrid": [
        [
            "Olive trees in Madrid are experiencing a serious olive fly infestation. We could see a 30% reduction in this year's crop. 🫒",
            "Brucellosis has been detected in 6 cows around Madrid. We need expert advice on how to handle this disease.",
            "Grapevines in Madrid are suffering from downy mildew. Early estimates suggest a 25% loss in grape production.",
            "Marek's disease has been identified in chickens across Madrid. Immediate assistance is required to prevent further issues.",
            "Apple orchards in Madrid are dealing with apple scab. We’re looking at a possible 20% loss in this year's harvest.",
            "Bovine tuberculosis has been reported in 10 cows in Madrid. We need urgent guidance to manage this condition.",
            "Corn fields in Madrid are struggling with corn earworm. We’re predicting a 15% loss in yield for this season.",
            "Avian influenza has been confirmed in poultry in Madrid. There are 8 cases so far, and we need quick intervention.",
            "Peach trees in Madrid are affected by peach scab. Early estimates indicate a 25% loss in peach production.",
            "Citrus trees in Madrid are dealing with citrus canker. The estimated damage could be around 20%."
        ]
    ],
    "Rome": [
        [
            "Vineyards in Rome are suffering from a grape phylloxera outbreak. We might see a 30% reduction in this year’s yield. 🍇",
            "Brucellosis cases have been detected in 7 cows in Rome. Urgent veterinary advice is needed to control this issue.",
            "Citrus trees in Rome are battling citrus greening. The damage could result in a 25% loss of this year’s crop.",
            "Marek's disease has been reported in poultry around Rome. Immediate help is necessary to manage this outbreak.",
            "Apple orchards in Rome are facing problems with apple scab. We might lose up to 20% of the crop this year.",
            "Bluetongue has been identified in 10 sheep in Rome. We are looking for guidance on how to address this situation.",
            "Olive trees in Rome are struggling with olive knot disease. We’re anticipating a 20% reduction in yield.",
            "Avian influenza has been detected in chickens in Rome. There are currently 9 cases, and we need urgent help.",
            "Berry bushes in Rome are affected by powdery mildew. The potential loss in berry production is around 25%. 🍓",
            "Corn fields in Rome are battling corn leaf blight. Estimated impact on the yield is about 15%."
        ]
    ],
    "Johannesburg": [
        [
            "Corn crops in Johannesburg are suffering from corn earworm infestation. Expected yield loss is up to 20%. 🌽",
            "PRRS has been detected in 8 pigs in Johannesburg. We need urgent advice on how to handle this disease.",
            "Tobacco plants in Johannesburg are affected by tobacco mosaic virus. We’re looking at a 25% decrease in yield.",
            "Marek's disease has been identified in several chickens in Johannesburg. Immediate intervention is needed.",
            "Sweet potato fields in Johannesburg are hit by sweet potato weevils. We might lose up to 30% of the crop this year.",
            "Brucellosis has been reported in 10 cows in Johannesburg. Immediate veterinary assistance is required.",
            "Grapevines in Johannesburg are suffering from downy mildew. Estimated impact on yield is about 20%. 🍇",
            "Avian influenza has been confirmed in poultry in Johannesburg. There are 7 cases, and we need quick action.",
            "Berry crops in Johannesburg are affected by powdery mildew. Potential loss could be up to 25%. 🍓",
            "Potato fields in Johannesburg are struggling with early blight. The anticipated loss in yield is around 15%. 🥔"
        ]
    ],
    "Paris": [
        [
            "Citrus trees in Paris are infested with citrus canker. We’re facing a potential 20% loss in this year’s crop. 🍊",
            "Brucellosis cases have been identified in 5 cows in Paris. Immediate veterinary advice is necessary to control the outbreak.",
            "Grapevines in Paris are dealing with downy mildew. We’re estimating a 25% reduction in grape production.",
            "Marek's disease has been spotted in chickens in Paris. Urgent help is needed to prevent further spread.",
            "Apple orchards in Paris are struggling with apple scab. We’re looking at a possible 25% loss of the crop.",
            "Bluetongue has been detected in 7 sheep around Paris. Seeking advice on management and treatment.",
            "Olive trees in Paris are battling olive knot disease. The estimated impact is a 20% reduction in yield.",
            "Avian influenza has been confirmed in poultry in Paris. Immediate measures are needed to handle the situation.",
            "Berry bushes in Paris are affected by powdery mildew. We’re concerned about a 25% loss in production. 🍓",
            "Corn fields in Paris are showing signs of corn leaf blight. Expected yield reduction is around 15%."
        ]
    ],
    "Lisbon": [
        [
            "Olive trees in Lisbon are suffering from an olive fruit fly infestation. Estimated loss could be up to 30% of this year’s crop. 🫒",
            "PRRS has been found in 6 pigs in Lisbon. We need expert advice to manage this issue effectively.",
            "Citrus trees in Lisbon are affected by citrus greening. Early estimates suggest a 25% loss in this year’s yield.",
            "Marek's disease has been reported in chickens in Lisbon. Immediate intervention is needed to prevent further outbreaks.",
            "Apple orchards around Lisbon are dealing with apple scab. The potential loss this year could be 20%. 🍏",
            "Bovine tuberculosis has been detected in 7 cows in Lisbon. Urgent veterinary care is required.",
            "Grapevines in Lisbon are affected by downy mildew. The impact on yield might be around 20%. 🍇",
            "Avian influenza has been confirmed in poultry in Lisbon. There are 9 cases so far, and immediate action is necessary.",
            "Berry bushes in Lisbon are suffering from powdery mildew. Potential loss could be 25% of the total production. 🍓",
            "Corn fields in Lisbon are dealing with corn blight. Expected impact on yield is around 15%."
        ]
    ],
    "Athens": [
        [
            "Vineyards in Athens are suffering from grape phylloxera. This could result in a 30% decrease in yield. 🍇",
            "Brucellosis has been detected in 7 cows in Athens. We urgently need guidance on how to manage and treat this outbreak.",
            "Citrus trees in Athens are battling citrus greening. The damage is estimated to be around 25% of the crop.",
            "Marek's disease has been identified in several chickens in Athens. Immediate intervention is necessary.",
            "Apple orchards in Athens are struggling with apple scab. We’re looking at a potential 20% loss in production this year.",
            "Bluetongue has been reported in 10 sheep across Athens. We are seeking expert advice on how to address this issue.",
            "Olive trees in Athens are affected by olive knot disease. The expected impact is a 20% reduction in yield.",
            "Avian influenza has been confirmed in poultry in Athens. There are currently 9 cases, and we need urgent help.",
            "Berry bushes in Athens are dealing with powdery mildew. This could lead to a 25% reduction in berry yield. 🍓",
            "Corn fields in Athens are experiencing corn leaf blight. Estimated impact on yield is about 15%."
        ]
    ],
    "Tokyo": [
        [
            "Cherry trees in Tokyo are dealing with a severe cherry fruit fly infestation. We might see a 30% loss in this year's crop. 🍒",
            "Bovine tuberculosis has been detected in 8 cows in Tokyo. Immediate veterinary care is needed.",
            "Tomato plants in Tokyo are suffering from late blight. We’re estimating a 25% reduction in yield this season.",
            "Marek's disease has been reported in chickens in Tokyo. Urgent measures are required to manage this outbreak.",
            "Apple orchards in Tokyo are facing issues with apple scab. Early estimates suggest a 20% loss in this year’s harvest. 🍎",
            "Bluetongue has been detected in 6 sheep in Tokyo. We need expert advice on how to handle this situation.",
            "Berry bushes in Tokyo are affected by powdery mildew. The potential loss in production could be up to 25%. 🍓",
            "Avian influenza has been confirmed in poultry in Tokyo. There are currently 7 cases, and immediate action is necessary.",
            "Olive trees in Tokyo are struggling with olive knot disease. Estimated damage could be around 20%. 🫒",
            "Corn crops in Tokyo are dealing with corn earworm. Expected yield loss is approximately 15%."
        ]
    ],
    "Shanghai": [
        [
            "Soybean fields in Shanghai are suffering from a severe aphid infestation. We could face up to a 30% reduction in yield this year. 🌱",
            "PRRS has been detected in 7 pigs in Shanghai. Urgent guidance on managing this disease is needed.",
            "Citrus trees in Shanghai are battling citrus canker. Early estimates suggest a 25% loss in this year’s crop. 🍊",
            "Marek's disease has been identified in several chickens in Shanghai. Immediate intervention is necessary.",
            "Apple orchards in Shanghai are struggling with apple scab. The potential loss could be around 20% of the crop this year. 🍏",
            "Bovine tuberculosis has been diagnosed in 6 cows near Shanghai. We need advice on treatment and containment.",
            "Our blueberry bushes in Shanghai are affected by mummy berry disease. We’re anticipating up to a 30% reduction in yield.",
            "Avian influenza has been confirmed in 8 poultry cases in Shanghai. Immediate measures are required to manage the outbreak.",
            "Olive trees in Shanghai are affected by olive knot disease. Expected loss could be around 20% this season. 🫒",
            "Corn fields in Shanghai are showing signs of corn blight. We’re looking at a 15% reduction in yield."
        ]
    ],
    "Bangkok": [
        [
            "Sweet potatoes in Bangkok are facing a severe sweet potato weevil infestation. We might lose up to 30% of the crop this year. 🍠",
            "Brucellosis has been detected in 8 cows in Bangkok. Immediate veterinary assistance is required.",
            "Tomato plants in Bangkok are suffering from tomato spotted wilt virus. The expected reduction in yield is 25%.",
            "Marek's disease has been reported in chickens in Bangkok. Urgent measures are needed to prevent further spread.",
            "Apple orchards in Bangkok are dealing with apple scab. Early estimates suggest a 20% loss in this year’s harvest. 🍎",
            "Bovine tuberculosis has been reported in 7 cows near Bangkok. We need expert advice on how to manage this outbreak.",
            "Berry bushes in Bangkok are suffering from powdery mildew. Potential loss could be 25% of the total production. 🍓",
            "Avian influenza has been confirmed in poultry in Bangkok. There are 9 cases so far, and immediate action is necessary.",
            "Olive trees in Bangkok are struggling with olive knot disease. The potential impact is around 20%. 🫒",
            "Corn crops in Bangkok are dealing with corn earworm infestation. Expected yield loss is around 15%."
        ]
    ],
    "Manila": [
        [
            "Citrus trees in Manila are suffering from citrus greening. Early estimates suggest a 25% loss in this year’s yield. 🍊",
            "PRRS has been detected in 7 pigs in Manila. Urgent veterinary advice is needed to manage this disease.",
            "Grapevines in Manila are battling downy mildew. We’re looking at a 20% reduction in this year’s yield.",
            "Marek's disease has been reported in chickens in Manila. Immediate intervention is necessary to prevent further issues.",
            "Apple orchards in Manila are experiencing problems with apple scab. Potential loss this year could be around 20%. 🍏",
            "Bovine tuberculosis has been diagnosed in 6 cows near Manila. We need urgent help with treatment and containment.",
            "Berry bushes in Manila are affected by mummy berry disease. Estimated damage could be up to 30% of the yield. 🍓",
            "Avian influenza has been confirmed in poultry in Manila. Immediate measures are required, with 8 cases reported.",
            "Olive trees in Manila are dealing with olive knot disease. The estimated impact could be around 20%. 🫒",
            "Corn fields in Manila are showing signs of corn blight. Expected impact on yield is about 15%."
        ]
    ],
    "Seoul": [
        [
            "Vineyards in Seoul are suffering from a serious grape phylloxera outbreak. We might see a 30% reduction in this year’s yield. 🍇",
            "Brucellosis has been detected in 6 cows in Seoul. Immediate veterinary care is required.",
            "Potato fields in Seoul are affected by early blight. We’re anticipating a 25% reduction in this year’s crop.",
            "Marek's disease has been identified in chickens in Seoul. Urgent measures are necessary to manage this situation.",
            "Apple orchards in Seoul are struggling with apple scab. Early estimates suggest a 20% loss in this year's harvest. 🍎",
            "Bluetongue has been reported in 8 sheep near Seoul. We need expert advice on handling this issue.",
            "Berry bushes in Seoul are suffering from powdery mildew. Potential loss could be around 25% of the total production. 🍓",
            "Avian influenza has been confirmed in poultry in Seoul. There are currently 9 cases, and immediate action is needed.",
            "Olive trees in Seoul are battling olive knot disease. The expected impact on yield is around 20%. 🫒",
            "Corn crops in Seoul are showing signs of corn earworm infestation. Expected yield loss is approximately 15%."
        ]
    ],
    "Hong Kong": [
        [
            "Citrus trees in Hong Kong are battling citrus canker. The potential loss could be around 30% of this year’s crop. 🍊",
            "PRRS has been detected in 8 pigs in Hong Kong. Urgent veterinary advice is necessary.",
            "Tomato plants in Hong Kong are affected by tomato spotted wilt virus. We’re estimating a 25% decrease in yield.",
            "Marek's disease has been reported in chickens in Hong Kong. Immediate action is required to prevent further spread.",
            "Apple orchards in Hong Kong are dealing with apple scab. Potential loss could be 20% of the crop this year. 🍎",
            "Bovine tuberculosis has been diagnosed in 7 cows in Hong Kong. We need immediate help with containment and treatment.",
            "Berry bushes in Hong Kong are suffering from powdery mildew. Potential loss in production could be up to 30%. 🍓",
            "Avian influenza has been confirmed in poultry in Hong Kong. Immediate measures are needed, with 10 cases reported.",
            "Olive trees in Hong Kong are struggling with olive knot disease. The estimated impact could be around 20%. 🫒",
            "Corn fields in Hong Kong are dealing with corn blight. Expected reduction in yield is around 15%."
        ]
    ],
    "Kuala Lumpur": [
        [
            "Sweet potatoes in Kuala Lumpur are facing a severe sweet potato weevil infestation. We might lose up to 30% of the crop this year. 🍠",
            "Brucellosis has been detected in 7 cows in Kuala Lumpur. Immediate veterinary care is needed.",
            "Tomato plants in Kuala Lumpur are suffering from late blight. Expected yield reduction is about 25%.",
            "Marek's disease has been reported in chickens in Kuala Lumpur. Urgent measures are necessary to manage this outbreak.",
            "Apple orchards in Kuala Lumpur are experiencing issues with apple scab. Early estimates suggest a 20% loss in this year’s harvest. 🍎",
            "Bovine tuberculosis has been diagnosed in 6 cows in Kuala Lumpur. We need expert advice on treatment and containment.",
            "Blueberry bushes in Kuala Lumpur are affected by mummy berry disease. Potential damage could be around 30% of the yield.",
            "Avian influenza has been confirmed in poultry in Kuala Lumpur. Immediate action is required, with 9 cases reported.",
            "Olive trees in Kuala Lumpur are struggling with olive knot disease. The estimated impact could be around 20%. 🫒",
            "Corn crops in Kuala Lumpur are dealing with corn earworm infestation. Expected yield loss is around 15%."
        ]
    ],
    "Mumbai": [
        [
            "Citrus trees in Mumbai are affected by citrus greening. Early estimates suggest a 25% loss in this year’s crop. 🍊",
            "PRRS has been detected in 6 pigs in Mumbai. Urgent veterinary assistance is needed.",
            "Grapevines in Mumbai are suffering from downy mildew. Expected yield reduction is around 20%. 🍇",
            "Marek's disease has been identified in chickens in Mumbai. Immediate measures are necessary to manage this outbreak.",
            "Apple orchards in Mumbai are struggling with apple scab. We might see a 20% loss in this year’s harvest. 🍏",
            "Bovine tuberculosis has been reported in 7 cows near Mumbai. Urgent help is required for treatment and containment.",
            "Berry bushes in Mumbai are affected by powdery mildew. Potential loss could be up to 25% of the total production. 🍓",
            "Avian influenza has been confirmed in poultry in Mumbai. Immediate action is necessary, with 8 cases reported.",
            "Olive trees in Mumbai are dealing with olive knot disease. Expected impact on yield is around 20%. 🫒",
            "Corn fields in Mumbai are showing signs of corn blight. Estimated impact on yield is around 15%."
        ]
    ],
    "Mexico City": [
        [
            "Corn fields in Mexico City are suffering from a severe corn earworm infestation. Expected yield reduction is up to 30%. 🌽",
            "Brucellosis has been found in 8 cows in Mexico City. Immediate veterinary intervention is essential.",
            "Tomato plants in Mexico City are battling late blight. The yield may be reduced by 20% this season.",
            "Marek's disease has been reported in several chickens in Mexico City. Urgent measures are needed to contain this outbreak.",
            "Apple orchards in Mexico City are dealing with apple scab. Early estimates suggest a 15% reduction in this year’s harvest. 🍏",
            "Bovine tuberculosis has been diagnosed in 6 cows in Mexico City. We need prompt assistance for treatment.",
            "Berry bushes in Mexico City are showing signs of powdery mildew. Potential loss could be up to 25% of the crop. 🍓",
            "Avian influenza has been confirmed in poultry in Mexico City. Immediate action is required with 10 cases reported.",
            "Olive trees in Mexico City are struggling with olive knot disease. Expected impact on yield is around 20%. 🫒",
            "Corn crops in Mexico City are affected by severe corn blight. Yield loss could be approximately 18%."
        ]
    ],
    "Guadalajara": [
        [
            "Citrus trees in Guadalajara are facing a serious citrus canker outbreak. Expected loss in crop yield could be 25%. 🍊",
            "Brucellosis has been detected in 7 pigs in Guadalajara. Immediate veterinary care is necessary.",
            "Grapevines in Guadalajara are battling downy mildew. The yield could be reduced by 22% this year.",
            "Marek's disease has been reported in chickens in Guadalajara. Urgent measures are needed to control this disease.",
            "Apple orchards in Guadalajara are affected by apple scab. Potential loss in harvest is estimated at 18%. 🍎",
            "Bovine tuberculosis has been reported in 5 cows in Guadalajara. We need expert advice on treatment and containment.",
            "Berry bushes in Guadalajara are suffering from mummy berry disease. Estimated impact on yield could be up to 30%. 🍓",
            "Avian influenza has been confirmed in poultry in Guadalajara. Immediate action is needed, with 8 cases reported.",
            "Olive trees in Guadalajara are struggling with olive knot disease. The impact could be around 20% on yield. 🫒",
            "Corn fields in Guadalajara are affected by corn earworm infestation. Yield loss is expected to be around 15%."
        ]
    ],
    "Monterrey": [
        [
            "Soybean fields in Monterrey are facing a severe aphid infestation. Yield reduction could be up to 30%. 🌱",
            "PRRS has been detected in 6 pigs in Monterrey. Immediate veterinary intervention is needed.",
            "Tomato plants in Monterrey are suffering from tomato spotted wilt virus. Expected yield reduction is around 25%.",
            "Marek's disease has been reported in chickens in Monterrey. Immediate measures are necessary to manage this outbreak.",
            "Apple orchards in Monterrey are dealing with apple scab. Early estimates suggest a 20% loss in this year’s harvest. 🍏",
            "Bovine tuberculosis has been identified in 8 cows in Monterrey. Urgent help with treatment is needed.",
            "Berry bushes in Monterrey are affected by powdery mildew. Potential yield loss could be up to 25%. 🍓",
            "Avian influenza has been confirmed in poultry in Monterrey. Immediate action is required, with 9 cases reported.",
            "Olive trees in Monterrey are dealing with olive knot disease. Expected impact on yield is around 20%. 🫒",
            "Corn crops in Monterrey are showing signs of severe corn blight. Yield loss could be approximately 15%."
        ]
    ],
    "Cancún": [
        [
            "Sweet potato fields in Cancún are heavily infested with sweet potato weevils. We might face up to a 30% reduction in yield. 🍠",
            "Brucellosis has been detected in 8 cows in Cancún. Immediate veterinary care is required.",
            "Tomato plants in Cancún are suffering from late blight. Expected yield reduction could be around 22%.",
            "Marek's disease has been reported in chickens in Cancún. Urgent measures are necessary to prevent further spread.",
            "Apple orchards in Cancún are experiencing apple scab. Potential loss in harvest could be around 18%. 🍏",
            "Bovine tuberculosis has been diagnosed in 7 cows in Cancún. We need prompt assistance for treatment and containment.",
            "Berry bushes in Cancún are affected by mummy berry disease. Potential loss could be up to 30% of the crop. 🍓",
            "Avian influenza has been confirmed in poultry in Cancún. Immediate action is needed, with 9 cases reported.",
            "Olive trees in Cancún are struggling with olive knot disease. Expected impact on yield is around 20%. 🫒",
            "Corn fields in Cancún are showing signs of corn earworm infestation. Expected yield loss is approximately 15%."
        ]
    ],
    "Puebla": [
        [
            "Citrus trees in Puebla are battling citrus greening. Expected crop loss could be around 25%. 🍊",
            "PRRS has been detected in 7 pigs in Puebla. Urgent veterinary intervention is necessary.",
            "Grapevines in Puebla are affected by downy mildew. We might see a 20% reduction in yield this year. 🍇",
            "Marek's disease has been reported in chickens in Puebla. Immediate measures are required to manage the outbreak.",
            "Apple orchards in Puebla are struggling with apple scab. Estimated loss in harvest could be around 20%. 🍎",
            "Bovine tuberculosis has been diagnosed in 6 cows in Puebla. Immediate assistance with treatment is needed.",
            "Berry bushes in Puebla are suffering from powdery mildew. Expected impact on yield could be up to 30%. 🍓",
            "Avian influenza has been confirmed in poultry in Puebla. Immediate action is required, with 8 cases reported.",
            "Olive trees in Puebla are dealing with olive knot disease. The impact on yield could be around 20%. 🫒",
            "Corn crops in Puebla are experiencing severe corn blight. Expected yield loss is about 15%."
        ]
    ],
    "Tijuana": [
        [
            "Citrus trees in Tijuana are struggling with citrus canker. Expected loss in crop yield could be around 30%. 🍊",
            "PRRS has been detected in 6 pigs in Tijuana. Immediate veterinary care is necessary.",
            "Tomato plants in Tijuana are affected by tomato spotted wilt virus. Yield reduction might be around 25%.",
            "Marek's disease has been reported in chickens in Tijuana. Urgent measures are required to control this outbreak.",
            "Apple orchards in Tijuana are facing apple scab issues. Estimated loss in harvest could be about 20%. 🍏",
            "Bovine tuberculosis has been identified in 7 cows in Tijuana. We need immediate help with treatment.",
            "Berry bushes in Tijuana are suffering from powdery mildew. Potential yield loss could be up to 25%. 🍓",
            "Avian influenza has been confirmed in poultry in Tijuana. Immediate action is necessary, with 10 cases reported.",
            "Olive trees in Tijuana are struggling with olive knot disease. Expected impact on yield could be around 20%. 🫒",
            "Corn crops in Tijuana are affected by corn earworm infestation. Expected yield loss is approximately 15%."
        ]
    ],
    "San Luis Potosí": [
        [
            "Citrus trees in San Luis Potosí are experiencing a severe outbreak of citrus greening. Potential crop loss is around 30%. 🍊",
            "PRRS has been detected in 7 pigs in San Luis Potosí. Immediate veterinary care is crucial.",
            "Tomato plants in San Luis Potosí are suffering from late blight. The yield might be reduced by 22% this season.",
            "Marek's disease has been reported in chickens in San Luis Potosí. Urgent measures are needed to manage this situation.",
            "Apple orchards in San Luis Potosí are affected by apple scab. Early estimates suggest a 20% reduction in this year’s harvest. 🍎",
            "Bovine tuberculosis has been diagnosed in 6 cows in San Luis Potosí. We need prompt assistance for treatment and containment.",
            "Blueberry bushes in San Luis Potosí are dealing with mummy berry disease. Expected yield loss could be around 30%. 🍓",
            "Avian influenza has been confirmed in poultry in San Luis Potosí. Immediate action is required, with 8 cases reported.",
            "Olive trees in San Luis Potosí are dealing with olive knot disease. The impact on yield could be about 20%. 🫒",
            "Corn fields in San Luis Potosí are showing signs of severe corn blight. Yield loss might be around 15%."
        ]
    ],
    "Walla Walla": [
        [
            "Walla Walla’s grapevines are battling a severe downy mildew outbreak. Expected yield loss is up to 25%. 🍇",
            "Brucellosis has been detected in 7 cows in Walla Walla. Immediate veterinary intervention is required.",
            "Tomato plants in Walla Walla are suffering from late blight. Yield reduction might be around 20%.",
            "Marek's disease has been reported in chickens in Walla Walla. Urgent measures are necessary to manage this outbreak.",
            "Apple orchards in Walla Walla are facing apple scab issues. Potential loss in harvest could be about 15%. 🍎",
            "Bovine tuberculosis has been identified in 6 cows in Walla Walla. Prompt treatment is essential.",
            "Berry bushes in Walla Walla are showing signs of powdery mildew. Expected yield loss could be up to 25%. 🍓",
            "Avian influenza has been confirmed in poultry in Walla Walla. Immediate action is needed, with 8 cases reported.",
            "Olive trees in Walla Walla are struggling with olive knot disease. Expected impact on yield is around 20%. 🫒",
            "Corn fields in Walla Walla are experiencing severe corn blight. Yield loss might be approximately 15%."
        ]
    ],
    "Asheville": [
        [
            "Sweet corn fields in Asheville are suffering from a severe corn earworm infestation. Expected yield reduction is 20%. 🌽",
            "Brucellosis has been found in 5 cows in Asheville. Immediate veterinary care is necessary.",
            "Tomato plants in Asheville are battling late blight. Expected reduction in yield could be around 18%.",
            "Marek's disease has been reported in chickens in Asheville. Urgent measures are needed to contain this outbreak.",
            "Apple orchards in Asheville are dealing with apple scab. Potential harvest loss could be around 17%. 🍏",
            "Bovine tuberculosis has been diagnosed in 7 cows in Asheville. Prompt treatment and containment are needed.",
            "Berry bushes in Asheville are suffering from mummy berry disease. Potential yield loss could be up to 30%. 🍓",
            "Avian influenza has been confirmed in poultry in Asheville. Immediate action is required, with 9 cases reported.",
            "Olive trees in Asheville are battling olive knot disease. Expected impact on yield is around 22%. 🫒",
            "Corn crops in Asheville are affected by corn earworm infestation. Yield loss might be about 15%."
        ]
    ],
    "Carson City": [
        [
            "Grapevines in Carson City are showing signs of severe downy mildew. Expected yield loss is up to 28%. 🍇",
            "PRRS has been detected in 6 pigs in Carson City. Immediate veterinary care is essential.",
            "Citrus trees in Carson City are struggling with citrus canker. Estimated crop loss could be around 25%. 🍊",
            "Marek's disease has been reported in chickens in Carson City. Urgent measures are required to manage this outbreak.",
            "Apple orchards in Carson City are affected by apple scab. Expected loss in harvest could be around 20%. 🍎",
            "Bovine tuberculosis has been diagnosed in 5 cows in Carson City. Immediate treatment is needed.",
            "Berry bushes in Carson City are affected by powdery mildew. Potential yield loss could be up to 25%. 🍓",
            "Avian influenza has been confirmed in poultry in Carson City. Immediate action is required, with 8 cases reported.",
            "Olive trees in Carson City are struggling with olive knot disease. Expected impact on yield is around 18%. 🫒",
            "Corn fields in Carson City are showing signs of severe corn blight. Expected yield reduction is about 17%."
        ]
    ],
    "Bozeman": [
        [
            "Sweet potato fields in Bozeman are facing a severe infestation of sweet potato weevils. Expected crop loss could be up to 30%. 🍠",
            "Brucellosis has been detected in 7 cows in Bozeman. Urgent veterinary intervention is needed.",
            "Tomato plants in Bozeman are suffering from late blight. Yield reduction might be around 20%.",
            "Marek's disease has been reported in chickens in Bozeman. Immediate action is necessary to control this outbreak.",
            "Apple orchards in Bozeman are struggling with apple scab. Expected loss in harvest could be around 18%. 🍏",
            "Bovine tuberculosis has been diagnosed in 6 cows in Bozeman. Prompt treatment and containment are needed.",
            "Berry bushes in Bozeman are affected by mummy berry disease. Potential yield loss could be up to 30%. 🍓",
            "Avian influenza has been confirmed in poultry in Bozeman. Immediate action is needed with 9 cases reported.",
            "Olive trees in Bozeman are dealing with olive knot disease. Expected impact on yield is around 20%. 🫒",
            "Corn fields in Bozeman are experiencing severe corn blight. Yield loss might be approximately 15%."
        ]
    ],
    "Starkville": [
        [
            "Citrus trees in Starkville are struggling with citrus greening. Expected crop loss could be around 30%. 🍊",
            "PRRS has been detected in 5 pigs in Starkville. Immediate veterinary care is needed.",
            "Grapevines in Starkville are suffering from severe downy mildew. Yield reduction could be around 22%. 🍇",
            "Marek's disease has been reported in chickens in Starkville. Urgent measures are required to manage this outbreak.",
            "Apple orchards in Starkville are facing apple scab issues. Expected loss in harvest could be around 20%. 🍎",
            "Bovine tuberculosis has been identified in 6 cows in Starkville. Immediate treatment is crucial.",
            "Berry bushes in Starkville are showing signs of powdery mildew. Potential yield loss could be up to 25%. 🍓",
            "Avian influenza has been confirmed in poultry in Starkville. Immediate action is required with 8 cases reported.",
            "Olive trees in Starkville are dealing with olive knot disease. Expected impact on yield is around 22%. 🫒",
            "Corn crops in Starkville are affected by corn earworm infestation. Expected yield loss is approximately 15%."
        ]
    ],
    "Traverse City": [
        [
            "Sweet corn fields in Traverse City are suffering from a severe corn earworm infestation. Estimated yield loss is 20%. 🌽",
            "Brucellosis has been detected in 6 cows in Traverse City. Immediate veterinary care is essential.",
            "Tomato plants in Traverse City are dealing with late blight. Yield reduction could be around 18%.",
            "Marek's disease has been reported in chickens in Traverse City. Urgent measures are needed to contain this outbreak.",
            "Apple orchards in Traverse City are affected by apple scab. Expected harvest loss could be around 17%. 🍏",
            "Bovine tuberculosis has been diagnosed in 5 cows in Traverse City. Immediate treatment and containment are required.",
            "Berry bushes in Traverse City are suffering from mummy berry disease. Expected yield loss could be up to 30%. 🍓",
            "Avian influenza has been confirmed in poultry in Traverse City. Immediate action is required with 9 cases reported.",
            "Olive trees in Traverse City are battling olive knot disease. Expected impact on yield is around 20%. 🫒",
            "Corn fields in Traverse City are experiencing severe corn blight. Yield loss might be approximately 15%."
        ]
    ],
    "Farmington": [
        [
            "Grapevines in Farmington are showing severe downy mildew symptoms. Expected yield loss could be up to 28%. 🍇",
            "Brucellosis has been detected in 7 cows in Farmington. Immediate veterinary care is needed.",
            "Citrus trees in Farmington are battling citrus canker. Estimated crop loss might be around 25%. 🍊",
            "Marek's disease has been reported in chickens in Farmington. Urgent measures are required to manage this outbreak.",
            "Apple orchards in Farmington are struggling with apple scab. Expected loss in harvest could be about 20%. 🍎",
            "Bovine tuberculosis has been diagnosed in 6 cows in Farmington. Prompt treatment and containment are crucial.",
            "Berry bushes in Farmington are affected by powdery mildew. Potential yield loss could be up to 25%. 🍓",
            "Avian influenza has been confirmed in poultry in Farmington. Immediate action is needed, with 8 cases reported.",
            "Olive trees in Farmington are dealing with olive knot disease. Expected impact on yield is around 18%. 🫒",
            "Corn fields in Farmington are showing signs of severe corn blight. Yield loss might be approximately 17%."
        ]
    ],
    "Alamosa": [
        [
            "Sweet potato fields in Alamosa are infested with sweet potato weevils. Expected loss could be up to 30%. 🍠",
            "Brucellosis has been found in 6 cows in Alamosa. Immediate veterinary intervention is needed.",
            "Tomato plants in Alamosa are suffering from late blight. Expected yield reduction might be around 22%.",
            "Marek's disease has been reported in chickens in Alamosa. Urgent measures are necessary to control this outbreak.",
            "Apple orchards in Alamosa are affected by apple scab. Expected loss in harvest could be around 20%."
        ]
    ],
    "Eureka Springs": [
        [
            "Sweet corn fields in Eureka Springs are facing a severe infestation of corn earworms. Expected yield loss is around 25%. 🌽",
            "Brucellosis has been detected in 5 cows in Eureka Springs. Immediate veterinary care is necessary.",
            "Tomato plants in Eureka Springs are struggling with late blight. Potential reduction in yield could be 20%.",
            "Marek's disease has been reported in chickens in Eureka Springs. Urgent measures are needed to manage this outbreak.",
            "Apple orchards in Eureka Springs are affected by apple scab. Estimated loss in harvest could be around 15%. 🍎",
            "Bovine tuberculosis has been diagnosed in 6 cows in Eureka Springs. Prompt treatment is required.",
            "Berry bushes in Eureka Springs are showing signs of powdery mildew. Expected yield loss is up to 20%. 🍓",
            "Avian influenza has been confirmed in poultry in Eureka Springs. Immediate action is needed with 7 cases reported.",
            "Olive trees in Eureka Springs are struggling with olive knot disease. Impact on yield could be around 18%. 🫒",
            "Corn crops in Eureka Springs are experiencing severe corn blight. Expected yield loss is approximately 15%."
        ]
    ],
    "Bainbridge": [
        [
            "Citrus trees in Bainbridge are battling citrus canker. Expected crop loss could be around 30%. 🍊",
            "PRRS has been detected in 6 pigs in Bainbridge. Immediate veterinary care is needed.",
            "Tomato plants in Bainbridge are affected by tomato spotted wilt virus. Yield reduction might be around 25%.",
            "Marek's disease has been reported in chickens in Bainbridge. Urgent action is required to control this outbreak.",
            "Apple orchards in Bainbridge are struggling with apple scab. Potential loss in harvest is estimated at 18%. 🍏",
            "Bovine tuberculosis has been diagnosed in 7 cows in Bainbridge. Immediate assistance with treatment is necessary.",
            "Berry bushes in Bainbridge are affected by mummy berry disease. Potential yield loss could be up to 30%. 🍓",
            "Avian influenza has been confirmed in poultry in Bainbridge. Immediate action is required with 8 cases reported.",
            "Olive trees in Bainbridge are struggling with olive knot disease. Expected impact on yield is around 20%. 🫒",
            "Corn fields in Bainbridge are showing signs of corn earworm infestation. Yield loss is expected to be around 15%."
        ]
    ],
    "Smithfield": [
        [
            "Sweet potato fields in Smithfield are heavily infested with sweet potato weevils. Expected crop loss could be up to 30%. 🍠",
            "Brucellosis has been detected in 7 cows in Smithfield. Urgent veterinary care is required.",
            "Tomato plants in Smithfield are suffering from late blight. Expected reduction in yield is about 22%.",
            "Marek's disease has been reported in chickens in Smithfield. Immediate measures are necessary to prevent further spread.",
            "Apple orchards in Smithfield are affected by apple scab. Potential loss in this year’s harvest could be around 20%. 🍎",
            "Bovine tuberculosis has been diagnosed in 6 cows in Smithfield. Prompt treatment and containment are needed.",
            "Berry bushes in Smithfield are suffering from powdery mildew. Expected yield loss could be up to 25%. 🍓",
            "Avian influenza has been confirmed in poultry in Smithfield. Immediate action is needed with 9 cases reported.",
            "Olive trees in Smithfield are dealing with olive knot disease. Estimated impact on yield is around 22%. 🫒",
            "Corn crops in Smithfield are showing signs of corn earworm infestation. Yield loss might be approximately 15%."
        ]
    ],
    "Ashland": [
        [
            "Citrus trees in Ashland are suffering from severe citrus greening. Expected crop loss could be up to 30%. 🍊",
            "PRRS has been detected in 6 pigs in Ashland. Immediate veterinary care is essential.",
            "Tomato plants in Ashland are struggling with tomato spotted wilt virus. Estimated reduction in yield is around 25%.",
            "Marek's disease has been reported in chickens in Ashland. Urgent measures are necessary to control this outbreak.",
            "Apple orchards in Ashland are dealing with apple scab. Expected harvest loss could be about 18%. 🍏",
            "Bovine tuberculosis has been diagnosed in 7 cows in Ashland. Immediate assistance with treatment is needed.",
            "Berry bushes in Ashland are affected by mummy berry disease. Potential yield loss could be up to 30%. 🍓",
            "Avian influenza has been confirmed in poultry in Ashland. Immediate action is required with 8 cases reported.",
            "Olive trees in Ashland are struggling with olive knot disease. Impact on yield could be around 20%. 🫒",
            "Corn fields in Ashland are affected by severe corn blight. Expected yield loss is approximately 15%."
        ]
    ],
    "Cambridge": [
        [
            "Sweet potato fields in Cambridge are facing a severe infestation of sweet potato weevils. Yield loss could be up to 30%. 🍠",
            "Brucellosis has been detected in 6 cows in Cambridge. Immediate veterinary care is crucial.",
            "Tomato plants in Cambridge are suffering from late blight. Estimated reduction in yield is about 22%.",
            "Marek's disease has been reported in chickens in Cambridge. Urgent measures are needed to manage this outbreak.",
            "Apple orchards in Cambridge are affected by apple scab. Potential loss in this year’s harvest is around 20%. 🍎",
            "Bovine tuberculosis has been diagnosed in 5 cows in Cambridge. Prompt treatment is necessary.",
            "Berry bushes in Cambridge are affected by powdery mildew. Potential yield loss could be up to 25%. 🍓",
            "Avian influenza has been confirmed in poultry in Cambridge. Immediate action is required, with 10 cases reported.",
            "Olive trees in Cambridge are dealing with olive knot disease. Expected impact on yield is around 22%. 🫒",
            "Corn crops in Cambridge are showing signs of severe corn blight. Yield loss might be approximately 15%."
        ]
    ],
    "Napa": [
        [
            "Grapevines in Napa are battling severe downy mildew. Expected yield reduction could be up to 30%. 🍇",
            "PRRS has been detected in 7 pigs in Napa. Immediate veterinary care is needed.",
            "Citrus trees in Napa are struggling with citrus canker. Potential crop loss is estimated at 25%. 🍊",
            "Marek's disease has been reported in chickens in Napa. Urgent measures are necessary to manage this outbreak.",
            "Apple orchards in Napa are facing apple scab issues. Expected loss in harvest is around 20%. 🍏",
            "Bovine tuberculosis has been diagnosed in 6 cows in Napa. Immediate assistance with treatment is essential.",
            "Blueberry bushes in Napa are affected by mummy berry disease. Potential loss in yield could be up to 30%. 🍓",
            "Avian influenza has been confirmed in poultry in Napa. Immediate action is needed, with 9 cases reported.",
            "Olive trees in Napa are dealing with olive knot disease. Estimated impact on yield is around 20%. 🫒",
            "Corn fields in Napa are showing signs of corn earworm infestation. Yield loss could be approximately 15%."
        ]
    ],
    "Jackson": [
        [
            "Sweet corn fields in Jackson are facing a severe corn earworm infestation. Expected yield loss is around 20%. 🌽",
            "Brucellosis has been detected in 5 cows in Jackson. Immediate veterinary intervention is necessary.",
            "Tomato plants in Jackson are suffering from late blight. Yield reduction might be about 18%.",
            "Marek's disease has been reported in chickens in Jackson. Urgent measures are needed to manage this outbreak.",
            "Apple orchards in Jackson are dealing with apple scab. Expected harvest loss could be around 15%. 🍎",
            "Bovine tuberculosis has been diagnosed in 6 cows in Jackson. Prompt treatment is needed.",
            "Berry bushes in Jackson are showing signs of powdery mildew. Yield loss could be up to 22%. 🍓",
            "Avian influenza has been confirmed in poultry in Jackson. Immediate action is needed, with 8 cases reported.",
            "Olive trees in Jackson are struggling with olive knot disease. Impact on yield could be around 18%. 🫒",
            "Corn crops in Jackson are affected by severe corn blight. Estimated yield loss is approximately 15%."
        ]
    ],
}

location_dev_data = {}

# Splitting location data
for key in location_training_data:
    eighty_percent = round(len(location_training_data[key][0]) * 0.8)
    location_dev_data[key] = [location_training_data[key][0][eighty_percent:]]
    location_training_data[key][0] = location_training_data[key][0][:eighty_percent]

# print(sum(len(location_training_data[key][0]) for key in location_training_data))
# print(sum(len(location_dev_data[key][0]) for key in location_dev_data))

