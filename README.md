# Визуализация

### Подготовка БД в Postgres

```console
# загрузка актуального образа Postrges
$ docker pull postgres:latest

# запуск контейнера с некоторым набором параметров
$ docker run --name test-postgres -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:15.2
```

### Запуск программного средства

```console
# установка необходимых зависимостей
$ pip3 install --user -r requirements.txt

# запуск основного модуля ПС
$ python3 -m main <params> 
```
по умолчанию параметры из конфига
