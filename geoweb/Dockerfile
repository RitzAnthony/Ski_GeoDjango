FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update ; apt-get --assume-yes install binutils libproj-dev gdal-bin

RUN wget http://download.osgeo.org/geos/geos-3.6.2.tar.bz2
RUN tar -xjf geos-3.6.2.tar.bz2
RUN cd geos-3.6.2; ./configure; make; make install

RUN wget http://download.osgeo.org/gdal/2.2.2/gdal-2.2.2.tar.gz
RUN tar -xzf gdal-2.2.2.tar.gz
RUN cd gdal-2.2.2; ./configure; make; make install

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code
RUN pip install --requirement requirements.txt
COPY . /code/

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

#CMD ["python","manage.py", "runserver"]