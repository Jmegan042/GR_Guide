import json
import requests
import time
import os
from pathlib import Path

def get_coordinates(address):
    time.sleep(1)  # Respect Nominatim's usage policy
    
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    
    headers = {
        "User-Agent": "GR_Guide/1.0"
    }
    
    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data:
            return {
                "lat": float(data[0]["lat"]),
                "lng": float(data[0]["lon"]),
                "display_address": data[0].get("display_name", "")
            }
        return None
    except Exception as e:
        print(f"Error geocoding {address}: {e}")
        return None

def get_address_from_coordinates(lat, lng):
    time.sleep(1)  # Respect Nominatim's usage policy
    
    base_url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lng,
        "format": "json"
    }
    
    headers = {
        "User-Agent": "GR_Guide/1.0"
    }
    
    try:
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("display_name", "")
    except Exception as e:
        print(f"Error reverse geocoding ({lat}, {lng}): {e}")
        return None

def update_category_files():
    # Get all category JSON files (relative to the script's parent directory)
    base_dir = Path(__file__).resolve().parent.parent
    category_dir = base_dir / "categories"
    if not category_dir.exists():
        print("Categories directory not found!")
        return
    
    for category_file in category_dir.glob("*.json"):
        print(f"\nProcessing {category_file.name}...")
        
        # Read category file
        with open(category_file, 'r') as f:
            data = json.load(f)
        
        # Process each place
        for place in data["places"]:
            print(f"\nChecking {place.get('name', '[Unnamed]')}...")
            
            # Case 1: No coordinates but has address
            if ("lat" not in place or "lng" not in place) and "address" in place:
                print(f"Looking up coordinates for {place.get('name', '[Unnamed]')}...")
                coords = get_coordinates(place["address"])
                if coords:
                    place["lat"] = coords["lat"]
                    place["lng"] = coords["lng"]
                    print(f"Found coordinates: ({coords['lat']}, {coords['lng']})")
            
            # Case 2: Has coordinates but no address
            elif "lat" in place and "lng" in place and "address" not in place:
                print(f"Looking up address for {place.get('name', '[Unnamed]')}...")
                address = get_address_from_coordinates(place["lat"], place["lng"])
                if address:
                    place["address"] = address
                    print(f"Found address: {address}")
        
        # Save updated category file
        with open(category_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Updated {category_file.name}")

if __name__ == "__main__":
    update_category_files()