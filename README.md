
## 🐋 Commands Docker and Docker-compose:

  
Create docker image
```bash
docker  build  -t  manager-product  .
```

Run docker image
```bash
docker-compose  up  app
```
  

Run postgres docker image

```sh
docker-compose  up  postgresql  -d
```
  

Run pgadim docker image

```sh
docker-compose  up  pgadmin  -d
```




## 🗄️Commands Alembic migration:

Init alembic
```bash
docker-compose  run  --user  1000  app  sh  -c  'alembic init migrations"'
```
  
Create migration
```bash
docker-compose  run  --user  1000  app  sh  -c  'alembic revision --autogenerate -m "add categories table"'
```


Run migration
```bash
docker-compose  run  --user  1000  app  sh  -c  'alembic upgrade head'
```

# 🛠️ Pytest

 Run test
```bash
docker-compose run --user  1000 app sh -c "pytest"
```

Run specific test
```bash
docker-compose run app sh -c "pytest -k my_test"
```