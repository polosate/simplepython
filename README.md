# simple_python
Workshop
## Requirements
python3  
docker  
docker-compose  
## Usage
1. Create virtual environment 
```bash
$ virtualenv -p /path/to/python .env
```
2. Activate it
```bash
$ source .env/bin/ativate
```
3. Bootstrap the DB  
```bash
$ docker-compose up -d db
$ docker-compose run --rm pyapp /bin/bash -c "cd /opt/services/pyapp/src && python -c  'import database; database.init_db()'"
```

4. Bring up the cluster  
```bash
$ docker-compose up -d
```
5. Browse to localhost:8080 to see the app in action


### Inside the DB container  
```bash
$ docker exec -t -i simplepython_db_1 /bin/bash
@ psql -h localhost -p 5432 -d simplepython_db_1 -U postgres --password
```
