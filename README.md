# Candy Shop

## Instalar dependencias

- Se recomienda utilizar un entorno virtual (venv)

```sh
pip install -r requirements.txt
```


## Ejecutar servidor de desarrollo

```sh
python manage.py runserver
```

## Rutas del proyecto

```json
{
    "category": "http://127.0.0.1:8000/category/",
    "category create": "http://127.0.0.1:8000/category/create",
    "category delete": "http://127.0.0.1:8000/category/delete/<int:pk>/",
    "candy": "http://127.0.0.1:8000/candy/",
    "customer": "http://127.0.0.1:8000/customer/",
    "order": "http://127.0.0.1:8000/order/",
    "order Details from a user and a order": "http://127.0.0.1:8000/order/orderDetails/<int:order_id>/",
    "orderItem": "http://127.0.0.1:8000/orderItem/"
}
```