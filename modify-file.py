# modify test.json

import json 
import numpy as np

# with open('original.json') as f:
#     curr_data = np.array(json.load(f))    
#     # update test.json with curr_data
#     with open('test.json', 'w') as f:
#         json.dump(curr_data.tolist(), f)
        
# with open('test.json') as f:
#     curr_data = np.array(json.load(f))
#     curr_data[0][0] = 0
#     # do this for all curr_data
#     for i in range(len(curr_data)):
#         curr_data[i][0] = 0
#     with open('test.json', 'w') as f:
#         json.dump(curr_data.tolist(), f)

counter = 0
while 1:
    for i in range(1, 21):
        with open(f'{i}_version.json') as f:
            curr_data = np.array(json.load(f))
            with open('test.json', 'w') as f:
                json.dump(curr_data.tolist(), f)
        while counter < 1000000:
            counter += 1
        counter = 0

    
