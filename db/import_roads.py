import json
import mysql.connector  # Using mysql.connector for MySQL/MariaDB

def read_and_write_coordinates(json_file, db_name, db_user, db_password, db_host, db_port):
  """
  This function reads a JSON file containing coordinates and writes them as a text field to a database.

  Args:
      json_file (str): Path to the JSON file containing coordinates.
      db_name (str): Name of the database.
      db_user (str): Username for the database.
      db_password (str): Password for the database.
      db_host (str): Hostname or IP address of the database server.
      db_port (int): Port number of the database server.
  """

  # Connect to the database
  conn = mysql.connector.connect(
      database=db_name, user=db_user, password=db_password, host=db_host, port=db_port
  )
  cur = conn.cursor()

  # Open the JSON file
  with open(json_file, 'r') as f:
    data = json.load(f)

  # Extract coordinates from the JSON data
  features = data.get('features', [])
  if not features:
      print("Error: 'features' key not found in JSON file.")
      return

  # Check if each feature has a LineString geometry
  for feature in features:
    geometry = feature.get('geometry')
    if not geometry or geometry['type'] != 'LineString':
      print(f"Warning: Skipping feature with invalid geometry type.")
      continue

    coordinates = geometry.get('coordinates')
    if not coordinates:
      print(f"Warning: Skipping feature with missing coordinates.")
      continue

    # Convert coordinates to JSON string
    coord_data = json.dumps(coordinates)

    # Prepare SQL statement (assuming you have a table named 'coordinates' with a text column 'coordinates_data')
    sql = "INSERT INTO roads (coordinates) VALUES (%s)"
    print(coord_data)

    # Insert coordinates into the database
    cur.execute(sql, (coord_data,))

  # Save changes to the database
  conn.commit()

  # Close the connection
  cur.close()
  conn.close()

  print("Coordinates successfully written to the database.")

# Replace with your actual values
json_file = "./roads.json"
db_name = "tpo25"
db_user = "kurir"
db_password = "kurir"
db_host = "localhost"
db_port = 3306  # Default port for MySQL/MariaDB

read_and_write_coordinates(json_file, db_name, db_user, db_password, db_host, db_port)
