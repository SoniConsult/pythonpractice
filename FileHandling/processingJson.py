import json
from collections import defaultdict



def processing_json(filePath,required_fields):
    total_entries = 0
    valid_entries = 0
    invalid_entries = 0
    missing_fields = defaultdict(int)

    try:
        with open('./FileHandling/data.json', 'r') as file:
            data = json.load(file)
        for entry in data:
            total_entries += 1
            missing_in_entry = []
            for field in required_fields:
                if field not in entry:
                    missing_in_entry.append(field)
                    missing_fields[field] += 1
            if missing_in_entry:
                invalid_entries += 1
            else:
                valid_entries += 1
        summary = {
            "total_entries": total_entries,
            "valid_entries": valid_entries,
            "invalid_entries": invalid_entries,
            "missing_fields": dict(missing_fields) 
        }

        return summary

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format. {e}")
        return None
    except FileNotFoundError as e:
        print(f"Error: File not found. {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None




path='./FileHandling/data.json'
def main():
    report = processing_json(path,['name','email'])
    print(report)

if __name__== "__main__":
    main()
