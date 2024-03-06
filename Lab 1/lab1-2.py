import arcpy
from flask import Flask, jsonify 
import psycopg2
from psycopg2 import sql

app = Flask(__name__)


with open(r"\\Mac\Home\Documents\GitHub\GIS5572\secure\database.txt", 'r') as file:
    database_key = file.read().strip()
    
#Connect to Database and Extract Geometry
@app.route('/geojson_polygon')
def get_geojson():
    conn = psycopg2.connect(
        dbname=dbname,
        user=dbuser,
        password=dbpass, #Should be database_key if not connecting to local 
        host= dbhost,
        port="5432"
        )
    
    cur = conn.cursor()

    query = """
        SELECT ST_AsGeoJSON(shape) AS geojson
        FROM lab1
    """
    cur.execute(query)
    geojson_data = cur.fetchone()[0]
    curr.close()
    conn.close()

    #Puts the wkt in the GeomFromText 
    # Return the GeoJSON data
    return jsonify(geojson_data)

if __name__ == '__main__':
    app.run(debug=False)
