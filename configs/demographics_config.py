# Demographic Data Configuration
# This file contains demographic data and their associated weights for the mutant population generator

# Age Groups
AGE_GROUPS = ['0-17', '18-34', '35-49', '50-64', '65+']

# Age Group Weights - Higher values mean more common
# Default weights are percentages of population
AGE_WEIGHTS_DICT = {
    '0-17': 15,
    '18-34': 45,
    '35-49': 25,
    '50-64': 10,
    '65+': 5
}

# Generate weights list in the same order as AGE_GROUPS
_raw_age_weights = [AGE_WEIGHTS_DICT[age_group] for age_group in AGE_GROUPS]
# Normalize weights to sum to 1 for np.random.choice
AGE_WEIGHTS = [weight / sum(_raw_age_weights) for weight in _raw_age_weights]

# Sex
SEX = ['Male', 'Female']

# Sex Weights - Higher values mean more common
# Default weights are percentages of population
SEX_WEIGHTS_DICT = {
    'Male': 46,
    'Female': 54
}

# Generate weights list in the same order as SEX
_raw_sex_weights = [SEX_WEIGHTS_DICT[sex] for sex in SEX]
# Normalize weights to sum to 1 for np.random.choice
SEX_WEIGHTS = [weight / sum(_raw_sex_weights) for weight in _raw_sex_weights]

# Gender Identity
GENDER_IDENTITY = ['Male', 'Female', 'Non-binary', 'Transgender Male', 'Transgender Female', 'Gender Fluid']

# Gender Identity Weights - Higher values mean more common
# Default weights are percentages of population
GENDER_IDENTITY_WEIGHTS_DICT = {
    'Male': 45,
    'Female': 47,
    'Non-binary': 5,
    'Transgender Male': 1,
    'Transgender Female': 1,
    'Gender Fluid': 1
}

# Generate weights list in the same order as GENDER_IDENTITY
_raw_gender_weights = [GENDER_IDENTITY_WEIGHTS_DICT[gender] for gender in GENDER_IDENTITY]
# Normalize weights to sum to 1 for np.random.choice
GENDER_IDENTITY_WEIGHTS = [weight / sum(_raw_gender_weights) for weight in _raw_gender_weights]
