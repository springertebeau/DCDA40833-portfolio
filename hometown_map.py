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
    
    Goal: Convert a street address (like "123 Main St, Fort Worth, TX") 
          into geographic coordinates (latitude, longitude) that can be 
          plotted on a map.
    
    Args:
        address (str): The address to geocode
        access_token (str): Your Mapbox access token
        
    Returns:
        tuple: (latitude, longitude) or (None, None) if geocoding fails
    """
    # URL encode the address to make it safe for use in a web request
    # Example: "123 Main St" becomes "123%20Main%20St"
    encoded_address = requests.utils.quote(address)
    
    # Build the Mapbox Geocoding API endpoint URL
    # This is the web address where we send our geocoding request
    url = f'https://api.mapbox.com/search/geocode/v6/forward?q={encoded_address}&access_token={access_token}'
    
    try:
        # Send HTTP GET request to the Mapbox API
        response = requests.get(url)
        
        # Raise an exception if the request failed (status code 4xx or 5xx)
        response.raise_for_status()
        
        # Parse the JSON response from the API
        data = response.json()
        
        # Check if we got any results back from the geocoding service
        if data.get('features') and len(data['features']) > 0:
            # Extract coordinates from the first result
            # The API returns the best match first
            coordinates = data['features'][0]['geometry']['coordinates']
            
            # Important: Mapbox returns [longitude, latitude] but we need [latitude, longitude]
            # This is because geographic coordinates are typically listed as (lat, long)
            longitude, latitude = coordinates
            
            # Print success message with rounded coordinates
            print(f"✓ Geocoded: {address} -> ({latitude:.4f}, {longitude:.4f})")
            return latitude, longitude
        else:
            # No results found - address might be invalid or too vague
            print(f"✗ No results found for: {address}")
            return None, None
            
    except requests.exceptions.RequestException as e:
        # Handle any errors that occurred during the HTTP request
        print(f"✗ Error geocoding {address}: {e}")
        return None, None
    
    # Small delay to avoid hitting API rate limits
    # Most free APIs limit how many requests you can make per second
    time.sleep(0.1)


def get_marker_color(location_type):
    """
    Get the marker color for a given location type.
    
    Goal: Assign a consistent color to each type of location
          (e.g., all restaurants are red, all parks are green)
    
    Args:
        location_type (str): The type of location
        
    Returns:
        str: The color name for the marker
    """
    # Look up the color in the TYPE_COLORS dictionary
    # If the type isn't found, use the 'Default' gray color
    return TYPE_COLORS.get(location_type, TYPE_COLORS['Default'])


def create_popup_html(name, description, image_url):
    """
    Create HTML content for a marker popup.
    
    Goal: Generate the HTML that will be displayed when a user clicks 
          on a map marker. This includes the location name, image, and 
          personal description.
    
    Args:
        name (str): Location name
        description (str): Location description
        image_url (str): URL to location image
        
    Returns:
        str: HTML string for the popup
    """
    # Create an HTML div with the location information
    # This uses an f-string to insert the variables into the HTML template
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
    
    # ========================================================================
    # STEP 1: Read the CSV file containing hometown locations
    # Goal: Load the location data from the CSV file into a pandas DataFrame
    # ========================================================================
    print("\n[1/4] Reading location data from CSV...")
    try:
        # Read the CSV file into a pandas DataFrame
        # DataFrame is like a spreadsheet or table in Python
        df = pd.read_csv(csv_file)
        
        # Print confirmation with the number of rows (locations)
        print(f"✓ Loaded {len(df)} locations from {csv_file}")
        
        # Show what columns are in the CSV file
        print(f"  Columns: {', '.join(df.columns.tolist())}")
    except Exception as e:
        # If reading the file fails, print the error and exit
        print(f"✗ Error reading CSV file: {e}")
        return
    
    # ========================================================================
    # STEP 2: Geocode all addresses to get latitude/longitude coordinates
    # Goal: Convert each street address into map coordinates
    # ========================================================================
    print("\n[2/4] Geocoding addresses using Mapbox API...")
    
    # Create empty lists to store the latitude and longitude values
    latitudes = []
    longitudes = []
    
    # Loop through each row in the DataFrame
    # iterrows() gives us both the index and the row data
    for idx, row in df.iterrows():
        # Call our geocode_address function for each address
        lat, lon = geocode_address(row['Address'], access_token)
        
        # Add the coordinates to our lists
        # (might be None if geocoding failed)
        latitudes.append(lat)
        longitudes.append(lon)
    
    # Add the coordinate columns to our DataFrame
    df['Latitude'] = latitudes
    df['Longitude'] = longitudes
    
    # Remove any rows where geocoding failed (where Latitude or Longitude is None)
    # dropna() removes rows with missing values
    df_clean = df.dropna(subset=['Latitude', 'Longitude'])
    
    # Calculate how many locations failed to geocode
    failed_count = len(df) - len(df_clean)
    
    if failed_count > 0:
        print(f"⚠ Warning: {failed_count} location(s) could not be geocoded")
    
    print(f"✓ Successfully geocoded {len(df_clean)} locations")
    
    # If no locations were successfully geocoded, we can't create a map
    if len(df_clean) == 0:
        print("✗ Error: No locations could be geocoded. Check your addresses.")
        return
    
    # ========================================================================
    # STEP 3: Calculate the map center point
    # Goal: Find the geographic center of all our locations to center the map
    # ========================================================================
    
    # Calculate the average (mean) latitude and longitude
    # This gives us the center point of all our locations
    center_lat = df_clean['Latitude'].mean()
    center_lon = df_clean['Longitude'].mean()
    print(f"\n[3/4] Map center: ({center_lat:.4f}, {center_lon:.4f})")
    
    # ========================================================================
    # STEP 4: Create the interactive map using Folium
    # Goal: Build the Folium map with custom Mapbox basemap and add markers
    # ========================================================================
    print("\n[4/4] Creating interactive map with Folium...")
    
    # Build the Mapbox tile URL for our custom basemap
    # This URL tells Folium how to fetch the map tiles from Mapbox
    # {z} = zoom level, {x} = x coordinate, {y} = y coordinate (filled in by Folium)
    tiles = f'https://api.mapbox.com/styles/v1/{style_username}/{style_id}/tiles/256/{{z}}/{{x}}/{{y}}@2x?access_token={access_token}'
    
    # Create the Folium map object
    m = folium.Map(
        location=[center_lat, center_lon],  # Where to center the map
        zoom_start=12,  # Initial zoom level (1=world, 20=building level)
        tiles=tiles,  # URL to our custom Mapbox basemap
        attr='Mapbox'  # Attribution text
    )
    
    # Add a marker for each location in our cleaned DataFrame
    for idx, row in df_clean.iterrows():
        # Get the appropriate marker color for this location's type
        color = get_marker_color(row['Type'])
        
        # Create the HTML content for the popup window
        popup_html = create_popup_html(
            row['Name'],
            row['Description'],
            row['Image_URL']
        )
        
        # Create and add the marker to the map
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],  # Where to place the marker
            popup=folium.Popup(popup_html, max_width=320),  # Popup content and width
            tooltip=row['Name'],  # Text shown when hovering over marker
            icon=folium.Icon(color=color, icon='info-sign')  # Marker color and icon
        ).add_to(m)  # Add this marker to our map
        
        # Print confirmation for each marker added
        print(f"  ✓ Added marker: {row['Name']} ({row['Type']}) - {color}")
    
    # ========================================================================
    # Add a legend to the map showing what each color represents
    # Goal: Help users understand the color-coding of markers
    # ========================================================================
    
    # Create the HTML for the legend box
    # This uses inline CSS to position and style the legend
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; right: 50px; width: 180px; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size:14px; padding: 10px; border-radius: 5px;
                box-shadow: 2px 2px 6px rgba(0,0,0,0.3);">
        <h4 style="margin-top:0;">Location Types</h4>
    '''
    
    # Get all unique location types that exist in our data
    types_in_data = df_clean['Type'].unique()
    
    # Add each type to the legend with its corresponding color
    for loc_type in sorted(types_in_data):
        # Get the color for this location type
        color = get_marker_color(loc_type)
        # Add a colored circle and the type name to the legend
        legend_html += f'<p><span style="color:{color};">⬤</span> {loc_type}</p>'
    
    # Close the legend HTML div
    legend_html += '</div>'
    
    # Add the legend to the map as an HTML element
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # ========================================================================
    # Save the map to an HTML file
    # Goal: Create a standalone HTML file that can be opened in a browser
    # ========================================================================
    
    # Save the map object to an HTML file
    m.save(output_file)
    
    # Print success message
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
