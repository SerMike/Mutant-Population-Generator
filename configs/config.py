from collections import defaultdict

# Constants
NUM_MUTANTS = 500000
CHUNK_SIZE = 100000

# Demographic Data
AGE_GROUPS = ['0-17', '18-34', '35-49', '50-64', '65+']
SEX = ['Male', 'Female']
GENDER_IDENTITY = ['Male', 'Female', 'Non-binary', 'Transgender Male', 'Transgender Female', 'Gender Fluid']

# Mutant Abilities
ABILITIES = [
    "Telepathy: Reading minds, mental communication.",
    "Telekinesis: Moving objects with the mind.",
    "Teleportation: Instantaneous travel from one place to another.",
    "Shape-shifting: Changing physical form.",
    "Elemental Control: Manipulating elements (fire, water, earth, air).",
    "Healing: Rapid recovery from injuries.",
    "Regeneration: Ability to regrow lost limbs or organs.",
    "Super Strength: Enhanced physical strength.",
    "Super Speed: Enhanced speed and reflexes.",
    "Flight: Ability to fly.",
    "Invisibility: Becoming unseen.",
    "Energy Manipulation: Creating, absorbing, and controlling energy.",
    "Weather Control: Manipulating weather patterns.",
    "Time Manipulation: Altering the flow of time.",
    "Precognition: Seeing the future.",
    "Retrocognition: Seeing past events.",
    "Illusions: Creating false perceptions.",
    "Phasing: Passing through solid matter.",
    "Force Fields: Creating protective barriers.",
    "Mind Control: Influencing others' actions and thoughts.",
    "Animal Communication: Talking to and controlling animals.",
    "Plant Manipulation: Controlling plant life.",
    "Size Alteration: Changing physical size.",
    "Duplication: Creating copies of oneself.",
    "Sound Manipulation: Controlling and creating sound.",
    "Density Control: Altering one's density.",
    "Intangibility: Becoming non-solid, ghost-like.",
    "Gravity Control: Manipulating gravitational forces.",
    "Magnetism: Controlling magnetic fields.",
    "Technopathy: Controlling and communicating with machines.",
    "Molecular Manipulation: Changing the molecular structure of objects.",
    "Enhanced Senses: Heightened sensory perception.",
    "Power Absorption: Absorbing and using others' powers.",
    "Power Mimicry: Copying others' powers.",
    "Power Negation: Cancelling out others' powers.",
    "Energy Projection: Emitting energy blasts.",
    "Pyrokinesis: Controlling and creating fire.",
    "Cryokinesis: Controlling and creating ice.",
    "Electrokinesis: Controlling and creating electricity.",
    "Hydrokinesis: Controlling and creating water.",
    "Geokinesis: Controlling and manipulating earth/rock.",
    "Aerokinesis: Controlling and creating air/wind.",
    "Biokinesis: Altering living organisms' biology.",
    "Toxikinesis: Creating and controlling toxins and poisons.",
    "Blood Manipulation: Controlling and using blood.",
    "Bone Manipulation: Controlling and using bones.",
    "Light Manipulation: Controlling and creating light.",
    "Shadow Manipulation: Controlling and creating shadows.",
    "Darkness Manipulation: Controlling and creating darkness.",
    "Solar Manipulation: Controlling and using solar energy.",
    "Lunar Manipulation: Controlling and using lunar energy.",
    "Plasma Manipulation: Controlling and creating plasma.",
    "Radiation Manipulation: Controlling and creating radiation.",
    "Elasticity: Stretching and reshaping the body.",
    "Seismic Manipulation: Creating and controlling earthquakes.",
    "Psionic Constructs: Creating physical objects with the mind.",
    "Telempathy: Sensing and manipulating emotions.",
    "Umbrakinesis: Controlling and creating shadows.",
    "Photokinesis: Controlling and creating light.",
    "Vitakinesis: Healing and altering life force.",
    "Atmospheric Manipulation: Controlling the atmosphere.",
    "Temperature Manipulation: Controlling and altering temperature.",
    "Pressure Manipulation: Controlling pressure in the environment.",
    "Psionic Energy: Using psionic energy for various effects.",
    "Chlorokinesis: Controlling plant life.",
    "Ecokinesis: Controlling the ecosystem.",
    "Spatial Manipulation: Altering space and dimensions.",
    "Dimensional Travel: Moving between dimensions.",
    "Reality Warping: Altering reality.",
    "Dream Manipulation: Controlling and entering dreams.",
    "Memory Manipulation: Altering and erasing memories.",
    "Sonic Scream: Emitting powerful sonic waves.",
    "Acid Generation: Creating and controlling acid.",
    "Explosion Manipulation: Creating and controlling explosions.",
    "Adoptive Muscle Memory: Learning physical tasks instantly.",
    "Omnilingualism: Understanding all languages.",
    "Enhanced Intellect: Superhuman intelligence.",
    "Enhanced Agility: Superhuman agility and reflexes.",
    "Tactile Telekinesis: Moving objects through touch.",
    "Omniscience: Knowing everything.",
    "Omnipresence: Being present everywhere simultaneously.",
    "Omnipotence: Unlimited power.",
    "Matter Ingestion: Consuming any form of matter.",
    "Substance Mimicry: Turning into any material.",
    "Vibration Manipulation: Controlling vibrations.",
    "Frequency Manipulation: Controlling frequencies of sound, light, etc.",
    "Fire Resistance: Immunity to fire.",
    "Ice Resistance: Immunity to cold and ice.",
    "Electric Resistance: Immunity to electricity.",
    "Poison Resistance: Immunity to toxins and poisons.",
    "Bulletproof: Impervious to bullets.",
    "Invulnerability: Complete resistance to physical harm.",
    "Enhanced Durability: Increased physical resilience.",
    "Emotion Control: Influencing and controlling emotions.",
    "Magic: Using magical spells and abilities.",
    "Alchemy: Transmuting matter.",
    "Cyberpathy: Controlling and communicating with computers.",
    "Summoning: Calling forth beings or objects.",
    "Animal Transformation: Changing into animals.",
    "Time Travel: Moving through time."
]

