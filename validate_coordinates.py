import json

def validate_coordinates():
    with open('places.json', 'r') as f:
        data = json.load(f)
    
    for place in data['places']:
        if 'lat' not in place or 'lng' not in place:
            print(f"❌ Missing coordinates for: {place['name']}")
            continue
            
        if not isinstance(place['lat'], (int, float)) or not isinstance(place['lng'], (int, float)):
            print(f"❌ Invalid coordinate type for: {place['name']}")
            print(f"   lat: {type(place['lat'])}, lng: {type(place['lng'])}")
            continue
            
        if not (-90 <= place['lat'] <= 90) or not (-180 <= place['lng'] <= 180):
            print(f"❌ Coordinates out of range for: {place['name']}")
            print(f"   lat: {place['lat']}, lng: {place['lng']}")
            continue
            
        print(f"✓ Valid coordinates for: {place['name']}")

if __name__ == "__main__":
    validate_coordinates()