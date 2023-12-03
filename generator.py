from faker import Faker
import random
from datetime import datetime, timedelta
import psycopg2

# Connect to your PostgreSQL database
connection = psycopg2.connect(
    dbname="weather",
    user="postgres",
    password="postgres-pass",
    host="91.185.84.92",
    port="5000"
)

cursor = connection.cursor()

fake = Faker()

# Function to generate random data for the cities table
def generate_cities_data(num_cities):
    cities_data = []
    for _ in range(num_cities):
        city_name = fake.city()
        cities_data.append((city_name,))
    return cities_data

# Function to generate random data for the forecast table
def generate_forecast_data(num_forecasts, num_cities):
    forecast_data = []
    for _ in range(num_forecasts):
        city_id = random.randint(1, num_cities)
        date_time = int((datetime.now() + timedelta(days=random.randint(1, 365))).timestamp())
        temperature = random.randint(-20, 40)
        summary = fake.text()
        forecast_data.append((city_id, date_time, temperature, summary))
    return forecast_data

try:
    print("Clean up")
    cursor.execute("truncate public.cities RESTART IDENTITY CASCADE; ")
    cursor.execute("truncate public.forecast RESTART IDENTITY CASCADE;")

    # Number of cities and forecasts to generate
    num_cities_to_generate = 50
    num_forecasts_to_generate = 150

    # Generate data for cities and forecast tables
    cities_data = generate_cities_data(num_cities_to_generate)
    forecast_data = generate_forecast_data(num_forecasts_to_generate, num_cities_to_generate)

    # Insert data into the cities table
    cursor.executemany("INSERT INTO public.cities (name) VALUES (%s);", cities_data)

    # Insert data into the forecast table
    cursor.executemany("INSERT INTO public.forecast (\"cityId\", \"dateTime\", temperature, summary) VALUES (%s, %s, %s, %s);", forecast_data)

    # Commit the changes
    connection.commit()

    print("Data inserted successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the database connection
    cursor.close()
    connection.close()