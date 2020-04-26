---
title: APIs for Users
permalink: /apis/users
toc: true
---


## List all Users (Staff Only)

**GET Request** - `/users`
{: .notice--info}

```bash
curl --location --request GET 'http://localhost:8000/users' \
--header 'Authorization: Basic staff_user_auth'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "users": [
        {
          "id": 1,
          "email": "test1@gmail.com",
          "joining_date": "2012-03-19",
          "profit": null
        },
        {
          "id": 2,
          "email": "test2@gmail.com",
          "joining_date": "2015-10-21",
          "profit": 0.05
        }
      ]
    }
    ```
2. Response - Unauthorized

    ```json
    {
      "Status Code": 401,
      "Message": "Wrong Authentication credentials"
    }
    ```
3. Response - Forbidden

    ```json
    {
      "Status Code": 403,
      "Message": "You do not have permission to perform this action"
    }
    ```

## Get details of a User

**GET Request** - `/user/id`
{: .notice--info}

```bash
curl --location --request GET 'http://localhost:8000/user/id' \
--header 'Authorization: Basic user_auth'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "id": 1,
      "email": "test1@gmail.com",
      "joining_date": "2012-03-19",
      "profit": null
    }
    ```
2. Response - Unauthorized

    ```json
    {
      "Status Code": 401,
      "Message": "Wrong Authentication credentials"
    }
    ```
3. Response - Forbidden

    ```json
    {
      "Status Code": 403,
      "Message": "You do not have permission to perform this action"
    }
    ```

## Create a new User

**POST Request** - `/user/new`
{: .notice--info}

```bash
curl --location --request POST 'http://localhost:8000/user/new' \
--header 'Content-Type: application/json' \
--data-raw '{
  "email": "sayam049@gmail.com",
  "password": "hello world"
}'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "Status Code": 200,
      "Message": "User successfully created"
    }
    ```
2. Response - Unprocessable Entity

    ```json
    {
      "Status Code": 422,
      "Message": "User with such Email ID already exists"
    }
    ```

## Delete a User

**DELETE Request** - `/user/id`
{: .notice--info}

```bash
curl --location --request DELETE 'http://localhost:8000/user/id' \
--header 'Authorization: Basic user_auth'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "Status Code": 200,
      "Message": "User successfully deleted"
    }
    ```
2. Response - Forbidden

    ```json
    {
      "Status Code": 403,
      "Message": "You do not have permission to perform this action"
    }
    ```
