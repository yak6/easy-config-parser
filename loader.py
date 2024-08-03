def load(valname, path):
    true_booleans = ["yes", "true"]
    false_booleans = ["no", "false"]
    with open(path, "r", encoding="utf-8") as file: 
        lines = [line.strip() for line in file]
    for line in lines:
        loaded_name = line.split(':', 1)[0]
        value = line.split('=', 1)[1]
        b = line.split('=', 1)[0]
        type = b.split(':', 1)[1]
        if valname == loaded_name:
            if type == "integer":
                return int(value)
            elif type == "float":
                return float(value)
            elif type == "boolean":
                value = value.lower()
                if value in [item.lower() for item in true_booleans]:
                    return True
                elif value in [item.lower() for item in false_booleans]:
                    return False
            elif type == "string":
                return str(value)
            else:
                print("Unknown data type: '{}'".format(type))
def get_type(valname, path):
    with open(path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file]
    for line in lines:
        if ':' in line and '=' in line:
            loaded_name, rest = line.split(':', 1)
            if valname == loaded_name:
                type = rest.split('=', 1)[0]
                return type
    return None

def replace(valname, new_value, path):
    def index_replace(my_list, index, new_element):
        if index < 0 or index >= len(my_list):
            raise IndexError("Index out of range.")
        my_list[index] = new_element

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    current_type = get_type(valname, path)
    if current_type is None:
        print(f"Value name '{valname}' not found.")
        return
    if current_type == "integer":
        new_value = int(new_value)
    elif current_type == "float":
        new_value = float(new_value)
    elif current_type == "boolean":
        new_value = new_value.lower()
        if new_value in ["yes", "true"]:
            new_value = "yes"
        elif new_value in ["no", "false"]:
            new_value = "no"
        else:
            print("Invalid boolean value.")
            return
    elif current_type == "string":
        new_value = str(new_value)
    else:
        print(f"Unknown data type: '{current_type}'")
        return
    new_lines = []
    found = False
    for line in lines:
        if ':' in line and '=' in line:
            loaded_name, rest = line.split(':', 1)
            if valname == loaded_name:
                new_lines.append(f"{valname}:{current_type}={new_value}\n")
                found = True
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if not found:
        new_lines.append(f"{valname}:{current_type}={new_value}\n")
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(new_lines)
