## Lab 2 Repository

This repository contains notebooks for pulling sports schedules, performing data quality assurance and quality control (QAQC) on elevation, land cover, and temperature data for the state of Minnesota, generating road lines for traffic scenarios during sporting events, and pushing data into a cloud geodatabase.

### Notebooks

1. **Sports Schedule Processing Notebook**
   - This notebook pulls sports schedules from a specified source, formats the data, and stores it in a structured format.

2. **Elevation Data QAQC Notebook**
   - This notebook retrieves Minnesota elevation data from the Minnesota Geospatial Commons, performs quality assurance and quality control checks, and ensures data integrity.

3. **Land Cover Data QAQC Notebook**
   - This notebook retrieves Minnesota land cover data from the Minnesota Geospatial Commons,, conducts quality assurance and quality control procedures, and validates the accuracy of the data.

4. **Temperature Data QAQC Notebook**
   - This notebook gathers Minnesota temperature data from the NOAA, conducts QAQC analysis to identify anomalies or inconsistencies, and ensures data reliability.

5. **Traffic Scenario Road Line Generation Notebook**
   - This notebook generates road lines for scenarios with and without traffic during sporting events, aiding in traffic management and planning. This notebook uses the ESRI Network.

6. **Cloud Geodatabase Data Pushing Notebook**
   - This notebook pushes all processed data, including sports schedules, elevation, land cover, temperature, and road lines, into a cloud geodatabase for storage and accessibility.

### Requirements

- Python 3.x
- Jupyter Notebook
- ArcGIS Pro
- PostgreSQL Cloud Database
- Relevant Python libraries for data processing, geospatial analysis, and database interaction

### Note

- Each notebook contains comments explaining the code.
- Data flow diagrams can be found in each notebook.

### Contributors (on SRS)

- Greg Kohler
- Laure Briol
- Logan Gall
