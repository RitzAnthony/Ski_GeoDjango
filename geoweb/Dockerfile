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
ADD requirements.txt /code
RUN pip install -r requirements.txt
ADD . /code/

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

#CMD ["python","manage.py", "runserver"]