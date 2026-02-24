# Lab 06: Custom Basemap Design & Interactive Hometown Map

## Files Created

I've set up the following files for your Lab 06:

- ✅ **lab06.html** - Portfolio page structure (needs your content)
- ✅ **hometown_locations.csv** - Sample CSV with Fort Worth locations (customize with your hometown)
- ✅ **hometown_map.py** - Python script for generating the interactive map (needs your Mapbox credentials)

## Next Steps to Complete the Lab

### Part 1: Create Your Custom Mapbox Basemap

1. **Create a Mapbox Account**
   - Go to [studio.mapbox.com](https://studio.mapbox.com/)
   - Sign up using your TCU email address

2. **Choose Your Design Inspiration**
   - Pick art, film, TV show, or any visual inspiration
   - Save reference images - you'll need them for your reflection

3. **Create Your Custom Style**
   - Click "New style" → Select "Blank" template
   - Add and customize these required components:
     - Land, water & sky
     - Road network
     - Place labels
     - POI labels
     - Terrain component
     - At least 12 individually styled layers total
   - Use "Style across zoom range" for different zoom levels

4. **Publish and Get Your Style URL**
   - Click "Publish" to save your style
   - Click "Share" → Make it "Public"
   - Copy your Style URL: `mapbox://styles/username/style_id`
   - **SAVE THIS!** You'll need it for Part 3

5. **Get Your Access Token**
   - Click your account → Access tokens
   - Copy your default public token (starts with `pk.`)
   - **SAVE THIS TOO!**

### Part 2: Customize Your Hometown Locations

1. **Edit hometown_locations.csv**
   - Currently has Fort Worth sample data
   - Replace with YOUR hometown locations (at least 10)
   - Include at least 3 different types (Restaurant, Park, Cultural, etc.)
   - Add personal descriptions (2-3 sentences each)
   - Find image URLs for each location

2. **CSV Format**
   ```
   Name,Address,Type,Description,Image_URL
   "Location Name","Full Street Address","Category","Why it's meaningful to you","https://..."
   ```

### Part 3: Run the Python Script

1. **Install Required Libraries**
   ```bash
   pip install folium pandas requests
   ```

2. **Update hometown_map.py**
   - Line 20: Replace `YOUR_MAPBOX_ACCESS_TOKEN_HERE` with your token
   - Line 24: Replace `YOUR_USERNAME/YOUR_STYLE_ID` with your style URL

3. **Run the Script**
   ```bash
   python hometown_map.py
   ```

4. **Check Output**
   - The script will create `hometown_map.html`
   - Open it in a browser to verify it works
   - Your custom basemap should be visible

### Part 4: Complete lab06.html

Edit [lab06.html](lab06.html) and replace all TODO sections:

1. **Part 1: Custom Basemap Section**
   - Describe your design inspiration
   - Add reference images (save to `images/` folder)
   - Add screenshot of your Mapbox basemap
   - Explain your scale-aware design choices

2. **Part 2: Dataset Section**
   - Describe your hometown
   - Explain why you chose these locations

3. **Part 3: Interactive Map Section**
   - The map should embed automatically via iframe
   - Verify the iframe src points to `hometown_map.html`

4. **Reflection Section** (250-500 words total)
   - **Design Inspiration:** How did your inspiration influence your map?
   - **Cartographic Challenges:** What was hard about designing for multiple scales?
   - **Technical Challenges:** What coding issues did you face? How did AI help?

5. **Self-Assessment Section**
   - Answer each of the 5 questions honestly
   - This shows critical self-reflection

### Part 5: Add Images

Create an `images/` folder if it doesn't exist and add:
- Reference images from your design inspiration
- Screenshot of your Mapbox basemap at different zoom levels
- Any other relevant images

## Checklist Before Submission

- [ ] Mapbox basemap created with 12+ styled layers
- [ ] hometown_locations.csv has YOUR hometown (10+ locations)
- [ ] hometown_map.py has your Mapbox credentials
- [ ] hometown_map.html generated and displays correctly
- [ ] lab06.html has all TODO sections completed
- [ ] Images added to images/ folder
- [ ] Written reflection is 250-500 words
- [ ] Self-assessment completed
- [ ] Navigation links work on all portfolio pages

## Files to Submit to D2L

1. hometown_locations.csv
2. hometown_map.py
3. hometown_map.html

## Common Issues & Solutions

**Map shows default basemap instead of my custom one:**
- Check that your style URL is correct in hometown_map.py
- Verify your style is set to "Public" in Mapbox Studio
- Make sure access token is correct

**Geocoding fails:**
- Check that addresses in CSV are complete and accurate
- Verify your Mapbox access token is valid
- Check your internet connection (API calls need internet)

**Pop-ups don't show images:**
- Verify image URLs are valid and publicly accessible
- Check that Image_URL column in CSV has proper URLs

**Script won't run:**
- Make sure you installed all required libraries
- Check Python version (3.7+ recommended)
- Verify CSV file is in the same directory as the script

## Resources

- [Mapbox Studio Manual](https://docs.mapbox.com/studio-manual/)
- [Mapbox Geocoding API](https://docs.mapbox.com/api/search/geocoding/)
- [Folium Documentation](https://python-visualization.github.io/folium/)
- [Unsplash](https://unsplash.com/) - Free images for your locations

## Need Help?

The Python script includes detailed error messages and will guide you if:
- Mapbox credentials are missing
- CSV file has issues  
- Geocoding fails

Good luck! 🗺️
