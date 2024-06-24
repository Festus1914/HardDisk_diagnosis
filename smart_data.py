import subprocess
import re

def get_smart_data(device, device_type='nvme'):
    """
    Retrieve raw S.M.A.R.T. data from a given device using the smartctl command.
    
    :param device: Device identifier, e.g., '//./PhysicalDrive0'
    :param device_type: Device type for smartctl, e.g., 'sat', 'scsi', 'nvme'
    :return: Raw output from smartctl command or an error message
    """
    try:
        result = subprocess.run(['smartctl', '-a', '-d', device_type, device], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running smartctl: {e}\nOutput: {e.output}\nError: {e.stderr}"
    except FileNotFoundError:
        return "smartctl not found. Please ensure it is installed and added to PATH."

def parse_smart_data(raw_data):
    """
    Parse the raw S.M.A.R.T. data to extract attributes.

    :param raw_data: Raw string output from the smartctl command
    :return: Dictionary of parsed S.M.A.R.T. attributes
    """
    attributes = {}
    lines = raw_data.split('\n')
    for line in lines:
        match = re.match(r'^\s*(\d+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)', line)
        if match:
            attr_id, attr_name, flag, value, worst, thresh, attr_type, updated, when_failed, raw_value = match.groups()
            attributes[attr_name] = {
                'id': attr_id,
                'flag': flag,
                'value': value,
                'worst': worst,
                'threshold': thresh,
                'type': attr_type,
                'updated': updated,
                'when_failed': when_failed,
                'raw_value': raw_value
            }
    return attributes

if __name__ == "__main__":
    device = '//./PhysicalDrive0'
    device_type = 'nvme'  
    raw_smart_data = get_smart_data(device, device_type)
    if raw_smart_data.startswith("Error"):
        print(raw_smart_data)
    else:
        smart_attributes = parse_smart_data(raw_smart_data)
        if smart_attributes:
            for attr, data in smart_attributes.items():
                print(f"{attr}: {data}")
        else:
            print("No SMART attributes found or unable to parse the data.")
