import json
import os

def split_categories():
    # Read the original places.json
    with open('places.json', 'r') as f:
        data = json.load(f)
    
    # Create categories directory if it doesn't exist
    if not os.path.exists('categories'):
        os.makedirs('categories')
    
    # Group places by category
    categories = {}
    for place in data['places']:
        category = place['category'].lower().replace(' ', '_')
        if category not in categories:
            categories[category] = {
                'color': data['categories'][place['category']],
                'places': []
            }
        # Remove the category field from the place
        place_copy = place.copy()
        del place_copy['category']
        categories[category]['places'].append(place_copy)
    
    # Write separate JSON files
    for category, category_data in categories.items():
        filename = f'categories/{category}.json'
        with open(filename, 'w') as f:  # Removed indent parameter from open()
            json.dump(category_data, f, indent=4)  # Added indent parameter to json.dump()
        print(f'Created {filename}')

if __name__ == '__main__':
    split_categories()