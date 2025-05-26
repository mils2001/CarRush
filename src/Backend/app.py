from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# MySQL database connection
db = mysql.connector.connect(
    host="carrush-mysql",  # Use service/container name if using Docker
    user="root",
    password="Awilo9701@",
    database="carrushdb"
)
cursor = db.cursor(dictionary=True)


# ------------------ Cars ------------------

# GET all cars
@app.route("/cars", methods=["GET"])
def get_cars():
    cursor.execute("SELECT * FROM cars")
    cars = cursor.fetchall()
    return jsonify(cars), 200

# POST a new car
@app.route("/cars", methods=["POST"])
def add_car():
    data = request.json
    query = """
        INSERT INTO cars (make, model, year, price_per_day, available)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        data["make"],
        data["model"],
        data["year"],
        data["price_per_day"],
        data.get("available", True)
    )
    cursor.execute(query, values)
    db.commit()
    return jsonify({"message": "Car added successfully!"}), 201


# ------------------ Rentals ------------------

# GET all rentals
@app.route("/rentals", methods=["GET"])
def get_rentals():
    cursor.execute("SELECT * FROM rentals")
    rentals = cursor.fetchall()
    return jsonify(rentals), 200

# POST a new rental
@app.route("/rentals", methods=["POST"])
def create_rental():
    data = request.json
    query = """
        INSERT INTO rentals (user_id, car_id, start_date, end_date, total_cost)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        data["user_id"],
        data["car_id"],
        data["start_date"],
        data["end_date"],
        data["total_cost"]
    )
    cursor.execute(query, values)
    db.commit()
    return jsonify({"message": "Rental created successfully!"}), 201


# ------------------ Root ------------------

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the CarRush API!"})


# ------------------ Main ------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

