import json
import os
from pathlib import Path

### this combines the individual category JSON files into a single places.json file for reference. 


def combine_categories():
    # Initialize the combined data structure
    combined_data = {
        "categories": {},
        "places": []
    }
    
    # Get all JSON files from the categories directory (relative to project root)
    base_dir = Path(__file__).resolve().parent.parent
    category_dir = base_dir / "categories"
    if not category_dir.exists():
        print("Categories directory not found!")
        return
    
    # Process each category file
    for category_file in category_dir.glob("*.json"):
        try:
            with open(category_file, 'r') as f:
                data = json.load(f)
                
            # Get category name from filename
            category_name = category_file.stem.title().replace('_', ' ')
            
            # Add category color to combined data
            combined_data["categories"][category_name] = data["color"]
            
            # Add places with category field
            for place in data["places"]:
                place_copy = place.copy()
                place_copy["category"] = category_name
                combined_data["places"].append(place_copy)
                
            print(f"Processed {category_file.name}: {len(data['places'])} places")
            
        except json.JSONDecodeError as e:
            print(f"Error reading {category_file.name}: {str(e)}")
        except KeyError as e:
            print(f"Missing key in {category_file.name}: {str(e)}")
    
    # Write combined data to places.json in the project root
    try:
        places_path = base_dir / 'places.json'
        with open(places_path, 'w') as f:
            json.dump(combined_data, f, indent=4)
        print(f"\nCreated places.json with:")
        print(f"- {len(combined_data['categories'])} categories")
        print(f"- {len(combined_data['places'])} total places")
    except Exception as e:
        print(f"Error writing places.json: {str(e)}")

if __name__ == "__main__":
    combine_categories()