# Ability Weights
WEIGHTS_DICT = defaultdict(lambda: 5)  # Default weight is 5 (uncommon)

COMMON_ABILITIES = [
    "Super Strength: Enhanced physical strength.",
    "Super Speed: Enhanced speed and reflexes.",
    "Flight: Ability to fly.",
    "Invisibility: Becoming unseen.",
    "Healing: Rapid recovery from injuries.",
    "Regeneration: Ability to regrow lost limbs or organs.",
    "Enhanced Senses: Heightened sensory perception.",
    "Fire Resistance: Immunity to fire.",
    "Ice Resistance: Immunity to cold and ice.",
    "Electric Resistance: Immunity to electricity.",
    "Poison Resistance: Immunity to toxins and poisons.",
    "Bulletproof: Impervious to bullets.",
    "Enhanced Durability: Increased physical resilience."
]

RARE_ABILITIES = [
    "Teleportation: Instantaneous travel from one place to another.",
    "Force Fields: Creating protective barriers.",
    "Mind Control: Influencing others' actions and thoughts.",
    "Phasing: Passing through solid matter.",
    "Power Absorption: Absorbing and using others' powers.",
    "Power Mimicry: Copying others' powers.",
    "Power Negation: Cancelling out others' powers.",
    "Pyrokinesis: Controlling and creating fire.",
    "Electrokinesis: Controlling and creating electricity.",
    "Molecular Manipulation: Changing the molecular structure of objects.",
    "Reality Warping: Altering reality.",
    "Time Manipulation: Altering the flow of time.",
    "Dimensional Travel: Moving between dimensions."
]

