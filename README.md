# Mutant Population Generator

## Description
The Mutant Population Generator is a tool designed to simulate the migration of the fictional mutant population from the Marvel universe to their new homeland of Krakoa. It generates a diverse mutant population from countries around the world and visualizes their migration patterns.

## Features
- **Population Generation:** Create a fictional mutant population with varied attributes.
- **Migration Simulation:** Simulate the migration of mutants to Krakoa.
- **Data Visualization:** Visualize the population distribution and migration patterns.
- **JSON Data Export:** Generate and save mutant population data in JSON format.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SerMike/Mutant-Population-Generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Mutant-Population-Generator
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the population generator:
   ```bash
   python mutant_generator.py
   ```
2. Visualize the generated population:
   ```bash
   python visualizer.py
   ```
3. View the results in `index.html`.
4. The generated mutant population data can also be found in `synthetic_mutant_data.json`.

## Files
- `mutant_generator.py`: Script to generate the mutant population.
- `visualizer.py`: Script to visualize the population data.
- `config.py`: Configuration file for the generator.
- `mutant_population.csv`: Generated mutant population data.
- `synthetic_mutant_data.json`: JSON file containing the generated mutant population data.
- `index.html`: HTML file to display the visualized data.

## Contributing
Currently still working on optimizing generator performance. Currently generates in a csv file. Working on JSON export.

## License
This project is licensed under the MIT License.
