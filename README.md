##Sensely. Office Automation with Python and the Internet of Things

###Slides
In order to serve the slides, navigate into the `slides/` directory and run the `present.sh` shell script
with command ```./present.sh```. This may require making the script executable. This can be accomplished
by running command ```chmod 755 present.sh```.

###Code
The code requires an installation of Postgres 9.5 and the Mosquitto message broker for the MQTT network
protocol. In order to simplify the installation of these dependencies, I use Docker and Docker-Compose
to run the application within containers. In order to build the project run 
```docker-compose build``` 
in the root directory. To create the database, run 
`docker-compose start db
./create_db.sh
`
. To launch the application, run
```docker-compose up```
. 
