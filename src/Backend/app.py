from flask import Flask
import mysql.connector
from mysql.connector import Error
import time

app = Flask(__name__)

def test_db_connection(retries=10, delay=5):
    for attempt in range(retries):
        try:
            connection = mysql.connector.connect(
                host='mysql',  # Must match the docker-compose service name
                user='root',
                password='Awilo9701@',
                database='carrushdb'
            )

            if connection.is_connected():
                print("✅ Connected to MySQL database")
                connection.close()
                return True
        except Error as e:
            print(f"⏳ Attempt {attempt + 1}: MySQL connection failed: {e}")
            time.sleep(delay)

    print("❌ Could not connect to MySQL after several attempts.")
    return False

@app.route('/')
def home():
    return 'Hello, CarRush backend is running!'

if __name__ == '__main__':
    if test_db_connection():
        app.run(host='0.0.0.0', port=5000)
    else:
        print("❌ Could not start Flask app due to DB issue.")

