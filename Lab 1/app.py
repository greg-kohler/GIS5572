import os
from flask import Flask, jsonify 
import psycopg2
from psycopg2 import sql

#Name App
app = Flask(__name__)

#Define database credentials
dbname = ""
dbuser = ""
dbpass = ""
dbhost = ""
    
#Connect to Database and Extract Geometry 
#App Route defines url
@app.route('/geojson_polygon.geojson')
def get_geojson():
    conn = psycopg2.connect(
        dbname=dbname,
        user=dbuser,
        password=dbpass,
        host= dbhost,
        port="5432"
        )
    
    cur = conn.cursor()

    query = """
        SELECT 
            json_build_object(
                'type', 'FeatureCollection',
                'features', json_agg(
                    json_build_object(
                        'type', 'Feature',
                        'geometry', ST_AsGeoJSON(ST_SetSRID(shape, 4326))::json,
                        'properties', json_build_object()
                    )
                ),
                'crs', 
                json_build_object(
                    'type', 'name',
                    'properties', 
                    json_build_object(
                        'name', 'epsg:4326'
                    )
                )
            ) AS geojson
        FROM lab1
    """
    cur.execute(query)
    geojson_data = cur.fetchone()[0]
    cur.close()
    conn.close()

    #Puts the wkt in the GeomFromText 
    # Return the GeoJSON data
    return geojson_data

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
