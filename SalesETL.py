# imports required modules for this project
import io
import requests
import zipfile
import pandas as pd

# 1
# retrives a data table from url (check getURL below) and 
# read from zip archive file
# puts the data into pandas dataframe

def getDataFromURL(url):

  # create in-memory file like object to retrieve the data
  zipBytes = io.BytesIO(requests.get(url).content)

  # read and retrieve .html content from zip archive
  with zipfile.ZipFile(zipBytes) as zipContent:
    htmlContent = zipContent.read('salesData.html')

  # initialize a pandas dataframe
  # selects a first table using [0], even though there is only one table in html document.
  dataFrame = pd.read_html(htmlContent)[0]

  return dataFrame

# 2
# to group by date and item
# grouped table with column date, product, sales and quantity

def groupByDateAndItem(data):
  groupedData = data.groupby(["Order Date", "Product"]).agg(sales = ("Sales", "sum"),
       quantity = ("Quantity Ordered", "sum"))
  return groupedData

# 3
# add a column name 'Owner'

def addOwnerColumn(df, name):
  df["Owner"] = name
  return df

# 4 
# Convert the dataframe to json and post it to a url (check postURL below)
# retrive status 200 when the data is achieved

def postJSONData(url, df):
  jsonData = df.to_dict(orient='records') # each records are converted to dict object 
  
  response = requests.post(
      url,
      json=jsonData
  )

  print(f'Status Code: {response.status_code}')

# the placement if URL should be in .env file. 
# This is for a Demo Only
# link to retrieve data table from 
getURL = 'https://abc.zipped./retrieveData?'

# Owner Name to add to all the column
# This could be another own function to add specific owner name to respective products.
ownerName = 'Pemba Gurung'

# link to post the data table to
postURL = 'https://to.post.thedata.to'

###############################################################################
# call the functions

# initialize dataframe from the url
df = getDataFromURL(getURL)

# group data by date and item
updatedData = groupByDateAndItem(df)

# Add owner field and 'Pemba Gurung' in all rows.
updatedData = addOwnerColumn(updatedData, ownerName)

# display the updated data after grouped and added coloumn
print(updatedData)

# post it to URL and returns 200 for status code when data is recieved
postJSONData(postURL, updatedData)
