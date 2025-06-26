import json
import os
from pathlib import Path

def validate_json_files():
    category_dir = Path("categories")
    if not category_dir.exists():
        print("Categories directory not found!")
        return

    for json_file in category_dir.glob("*.json"):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                print(f"✓ {json_file.name} is valid JSON")
                print(f"  Contains {len(data['places'])} places")
        except json.JSONDecodeError as e:
            print(f"✗ Error in {json_file.name}: {str(e)}")
        except KeyError as e:
            print(f"✗ Missing key in {json_file.name}: {str(e)}")

if __name__ == "__main__":
    validate_json_files()