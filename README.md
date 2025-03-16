# Mutant Population Generator

This project generates and analyzes a diverse population of mutants with various abilities, demographics, and characteristics. The system is designed to be configurable and produces a heatmap visualization of the data.

## Project Structure

```
Mutant-Population-Generator/
├── configs/                                # Configuration files
│   ├── constants.py                        # Global settings and constants
│   ├── demographics_config.py              # Age, sex, and gender settings
│   ├── mutant_abilities_config.py          # Mutant powers and their rarity
│   ├── occupations_config.py               # Occupation categories and weights
│   ├── countries_config.py                 # Country data and language settings
│   └── README.md                           # Configuration documentation
├── data/                                   # Generated data files
│   └── mutant_population.csv               # Main output file
├── visualizations/                         # Visualization scripts and output
│   ├── country_heatmap.py                  # Country distribution visualization
│   ├── mutant_population_heatmap.html      # Interactive heatmap output
│   ├── index.html                          # Main visualization dashboard
│   └── visualizer.py                       # General visualization utilities
└── mutant_generator.py                     # Main generator script
```

## Features

### 1. Data Generation
- Generates large-scale mutant populations (default: 500,000 mutants)
- Memory-efficient chunked processing
- Consistent and configurable weighting system
- Detailed mutant profiles including:
  - Unique abilities and their descriptions
  - Demographics (age, sex, gender identity)
  - Geographic distribution
  - Language capabilities
  - Previous occupations

### 2. Visualizations
- Interactive choropleth map showing global mutant distribution
- Custom color gradients (blue-to-orange) for population density
- Hover information with detailed statistics
- Population percentage and raw count displays
- Top 10 countries statistics

## Configuration System

The generator uses a consistent weighting system across all configuration files:

1. **Higher values = more common**: For all weights, higher numerical values mean the trait is more common
2. **Dictionary-based weights**: Each trait has a corresponding weight in a dictionary
3. **Category-based weights**: Traits are often grouped into categories with shared weights
4. **Centralized constants**: Common weighting values are defined in `constants.py`
5. **Normalized weights**: All weights are automatically normalized for statistical distribution

## How to Use

### 1. Generate Mutant Population
```bash
python mutant_generator.py
```
This will create a CSV file in the data directory with the complete mutant population.

### 2. Create Visualizations
```bash
python visualizations/country_heatmap.py
```
This will generate an interactive HTML visualization showing the global distribution of mutants.

## How to Adjust Weights

### Adjusting Global Category Weights
Edit the distribution dictionaries in `constants.py`:

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
Modify category assignments in the respective config files:

```python
# Example: Making "Telepathy" more common
COMMON_ABILITIES = [
    "Super Strength: Enhanced physical strength.",
    "Telepathy: Reading minds, mental communication.",  # Added to common abilities
    # ... other abilities ...
]
```

### Adding New Traits
1. Add the trait to the appropriate list in the config file
2. Assign it to a category or give it a specific weight
3. The weighting system will automatically include it in generation

## Visualization Customization

The visualization system supports various customization options:

### Color Schemes
- Current: Blue (low) to Orange (high) gradient
- Multiple color stops for better differentiation
- Customizable through `custom_color_scale` in country_heatmap.py

### Map Features
- Interactive zooming and panning
- Hover information with detailed statistics
- Customizable map projection and appearance
- Adjustable color scales and gradients

## Weight Calculation

Each config file follows this pattern for calculating weights:

1. Define the main list of traits
2. Categorize traits by rarity/frequency
3. Create a dictionary mapping each trait to its weight
4. Generate and normalize weights list
5. Apply weights in the generator

This ensures consistent and statistically sound distribution across all mutant characteristics. 