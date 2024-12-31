import requests
import json

headers = {
    'tracestate': '6126119@nr=0-1-6126119-1386228222-aa796806bb871c9a----1735576321911',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.purplle.com/search?q=Lip',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'is_SSR': 'false',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjYxMjYxMTkiLCJhcCI6IjEzODYyMjgyMjIiLCJpZCI6ImFhNzk2ODA2YmI4NzFjOWEiLCJ0ciI6IjllZWFhZjdkNjZlMWM2ZmFhOGMxOWRhN2M3MGI2MGI4IiwidGkiOjE3MzU1NzYzMjE5MTF9fQ==',
    'sec-ch-ua-mobile': '?0',
    'traceparent': '00-9eeaaf7d66e1c6faa8c19da7c70b60b8-aa796806bb871c9a-01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiI3REVRUmhoZTZNSUc5UGZBckEiLCJtb2RlX2RldmljZSI6ImRlc2t0b3AiLCJtb2RlX2RldmljZV90eXBlIjoid2ViIiwiaWF0IjoxNzM1MDg0ODI1LCJleHAiOjE3NDI4NjA4MjUsImF1ZCI6IndlYiIsImlzcyI6InRva2VubWljcm9zZXJ2aWNlIn0.NCbbHyT1nsdyl2QnJGrq85BWfhYrxIUMey0P5ViEWK4',
    'visitorppl': '7DEQRhhe6MIG9PfArA',
    'mode_device': 'desktop',
}

params = {
    'tenant': 'PURPLLE_COM',
    'sub_tenant': 'MAIN_SITE',
    'pincode': '380008',
    'userType': '0',
    'list_type': 'search',
    'list_type_value': 'lip',
    'page': '1',
    'sort_by': 'rel',
    'elite': '0',
    'mode_device': 'desktop',
    'ab_experiment_listing': 'c',
    'identifier': '7DEQRhhe6MIG9PfArA',
}




response = requests.get('https://www.purplle.com/neo/merch/items/v2', params=params, headers=headers)
print(response)
p_count=1
for page in range(1,50):
    params['page']=page
    print(f"page_no{params['page']}")
    response = requests.get('https://www.purplle.com/neo/merch/items/v2', params=params, headers=headers)
    if response.status_code==200:
     print(f"status_code {response.status_code}")
    json_data=response.json()
    data=json_data['items']
   
    for product in data:
        p_count+=1
        name=product['name']
        print(p_count)
        print(name)

# page = 0
# p_count=0
# while True:
#         params['page'] = str(page)
#         print(f"Fetching page {page}...")
#         print(f"Fetching page {params['page']}...")
        
#         # Send the request
#         response = requests.get('https://www.purplle.com/neo/merch/items/v2', headers=headers, params=params)
        
        
#         if response.status_code != 200:
#             print(f"Error: Received status code {response.status_code}")
#             break
        
#         # Parse the JSON response
#         json_data = response.json()
#         data=json_data['items']
#         for product in data:
#                 p_count+=1
#                 name=product['name']
#                 print(p_count)
#                 print(name)

#                 # print(data)
        
#         # Check if there is data in the response
#         # if not json_data.get('items'):  # Adjust the key based on the actual response structure
#         #     print("No more data to fetch.")
#         #     break
        
#         # Process or save the data
#         # print(json.dumps(data, indent=2))  # Replace this with your processing logic
        
#         # Increment the page number
#         page += 1

# # Run the function


