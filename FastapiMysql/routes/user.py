from fastapi import APIRouter, HTTPException
from config.db import conn
from models.index import users
from schemas.index import  User
from schemas.index import UserUpdate
user = APIRouter()

#get request to get all user data
@user.get('/')
async def getUser():
    result  =  conn.execute(users.select()).fetchall()
    keys = ['id', 'name', 'email', 'password']
    json_result = [dict(zip(keys, row)) for row in result]
    print(json_result)
    return json_result

# get request to get user data by id
@user.get('/{id}')
async def getUser(id:int):
    result = conn.execute(users.select().where(users.c.id ==id )).fetchall()
    conn.commit()  
    keys = ['id', 'name', 'email', 'password']
    json_result = [dict(zip(keys, row)) for row in result]
    print(json_result)
    return json_result


# post request to create user
@user.post('/')
async def CreateUser(user:User):
    test = "hi"
    conn.execute(users.insert().values(
        name = user.name,
        email = user.email,
        password = user.password,
    ))
    # return {"msg" : " this user is craeted successfully"}
    result = conn.execute(users.select()).fetchall()
    conn.commit()  
    keys = ['id', 'name', 'email', 'password']
    json_result = [dict(zip(keys, row)) for row in result]
    print(json_result)
    return json_result
    


# put request to update user data
@user.put('/{id}')
async def updateUser(id :int , user:UserUpdate):
    existing_user = conn.execute(users.select().where(users.c.id == id)).fetchone()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = {
        "name": user.name if user.name else existing_user.name,
        "email": user.email if user.email else existing_user.email,
        "password": user.password if user.password else existing_user.password,
    }
    conn.execute(users.update().where(users.c.id == id).values(**update_data))
    conn.commit()  
    updated_user = conn.execute(users.select().where(users.c.id == id)).fetchone()
    keys = ['id', 'name', 'email', 'password']
    json_result = dict(zip(keys, updated_user)) if updated_user else None
    print(json_result)
    return json_result


# delete request to delete user data
@user.delete('/{id}')
async def deleteUser(id:int):
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()  
    result = conn.execute(users.select()).fetchall()
    keys = ['id', 'name', 'email', 'password']
    json_result = [dict(zip(keys, row)) for row in result]
    print(json_result)
    return json_result