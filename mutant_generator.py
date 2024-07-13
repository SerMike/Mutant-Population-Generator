import random
import numpy as np
import pandas as pd
from config import (ABILITIES, WEIGHTS, NUM_MUTANTS, CHUNK_SIZE, LANGUAGE_WEIGHTS, COUNTRIES, SEX,
                    GENDER_IDENTITY, OCCUPATIONS, COUNTRY_WEIGHTS, OCCUPATION_WEIGHTS)

print("\nGenerating mutant population...")


def generate_mutants_chunk(chunk_size, start_id):
    country_list = list(COUNTRY_WEIGHTS.keys())
    country_weights = list(COUNTRY_WEIGHTS.values())
    age_groups = ['0-17', '18-34', '35-49', '50-64', '65+']
    age_probabilities = [0.15, 0.45, 0.25, 0.1, 0.05]

    # Pre-generate random choices
    countries = random.choices(country_list, weights=country_weights, k=chunk_size)
    age_groups = np.random.choice(age_groups, size=chunk_size, p=age_probabilities)
    sexes = random.choices(SEX, k=chunk_size)
    gender_identities = random.choices(GENDER_IDENTITY, weights=[0.46, 0.46, 0.04, 0.02, 0.02, 0.005], k=chunk_size)
    abilities = random.choices(ABILITIES, weights=WEIGHTS, k=chunk_size)
    num_languages = np.random.choice([1, 2, 3, 4, 5], size=chunk_size, p=LANGUAGE_WEIGHTS)
    occupations = random.choices(OCCUPATIONS, weights=OCCUPATION_WEIGHTS, k=chunk_size)

    data = []
    for i in range(chunk_size):
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
    chunks = []
    for start_id in range(1, NUM_MUTANTS + 1, CHUNK_SIZE):
        chunk = generate_mutants_chunk(min(CHUNK_SIZE, NUM_MUTANTS - start_id + 1), start_id)
        chunks.append(chunk)

    final_df = pd.concat(chunks, ignore_index=True)

    file_path = 'mutant_population.csv'
    final_df.to_csv(file_path, index=False)
    print(f"\nData successfully saved to {file_path}"
          f"\nA total of {NUM_MUTANTS} mutants have been generated."
          f"\nThat's a whole lotta mutants!")


if __name__ == "__main__":
    main()
