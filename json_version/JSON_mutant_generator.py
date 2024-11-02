import json
import random
import numpy as np
from datetime import datetime, timedelta

print("\nGenerating mutant population...\n")

NUM_RECORDS = 50000

def generate_mutant_dataset(num_records=NUM_RECORDS):
    # Constants for data generation

    countries = {
        "Asia": [
            "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia",
            "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan",
            "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia",
            "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar",
            "Russia", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan",
            "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates",
            "Uzbekistan", "Vietnam", "Yemen"
        ],
        "North America": [
            "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba",
            "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras",
            "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia",
            "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States of America"
        ],
        "Europe": [
            "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria",
            "Croatia", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece",
            "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania",
            "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia",
            "Norway", "Poland", "Portugal", "Romania", "San Marino", "Serbia", "Slovakia", "Slovenia",
            "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Vatican City"
        ],
        "Africa": [
            "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon",
            "Central African Republic", "Chad", "Comoros", "Congo", "Democratic Republic of the Congo",
            "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia",
            "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya",
            "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia",
            "Niger", "Nigeria", "Rwanda", "São Tomé and Príncipe", "Senegal", "Seychelles", "Sierra Leone",
            "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda",
            "Zambia", "Zimbabwe"
        ],
        "South America": [
            "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru",
            "Suriname", "Uruguay", "Venezuela"
        ],
        "Oceania": [
            "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand",
            "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"
        ]
    }


    power_families = {
        "Energy Manipulation": ["Energy Projection", "Force Field Generation", "Plasma Control",
                                "Solar Energy Absorption"],
        "Physical Enhancement": ["Super Strength", "Enhanced Speed", "Invulnerability", "Regeneration"],
        "Mental Powers": ["Telepathy", "Telekinesis", "Mind Control", "Precognition"],
        "Elemental Control": ["Pyrokinesis", "Hydrokinesis", "Aerokinesis", "Geokinesis"],
        "Matter Manipulation": ["Molecular Restructuring", "Density Control", "Phase Shifting"],
        "Biological": ["Shapeshifting", "Healing Factor", "Bio-Energy Manipulation"],
        "Environmental": ["Weather Control", "Gravity Manipulation", "Time Manipulation"],
        "Psychic Abilities": ["Empathy", "Astral Projection", "Psychometry"],
        "Reality Alteration": ["Probability Manipulation", "Reality Warping", "Dimensional Control"]
    }

    languages = {
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
    'Sudan': ['Arabic', 'English']
    }

    occupations = [
        "Teacher", "Nurse", "Retail Sales Associate", "Office Clerk", "Customer Service Representative",
        "Food Service Worker", "Cashier", "Janitor", "Truck Driver", "Laborer",
        "Administrative Assistant", "Salesperson", "Factory Worker", "Construction Worker", "Manager", "Accountant", "Software Developer", "Engineer", "Electrician", "Plumber",
        "Mechanic", "Police Officer", "Firefighter", "Chef", "Waiter/Waitress",
        "Farmer", "Driver", "Security Guard", "Hairdresser", "Carpenter", "Doctor", "Lawyer", "Architect", "Psychologist", "Pharmacist",
        "Dentist", "Veterinarian", "Journalist", "Graphic Designer", "Financial Analyst",
        "Real Estate Agent", "Physical Therapist", "Photographer", "Pilot", "Social Worker", "Astronomer", "Marine Biologist", "Archaeologist", "Zoologist", "Art Therapist",
        "Meteorologist", "Geologist", "Statistician", "Anthropologist", "Optometrist",
        "Chiropractor", "Urban Planner", "Speech Pathologist", "Actuary", "Biomedical Engineer", "Quantum Physicist", "Neuroscientist", "Robotics Engineer", "Astrophysicist", "Cryptocurrency Specialist",
        "Nanotechnologist", "Volcanologist", "Ethnobotanist", "Ethical Hacker", "Geneticist",
        "Epidemiologist", "Oceanographer", "Paleontologist", "Toxicologist", "Seismologist", "Egyptologist", "Space Archaeologist", "Locomotive Engineer", "Horolologist", "Hippotherapist",
        "Numismatist", "Perfumer", "Fugitive Recovery Agent", "Geomicrobiologist", "Pyrotechnician",
        "Glassblower", "Hydrologist", "Kinesiology Researcher", "Metrologist", "Campanologist"
    ]

    def generate_power_details():
        family = random.choice(list(power_families.keys()))
        power = random.choice(power_families[family])
        control_levels = ["Novice", "Intermediate", "Advanced", "Expert", "Master"]

        return {
            "mutant_power_name": power,
            "mutant_power_set_family": family,
            "power_manifestation_age": random.randint(8, 31),
            "power_control_level": random.choice(control_levels),
            "power_strength_rating": random.randint(1, 10)
        }

    def generate_location():
        continent = random.choice(list(countries.keys()))
        country = random.choice(countries[continent])
        return {
            "continent": continent,
            "country": country
        }

    def generate_parentage():
        parent_types = ["human: no powers", "mutant: low-level powers", "mutant: significant powers"]
        weights = [0.75, 0.2, 0.05]  # 75% human, 20% low-level, 5% significant
        return {
            "mother": random.choices(parent_types, weights=weights)[0],
            "father": random.choices(parent_types, weights=weights)[0]
        }

    # Generate the dataset
    dataset = []
    for i in range(num_records):
        location = generate_location()
        power_details = generate_power_details()
        age_group = ['0-17', '18-34', '35-49', '50-64', '65+']
        age_weights = [0.15, 0.45, 0.25, 0.1, 0.05]

        gender_options = ["Male", "Female", "Non-binary", "Gender Fluid", "Transgender Male", "Transgender Female"]
        gender_weights = [0.45, 0.45, 0.03, 0.02, 0.025, 0.025]

        record = {
            "id": i + 1,
            "age": np.random.choice(age_group, p=age_weights),
            "gender_identity": random.choices(gender_options, weights=gender_weights)[0],
            "location": location,
            "occupation": random.choice(occupations) if age_group != '0-17' else "Minor",
            "registration_status": random.choice(["Registered", "Unregistered"]),
            "known_mutant_parentage": generate_parentage(),
            **power_details,  # Unpack power details
            "incident_count": random.randint(0, 5),
            "last_assessment_date": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        }
        dataset.append(record)

    return {
        "mutant_population_data": dataset,
        "metadata": {
            "total_records": num_records,
            "generation_date": datetime.now().strftime("%Y-%m-%d"),
            "power_set_families": list(power_families.keys()),
            "geographic_distribution": {continent: len(countries) for continent, countries in countries.items()}
        }
    }


# Generate the dataset
synthetic_data = generate_mutant_dataset(NUM_RECORDS)

# Save to file
with open('synthetic_mutant_data.json', 'w') as f:
    json.dump(synthetic_data, f, indent=2)

print(f"\nData successfully saved to 'synthetic_mutant_data.json'"
          f"\nA total of {NUM_RECORDS} mutants have been generated."
          f"\n\nThat's a whole lotta mutants!")