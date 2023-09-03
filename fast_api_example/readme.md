# Fast API Example

Link : https://fastapi.tiangolo.com/tutorial/first-steps/

Run command

```shell
python -m uvicorn main:app --reload
```

**Localhost**

```
GET http://127.0.0.1:8000/
```

**Swagger**

```
http://127.0.0.1:8000/docs
```

FastAPI is a class that inherits directly from **Starlette**. You can use all the Starlette functionality with FastAPI too.

```
POST http://127.0.0.1:8000/items
Body : 
{
    "name" : "Manish",
    "price" : 20,
    "tax" : 2
}
```

```
PUT http://127.0.0.1:8000/items/123
Body : 
{
    "item" :  {
        "name" : "Sandeep",
        "price" : 10,
        "tax" : 2
    }
}
```

```
GET http://127.0.0.1:8000/items/345
Response HTTP 404
{
    "detail": "Item not found"
}
```

