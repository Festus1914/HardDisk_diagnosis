import json
from disk_info import get_disk_info
from smart_data import get_smart_data, parse_smart_data

def diagnose_harddisk():
    disk_info = get_disk_info()
    device = 'PhysicalDrive0'
    raw_smart_data = get_smart_data(device)
    smart_attributes = parse_smart_data(raw_smart_data)

    diagnosis = {
        'disk_info': disk_info,
        'smart_attributes': smart_attributes
    }

    return diagnosis

if __name__ == "__main__":
    diagnosis = diagnose_harddisk()
    print(json.dumps(diagnosis, indent=4))
