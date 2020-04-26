---
title: APIs for Accounts
permalink: /apis/accounts
toc: true
---


## Get all Accounts for a User

**GET Request** - `/user/id/accounts`
{: .notice--info}

```bash
curl --location --request GET 'http://localhost:8000/user/id/accounts' \
--header 'Authorization: Basic user_auth'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "accounts": [
        {
          "exchange": "BITMEX",
          "api_key": "api_key",
          "secret_key": "secret_key"
        },
        {
          "exchange": "CONCURRENCY.COM",
          "api_key": "api_key",
          "secret_key": "secret_key"
        },
        {
          "exchange": "BINANCE",
          "api_key": "api_key",
          "secret_key": "secret_key"
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

## Create a new Account

**POST Request** - `/user/id/accounts/new`
{: .notice--info}

```bash
curl --location --request POST 'http://localhost:8000/user/id/accounts/new' \
--header 'Authorization: Basic user_auth' \
--header 'Content-Type: application/json' \
--data-raw '{
  "Exchange": "BITMEX",
  "api_key": "api_key",
  "secret_key": "secret_key"
}'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "Status Code": 200,
      "Message": "Account successfully created"
    }
    ```
2. Response - Unauthorized

    ```json
    {
      "Status Code": 401,
      "Message": "Wrong Authentication credentials"
    }
    ```
3. Response - Unprocessable Entity

    ```json
    {
        "Status Code": 422,
        "Message": "Account for that exchange already exists"
    }
    ```

## Delete an Account

**DELETE Request** - `/user/id/accounts/exchange_name`
{: .notice--info}

```bash
curl --location --request DELETE 'http://localhost:8000/user/id/accounts/exchange_name' \
--header 'Authorization: Basic user_auth'
```

### Sample Responses

1. Response - OK

    ```json
    {
        "Status Code": 200,
        "Message": "Account successfully deleted"
    }
    ```
2. Response - Forbidden

    ```json
    {
      "Status Code": 403,
      "Message": "You do not have permission to perform this action"
    }
    ```
