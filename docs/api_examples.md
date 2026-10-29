# Примеры запросов API

## Вход и получение JWT

`POST /api/auth/login/`

```json
{"username": "admin", "password": "your-password"}
```

Ответ содержит `access` и `refresh`. Используйте `access` как Bearer token.

## Создание марки

`POST /api/brands/`

```json
{"name": "Toyota", "country": "Japan"}
```

## Создание автомобиля

`POST /api/cars/`

```json
{
  "brand": 1,
  "model": "Camry",
  "year": 2024,
  "price": "3200000.00",
  "color": "Белый",
  "engine_volume": "2.5",
  "fuel_type": "petrol",
  "mileage": 0,
  "status": "available",
  "vin": "JTNB11HK0J3000001",
  "description": "Учебная запись"
}
```

## Создание клиента

`POST /api/clients/`

```json
{"full_name": "Иван Иванов", "phone": "+79990000000", "email": "ivan@example.com"}
```

## Создание заказа

`POST /api/orders/`

```json
{"client": 1, "car": 1, "manager": 1, "order_type": "sale", "status": "new", "price": "3200000.00"}
```
