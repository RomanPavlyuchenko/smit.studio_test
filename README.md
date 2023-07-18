##  Запуск проекта
Подготовка к запуску
```
apt-get update
apt-get install -y docker-compose git
git clone https://github.com/RomanPavlyuchenko/smit.studio_test.git
cd smit.studio_test
mv .env.pub .env
```
Команда для запуска проекта
```
docker-compose up
```

## Описание
Реализован REST API сервис по расчёту стоимости страхования в зависимости от типа груза и объявленной стоимости.\
Тарифы для расчетов загружаются из файла json и request body.\
Сервис возращает declared_value * rate(из актуального тарифа).\
Сервис разворачивается внутри Docker.

### Технологии, использованные при реализации проекта
- FastApi
- Tortoise ORM
- Postgresql
- Docker, Docker-compose
