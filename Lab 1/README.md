# ArcGIS to Cloud Data Pipeline

This repository contains code and instructions for setting up an automated data pipeline from ArcGIS to cloud software.

## Overview:

This project aimed to create a data pipeline from ArcGIS to Google Cloud services.  ArcPy Geometry primitives were used to create polygons, converted to (WKT) format, imported into a PostGIS database, and then the Flask application was used to retrieve polygon data from the database as a GeoJSON object in ArcOnline.

## Contents:

Lab1-2 (2).ipynb (Jupyter Notebook): Creates polygons, converts polygons to WKT, and imports into database).

app.py: Includes the Flask application (app.py) for retrieving polygon data from PostGIS and serving as GeoJSON.

Dockerfile: This Dockerfile sets up an environment for running a Python application. It installs dependencies, sets an environment variable, and specifies the command to run the application. Its dependencies are listed in a file named requirements.txt.

requirements.txt: A list of dependencies required for the Flask app and Dockerfile to run.

Other Lab Files: Contains other files for the lab including the CSV for Part 1, and the SRS for Lab 1.1

## Instructions:

Refer to the notebooks for creating polygons using ArcPy Geometry primitives, converting to WKT, and importing into PostGIS using psycopg2.

Set up a Flask application using the provided app.py file to retrieve polygon data from PostGIS.

Follow the documentation to deploy the Flask application on Google Cloud Run. We followed this tutorial: https://www.youtube.com/watch?v=0mfng-vih_I

Follow lab instructions for the remainder. We followed this tutorial: https://github.com/runck014/cloud_run_demo

## Note:
For a detailed explanation of the data flow, refer to the provided video recording linked in Lab1-2 Document

Parts of SQL Query and code written with guidance from chat.openai.com (ChatGPT)