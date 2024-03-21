from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

database_key = 

DB_NAME = "gis5572"
DB_USER = "postgres"
DB_PASSWORD = database_key
DB_HOST = ""
DB_PORT = ""


# Route to retrieve polygon as GeoJSON
@app.route('/elev_kriging_point')
def elev_kriging_point():
    # Connect to the database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute SQL query to retrieve the polygon
    cur.execute("""SELECT
                    json_build_object(
                        'type', 'FeatureCollection',
                        'features', json_agg(
                            json_build_object(
                                'type', 'Feature',
                                'geometry', ST_AsGeoJSON(ST_Transform(ST_SetSRID(shape, 26915), 4326))::json,
                                'properties', json_build_object(
                                    'objectid', objectid,
                                    'pointid', pointid,
                                    'grid_code', grid_code
                                )
                            )
                        ),
                        'crs',
                        json_build_object(
                            'type', 'name',
                            'properties',
                            json_build_object(
                                'name', 'EPSG:4326'
                            )
                        )
                    ) AS geojson
                FROM elev_kriging_point;
                """)
    rows = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return rows


# Route to retrieve polygon as GeoJSON
@app.route('/Elev_Accur')
def elevation_accuracy():
    # Connect to the database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute SQL query to retrieve the polygon
    cur.execute("""SELECT
                    json_build_object(
                        'type', 'FeatureCollection',
                        'features', json_agg(
                            json_build_object(
                                'type', 'Feature',
                                'geometry', ST_AsGeoJSON(ST_Transform(ST_SetSRID(shape, 26915), 4326))::json,
                                'properties', json_build_object(
                                    'objectid', objectid,
                                    'pointid', pointid,
                                    'grid_code', grid_code,
                                    'RASTERVALU', RASTERVALU,
                                    'Difference', Difference
                                )
                            )
                        ),
                        'crs',
                        json_build_object(
                            'type', 'name',
                            'properties',
                            json_build_object(
                                'name', 'EPSG:4326'
                            )
                        )
                    ) AS geojson
                FROM Elev_Accur;
                """)
    rows = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return rows



# Route to retrieve polygon as GeoJSON
@app.route('/temp_kriging_point')
def temp_kriging_point():
    # Connect to the database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute SQL query to retrieve the polygon
    cur.execute("""SELECT
                    json_build_object(
                        'type', 'FeatureCollection',
                        'features', json_agg(
                            json_build_object(
                                'type', 'Feature',
                                'geometry', ST_AsGeoJSON(ST_SetSRID(shape, 4326))::json,
                                'properties', json_build_object(
                                    'objectid', objectid,
                                    'pointid', pointid,
                                    'grid_code', grid_code
                                )
                            )
                        ),
                        'crs',
                        json_build_object(
                            'type', 'name',
                            'properties',
                            json_build_object(
                                'name', 'EPSG:4326'
                            )
                        )
                    ) AS geojson
                FROM temp_kriging_point;
                """)
    rows = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return rows


# Route to retrieve polygon as GeoJSON
@app.route('/Temp_Accur')
def temperature_accuracy():
    # Connect to the database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute SQL query to retrieve the polygon
    cur.execute("""SELECT
                    json_build_object(
                        'type', 'FeatureCollection',
                        'features', json_agg(
                            json_build_object(
                                'type', 'Feature',
                                'geometry', ST_AsGeoJSON(ST_SetSRID(shape, 4326))::json,
                                'properties', json_build_object(
                                    'objectid', objectid,
                                    'field1', field1,
                                    'value_max', value_max,
                                    'RASTERVALU', RASTERVALU,
                                    'Difference', Difference
                                )
                            )
                        ),
                        'crs',
                        json_build_object(
                            'type', 'name',
                            'properties',
                            json_build_object(
                                'name', 'EPSG:4326'
                            )
                        )
                    ) AS geojson
                FROM Temp_Accur;
                """)
    rows = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return rows




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
