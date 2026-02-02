## The Project Description

The Goal of this project is to extract data from a zipped HTML document, tranform the data and load the transformed data to an external API in JSON format. This project is built in a scalable manner, so we can pass in a dataframe as often as we need.

## Features

- First, extracts the data and load it into a pandas dataframe.

## Display Data

![Extracted Data](./images/DataFrame.png)

- After the script groups the data by date and item,
  It shows the aggregated sales and units for each item on each day.
  Every row have an entry for order date, product, sales, and quantity.

## Transformed Data

![Tranfromed Data](./images/AggregatedData.png)

## Post Data to External URL

- Atlast, the dataframe is converted to json and post it to external API for downstream application. Successful post will return HTTP status code 200.

![API Delivery Data](./images/PostData.png)
