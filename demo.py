import requests
import json
import time
from glob import glob
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0',
    'Accept-Language': 'en-US,en;q=0.8',
    'ApiJwtToken': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzNDM0MzQyMzI0IiwibmFtZSI6Ik1hcnRpbiBCdXJlcyIsImlhdCI6MjQyNDQzMzI0M30.MPq6DUA7EhVdaEi_mmGtDMPnem9l4bzvn4ZOOP39R-Q',
}

response = requests.get('https://www.avcrashes.net/api/accidents/'+str(813), headers=headers)



attempt = 900
'''
for i in range(attempt):

    response = requests.get('https://www.avcrashes.net/api/accidents/'+str(i), headers=headers)

    if response.status_code == 200:
        data = response.json()['accident']
        if len(data) == 1:
            data = data[0]

        # Serializing json
        json_object = json.dumps(data, indent=4)

        # Writing to sample.json
        with open(f"out_data/accident_{i}.json", "w") as outfile:
            outfile.write(json_object)

        pass
    time.sleep(0.5)
    pass
'''

for i in range(attempt):
    filepath = f"out_data/accident_{i}.json"
    if os.path.isfile(filepath):
        pass
    else:
        response = requests.get('https://www.avcrashes.net/api/accidents/'+str(i), headers=headers)
        if response.status_code == 200:
            data = response.json()['accident'][0]
            # Serializing json
            json_object = json.dumps(data, indent=4)

            # Writing to sample.json
            with open(f"out_data/accident_{i}.json", "w") as outfile:
                outfile.write(json_object)

        else:
            print(response.status_code, 'https://www.avcrashes.net/api/accidents/'+str(i))
        time.sleep(1)



