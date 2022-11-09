from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price: float
    brand: Optional[str] = None

class Item(BaseModel):
    name:str = None
    price: float = None
    brand: Optional[str] = None

app = FastAPI()

"""
Endpoint: after slash

fastbook.com/home
baseurl      endpoint

GET: return information
POST: creating something new
PUT: update something existing
DELETE: getting rid of information
"""

@app.get("/")
def home():
    return {"Data": "Test"}

"""
--reload: reload uvicorn server every time you change

http://127.0.0.1:8000/docs

API의 역할이란?
아마존을 예로 들자면
frontend과 separate되어있고
모바일앱, 웹앱 등 여러가지 환경을 위해서 각각의 system을 만드는 것이 아닌
access to the same information by sending a request to API를 하여
원하는 정보를 얻을 수 있는 것
즉, API information은 같고 display의 차이일 뿐

홀서버를 예로 많이 든다
"""

@app.get("/about")
def about():
    return {"Data": "About"}

inventory = {
    1:{
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The ID of the item you'd like to search", gt=0)): # int가 아니면 fastapi 쪽에서 자동으로 error
    return inventory[item_id]


"""
Path parameter
Path first arg는 default 값
gt: greater than
lt: less than

how to accept query parameter for an endpoint?
facebook.com/home?redirect=/tim&msg=fail"
"""

@app.get("/get-by-name")
def get_item(name:str = Query(None, title="Name", description="")): # Query
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item name not found")    # use default status code

"""
Query paramter
http://127.0.0.1:8000/get-by-name?name=Milk
=> {"name":"Milk","price":3.99,"brand":"Regular"}

add argument "test"
*: take unlimited positional arguments and the rest is key arguments

http://127.0.0.1:8000/get-by-name?name=Milk&test=2
=> {"name":"Milk","price":3.99,"brand":"Regular"}

Putting both path and query parameters
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id:int, name: Optional[str] = None, test: int):
                path param   optional query param        mandatory query param

TODO: Path parameter하고 Query parameter의 차이점은 뭐지?
"""

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
    
    inventory[item_id] = item # will automatically change to dict
    return inventory[item_id]

"""
Basemodel이라는 걸 써야함

TODO: item 주소에서는 어떻게 넣는 거지?
"""

@app.put("/update-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
    
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description= "The ID")): # ...: required
    if item_id not in inventory:
        return {"Error": "Item ID already exists."}
    
    del inventory[item_id]
    return {"Success": "Item deleted"}

"""
Status Code
HttpException으로 에러 핸들링할 수 있음
200 - Success
400 - Bad Request
404 - Page Not found
"""