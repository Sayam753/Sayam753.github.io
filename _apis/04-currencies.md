---
title: APIs for Currencies
permalink: /apis/currencies
toc: true
---


## Create a new Currency (Staff Only)

**POST Request** - `/exchange/id/currency/new`
{: .notice--info}

```bash
curl --location --request POST 'http://localhost:8000/exchange/id/currency/new' \
--header 'Authorization: Basic staff_user_auth' \
--header 'Content-Type: application/json' \
--data-raw '{
  "exchange": "Bitcoin",
  "symbol": "USD"
}'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "Status Code": 200,
      "Message": "Currency successfully created"
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
4. Response - Unprocessable Entity

    ```json
    {
        "Status Code": 422,
        "Message": "Currency already exists"
    }
    ```
5. Response - Unprocessable Entity

    ```json
    {
        "Status Code": 422,
        "Message": "Exchange does not exist"
    }
    ```

## Edit a Currency (Staff Only)

**PUT Request** - `/exchange/id/currency/id`
{: .notice--info}

```bash
curl --location --request PUT 'http://localhost:8000/exchange/id/currency/id' \
--header 'Authorization: Basic staff_user_auth' \
--header 'Content-Type: application/json' \
--data-raw '{
  "exchange": "Litecoin",
  "symbol": "USD"
}'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "Status Code": 200,
      "Message": "Currency successfully updated"
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
4. Response - Not Found

    ```json
    {
      "Status Code": 404,
      "Message": "Exchange not found"
    }
    ```
5. Response - Not Found

    ```json
    {
        "Status Code": 404,
        "Message": "Currency not found"
    }
    ```
6. Response - Unprocessable Entity

    ```json
    {
        "Status Code": 422,
        "Message": "Currency already exists"
    }
    ```

## Delete a Currency (Staff Only)

**DELETE Request** - `/exchange/id/currency/id`
{: .notice--info}

```bash
curl --location --request DELETE 'http://localhost:8000/exchange/id/currency/id' \
--header 'Authorization: Basic staff_user_auth'
```

### Sample Responses

1. Response - OK

    ```json
    {
        "Status Code": 200,
        "Message": "Currency successfully deleted"
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
4. Response - Not Found

    ```json
    {
        "Status Code": 404,
        "Message": "Exchange not found"
    }
    ```
5. Response - Not Found

    ```json
    {
        "Status Code": 404,
        "Message": "Currency not found"
    }
    ```
