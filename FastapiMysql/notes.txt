def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name
 we can write  the types also in the python as we write in the typescript   , now supporse   you want to add name and age 
 then you will  not able  to do that as you have  to convert  the age in the string to add in the name 

 apart from that there are the generic types as dict , set , tuple


 def process_items(items: list[str]):   # here list c an have  the internel types so we  have to specify that types also
    for item in items:    # this is called type parameter 
        print(item)

def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():  # basically you  have to give types for the dictionary 
        print(item_name)
        print(item_price)

def process_item(item: int | str):        # this can be of any type 
    print(item)


def say_hi(name: Optional[str] = None):  # optional with the none use 
    if name is not None:    #   Optional[Something] is actually a shortcut for Union[Something, None], they are equivalent.
        print(f"Hey {name}!")  # here basically second one is better 
    else:
        print("Hello World")

##### this is classes, in which you can define the own generic types also 
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name  


### pydantic model is basically used for the  data validation  ans convert them in the appropriate types 
#### fast api is complelety based on the pydantic models 
class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123



#######   async and await 
if you are dealing with some third party(api,db,file system,io operation  these are generally slow)
then you have to use async and await in the function to make
code synchronous 
@app.get('/')
async def read_results():
    results = await some_library()
    return results
concurrency and parrallelis is who is better. that is no the moral of the story , as when there is lot of the waiting is
involved like the web application then we can say that concurrency is better 

#####Coroutine
Coroutine is just the very fancy term for the thing returned by an async def function.

## reading the env variable in the python 
import os   #  this is the os module 
name = os.getenv("MY_NAME", "World")  # if no value is found then world is the default ans
print(f"Hello {name} from Python")

python -m venv directory    # command to create virtual env
### use of virtual enviornment 
when you write multiple program that work on the different packages , these program sometime depend on different version 
of the same packages

fastapi will generate schema for the all apis , this is the best thing (openApi do this job basically)

# keet note of that path /users/me is declared before the /users/{user)id} . this order should be followed 
# only single route can be declared on this 


# how to validate the data with the  help of the enum in the route 
from enum import Enum

from Other_stuff.fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# query parameter -< when you declare basically the parameter of the other function as the path parameter then they are 
# generally refered as the query parameter in that 

# concept of the optional parameter 
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

Request body -< when you want to send data from client to the api then data is sent using the request body 
but sometime request body as such is not present it is sent some query parameter to the api  . in the fastapi request body 
is sent using the pydantic models 


# models decalation to define any query paramter optional 
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item

## decalring the request body and the  path parameter at the same time 
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

## with request body + path parameter + query paramter this is the form of the api having all three things 
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


The function parameters will be recognized as follows:

If the parameter is also declared in the path, it will be used as a path parameter.
If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.

# this is how you can basically restrict the length of the query parameter 
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

 q: Annotated[str, Query()] = "rick"  # if you want to give default value to the query paramter 

 # use  of the regular expression in the query paramter   ^ means starts with  $ ends there does not have any chars after that 
 @app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")  # can use the regex also 
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# ... use of ellipse to show that  parameter is  basically mandatory 
@app.get("/items/")
async def read_items(q: Annotated[str | None ,  Query(min_length=3)] = ...): # by adding none parameter is req but it can accept none
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# accepted the list of vakues in the query paramter
@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None (["default", "Values"])) : # can give default value to list
    query_items = {"q": q}
    return query_items


# add more meta data to the query parameter  like we have added title and the description to it 
@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# to set the alias to the query parameter items_query alias can be items-query 
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# if you want to show that alias is depricated then 
@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# if you want to exclude a parameter then use that 
@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}


# putting validation on the path parameter 
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# to make them kwargs , like key value pair items 
@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get" ge =1), q: str):  # greater than 1 
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# group all the query paramter by using the pydantic model 
class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

# if you want to rectrict the query parameter you want to receive then 
class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

#But if you want it to expect a JSON with a key item and inside of it the model contents, as it does when you declare extra body parameters, you can use the special Body parameter embed
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

# we can define models and having other models .this is called submodel structuring 
class Image(BaseModel):
    url: http # you can put special type of the validation as well 
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None
    

 # other data type can be the frozen set 
in request list will be read out by elliminating the duplicate values and convert it to the set     , in response 
set will be converting to the list

# if you want to take value from the cookie then use in such a way that in the api 
@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}

# if you want to take the values from the header then use in such a way that 
@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}

# to deal with header as they  have hipen generally in their words
# if you get the headers duplicate then define them in the list 
@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
):
    return {"strange_header": strange_header}

# how to define the model for the request 
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.get("/items/")
async def read_items() -> list[Item]:  # here i have define the list[item] as the response type 
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]

# if you want to return something that is way different from then use the response_model 
# if you declare  both responsemodel and return type then response model will take the priority 
@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

# from the pydantic model basically install the various email, password validator then use them instead of the string 
from pydantic import BaseModel, EmailStr

# inheritence type in the models of the pydantic 
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user

# how to return the response directly 
@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response: # here basically response is the class
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

@app.get("/teleport")
async def get_teleport() -> RedirectResponse:    # redirectResponse is the subclass of the response 
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# this will fail  as there is as such no pydantic model having mix of the response and dict 
@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}

# this wil makes things work , by skipping the response model 
@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}

# use of the response_model_exclude , whlile many optional parameter in the nosql , so do not want json so long 
# then use this 
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]

# inheritence and can add our own attributes also , but if that class is empty then use pass 
class UserOut(UserBase):
    pass

# if you want to return the union of 2 things in the response then use in such a way that 
@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]

# if you want to return the status code in the api then use this way 
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# you have to use status code in this way , this is much better than that 
# you have to import status from the fastapi 
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}

# when you have to deal with the form instead of the json , then you have to handle the api in the diff way
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

# when you want to create the model for the form  then use in this way 
class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"} to forbid any extra field , if any extra data is sent then give error to client

@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data

# if you want to deal with files in the api then use this way
from fastapi import FastAPI, File, UploadFile
app = FastAPI()
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# if you want to add some description to the file then use api in these ways 
@app.post("/files/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}

# if you want to deal with several files upload then use this method
@app.post("/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}
@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}

@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

# how to raise the exception in the api with good content 
# you can also add the custom headers in that 
from fastapi import FastAPI, HTTPException
app = FastAPI()
items = {"foo": "The Foo Wrestlers"}
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found",headers={"X-Error": "There goes my error"},
)
    return {"item": items[item_id]}


# if you want to create your own exception then also there is a way to do that 
# first of all create a class for that exception then craete a exceution handler for that , raise that exception smoothly
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name
app = FastAPI()
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )
@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}

# overriding the default errors with some errors 
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
@app.exception_handler(RequestValidationError)

async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}


# use of keyword tag in the api 
@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]

# what if there are more tags there , so use enums for them , if further inc , scalable is also there 
class Tags(Enum):
    items = "items"
    users = "users"
@app.get("/items/", tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]
@app.get("/users/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]


# addition of the summary and description tag in the api 
@app.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
)
async def create_item(item: Item):
    return item

# depricate the paths 
@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]


# use of the jsonable encoder 
from fastapi.encoders import jsonable_encoder
@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data

# now learn more about the dependency injection 


# match statement is similar to the switch statement 
case 401 | 403 | 404: 
case (x, y):  # want to match with the 2-d point 

# lambda keyword  for the small and anonymous function 
# for creating c like structure having multiple fields with multiple data types then  use the dataclass from the python

# generators -< used for creating iterators 
they are wriiten like function but use yield to return the data
whenever next() is called itertor resumes from where it has  stopped (remember all its last executed values)







