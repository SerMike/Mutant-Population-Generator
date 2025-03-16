# Constants Configuration
# This file contains global constants and settings for the mutant population generator

# Generator Settings
NUM_MUTANTS = 500000  # Total number of mutants to generate
CHUNK_SIZE = 100000   # Number of mutants to generate in each chunk for memory efficiency

# Weighting System Constants
# These values can be adjusted to change the overall distribution of traits

# Ability Distribution Settings
# Adjusting these values will change the relative frequency of different ability categories
ABILITY_DISTRIBUTION = {
    'Common': 10,     # Common abilities (e.g., Super Strength, Flight)
    'Uncommon': 5,    # Default weight for most abilities
    'Rare': 2,        # Rare abilities (e.g., Teleportation, Mind Control)
    'Omega': 1        # Extremely rare/powerful abilities (e.g., Reality Warping)
}

# Occupation Distribution Settings
# Adjusting these values will change the relative frequency of different occupation categories
OCCUPATION_DISTRIBUTION = {
    'Very Common': 25,       # Very common occupations (e.g., Teacher, Nurse)
    'Common': 15,            # Common occupations (e.g., Engineer, Plumber)
    'Moderately Common': 8,  # Moderately common occupations (e.g., Doctor, Lawyer)
    'Uncommon': 4,           # Uncommon occupations (e.g., Astronomer, Geologist)
    'Rare': 2,               # Rare occupations (e.g., Quantum Physicist, Neuroscientist)
    'Very Rare': 1           # Very rare occupations (e.g., Egyptologist, Campanologist)
}

# Language Distribution Settings
# Probability weights for languages by position in a country's language list
# For example, for a country with 3 languages, the first language has 70% probability,
# the second has 25% probability, and the third has 4% probability
LANGUAGE_DISTRIBUTION = [0.7, 0.25, 0.04, 0.009, 0.001]

# Debug Settings
DEBUG_MODE = False  # Set to True to enable debug output
VERBOSE = False     # Set to True for more detailed output during generation 