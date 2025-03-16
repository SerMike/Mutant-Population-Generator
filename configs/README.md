# Mutant Population Generator Configuration

This directory contains configuration files for the Mutant Population Generator. The configuration system is designed to be easily adjustable and consistent across different aspects of mutant generation.

## Configuration Files

- **constants.py**: Central configuration file with global settings and weighting constants
- **demographics_config.py**: Configuration for demographic data (age, sex, gender identity)
- **mutant_abilities_config.py**: Configuration for mutant abilities and their rarity
- **occupations_config.py**: Configuration for occupations and their frequency
- **countries_config.py**: Configuration for countries, languages, and population-based weights

## Weighting System

The generator uses a consistent weighting system across all configuration files:

1. **Higher values = more common**: For all weights, higher numerical values mean the trait is more common
2. **Dictionary-based weights**: Each trait has a corresponding weight in a dictionary
3. **Category-based weights**: Traits are often grouped into categories with shared weights
4. **Centralized constants**: Common weighting values are defined in `constants.py`

## How to Adjust Weights

### Adjusting Global Category Weights

To change the overall distribution of traits by category, edit the distribution dictionaries in `constants.py`:

```python
# Example: Making rare abilities slightly more common
ABILITY_DISTRIBUTION = {
    'Common': 10,     
    'Uncommon': 5,    
    'Rare': 3,        # Changed from 2 to 3
    'Omega': 1        
}
```

### Adjusting Individual Trait Weights

To change the weight of a specific trait, find its category in the appropriate config file and adjust its assignment:

```python
# Example: Making "Telepathy" more common by adding it to COMMON_ABILITIES
COMMON_ABILITIES = [
    "Super Strength: Enhanced physical strength.",
    "Telepathy: Reading minds, mental communication.",  # Added to common abilities
    # ... other abilities ...
]
```

### Adding New Traits

To add new traits:

1. Add the trait to the appropriate list in the config file
2. Assign it to a category or give it a specific weight
3. The weighting system will automatically include it in generation

## Weight Calculation

Each config file follows this pattern for calculating weights:

1. Define the main list of traits
2. Categorize traits by rarity/frequency
3. Create a dictionary mapping each trait to its weight
4. Generate a weights list in the same order as the main traits list

This ensures consistent weight application across the generator. 