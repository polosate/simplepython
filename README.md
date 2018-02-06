# simple_python
Workshop
## Requirements
python3  
docker  
docker-compose  
## Usage
1. Create virtual environment  
`$ virtualenv -p /path/to/python .env`
2. Activate it  
`$ source .env/bin/ativate`
3. Bootstrap the DB  
`$ docker-compose up -d db`  
`$ docker-compose run --rm pyapp /bin/bash -c "cd /opt/services/pyapp/src && python -c  'import database; database.init_db()'"`
4. Bring up the cluster  
`docker-compose up -d`
5. Inside the DB container  
`docker exec -t -i container_name /bin/bash`
`psql -h localhost -p port -d db_name -U username --password`


Browse to localhost:8080 to see the app in action
