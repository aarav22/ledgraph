import json 
from PIL import ImageColor

with open('pranav-3.json') as f:
    data = json.load(f)
    # convert each key to a new json file with the key_version.json name
    for key in data:
        curr_data = data[key]
        new_data = []
        # for each hex value in curr data convert it to [R, G, B] value:
        for hex_code in curr_data:
            rgb_vals = ImageColor.getcolor(hex_code, "RGB")
            # convert the tupple to a list:
            rgb_vals = [rgb_vals[0], rgb_vals[1], rgb_vals[2]]
            new_data.append(rgb_vals)
        with open(key + '_version.json', 'w') as f:
            json.dump(new_data, f)