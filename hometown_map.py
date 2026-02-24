"""
Lab 06: Custom Basemap Design & Interactive Hometown Map
Python script for creating an interactive map with Mapbox basemap and hometown locations

Author: Springer Tebeau
Date: February 2026
"""

import pandas as pd
import folium
import requests
import time

# ============================================================================
# CONFIGURATION - YOU MUST UPDATE THESE VALUES
# ============================================================================

# Your Mapbox Access Token (starts with 'pk.')
# Get from: https://studio.mapbox.com/ -> Account -> Access tokens
MAPBOX_ACCESS_TOKEN = 'YOUR_MAPBOX_ACCESS_TOKEN_HERE'

# Your Mapbox Style URL (format: mapbox://styles/username/style_id)
# Get from: Mapbox Studio -> Your Style -> Share -> Style URL
MAPBOX_STYLE_URL = 'mapbox://styles/YOUR_USERNAME/YOUR_STYLE_ID'

# Extract username and style_id from the style URL
# Format: mapbox://styles/username/style_id
if MAPBOX_STYLE_URL.startswith('mapbox://styles/'):
    parts = MAPBOX_STYLE_URL.replace('mapbox://styles/', '').split('/')
    MAPBOX_USERNAME = parts[0]
    MAPBOX_STYLE_ID = parts[1]
else:
    print("Error: Invalid Mapbox Style URL format")
    MAPBOX_USERNAME = 'YOUR_USERNAME'
    MAPBOX_STYLE_ID = 'YOUR_STYLE_ID'

# CSV file with hometown locations
CSV_FILE = 'hometown_locations.csv'

# Output HTML file
OUTPUT_FILE = 'hometown_map.html'

# Map center coordinates (will be updated based on data)
# Default: Fort Worth, TX
DEFAULT_CENTER = [32.7555, -97.3308]

# ============================================================================
# MARKER COLORS FOR DIFFERENT LOCATION TYPES
# ============================================================================

TYPE_COLORS = {
    'Restaurant': 'red',
    'Park': 'green',
    'Cultural': 'purple',
    'Historical': 'orange',
    'Education': 'blue',
    'Recreation': 'cadetblue',
    'Shopping': 'pink',
    'Default': 'gray'
}

# ============================================================================
# FUNCTIONS
# ============================================================================

def geocode_address(address, access_token):
    """
    Geocode an address using the Mapbox Geocoding API.
    
    Args:
        address (str): The address to geocode
        access_token (str): Your Mapbox access token
        
    Returns:
        tuple: (latitude, longitude) or (None, None) if geocoding fails
    """
    # URL encode the address
    encoded_address = requests.utils.quote(address)
    
    # Mapbox Geocoding API endpoint
    url = f'https://api.mapbox.com/search/geocode/v6/forward?q={encoded_address}&access_token={access_token}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        
        data = response.json()
        
        # Check if we got results
        if data.get('features') and len(data['features']) > 0:
            # Get the first result's coordinates
            coordinates = data['features'][0]['geometry']['coordinates']
            # Mapbox returns [longitude, latitude], we need [latitude, longitude]
            longitude, latitude = coordinates
            print(f"✓ Geocoded: {address} -> ({latitude:.4f}, {longitude:.4f})")
            return latitude, longitude
        else:
            print(f"✗ No results found for: {address}")
            return None, None
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Error geocoding {address}: {e}")
        return None, None
    
    # Small delay to avoid hitting API rate limits
    time.sleep(0.1)


def get_marker_color(location_type):
    """
    Get the marker color for a given location type.
    
    Args:
        location_type (str): The type of location
        
    Returns:
        str: The color name for the marker
    """
    return TYPE_COLORS.get(location_type, TYPE_COLORS['Default'])


def create_popup_html(name, description, image_url):
    """
    Create HTML content for a marker popup.
    
    Args:
        name (str): Location name
        description (str): Location description
        image_url (str): URL to location image
        
    Returns:
        str: HTML string for the popup
    """
    html = f"""
    <div style="width: 300px; font-family: Arial, sans-serif;">
        <h3 style="margin-top: 0; color: #333;">{name}</h3>
        <img src="{image_url}" alt="{name}" 
             style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px; margin: 10px 0;">
        <p style="color: #666; line-height: 1.6;">{description}</p>
    </div>
    """
    return html


