# Containerized Flask app on DockerHub
This project is an implementation of a containerized web-based application (flask framework) based on the guidelines of the Cloud computing at scale class @ Duke University.

## Overview
This flask application in python interacts with the user to upload and image and its corresponding annotation file in a xml format. Then, parse this xml file into a txt format file. Finally, output a plot of the input image with its corresponding patches included in the txt file.

### Example of an xml file

```xml
<?xml version="1.0"?>
-<annotation>
  <folder>DE_Feb10</folder>
  <filename>University of Delaware.jpg</filename>
  <path>~\Wind New Annotated\NE_feb10\DE_Feb10\University of Delaware.jpg</path>
-<source>
  <database>Unknown</database>
  </source>
-<size>
  <width>608</width>
  <height>608</height>
  <depth>3</depth>
  </size>
  <segmented>0</segmented>
-<object>
  <name>wind_turbine</name>
  <pose>Unspecified</pose>
  <truncated>0</truncated>
  <difficult>0</difficult>
  -<bndbox>
    <xmin>270</xmin>
    <ymin>279</ymin>
    <xmax>324</xmax>
    <ymax>342</ymax>
   </bndbox>
</object>
</annotation>
```

### Example of the parsed xml file into a txt file (label, x, y, width, height) scaled according to the input image size in pixels

```
0 0.4128289473684211 0.4917763157894737 0.0756578947368421 0.15789473684210525
0 0.7639802631578947 0.16776315789473684 0.07401315789473684 0.16447368421052633
```

### Plot example of the image and its corresponding txt file with the patches
![plot](img_path/plot_png_example.png)

## Prerequisites

For the execution of the Container, **Docker** is required.    
It could be downloaded from https://www.docker.com/products/docker-desktop

[Project_DockerHub](https://hub.docker.com/r/josemoscoso/cloud_computing_2nd_project/tags?page=1&ordering=last_updated)
```josemoscoso/cloud_computing_2nd_project```

-Pull docker image
```docker pull josemoscoso/cloud_computing_2nd_project:latest```

-Run docker image
```docker run -p 8080:8085 josemoscoso/cloud_computing_2nd_project```

## Guide to use the container

* The application  operates on port 8080.      
* To upload an image file (jpeg, jpg or png) and a xml file open:
```localhost:8080/```
* To parse a xml file into a txt file use:
```localhost:8080/parse_xml```
* To plot the initial input image file annotated with the txt file use:
```localhost:8080/plot_png```

## Links to documentation

> Flask :  https://flask.palletsprojects.com/en/1.1.x/    
> Containers and Docker : https://www.docker.com/resources/what-container.
