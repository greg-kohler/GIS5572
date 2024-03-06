import arcpy
from flask import Flask, jsonify 
import psycopg2
from psycopg2 import sql

#Define Credentials


#Opens Password - Not Needed Until Connecting to Cloud
with open(r"\\Mac\Home\Documents\GitHub\GIS5572\secure\database.txt", 'r') as file:
    database_key = file.read().strip()
    

#Make the Shape
spatial_reference = arcpy.SpatialReference(4326)
point1 = arcpy.Point(2.2945, 48.8584)
point2 = arcpy.Point(-74.0445, 40.6892)
point3 = arcpy.Point(-72.5450,  -13.1631)

# Create an array of points
myarray = arcpy.Array([point1, point2, point3])
mypolygon = arcpy.Polygon(myarray)
mypolygon_wkt = mypolygon.WKT

#Connect to Database
conn = psycopg2.connect(
    dbname=db,
    user=dbuser,
    password=dbpass, #Should be database_key if not connecting to local 
    host= dbhost,
    port="5432"
    )
cur = conn.cursor()

# Create the table - Only Run Once
#table = sql.SQL("""
#    CREATE TABLE lab15572 (
#    id SERIAL PRIMARY KEY,
#   shape GEOMETRY(MultiPolygon, 4326)
#    );
#""")

# Insert polygon into the table
#Percent sign can be ready within the query 
insert_query = sql.SQL("""
    INSERT INTO lab15572 (shape)
    VALUES (ST_GeomFromText(%s, 4326));
""")

#Pulls query from variable and inserts into database. 
#cur.execute(table)
cur.execute(insert_query, [mypolygon_wkt])
conn.commit()
cur.close()
conn.close()
