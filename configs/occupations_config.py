# Occupations Configuration
# This file contains occupation data and their associated weights for the mutant population generator

from configs.constants import OCCUPATION_DISTRIBUTION

# Occupation Categories and their weights
# Higher values mean more common occupations
OCCUPATION_CATEGORY_WEIGHTS = OCCUPATION_DISTRIBUTION

# Categorized Occupations
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

# Flatten occupations list for easy access
OCCUPATIONS = [occupation for category in CATEGORIZED_OCCUPATIONS.values() for occupation in category]

# Create a dictionary mapping each occupation to its weight
OCCUPATION_WEIGHTS_DICT = {}
for category, occupations in CATEGORIZED_OCCUPATIONS.items():
    for occupation in occupations:
        OCCUPATION_WEIGHTS_DICT[occupation] = OCCUPATION_CATEGORY_WEIGHTS[category]

# Generate raw weights list in the same order as OCCUPATIONS
_raw_occupation_weights = [OCCUPATION_WEIGHTS_DICT[occupation] for occupation in OCCUPATIONS]

# Normalize weights to sum to 1 for np.random.choice
OCCUPATION_WEIGHTS = [weight / sum(_raw_occupation_weights) for weight in _raw_occupation_weights]
