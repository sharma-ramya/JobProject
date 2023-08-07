# initial setup for leaflet
sudo apt install gdal-bin libgdal-dev

sudo apt install python3-gdal

sudo apt install binutils libproj-dev

# in virtual enviornment 

pip install django
pip install djangorestframework
pip install psycopg2-binary
pip install python-decouple
pip install django-leaflet

# for db seprate terminal run this docker file

docker run --name=postgis -d -e POSTGRES_USER=leaflet -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:13.0
