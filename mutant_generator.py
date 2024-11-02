import random
import numpy as np
import pandas as pd
from demographics_config import AGE_GROUPS, AGE_WEIGHTS, SEX, SEX_WEIGHTS, GENDER_IDENTITY, GENDER_IDENTITY_WEIGHTS
from mutant_abilities_config import ABILITIES, WEIGHTS_DICT, WEIGHTS
from countries_config import COUNTRIES, COUNTRY_WEIGHTS, LANGUAGE_WEIGHTS
from occupations_config import OCCUPATIONS, OCCUPATION_WEIGHTS


# Constants
NUM_MUTANTS = 50000


# Program runnning message...
print("\nGenerating mutant population...")


def generate_mutants(start_id):
    # Pre-generate random choices
        
    age_groups = np.random.choice(AGE_GROUPS, p=AGE_WEIGHTS, size=NUM_MUTANTS)
    sexes = np.random.choice(SEX, size=NUM_MUTANTS, p=SEX_WEIGHTS)
    gender_identities = np.random.choice(GENDER_IDENTITY, size=NUM_MUTANTS, p=GENDER_IDENTITY_WEIGHTS)
    num_languages = np.random.choice([1, 2, 3, 4, 5], size=NUM_MUTANTS, p=LANGUAGE_WEIGHTS)

    total_abilities_weight = sum(WEIGHTS)
    normalized_abilities_weights = [weight / total_abilities_weight for weight in WEIGHTS]
    abilities = np.random.choice(ABILITIES, size=NUM_MUTANTS, p=normalized_abilities_weights)

    total_occupations_weight = sum(OCCUPATION_WEIGHTS)
    normalized_occupations_weights = [weight / total_occupations_weight for weight in OCCUPATION_WEIGHTS]
    occupations = np.random.choice(OCCUPATIONS, size=NUM_MUTANTS, p=normalized_occupations_weights)

    total_countries_weight = sum(COUNTRY_WEIGHTS.values())
    normalized_countries_weights = [weight / total_countries_weight for weight in COUNTRY_WEIGHTS.values()]
    countries = np.random.choice(list(COUNTRY_WEIGHTS.keys()), size=NUM_MUTANTS, p=normalized_countries_weights)


    data = []
    for i in range(NUM_MUTANTS):
        mutant_id = start_id + i
        country = countries[i]
        age_group = age_groups[i]
        sex = sexes[i]
        gender_identity = gender_identities[i]
        ability, description = abilities[i].split(': ', 1)

        country_languages = COUNTRIES[country]
        spoken_languages = "; ".join(random.sample(country_languages, min(num_languages[i], len(country_languages))))
        previous_occupation = 'N/A' if age_group == '0-17' else occupations[i]

        data.append([mutant_id, country, ability, description, age_group, sex, gender_identity, spoken_languages,
                     previous_occupation])

    return pd.DataFrame(data, columns=['mutant_id', 'country_of_origin', 'unique_mutant_ability',
                                       'mutant_ability_description', 'age_group', 'sex',
                                       'gender_identity', 'spoken_languages', 'previous_occupation'])


def main():
    # Generate all mutants
    final_df = generate_mutants(start_id=1)

    file_path = 'mutant_population.csv'
    final_df.to_csv(file_path, index=False)
    print(f"\nData successfully saved to {file_path}"
          f"\nA total of {NUM_MUTANTS} mutants have been generated."
          f"\n\nThat's a whole lotta mutants!\n")


if __name__ == "__main__":
    main()