OMEGA_ABILITIES = [
    "Telepathy: Reading minds, mental communication.",
    "Weather Control: Manipulating weather patterns.",
    "Reality Warping: Altering reality.",
    "Time Travel: Moving through time.",
    "Omniscience: Knowing everything.",
    "Omnipresence: Being present everywhere simultaneously.",
    "Omnipotence: Unlimited power."
]

for power in COMMON_ABILITIES:
    WEIGHTS_DICT[power] = 10

for power in RARE_ABILITIES:
    WEIGHTS_DICT[power] = 2

for power in OMEGA_ABILITIES:
    WEIGHTS_DICT[power] = 1

WEIGHTS = [WEIGHTS_DICT[power] for power in ABILITIES]

# Countries and Languages
COUNTRIES = defaultdict(lambda: ['English'])
COUNTRIES.update({
    'China': ['Mandarin', 'Cantonese', 'English'],
    'India': ['Hindi', 'English', 'Bengali', 'Telugu', 'Marathi', 'Tamil', 'Urdu'],
    'USA': ['English', 'Spanish'],
    'Brazil': ['Portuguese'],
    'Russia': ['Russian', 'English'],
    'Japan': ['Japanese', 'English'],
    'Germany': ['German', 'English'],
    'France': ['French', 'English'],
    'Canada': ['English', 'French'],
    'Australia': ['English'],
    'UK': ['English'],
    'Mexico': ['Spanish'],
    'Italy': ['Italian', 'English'],
    'South Korea': ['Korean', 'English'],
    'Argentina': ['Spanish'],
    'Spain': ['Spanish', 'Catalan'],
    'Pakistan': ['Urdu', 'English', 'Punjabi'],
    'Bangladesh': ['Bengali', 'English'],
    'Nigeria': ['English', 'Hausa', 'Yoruba', 'Igbo'],
    'Philippines': ['Filipino', 'English'],
    'Vietnam': ['Vietnamese', 'English'],
    'Egypt': ['Arabic', 'English'],
    'Turkey': ['Turkish', 'English'],
    'Thailand': ['Thai', 'English'],
    'Iran': ['Persian', 'English'],
    'South Africa': ['English', 'Zulu', 'Xhosa', 'Afrikaans'],
    'Ukraine': ['Ukrainian', 'Russian'],
    'Malaysia': ['Malay', 'English'],
    'Saudi Arabia': ['Arabic', 'English'],
    'Indonesia': ['Indonesian', 'English'],
    'Poland': ['Polish', 'English'],
    'Netherlands': ['Dutch', 'English'],
    'Belgium': ['Dutch', 'French', 'German'],
    'Greece': ['Greek', 'English'],
    'Portugal': ['Portuguese', 'English'],
    'Chile': ['Spanish'],
    'Czech Republic': ['Czech', 'English'],
    'Romania': ['Romanian', 'English'],
    'Sweden': ['Swedish', 'English'],
    'Hungary': ['Hungarian', 'English'],
    'Switzerland': ['German', 'French', 'Italian'],
    'Austria': ['German', 'English'],
    'Norway': ['Norwegian', 'English'],
    'Israel': ['Hebrew', 'English', 'Arabic'],
    'New Zealand': ['English', 'Maori'],
    'Singapore': ['English', 'Mandarin', 'Malay', 'Tamil'],
    'Denmark': ['Danish', 'English'],
    'Ireland': ['English', 'Irish'],
    'Finland': ['Finnish', 'English'],
    'Colombia': ['Spanish'],
    'Venezuela': ['Spanish'],
    'Peru': ['Spanish', 'Quechua'],
    'Ecuador': ['Spanish'],
    'Bolivia': ['Spanish', 'Quechua'],
    'Paraguay': ['Spanish', 'Guarani'],
    'Uruguay': ['Spanish'],
    'Cuba': ['Spanish'],
    'Honduras': ['Spanish'],
    'Guatemala': ['Spanish'],
    'El Salvador': ['Spanish'],
    'Nicaragua': ['Spanish'],
    'Costa Rica': ['Spanish'],
    'Panama': ['Spanish'],
    'Slovakia': ['Slovak', 'English'],
    'Croatia': ['Croatian', 'English'],
    'Serbia': ['Serbian', 'English'],
    'Bulgaria': ['Bulgarian', 'English'],
    'Slovenia': ['Slovene', 'English'],
    'Bosnia and Herzegovina': ['Bosnian', 'Croatian', 'Serbian'],
    'North Macedonia': ['Macedonian', 'Albanian'],
    'Albania': ['Albanian', 'English'],
    'Estonia': ['Estonian', 'English'],
    'Latvia': ['Latvian', 'Russian', 'English'],
    'Lithuania': ['Lithuanian', 'English'],
    'Belarus': ['Belarusian', 'Russian'],
    'Armenia': ['Armenian', 'Russian'],
    'Azerbaijan': ['Azerbaijani', 'Russian'],
    'Georgia': ['Georgian', 'Russian'],
    'Kazakhstan': ['Kazakh', 'Russian'],
    'Uzbekistan': ['Uzbek', 'Russian'],
    'Turkmenistan': ['Turkmen', 'Russian'],
    'Kyrgyzstan': ['Kyrgyz', 'Russian'],
    'Tajikistan': ['Tajik', 'Russian'],
    'Mongolia': ['Mongolian', 'Russian'],
    'Afghanistan': ['Pashto', 'Dari'],
    'Nepal': ['Nepali', 'English'],
    'Sri Lanka': ['Sinhala', 'Tamil'],
    'Myanmar': ['Burmese'],
    'Cambodia': ['Khmer', 'English'],
    'Laos': ['Lao', 'French'],
    'Jordan': ['Arabic', 'English'],
    'Lebanon': ['Arabic', 'French'],
    'Iraq': ['Arabic', 'Kurdish'],
    'Syria': ['Arabic', 'Kurdish'],
    'Yemen': ['Arabic'],
    'Oman': ['Arabic'],
    'Qatar': ['Arabic', 'English'],
    'UAE': ['Arabic', 'English'],
    'Kuwait': ['Arabic', 'English'],
    'Bahrain': ['Arabic', 'English'],
    'Libya': ['Arabic'],
    'Morocco': ['Arabic', 'French'],
    'Algeria': ['Arabic', 'French'],
    'Tunisia': ['Arabic', 'French'],
    'Sudan': ['Arabic', 'English'],
})

