import pandas as pd
import plotly.express as px
import plotly.io as pio
import pycountry

def convert_country_name_to_code(country_name):
    """Convert country name to ISO 3166-1 alpha-3 code"""
    try:
        # Try direct lookup
        country = pycountry.countries.get(name=country_name)
        if country:
            return country.alpha_3
        
        # Try common name variations
        name_variations = {
            'USA': 'USA',
            'UK': 'GBR',
            'Russia': 'RUS',
            'South Korea': 'KOR',
            'North Korea': 'PRK',
            'UAE': 'ARE',
            'Vietnam': 'VNM',
            'Laos': 'LAO',
            'Syria': 'SYR',
            'Venezuela': 'VEN',
            'Taiwan': 'TWN',
            'Iran': 'IRN',
            'Côte d\'Ivoire': 'CIV'
        }
        
        if country_name in name_variations:
            return name_variations[country_name]
        
        # Try searching by common name
        for country in pycountry.countries:
            if country_name.lower() in country.name.lower():
                return country.alpha_3
    except:
        pass
    return None

def create_country_heatmap(data_file='data/mutant_population.csv', output_file='visualizations/mutant_population_heatmap.html'):
    """Create a choropleth heatmap showing mutant distribution by country"""
    
    # Read the data
    df = pd.read_csv(data_file)
    
    # Count mutants by country
    country_counts = df['country_of_origin'].value_counts().reset_index()
    country_counts.columns = ['country', 'count']
    
    # Calculate percentage of total mutants
    total_mutants = country_counts['count'].sum()
    country_counts['percentage'] = (country_counts['count'] / total_mutants) * 100
    
    # Add country codes for mapping
    country_counts['iso_alpha'] = country_counts['country'].apply(convert_country_name_to_code)
    
    # Create a custom color scale that transitions from blue (low) to orange (high)
    # Using multiple color stops for better gradient differentiation
    custom_color_scale = [
        [0, 'rgb(8,48,107)'],        # Deep blue
        [0.1, 'rgb(33,102,172)'],    # Medium blue
        [0.2, 'rgb(67,147,195)'],    # Light blue
        [0.3, 'rgb(146,197,222)'],   # Very light blue
        [0.4, 'rgb(247,247,247)'],   # White/neutral
        [0.5, 'rgb(253,219,199)'],   # Very light orange
        [0.7, 'rgb(244,165,130)'],   # Light orange
        [0.8, 'rgb(214,96,77)'],     # Medium orange
        [1, 'rgb(178,24,43)']        # Deep orange
    ]
    
    # Create the choropleth map
    fig = px.choropleth(
        country_counts,
        locations='iso_alpha',
        color='percentage',
        hover_name='country',
        hover_data={
            'iso_alpha': False,
            'count': True,
            'percentage': ':.2f'
        },
        color_continuous_scale=custom_color_scale,
        title='Global Mutant Population Distribution',
        labels={
            'percentage': 'Percentage of Global Mutant Population',
            'count': 'Number of Mutants'
        }
    )
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Global Mutant Population Distribution',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24}
        },
        geo={
            'showframe': False,
            'showcoastlines': True,
            'projection_type': 'equirectangular',
            'showland': True,
            'landcolor': 'rgb(243, 243, 243)',  # Light gray land
            'showocean': True,
            'oceancolor': 'rgb(230, 230, 230)'  # Slightly darker gray ocean
        },
        width=1200,
        height=800,
        margin={"r":0,"t":30,"l":0,"b":0}
    )
    
    # Add colorbar title and customize its appearance
    fig.update_coloraxes(
        colorbar_title="% of Global<br>Mutant Population",
        colorbar=dict(
            len=0.8,  # Make the colorbar shorter
            thickness=20,  # Make the colorbar wider
            title_font=dict(size=14),
            tickfont=dict(size=12)
        )
    )
    
    # Save the plot
    pio.write_html(fig, output_file)
    print(f"Heatmap has been saved to {output_file}")
    
    # Generate statistics
    print("\nMutant Population Statistics:")
    print("-" * 30)
    print(f"Total number of mutants: {total_mutants:,}")
    print("\nTop 10 countries by mutant population:")
    top_10 = country_counts.nlargest(10, 'count')
    for _, row in top_10.iterrows():
        print(f"{row['country']}: {row['count']:,} mutants ({row['percentage']:.2f}%)")

if __name__ == "__main__":
    create_country_heatmap() 