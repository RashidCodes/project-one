# Project plan 

## Objective 
What would you like people to do with the data you have produced? Are you supporting BI or ML use-cases? 

<blockquote>The goal is provide crypto data for BI purposes.</blockquote>

<br/>

## Consumers 
What users would find your data useful?

<blockquote>Crypto investment bankers.</blockquote>

<br/>

## Questions 
What questions are you trying to solve with your data? 

1. Correlation between btc and eth prices.
2. General price trends (economic events)
3. Risk to reward ratio 
4. Portfolio optimisations with altcoins 


<br/>

## Source dataset

### CoinGecko API

- URL: https://algotrading101.com/learn/coingecko-api-guide/
- How to use :
1. Need to "pip install pycoingecko" first
2. Use required api documentation : https://www.coingecko.com/api/documentations/v3#
3. import the CoinGecko library and set the client up

```
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

<br/>


## Target database
There is a database named "crypto" created using Postgres and will be used as target database.

## ERD 

<img src='ERD.png' />

<br/>

## Extract & Load

### 1. Coins table: 
- Description: This table contains list of available coins using CoinGecko with only three columns required ('id','name','symbol').
- Type: Full , this means it will be fully extracted every time we run the code and will be loaded fully into the crypto database
- How it's getting extracted : In order to get a list of available coins using CoinGecko, the following needs to be done:

```
cg.get_coins_list()
```

So to extract coins table required for this project here is the code has been use: 
```
df = pd.DataFrame(cg.get_coins_list(), columns=['id','name','symbol'])
```


### 2. Trending table:
- Description: This table contains list of top 7 trends for the day. 
- Type: Full , this means it will be fully extracted every time we run the code and will be loaded fully into the crypto database
- How it's getting extracted : The following can be used to obtain the trending coins using CoinGecko:
```
cg.get_search_trending()
```

In this project, trending data has been extracted using below code, and then unnecessary columns are droped.
```
trend = cg.get_search_trending()
```

### 3. Coins_history table:
- Description: This table contains historical daily data (price , marketcap) for this list of coins ('bitcoin','litecoin','ethereum','solana' ,'umee','terra-luna','evmos','dejitaru-tsuka','reserve-rights-token','insights-network')
<br>
- Type: incremental, means it extracts data since the last day and upsert it into the correspondant table in crypto database
- How it's getting extracted : In this project, coins_history data has been extracted using below code, and then unnecessary columns are droped.
```
data = cg.get_coin_history_by_id(id=coin,date=date_variable, localization='false')
```

### 4. Coin_price_history table:
- Description: This table contains historical market data include price, market cap, and 24h volume. Data granularity is automatic  and cannot be adjusted.
- Type: incremental, it extracts 1 day from current time = 5 minute interval data
- How it's getting extracted : In this project, coin_price_history data has been extracted using below code. It loops through thist list of coins('bitcoin','litecoin','ethereum','solana' ,'umee','terra-luna','evmos','dejitaru-tsuka','reserve-rights-token','insights-network') and concatinate the data of each coin to to bottoim of the dataframe.
```
price_date = cg.get_coin_market_chart_by_id(id=coin,vs_currency='usd',days=number_of_days)
```

<br/>

## Transformation


<br>

## Breakdown of tasks 

<table>
  <tr>
    <th>Task</th>
    <th>Parties</th>
  </tr>
  <tr>
    <td>Extract and Load</td>
    <td>Puneet, Helen</td>
  </tr>
  <tr>
    <td>Transform</td>
    <td>Anoop, Rashid</td>
  </tr>
  <tr>
    <td>Stitching the ELT Pipeline Together</td>
    <td>Puneet, Helen, Anoop, Rashid</td>
  </tr>
  <tr>
    <td>Unit tests and documentation</td>
    <td>Puneet, Helen, Anoop, Rashid</td>
  </tr>
  <tr>
    <td>Dockerize solution</td>
    <td>Puneet, Helen, Anoop, Rashid</td>
  </tr>
  <tr>
    <td>Creating the AWS Services (RDS, ECS)</td>
    <td>Anoop, Rashid</td>
  </tr>
  <tr>
    <td>Pair program on deploying the solution to AWS </td>
    <td>Anoop, Rashid</td>
  </tr>
</table>