LANGUAGE_WEIGHTS = [0.7, 0.25, 0.04, 0.009, 0.001]

# Country population data (2021 estimates, millions)
COUNTRY_POPULATIONS = {
    'China': 1439,
    'India': 1380,
    'USA': 531,
    'Indonesia': 273,
    'Pakistan': 220,
    'Brazil': 212,
    'Nigeria': 206,
    'Bangladesh': 164,
    'Russia': 145,
    'Mexico': 128,
    'Japan': 126,
    'Philippines': 109,
    'Egypt': 102,
    'Vietnam': 97,
    'Turkey': 84,
    'Iran': 84,
    'Germany': 83,
    'Thailand': 70,
    'UK': 68,
    'France': 65,
    'Italy': 60,
    'South Africa': 59,
    'Tanzania': 59,
    'Myanmar': 54,
    'South Korea': 51,
    'Colombia': 50,
    'Kenya': 53,
    'Spain': 47,
    'Argentina': 45,
    'Ukraine': 44,
    'Algeria': 43,
    'Sudan': 43,
    'Uganda': 45,
    'Iraq': 40,
    'Poland': 38,
    'Canada': 38,
    'Morocco': 36,
    'Saudi Arabia': 34,
    'Uzbekistan': 33,
    'Malaysia': 32,
    'Peru': 33,
    'Angola': 32,
    'Ghana': 31,
    'Mozambique': 31,
    'Yemen': 29,
    'Nepal': 29,
    'Venezuela': 28,
    'Madagascar': 27,
    'Cameroon': 26,
    "Côte d'Ivoire": 26,
    'Australia': 25,
    'Niger': 24,
    'Taiwan': 24,
    'Sri Lanka': 22,
    'Burkina Faso': 21,
    'Mali': 20,
    'Romania': 19,
    'Malawi': 19,
    'Chile': 19,
    'Kazakhstan': 19,
    'Zambia': 18,
    'Guatemala': 18,
    'Ecuador': 17,
    'Syria': 17,
    'Netherlands': 17,
    'Senegal': 16,
    'Cambodia': 16,
    'Chad': 16,
    'Somalia': 15,
    'Zimbabwe': 15,
    'Guinea': 13,
    'Rwanda': 13,
    'Benin': 12,
    'Burundi': 12,
    'Tunisia': 12,
    'Bolivia': 12,
    'Belgium': 12,
    'Haiti': 11,
    'Cuba': 11,
    'South Sudan': 11,
    'Dominican Republic': 11,
    'Czech Republic': 11,
    'Greece': 10,
    'Jordan': 10,
    'Portugal': 10,
    'Azerbaijan': 10,
    'Sweden': 10,
    'Honduras': 10,
    'United Arab Emirates': 10,
    'Hungary': 10,
    'Tajikistan': 9,
    'Belarus': 9,
    'Austria': 9,
    'Papua New Guinea': 9,
    'Serbia': 9,
    'Israel': 9,
    'Switzerland': 9,
    'Togo': 8,
    'Sierra Leone': 8,
    'Hong Kong': 7,
    'Laos': 7,
    'Paraguay': 7,
    'Bulgaria': 7,
    'Libya': 7,
    'Lebanon': 7,
    'Nicaragua': 7,
    'Kyrgyzstan': 6,
    'El Salvador': 6,
    'Turkmenistan': 6,
    'Singapore': 6,
    'Denmark': 6,
    'Finland': 6,
    'Congo': 5,
    'Slovakia': 5,
    'Norway': 5,
    'Oman': 5,
    'Palestine': 5,
    'Costa Rica': 5,
    'Liberia': 5,
    'Ireland': 5,
    'Central African Republic': 5,
    'New Zealand': 5,
    'Mauritania': 5,
    'Panama': 4,
    'Kuwait': 4,
    'Croatia': 4,
    'Moldova': 4,
    'Georgia': 4,
    'Eritrea': 3,
    'Uruguay': 3,
    'Bosnia and Herzegovina': 3,
    'Mongolia': 3,
    'Armenia': 3,
    'Jamaica': 3,
    'Qatar': 3,
    'Albania': 3,
    'Lithuania': 3,
    'Namibia': 3,
    'Gambia': 2,
    'Botswana': 2,
    'Gabon': 2,
    'Lesotho': 2,
    'North Macedonia': 2,
    'Slovenia': 2,
    'Guinea-Bissau': 2,
    'Latvia': 2,
    'Bahrain': 2,
    'Equatorial Guinea': 1,
    'Trinidad and Tobago': 1,
    'Estonia': 1,
    'Timor-Leste': 1,
    'Mauritius': 1,
    'Cyprus': 1,
    'Eswatini': 1,
    'Djibouti': 1,
    'Fiji': 1,
    'Comoros': 1,
    'Guyana': 1,
    'Bhutan': 1,
    'Solomon Islands': 1,
    'Montenegro': 1,
    'Luxembourg': 1,
    'Suriname': 1,
    'Cabo Verde': 1,
    'Maldives': 1,
    'Malta': 1,
    'Brunei': 1,
    'Belize': 1,
    'Bahamas': 1,
    'Iceland': 1,
    'Vanuatu': 1,
    'Barbados': 1,
    'Sao Tome & Principe': 1,
    'Samoa': 1,
    'Saint Lucia': 1,
    'Kiribati': 1,
    'Micronesia': 1,
    'Grenada': 1,
    'St. Vincent & Grenadines': 1,
    'Tonga': 1,
    'Seychelles': 1,
    'Antigua and Barbuda': 1,
    'Andorra': 1,
    'Dominica': 1,
    'Marshall Islands': 1,
    'Saint Kitts & Nevis': 1,
    'Monaco': 1,
    'Liechtenstein': 1,
    'San Marino': 1,
    'Palau': 1,
    'Tuvalu': 1,
    'Nauru': 1,
    'Vatican City': 1,
}

