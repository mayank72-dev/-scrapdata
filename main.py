import requests
from lxml import html
import mysql.connector
from urllib.parse import urljoin  # Correctly join the URLs
from scrapy.selector import Selector  # Use the correct Selector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="admin123",  # Replace with your MySQL password
    # database="quotes_data"  # Make sure you select the correct database
)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS quotesdata")
cursor.execute("USE quotesdata")
cursor.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT,
    author VARCHAR(255),
    tags TEXT,
    description TEXT,
    birth_date TEXT,
    place TEXT
)
""")

base_url = "https://quotes.toscrape.com/"
page = 1
count_data=1
while True:
    
    # Fetch the webpage for the current page number
    response = requests.get(f"{base_url}page/{page}/")

    if response.status_code == 200:
        print(f"Process page {page}, status code {response.status_code}")
        select = Selector(text=response.text)
        quotes = select.xpath(".//div[@class='quote']")

        for quote in quotes:
            count_data+=1
            # Extract quote details
            text = quote.xpath(".//span[@class='text']/text()").get()
            author = quote.xpath(".//small[@class='author']/text()").get()
            taglist = quote.xpath(".//a[@class='tag']/text()").getall()
            tags = ', '.join(taglist)
            print(text)
            print(author)
            print(tags)
            print(count_data)

            
            about_links = quote.xpath(".//span/small[@class='author']/following-sibling::a/@href").get()

         
            about_pg_url = urljoin(base_url, about_links)

            about_response = requests.get(about_pg_url)

            if about_response.status_code == 200:
                select1 = Selector(text=about_response.text)

                description = select1.xpath("//div[@class='author-description']//text()").get()
                

                birth_date = select1.xpath("//span[@class='author-born-date']//text()").get()
                place = select1.xpath("//span[@class='author-born-location']//text()").get()
                print(description)
                print(place)
                print(birth_date)

            else:
                description, birth_date, place = None, None, None

            # Insert into database
            sql = """
                INSERT INTO quotes (title, author, tags, description, birth_date, place)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (text, author, tags, description, birth_date, place)
            cursor.execute(sql, values)

        conn.commit()
        print(f"Inserted {count_data} rows from page {page}")

        
        next_page_link = select.xpath("//li[@class='next']/a/@href").get()
        if not next_page_link:
            break  
        page += 1
        count_data+=1  

    else:
        print(f"Failed to fetch page {page}. Status code: {response.status_code}")
        break

# Close the database connection
cursor.close()
conn.close()
