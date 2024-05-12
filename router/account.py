import re
import json
import asyncio
from fastapi import APIRouter
from fastapi import HTTPException, status, Response
from schema.accounut import Account


router = APIRouter(
    prefix="/account",
    tags=["account"],
)


def get_data():
    with open('data/account.json') as f:
        data = json.load(f)
        f.close()
    return data

def save_data(data):
    with open('data/account.json', 'w') as f:
        json.dump(data, f, indent=4)
        f.close()

@router.get("/")
async def get_account():
    acc = get_data()
    return acc

@router.post("/")
async def create_account(account: Account):
    acc = account
    err = ''
    success = False

    acc_data = get_data()
    usernames = [item["username"] for item in acc_data]
    
    if acc.username in usernames:
        err = "username is exists!"
    elif len(acc.username) < 3:
        err = "username too short!"
    elif len(acc.username) > 32:
        err = "username too long!"
    elif not re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$", acc.password):
        err = "password must contain at least one uppercase letter, one lowercase letter, and one digit!"
    else:
        acc_data.append({ "username": acc.username, "password": acc.password })
        save_data(acc_data)
        success = True
        return {
            "success": success
        }
    
    return {
        "success": success,
        "reason": err
    }

user_wrong_password_count = {data["username"]: 0 for data in get_data()}
@router.post("/validate")
async def validate_account(account: Account):
    acc = account
    err = ''
    success = False

    acc_data = get_data()
    for data in acc_data:
        if data["username"] == acc.username:
            if data["password"] == acc.password:
                user_wrong_password_count[acc.username] = 0
                success = True
                return {
                    "success": success
                }
            else:
                user_wrong_password_count[acc.username] += 1
                if user_wrong_password_count[acc.username] >= 5:
                    err = 'Too many wrong attempts. Please try again later.'
                    user_wrong_password_count[acc.username] = 0
                else:
                    err = "password is wrong!"
    
    if not success and err == '':
        err = "username doesn't exit!"
    
    return {
        "success": success,
        "error": err
    }