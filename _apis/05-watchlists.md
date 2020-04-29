---
title: APIs for Watchlists
permalink: /apis/watchlists
toc: true
---


## Get all Watches

**GET Request** - `/watches`
{: .notice--info}

```bash
curl --location --request GET 'http://localhost:8000/watches' \
--header 'Authorization: Basic user_auth'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "subscriptions": [
        {
          "exhange": "BTC",
          "currency": "USD"
        },
        {
          "exhange": "BTC",
          "currency": "ETH"
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

## Create a Watchlist

**PUT Request** - `/watch/exchange_name/currency_name`
{: .notice--info}

```bash
curl --location --request PUT 'http://localhost:8000/watch/exchange_name/currency_name' \
--header 'Authorization: Basic user_auth'
```

### Sample Responses

1. Response - OK

    ```json
    {
      "Status Code": 200,
      "Message": "Successfully subscribed"
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

## Delete a Watch

**DELETE Request** - `/watch/exchange_name/currency_name`
{: .notice--info}

```bash
curl --location --request DELETE 'http://localhost:8000/watch/exchange_name/currency_name' \
--header 'Authorization: Basic user_auth'
```

### Sample Responses

1. Response - OK

    ```json
    {
        "Status Code": 200,
        "Message": "Successfully unsubscribed"
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
        "Message": "Currency not found"
    }
    ```
5. Response - Not Found

    ```json
    {
        "Status Code": 404,
        "Message": "Exchange not found"
    }
    ```
6. Response - Unprocessable Entity

    ```json
    {
        "Status Code": 422,
        "Message": "Already not subscribed"
    }
    ```
