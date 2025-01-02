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


#============================================update ========================================
#============code
import os

import requests
import json
import mysql.connector
from urllib.parse import urljoin  # Correctly join the URLs

from parsel import Selector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    # database ="scrap_data"

)
cursor = conn.cursor()
# Create table if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS scrap_data")
cursor.execute("USE scrap_data")
cursor.execute("DROP TABLE IF  EXISTS scrap_data")
cursor.execute("""
CREATE TABLE IF NOT EXISTS  product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT,
    image_data LONGBLOB NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    offerPrice DECIMAL(10, 2) NOT NULL,
    rating_avg DECIMAL(10, 2) NOT NULL,
    discount DECIMAL(10, 2) NOT NULL,
    ratingCount DECIMAL(10, 2) NOT NULL,
    stock_status INTEGER NOT NULL,
    product_details_url TEXT
)
""")


headers = {
    'tracestate': '6126119@nr=0-1-6126119-1386228222-3d7d86ed6044b973----1735281875081',
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.purplle.com/search?q=Lip',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'is_SSR': 'false',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjYxMjYxMTkiLCJhcCI6IjEzODYyMjgyMjIiLCJpZCI6IjNkN2Q4NmVkNjA0NGI5NzMiLCJ0ciI6IjdlODkzOWVkYTZhZGNhNzdkMmE5Zjk0YjJlYmJkZGRmIiwidGkiOjE3MzUyODE4NzUwODF9fQ==',
    'sec-ch-ua-mobile': '?0',
    'traceparent': '00-7e8939eda6adca77d2a9f94b2ebbdddf-3d7d86ed6044b973-01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJmbVBnOHFqM3pVWEJPOHh0RFkiLCJtb2RlX2RldmljZSI6ImRlc2t0b3AiLCJtb2RlX2RldmljZV90eXBlIjoid2ViIiwiaWF0IjoxNzM1MTg4MDE2LCJleHAiOjE3NDI5NjQwMTYsImF1ZCI6IndlYiIsImlzcyI6InRva2VubWljcm9zZXJ2aWNlIn0.mSHY8QgWLdqSbrYJVptB2hn1wPofkx8vqm8bKfWHlMk',
    'visitorppl': 'fmPg8qj3zUXBO8xtDY',
    'mode_device': 'desktop',
}

params = {
    'tenant': 'PURPLLE_COM',
    'sub_tenant': 'MAIN_SITE',
    'pincode': '380001',
    'userType': '0',
    'list_type': 'search',
    'list_type_value': 'lip',
    'page': '1',
    'sort_by': 'rel',
    'elite': '0',
    'mode_device': 'desktop',
    'ab_experiment_listing': 'c',
    'identifier': 'fmPg8qj3zUXBO8xtDY',
}



base_url='https://www.purplle.com/neo/merch/items/v2'


page = 1 #page count
p_count=0 #product count
product_search= input("Enter  Item::")
params['list_type_value']= product_search

while True:

        # params['list_type_value']='Shmpoo'
        # params['list_type_value']='lip'
        # params['list_type_value']='makupkit '
        params['page'] = str(page)
        print(f"Fetch page {params['page']}...")

        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error: status code {response.status_code}")
            break
            #parse data

        json_data = response.json()
        data=json_data['items']

        for product in data:
                product_urls=product['type']
                p_count+=1
                name=product['name']

                image_data = product['thumb_image_url']
                price= product['price']
                offerPrice = product['our_price']
                rating_avg = product['data_socialaction']['rating_avg']
                rating_Count = product['data_socialaction']['rating_count']
                discount=product['discount']
                stock_status=product ['stock_status']
                product_id=product['id']
                product_url = product['url']
                product_details_url  = f'https://www.purplle.com/product/{product_url}'

           



                #     htmtl_text=response1.text
                #     response_selector=Selector(text=htmtl_text) # convert response to text
                #     dese =  response_selector.xpath('//script[@ type="application/json"]//text()').get()   #discrip
                #     # j_data=response_selector.xpath('//script[@ type="application/json"]//text()').get()
                #     json_load=json.loads(dese)
                #     desc=json_load['description']
                #     print(desc)

                print(p_count)
                print(f'Pname ={name}')
                print(f'price ={price}')
                print(f'img = {image_data}')
                print(f'offerPrice={offerPrice}')
                print(f'rating_avg= {rating_avg}')
                print(f'rating_Count {rating_Count}')
                print(f'discount = {discount}')
                print(f'stock_status = {stock_status}')
                print(f'url = {product_url}')
                print(f'product_details_url = {product_details_url}')

                # with open("response.json", "w") as json_file:
                #     json.dump(data, json_file,)


                dir = f""

                file_data = dir + str("Product" + '_' + f'{str(page)}') + ".json"
                res_data_json = f"D:\\json_data\\JSON\\product_data\\{file_data}"

                #  directory exists
                os.makedirs(os.path.dirname(res_data_json), exist_ok=True)

                if os.path.exists(res_data_json):
                    with open(res_data_json, 'r', encoding='utf-8') as file:
                        data_from_page = file.read()
                        data = data_from_page

                else:
                    with open(res_data_json, 'w', encoding='utf-8') as file:
                        file.write(response.text)
                        data = response.text
                    print(f"Page saved {page}!")

                sql = """
                                     INSERT INTO product (name,image_data, price, offerPrice,rating_avg,discount, ratingCount, stock_status,product_details_url)
                                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                 """
                values = (name,image_data, price, offerPrice, rating_avg, discount, rating_Count,stock_status,product_details_url)
                cursor.execute(sql, values)
                conn.commit()
                print(f"Inserted  page {page}")

        page += 1




