import os
from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

app = Flask(__name__)

# Database connection parameters
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

# Endpoint to fetch data from PostgreSQL
print("USER:", os.getenv('DB_USER'))


@app.route('/teams', methods=['GET'])
def get_teams():
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        # Execute a query
        cursor.execute("SELECT * FROM teams")
        rows = cursor.fetchall()

        # Close the connection
        cursor.close()
        connection.close()

        # Return data as JSON
        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/plays/offense', methods=['GET'])
def get_off_plays():
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        # Execute a query
        cursor.execute("SELECT * FROM offense_plays")
        rows = cursor.fetchall()
        print(rows)

        # Close the connection
        cursor.close()
        connection.close()

        # Return data as JSON
        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/plays/defense', methods=['GET'])
def get_def_plays():
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        # Execute a query
        cursor.execute("SELECT * FROM defense_plays")
        rows = cursor.fetchall()
        print(rows)

        # Close the connection
        cursor.close()
        connection.close()

        # Return data as JSON
        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
