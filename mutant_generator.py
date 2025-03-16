import random
import numpy as np
import pandas as pd
from configs.constants import NUM_MUTANTS as TOTAL_MUTANTS, CHUNK_SIZE
from configs.demographics_config import AGE_GROUPS, AGE_WEIGHTS, SEX, SEX_WEIGHTS, GENDER_IDENTITY, GENDER_IDENTITY_WEIGHTS
from configs.mutant_abilities_config import ABILITIES, ABILITY_WEIGHTS_DICT, ABILITY_WEIGHTS
from configs.countries_config import COUNTRIES, COUNTRY_LIST, COUNTRY_WEIGHTS, LANGUAGE_POSITION_WEIGHTS
from configs.occupations_config import OCCUPATIONS, OCCUPATION_WEIGHTS


# Program running message...
print("\nGenerating mutant population...")


def generate_mutants(num_to_generate, start_id):
    """Generate a specified number of mutants starting from the given ID"""
    # Pre-generate random choices
        
    age_groups = np.random.choice(AGE_GROUPS, p=AGE_WEIGHTS, size=num_to_generate)
    sexes = np.random.choice(SEX, size=num_to_generate, p=SEX_WEIGHTS)
    gender_identities = np.random.choice(GENDER_IDENTITY, size=num_to_generate, p=GENDER_IDENTITY_WEIGHTS)
    num_languages = np.random.choice([1, 2, 3, 4, 5], size=num_to_generate, p=LANGUAGE_POSITION_WEIGHTS)

    # All weights are pre-normalized in their respective config files
    abilities = np.random.choice(ABILITIES, size=num_to_generate, p=ABILITY_WEIGHTS)
    occupations = np.random.choice(OCCUPATIONS, size=num_to_generate, p=OCCUPATION_WEIGHTS)
    countries = np.random.choice(COUNTRY_LIST, size=num_to_generate, p=COUNTRY_WEIGHTS)

    data = []
    for i in range(num_to_generate):
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


def generate_in_chunks():
    """Generate mutants in chunks to manage memory usage for large datasets"""
    chunks = []
    num_chunks = (TOTAL_MUTANTS + CHUNK_SIZE - 1) // CHUNK_SIZE  # Ceiling division
    
    for i in range(num_chunks):
        start_id = i * CHUNK_SIZE + 1
        chunk_size = min(CHUNK_SIZE, TOTAL_MUTANTS - i * CHUNK_SIZE)
        
        print(f"Generating chunk {i+1}/{num_chunks} (mutants {start_id} to {start_id + chunk_size - 1})...")
        chunk_df = generate_mutants(chunk_size, start_id)
        chunks.append(chunk_df)
    
    return pd.concat(chunks, ignore_index=True)


def main():
    if TOTAL_MUTANTS <= CHUNK_SIZE:
        # Generate all mutants at once if the number is small enough
        final_df = generate_mutants(TOTAL_MUTANTS, start_id=1)
    else:
        # Generate in chunks for large datasets
        final_df = generate_in_chunks()

    file_path = 'data/mutant_population.csv'
    final_df.to_csv(file_path, index=False)
    print(f"\nData successfully saved to {file_path}"
          f"\nA total of {TOTAL_MUTANTS} mutants have been generated."
          f"\n\nThat's a whole lotta mutants!\n")


if __name__ == "__main__":
    main()
