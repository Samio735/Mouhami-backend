import json
import random
import mysql.connector
from bs4 import BeautifulSoup
import re
import requests

#------------------------------------round1--------------------------#
base_url = "https://avocatalgerien.com/listings/page/"
num_pages = 72

cabinets_data = []

for page_num in range(1, num_pages + 1):
    print("\n\n\n\n page", page_num)
    url = f"{base_url}{page_num}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        entry_titles = soup.find_all('h2', class_='entry-title')

        for title in entry_titles:
            entry_url = title.find('a')['href'].strip()
            print("\n\n\n\n---the information---")
            response = requests.get(entry_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                name = soup.find("h1", class_="entry-title").text.strip()
                location = soup.find("li", class_="address").text.strip()
                telephone = soup.find("li", class_="phone").find("span").text.strip()
                image_url = soup.find("div", class_="larger").find("img")["src"]

                categories = [category.text.strip() for category in soup.find("p", class_="listing-cat").find_all("a")]

                reviews = soup.find("p", class_="reviews").text.strip()
                added_by = soup.find("span", class_="fn").text.strip()
                date_added = soup.find("div", class_="added").find("span", class_="date updated").text.strip()

                avis_section = soup.find("section", id="reviews")
                avis_content = avis_section.find("p").text.strip() if avis_section else "Avis section not found."

                hours_section = soup.find("section", id="hours")
                hours_content = hours_section.find("p").text.strip() if hours_section else "Heure D'ouverture section not found."

                email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text)
                email = email_match.group() if email_match else "Email not found."
                languages=['arabic','french','english']
                random_language_length = random.randint(1, 3)
                random_languages = random.sample(languages, random_language_length)
                cabinet_info = {
                    "user":None,
                    "name": name,
                    "location": location,
                    "phone": telephone,
                    "email": email.encode().decode('unicode_escape'),
                    "photo": image_url,
                    "specialities": categories,
                    "lng":None,
                    "lat":None,
                    "rating":None,
                    "languages":random_languages,
                     }

                cabinets_data.append(cabinet_info)

            else:
                print(f"Failed to retrieve the entry_url. Status code: {response.status_code}")

with open('cabinets.json', 'w', encoding='utf-8') as json_file:
    json.dump(cabinets_data, json_file, ensure_ascii=False, indent=4)

print("Data saved to cabinets.json.")




#------------------------------------round2--------------------------#
print("Now insertion in Database!!")



def connect_to_database():

    config = {
        'user': 'root',
        'password': '1234',
        'host': 'localhost',
        'database': 'muhami',
        'raise_on_warnings': True,
    }
    connection = mysql.connector.connect(**config)
    return connection

with open('cabinets.json', 'r', encoding='utf-8') as json_file:
    cabinets_data = json.load(json_file)
    

connection = connect_to_database()
cursor = connection.cursor()

for cabinet_info in cabinets_data:
    specialities_str = ', '.join(cabinet_info['specialities'])
    languages_str = ', '.join(cabinet_info['languages'])
    lng = cabinet_info.get('lng', None)  
    lat = cabinet_info.get('lat', None)  
    rating = cabinet_info.get('rating', None) 
    cursor.execute("""
        INSERT INTO Lawyer (name, location, phone, email, photo, lng, lat, rating)
        VALUES (%(name)s, %(location)s, %(phone)s, %(email)s, %(photo)s, %(lng)s, %(lat)s, %(rating)s)
    """, {'name': cabinet_info['name'], 'location': cabinet_info['location'], 'phone': cabinet_info['phone'],
          'email': cabinet_info['email'], 'photo': cabinet_info['photo'], 'lng': lng, 'lat': lat, 'rating': rating})
    lawyer_id = cursor.lastrowid





    for speciality in cabinet_info['specialities']:
        cursor.execute("SELECT specialities_id FROM Specialities WHERE name = %s", (speciality,))
        speciality_result = cursor.fetchone()
        if speciality_result:
            speciality_id = speciality_result[0]
            cursor.fetchall()
            cursor.execute("""
                INSERT INTO Lawyer_specialities (lawyer_id, specialities_id)
                VALUES (%s, %s)
            """, (lawyer_id, speciality_id))
            
        else:
            print(f"Speciality not found in the Specialities table: {speciality}")







    for language in cabinet_info['languages']:
        cursor.execute("SELECT language_id FROM Language WHERE name = %s", (language,))
        
        language_result = cursor.fetchone() 
        if language_result:
            language_id = language_result[0]
            print("lawer",lawyer_id)
            cursor.execute("""
                INSERT INTO Lawyer_languages (lawyer_id, languages_id)
                VALUES (%s, %s)
            """, (lawyer_id, language_id))
        else:
            print(f"Language not found in the Language table: {language}")




connection.commit()

cursor.close()
connection.close()

print("Data inserted in database successfully.")
