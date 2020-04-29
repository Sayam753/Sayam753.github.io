---
title: APIs for Exchanges
permalink: /apis/exchanges
toc: true
---


## List all Exchanges

**GET Request** - `/exchanges`
{: .notice--info}

```bash
curl --location --request GET 'http://localhost:8000/exchanges'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "exchanges": [
        {
          "id": 1,
          "name": "Bitcoin",
          "curriencies": [
            {
              "id": 1,
              "symbol": "USD"
            },
            {
              "id": 2,
              "symbol": "LTC"
            }
          ]
        },
        {
          "id": 2,
          "name": "Ethereum",
          "curriencies": [
            {
              "id": 1,
              "symbol": "USD"
            },
            {
              "id": 2,
              "symbol": "LTC"
            }
          ]
        }
      ]
    }
    
    ```

## Get an exchange

**GET Request** - `/exchange/id`
{: .notice--info}

```bash
curl --location --request GET 'http://localhost:8000/exchange/id'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "id": 1,
      "name": "Bitcoin",
      "curriencies": [
        {
          "id": 1,
          "symbol": "USD"
        },
        {
          "id": 2,
          "symbol": "LTC"
        }
      ]
    }
    ```
2. Response - Not Found

    ```json
    {
      "Status Code": 404,
      "Message": "Exchange not found"
    }
    ```

## Edit an Exchange (Staff Only)

**PUT Request** - `/exchange/id`
{: .notice--info}

```bash
curl --location --request PUT 'http://localhost:8000/exchange/id' \
--header 'Authorization: Basic staff_user_auth' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "Litecoin"
}'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "Status Code": 200,
      "Message": "Exchange successfully updated"
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
5. Response - Unprocessable Entity

    ```json
    {
        "Status Code": 422,
        "Message": "Exchange already exists"
    }
    ```

## Create a new Exchange (Staff Only)

**POST Request** - `/exchange/new`
{: .notice--info}

```bash
curl --location --request POST 'http://localhost:8000/exchange/new' \
--header 'Authorization: Basic staff_user_auth' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "Bitcoin"
}'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "Status Code": 200,
      "Message": "Exchange successfully created"
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
        "Message": "Exchange already exists"
    }
    ```

## Delete an Exchange (Staff Only)

**DELETE Request** - `/exchange/id`
{: .notice--info}

```bash
curl --location --request DELETE 'http://localhost:8000/exchange/id' \
--header 'Authorization: Basic staff_user_auth'
```

### Sample Responses

1. Response - OK

    ```json
    {
        "Status Code": 200,
        "Message": "Exchange successfully deleted"
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
