# Django/GeoDjango examples

This folder contains a Django project with example seen in class, including GeoDjango, and Django+Leaflet.

## Prerequisites

### Install Python. 

One convenient way is to use the [Anaconda](https://www.anaconda.com/distribution/#download-section) distribution. 

### Install Django. 

Detailed instructions can be found in the Django [documentation](https://docs.djangoproject.com/en/2.1/topics/install/#installing-official-release). 
In general using anaconda the following command will do the job: 
`conda install -c anaconda django=2.1`

### Install Postgres/PostGIS

Several distributions are available depending on your OS, details can be found [here](https://www.postgresql.org/download/)

### Install GeoDjango dependencies

GeoDjango requires installation of several library dependencies, including GEOS, GDAL, etc. as detailed [here](https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install).

Please follow the [macos](https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/#macos) and [windows](https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/#windows) instructions if your are using these OS.

For **macOS**, using Postgres.app is probably the simplest way. Once it is done the gdal and libgeoip can be installed using homebrew as described in the instructions.

For *windows**, it is important to install psycopg2 (the postgis lirbary that python uses for connecting with the DB). In general it can be installed using `pip install psycopg2-binary` from an anaconda console.
It is also important to install the GDAL, GEOS, and other libraries, which can be done by installing the OSGeo4W package, as explained in the instructions. 

One common error in windows is that the GDAL dll is not found. To solve this, you can add a reference to it in the settings.py file of the django project: `
GDAL_LIBRARY_PATH = 'C:\\OSGeo4W64\\bin\\gdal204.dll'`

Also it is important to set up the environment variables as explained in the [instructions](https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/#modify-windows-environment)


### Django leaflet

`conda install -c conda-forge django-leaflet`


## Configuration

Once all dependencies are done, the following set up steps need to be followed.

### testGIS database

After installation, create a database named `testGIS`, if you haven't done it yet.
Enable the postgis exetensions in the new database, if not done already: `CREATE EXTENSION postgis`.

Afterwards, you may import the `cantons` table from the shapefile of the Swiss canton [borders](https://cyberlearn.hes-so.ch/mod/resource/view.php?id=952453). 
This can be done using QGIS as we have seen in class. 

### Migrations

If everything is ready, you may go to the geoweb folder, where `manage.py` is located, and run 

`python manage.py makemigrations swissgeo`

And then execute the migration:

`python manage.py migrate`

This should create the swissgeo_city, and swissgeo_hospital tables. You can verify this in pgAdmin.

You may also get a message saying that the table 'cantons' already exists. Now you can also execute the migrations in 'fake' mode to enable the cantons table in the model:

`python manage.py migrate --fake`

### Admin UI

To access the admin UI, you may need to create a superuser:

`python manage.py createsuperuser`


## Run

To run the project:

`python manage.py runserver`

You should be able to access the URLs as described in class. You may first enter the admin UI (http://127.0.0.1:8000/admin
) to add cities, hospitals, and to check if the cantons have been loaded.




