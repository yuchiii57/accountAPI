# accountAPI
Create easy FastAPI to create account and account validate  
Using json file to store the account data

## BaseURL
```
https://127.0.0.1:8000/account
```

## GET /account
Return the all account data from json file

### Return Data
```
[
    {
        "username": "abc",
        "password": "Abc123"
    },
    {
        "username": "abc123",
        "password": "123Abc"
    }
]
```

## POST /account
Create Account with request body, will check user name cannot duplicate and password with a
minimum length of 8 characters and a maximum length of 32 characters,
containing at least 1 uppercase letter, 1 lowercase letter, and 1 number.

### Request Body
```
{
  "username": "john_doe",
  "password": "John123"
}
```

### Return Data
```
{
    "success": true
}
```

#### if error for example
```
{
    "success": false,
    "reason": "password must contain at least one uppercase letter, one lowercase letter, and one digit!"
}
```

## POST /account/validate
Validate the account, will to check with json file to confirm user name exits and password is validated. If an acoount password fails 5 times, will return the user should wait one minute before attempting to verify the password again.

### Request Body
```
{
  "username": "john_doe",
  "password": "John123"
}
```

### Return Data
```
{
    "success": true
}
```
#### if error for example
```
{
    "success": false,
    "error": "username doesn't exit!"
}
```
