# Визуализация

### Запуск графического интерфейса под ОС Windows
```console
$ python -m app
```
Для загрузки файла в БД необходимо выбрать исходный .xlsx файл(Файл => Импорт)

![Import file](./img-examples/import.png)

После выбора файла необходимо задать параметры подключения к бд (Настройки => Параметры запуска)

![Settings](./img-examples/settings1.png)
![Settings](./img-examples/settings2.png)

Пример параметров:
```
    База данных: "postgres"
    Пользователь: "postgres"
    Пароль: "postgres"
    Хост: "127.0.0.1"
    Порт: "5432"
    Перезапись: false
```
После выбора файла и ввода параметров запуск программы (Старт => Запуск с текущими настройками)

![Run](./img-examples/run.png)

### Подготовка БД в Postgres
Загрузка образа Postrges
```console
$ docker pull postgres:15.2
```


Запуск контейнера с некоторым набором параметров

```console
$ docker run --name test-postgres -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:15.2
```

### Зависимости:
```
openpyxl==3.1.2
psycopg2==2.9.5
loguru==0.6.0
PyQt5==5.15.9
```
При возникновении ошибки установки 'psycopg2' использовать 'psycopg2-binary'

### Запуск программного средства

Установка необходимых зависимостей
```console
$ pip3 install --user -r requirements.txt
```

Запуск основного модуля ПС
```console
$ python3 -m main <params> 
```

### Параметры запуска:
    '-f' или '--filename' - путь до входного .xlsx файла (обязательный параметр)
    '-d' или '--database' - название БД
    '-u' или '--user' - имя пользователя
    '-ps' или '--password' - пароль
    '-ht' или '--host' - сервер postgres
    '-p' или '--port' - порт
    '-o' или '--overwrite' - флаг, позволяющий перезаписывать значения в бд вместо добавления
По умолчанию каждый параметр (кроме filename) принимает значение из конфигурационного json-файла



### Конфигурационный файл

При запуске программного средства без параметров параметры подключения к Postgres будут считываться из конфигурационного json-файла **config-json**, пример оформления которого представлен ниже:
```json
{
    "database": "postgres",
    "user":     "postgres",
    "password": "postgres",
    "host":     "127.0.0.1",
    "port":     "5432",
    "overwrite": false,
    "log_file": "logs.log"
}
```
