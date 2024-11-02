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
  