def create_hometown_map(csv_file, access_token, style_username, style_id, output_file):
    """
    Main function to create the interactive hometown map.
    
    Args:
        csv_file (str): Path to the CSV file with location data
        access_token (str): Mapbox access token
        style_username (str): Your Mapbox username
        style_id (str): Your Mapbox style ID
        output_file (str): Path for the output HTML file
    """
    print("\n" + "="*70)
    print("CREATING HOMETOWN INTERACTIVE MAP")
    print("="*70)
    
    # Step 1: Read the CSV file
    print("\n[1/4] Reading location data from CSV...")
    try:
        df = pd.read_csv(csv_file)
        print(f"✓ Loaded {len(df)} locations from {csv_file}")
        print(f"  Columns: {', '.join(df.columns.tolist())}")
    except Exception as e:
        print(f"✗ Error reading CSV file: {e}")
        return
    
    # Step 2: Geocode all addresses
    print("\n[2/4] Geocoding addresses using Mapbox API...")
    latitudes = []
    longitudes = []
    
    for idx, row in df.iterrows():
        lat, lon = geocode_address(row['Address'], access_token)
        latitudes.append(lat)
        longitudes.append(lon)
    
    # Add coordinates to dataframe
    df['Latitude'] = latitudes
    df['Longitude'] = longitudes
    
    # Remove rows where geocoding failed
    df_clean = df.dropna(subset=['Latitude', 'Longitude'])
    failed_count = len(df) - len(df_clean)
    
    if failed_count > 0:
        print(f"⚠ Warning: {failed_count} location(s) could not be geocoded")
    
    print(f"✓ Successfully geocoded {len(df_clean)} locations")
    
    if len(df_clean) == 0:
        print("✗ Error: No locations could be geocoded. Check your addresses.")
        return
    
    # Step 3: Calculate map center
    center_lat = df_clean['Latitude'].mean()
    center_lon = df_clean['Longitude'].mean()
    print(f"\n[3/4] Map center: ({center_lat:.4f}, {center_lon:.4f})")
    
    # Step 4: Create the Folium map with custom Mapbox basemap
    print("\n[4/4] Creating interactive map with Folium...")
    
    # Create Mapbox tile URL
    # Format: https://api.mapbox.com/styles/v1/{username}/{style_id}/tiles/256/{z}/{x}/{y}@2x?access_token={access_token}
    tiles = f'https://api.mapbox.com/styles/v1/{style_username}/{style_id}/tiles/256/{{z}}/{{x}}/{{y}}@2x?access_token={access_token}'
    
    # Create the map
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=12,
        tiles=tiles,
        attr='Mapbox'
    )
    
    # Add markers for each location
    for idx, row in df_clean.iterrows():
        # Get marker color based on type
        color = get_marker_color(row['Type'])
        
        # Create popup HTML
        popup_html = create_popup_html(
            row['Name'],
            row['Description'],
            row['Image_URL']
        )
        
        # Create the marker
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=folium.Popup(popup_html, max_width=320),
            tooltip=row['Name'],
            icon=folium.Icon(color=color, icon='info-sign')
        ).add_to(m)
        
        print(f"  ✓ Added marker: {row['Name']} ({row['Type']}) - {color}")
    
    # Add a legend
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; right: 50px; width: 180px; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size:14px; padding: 10px; border-radius: 5px;
                box-shadow: 2px 2px 6px rgba(0,0,0,0.3);">
        <h4 style="margin-top:0;">Location Types</h4>
    '''
    
    # Add each type to the legend
    types_in_data = df_clean['Type'].unique()
    for loc_type in sorted(types_in_data):
        color = get_marker_color(loc_type)
        legend_html += f'<p><span style="color:{color};">⬤</span> {loc_type}</p>'
    
    legend_html += '</div>'
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # Save the map
    m.save(output_file)
    print(f"\n✓ Map saved to: {output_file}")
    print("="*70)
    print("SUCCESS! Open the HTML file in a web browser to view your map.")
    print("="*70 + "\n")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Check if configuration is set
    if MAPBOX_ACCESS_TOKEN == 'YOUR_MAPBOX_ACCESS_TOKEN_HERE':
        print("\n" + "!"*70)
        print("ERROR: You must set your Mapbox access token!")
        print("!"*70)
        print("\nTo fix this:")
        print("1. Go to https://studio.mapbox.com/")
        print("2. Click on your account -> Access tokens")
        print("3. Copy your default public token (starts with 'pk.')")
        print("4. Update the MAPBOX_ACCESS_TOKEN variable at the top of this script")
        print("\n" + "!"*70 + "\n")
    elif MAPBOX_STYLE_URL == 'mapbox://styles/YOUR_USERNAME/YOUR_STYLE_ID':
        print("\n" + "!"*70)
        print("ERROR: You must set your Mapbox style URL!")
        print("!"*70)
        print("\nTo fix this:")
        print("1. Go to Mapbox Studio and open your custom style")
        print("2. Click 'Share' button")
        print("3. Copy the Style URL (format: mapbox://styles/username/style_id)")
        print("4. Update the MAPBOX_STYLE_URL variable at the top of this script")
        print("\n" + "!"*70 + "\n")
    else:
        # Run the main function
        create_hometown_map(
            CSV_FILE,
            MAPBOX_ACCESS_TOKEN,
            MAPBOX_USERNAME,
            MAPBOX_STYLE_ID,
            OUTPUT_FILE
        )
