import pandas as pd
import folium
from folium.plugins import HeatMap
from config import COUNTRY_POPULATIONS, TOTAL_POPULATION

# Load the data
print("Loading data...")
df = pd.read_csv('mutant_population.csv')

print("Generating heatmap...")

# Count mutants per country
country_counts = df['country_of_origin'].value_counts().reset_index()
country_counts.columns = ['country', 'mutant_count']

# Dictionary of country centroids (approximate)
country_locations = {
    'China': [35.86166, 104.195397],
    'India': [20.593684, 78.96288],
    'USA': [37.09024, -95.712891],
    'Indonesia': [-0.789275, 113.921327],
    'Pakistan': [30.375321, 69.345116],
    'Brazil': [-14.235004, -51.92528],
    'Nigeria': [9.081999, 8.675277],
    'Bangladesh': [23.684994, 90.356331],
    'Russia': [61.52401, 105.318756],
    'Mexico': [23.634501, -102.552784],
    'Japan': [36.204824, 138.252924],
    'Philippines': [12.879721, 121.774017],
    'Egypt': [26.820553, 30.802498],
    'Vietnam': [14.058324, 108.277199],
    'Turkey': [38.963745, 35.243322],
    'Iran': [32.427908, 53.688046],
    'Germany': [51.165691, 10.451526],
    'Thailand': [15.870032, 100.992541],
    'UK': [55.378051, -3.435973],
    'France': [46.227638, 2.213749],
    'Italy': [41.87194, 12.56738],
    'South Africa': [-30.559482, 22.937506],
    'Tanzania': [-6.369028, 34.888822],
    'Myanmar': [21.913965, 95.956223],
    'South Korea': [35.907757, 127.766922],
    'Colombia': [4.570868, -74.297333],
    'Kenya': [-0.023559, 37.906193],
    'Spain': [40.463667, -3.74922],
    'Argentina': [-38.416097, -63.616672],
    'Ukraine': [48.379433, 31.16558],
    'Algeria': [28.033886, 1.659626],
    'Sudan': [12.862807, 30.217636],
    'Uganda': [1.373333, 32.290275],
    'Iraq': [33.223191, 43.679291],
    'Poland': [51.919438, 19.145136],
    'Canada': [56.130366, -106.346771],
    'Morocco': [31.791702, -7.09262],
    'Saudi Arabia': [23.885942, 45.079162],
    'Uzbekistan': [41.377491, 64.585262],
    'Malaysia': [4.210484, 101.975766],
    'Peru': [-9.189967, -75.015152],
    'Angola': [-11.202692, 17.873887],
    'Ghana': [7.946527, -1.023194],
    'Mozambique': [-18.665695, 35.529562],
    'Yemen': [15.552727, 48.516388],
    'Nepal': [28.394857, 84.124008],
    'Venezuela': [6.42375, -66.58973],
    'Madagascar': [-18.766947, 46.869107],
    'Cameroon': [7.369722, 12.354722],
    "Côte d'Ivoire": [7.539989, -5.54708],
    'Australia': [-25.274398, 133.775136],
    'Niger': [17.607789, 8.081666],
    'Taiwan': [23.69781, 120.960515],
    'Sri Lanka': [7.873054, 80.771797],
    'Burkina Faso': [12.238333, -1.561593],
    'Mali': [17.570692, -3.996166],
    'Romania': [45.943161, 24.96676],
    'Malawi': [-13.254308, 34.301525],
    'Chile': [-35.675147, -71.542969],
    'Kazakhstan': [48.019573, 66.923684],
    'Zambia': [-13.133897, 27.849332],
    'Guatemala': [15.783471, -90.230759],
    'Ecuador': [-1.831239, -78.183406],
    'Syria': [34.802075, 38.996815],
    'Netherlands': [52.132633, 5.291266],
    'Senegal': [14.497401, -14.452362],
    'Cambodia': [12.565679, 104.990963],
    'Chad': [15.454166, 18.732207],
    'Somalia': [5.152149, 46.199616],
    'Zimbabwe': [-19.015438, 29.154857],
    'Guinea': [9.945587, -9.696645],
    'Rwanda': [-1.940278, 29.873888],
    'Benin': [9.30769, 2.315834],
    'Burundi': [-3.373056, 29.918886],
    'Tunisia': [33.886917, 9.537499],
    'Bolivia': [-16.290154, -63.588653],
    'Belgium': [50.503887, 4.469936],
    'Haiti': [18.971187, -72.285215],
    'Cuba': [21.521757, -77.781167],
    'South Sudan': [6.876991, 31.306978],
    'Dominican Republic': [18.735693, -70.162651],
    'Czech Republic': [49.817492, 15.472962],
    'Greece': [39.074208, 21.824312],
    'Jordan': [30.585164, 36.238414],
    'Portugal': [39.399872, -8.224454],
    'Azerbaijan': [40.143105, 47.576927],
    'Sweden': [60.128161, 18.643501],
    'Honduras': [15.199999, -86.241905],
    'United Arab Emirates': [23.424076, 53.847818],
    'Hungary': [47.162494, 19.503304],
    'Tajikistan': [38.861034, 71.276093],
    'Belarus': [53.709807, 27.953389],
    'Austria': [47.516231, 14.550072],
    'Papua New Guinea': [-6.314993, 143.95555],
    'Serbia': [44.016521, 21.005859],
    'Israel': [31.046051, 34.851612],
    'Switzerland': [46.818188, 8.227512],
    'Togo': [8.619543, 0.824782],
    'Sierra Leone': [8.460555, -11.779889],
    'Hong Kong': [22.396428, 114.109497],
    'Laos': [19.85627, 102.495496],
    'Paraguay': [-23.442503, -58.443832],
    'Bulgaria': [42.733883, 25.48583],
    'Libya': [26.3351, 17.228331],
    'Lebanon': [33.854721, 35.862285],
    'Nicaragua': [12.865416, -85.207229],
    'Kyrgyzstan': [41.20438, 74.766098],
    'El Salvador': [13.794185, -88.89653],
    'Turkmenistan': [38.969719, 59.556278],
    'Singapore': [1.352083, 103.819836],
    'Denmark': [56.26392, 9.501785],
    'Finland': [61.92411, 25.748151],
    'Congo': [-0.228021, 15.827659],
    'Slovakia': [48.669026, 19.699024],
    'Norway': [60.472024, 8.468946],
    'Oman': [21.512583, 55.923255],
    'Palestine': [31.952162, 35.233154],
    'Costa Rica': [9.748917, -83.753428],
    'Liberia': [6.428055, -9.429499],
    'Ireland': [53.41291, -8.24389],
    'Central African Republic': [6.611111, 20.939444],
    'New Zealand': [-40.900557, 174.885971],
    'Mauritania': [21.00789, -10.940835],
    'Panama': [8.537981, -80.782127],
    'Kuwait': [29.31166, 47.481766],
    'Croatia': [45.1, 15.2],
    'Moldova': [47.411631, 28.369885],
    'Georgia': [42.315407, 43.356892],
    'Eritrea': [15.179384, 39.782334],
    'Uruguay': [-32.522779, -55.765835],
    'Bosnia and Herzegovina': [43.915886, 17.679076],
    'Mongolia': [46.862496, 103.846656],
    'Armenia': [40.069099, 45.038189],
    'Jamaica': [18.109581, -77.297508],
    'Qatar': [25.354826, 51.183884],
    'Albania': [41.153332, 20.168331],
    'Lithuania': [55.169438, 23.881275],
    'Namibia': [-22.95764, 18.49041],
    'Gambia': [13.443182, -15.310139],
    'Botswana': [-22.328474, 24.684866],
    'Gabon': [-0.803689, 11.609444],
    'Lesotho': [-29.609988, 28.233608],
    'North Macedonia': [41.608635, 21.745275],
    'Slovenia': [46.151241, 14.995463],
    'Guinea-Bissau': [11.803749, -15.180413],
    'Latvia': [56.879635, 24.603189],
    'Bahrain': [25.930414, 50.637772],
    'Equatorial Guinea': [1.650801, 10.267895],
    'Trinidad and Tobago': [10.691803, -61.222503],
    'Estonia': [55.169438, 23.881275],
    'Timor-Leste': [-8.874217, 125.727539],
    'Mauritius': [-20.348404, 57.552152],
    'Cyprus': [35.126413, 33.429859],
    'Eswatini': [-26.522503, 31.465866],
    'Djibouti': [11.825138, 42.590275],
    'Fiji': [-16.578193, 179.414413],
    'Comoros': [-11.875001, 43.872219],
    'Guyana': [4.860416, -58.93018],
    'Bhutan': [27.514162, 90.433601],
    'Solomon Islands': [-9.64571, 160.156194],
    'Montenegro': [42.708678, 19.37439],
    'Luxembourg': [49.815273, 6.129583],
    'Suriname': [3.919305, -56.027783],
    'Cabo Verde': [16.002082, -24.013197],
    'Maldives': [3.202778, 73.22068],
    'Malta': [35.937496, 14.375416],
    'Brunei': [4.535277, 114.727669],
    'Belize': [17.189877, -88.49765],
    'Bahamas': [25.03428, -77.39628],
    'Iceland': [64.963051, -19.020835],
    'Vanuatu': [-15.376706, 166.959158],
    'Barbados': [13.193887, -59.543198],
    'Sao Tome & Principe': [0.18636, 6.613081],
    'Samoa': [-13.759029, -172.104629],
    'Saint Lucia': [13.909444, -60.978893],
    'Kiribati': [-3.370417, -168.734039],
    'Micronesia': [7.425554, 150.550812],
    'Grenada': [12.262776, -61.604171],
    'St. Vincent & Grenadines': [12.984305, -61.287228],
    'Tonga': [-21.178986, -175.198242],
    'Seychelles': [-4.679574, 55.491977],
    'Antigua and Barbuda': [17.060816, -61.796428],
    'Andorra': [42.546245, 1.601554],
    'Dominica': [15.414999, -61.370976],
    'Marshall Islands': [7.131474, 171.184478],
    'Saint Kitts & Nevis': [17.357822, -62.782998],
    'Monaco': [43.750298, 7.412841],
    'Liechtenstein': [47.166, 9.555373],
    'San Marino': [43.94236, 12.457777],
    'Palau': [7.51498, 134.58252],
    'Tuvalu': [-7.109535, 177.64933],
    'Nauru': [-0.522778, 166.931503],
    'Vatican City': [41.902916, 12.453389],
}

# Prepare data for heatmap
heatmap_data = []
for _, row in country_counts.iterrows():
    if row['country'] in country_locations:
        lat, lon = country_locations[row['country']]
        heatmap_data.append([lat, lon, row['mutant_count']])

# Create map centered on a middle point
m = folium.Map(location=[20, 0], zoom_start=2)

# Add heatmap layer
HeatMap(heatmap_data).add_to(m)

# Add markers for top countries
top_countries = country_counts.nlargest(30, 'mutant_count')
for _, row in top_countries.iterrows():
    country = row['country']
    count = row['mutant_count']
    if country in country_locations:
        lat, lon = country_locations[country]
        folium.Marker(
            [lat, lon],
            popup=f"{country}: {count} mutants",
            tooltip=country
        ).add_to(m)

# Save the map
m.save("mutant_population_heatmap.html")

print("\nHeatmap has been generated and saved as 'mutant_population_heatmap.html'"
      "\nDone!")