TOTAL_POPULATION = sum(COUNTRY_POPULATIONS.values())
COUNTRY_WEIGHTS = {country: population / TOTAL_POPULATION for country, population in COUNTRY_POPULATIONS.items()}

# Occupations
OCCUPATION_CATEGORIES = {
    'Very Common': 25,
    'Common': 15,
    'Moderately Common': 8,
    'Uncommon': 4,
    'Rare': 2,
    'Very Rare': 1
}

CATEGORIZED_OCCUPATIONS = {
    'Very Common': [
        "Teacher", "Nurse", "Retail Sales Associate", "Office Clerk", "Customer Service Representative",
        "Food Service Worker", "Cashier", "Janitor", "Truck Driver", "Laborer",
        "Administrative Assistant", "Salesperson", "Factory Worker", "Construction Worker", "Manager"
    ],
    'Common': [
        "Accountant", "Software Developer", "Engineer", "Electrician", "Plumber",
        "Mechanic", "Police Officer", "Firefighter", "Chef", "Waiter/Waitress",
        "Farmer", "Driver", "Security Guard", "Hairdresser", "Carpenter"
    ],
    'Moderately Common': [
        "Doctor", "Lawyer", "Architect", "Psychologist", "Pharmacist",
        "Dentist", "Veterinarian", "Journalist", "Graphic Designer", "Financial Analyst",
        "Real Estate Agent", "Physical Therapist", "Photographer", "Pilot", "Social Worker"
    ],
    'Uncommon': [
        "Astronomer", "Marine Biologist", "Archaeologist", "Zoologist", "Art Therapist",
        "Meteorologist", "Geologist", "Statistician", "Anthropologist", "Optometrist",
        "Chiropractor", "Urban Planner", "Speech Pathologist", "Actuary", "Biomedical Engineer"
    ],
    'Rare': [
        "Quantum Physicist", "Neuroscientist", "Robotics Engineer", "Astrophysicist", "Cryptocurrency Specialist",
        "Nanotechnologist", "Volcanologist", "Ethnobotanist", "Ethical Hacker", "Geneticist",
        "Epidemiologist", "Oceanographer", "Paleontologist", "Toxicologist", "Seismologist"
    ],
    'Very Rare': [
        "Egyptologist", "Space Archaeologist", "Locomotive Engineer", "Horolologist", "Hippotherapist",
        "Numismatist", "Perfumer", "Fugitive Recovery Agent", "Geomicrobiologist", "Pyrotechnician",
        "Glassblower", "Hydrologist", "Kinesiology Researcher", "Metrologist", "Campanologist"
    ]
}

OCCUPATIONS = [occupation for category in CATEGORIZED_OCCUPATIONS.values() for occupation in category]

OCCUPATION_WEIGHTS = []
for category, occupations in CATEGORIZED_OCCUPATIONS.items():
    OCCUPATION_WEIGHTS.extend([OCCUPATION_CATEGORIES[category]] * len(occupations))

# Usage example
# from config import NUM_MUTANTS, CHUNK_SIZE, ABILITIES, WEIGHTS, COUNTRIES, SEX, GENDER_IDENTITY, \
#     OCCUPATIONS, LANGUAGE_WEIGHTS, COUNTRY_WEIGHTS, OCCUPATION_WEIGHTS