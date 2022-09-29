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

## Source datasets 
What datasets are you sourcing from?


### CoinAPI

- https://www.coinapi.io/

<br/>

### Alpaca

- Find coins available [here](https://alpaca.markets/learn/getting-started-with-alpaca-crypto-api/)
- Docs on Historical Crypto data can be found [here](https://alpaca.markets/docs/api-references/market-data-api/crypto-pricing-data/historical/)


Use the snippet below to curl in some historical data


```bash

curl --request GET 'https://data.alpaca.markets/v1beta2/crypto/trades?symbols=DOGE/USD&start=2022-03-01T00:00:00.00Z&end=2022-03-05T00:00:00.00Z' \
--header 'Apca-Api-Key-Id: <api-key-id>' \
--header 'Apca-Api-Secret-Key: <api-secret-key>'

```

<br/>

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
    <td>Stitching the ELT Pipeline Together</td>
    <td>Puneet, Helen</td>
  </tr>
  <tr>
    <td>Unit tests and documentation</td>
    <td>Puneet, Helen</td>
  </tr>
  <tr>
    <td>Transform</td>
    <td>Anoop, Rashid</td>
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


