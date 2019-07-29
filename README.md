#stockPredictionRepo
Just exploring what I can do with RNN's and other modules people have provided.

####DISCLAIMER
Nothing in this repository is meant to give you any sort of financial advice. This was done purely for experimental and exploratory purposes while at an internship.

__Requires Python 3__
* Tested with and written in Python 3.7.3.

##Required modules:
* tensorflow
  * pre 2.0.0
* numpy
* pandas
* pandas_datareader
* stockstats
* textblob
* selenium
* datetime
* collections
* sklearn
* random
* time

##How to use:
1. Install requirements.
1. Clone this repository.
1. Go into the stockPredictionRepo folder.
   1. Ex: For Linux, simply run '<cd stockPredictionRepo>' right after cloning the repository in your terminal.
1. Run '<python *FILENAME*>' using whichever python file with the name '<*FILENAME*>' you'd like to run. Here's a list of runnable files:
   1. '<generateCompanyModel.py>' || Generates a model for each epoch and puts it in the models folder. Pick the model you like most, rename it to '<RNN_NAMEOFCOMPANY.model>' (Ex. '<RNN_Yelp.model>'), then move it to the '<best_models>' folder.
   1. '<getCompanyPrediction.py>' || Tries to predict whether the price of a particular company's stock will go up or down in the next 30 days.
   1. '<testCompanyModel.py>' || Uses your chosen model from the '<best_models>' folder to validate that particular company's most recent 5% of stock data. Just make sure that the company name you entered matches one of the models in the '<best_models>' folder.
   1. '<writeSentimentToCSV.py>' || Web-scrapes the current sentiment of a company and saves it in a unique CSV file.


Models generated using this repo are of a specific form: each prediction uses the last 60 days of information as reference data to predict whether the price will rise or fall in 30 days.

Again, please __do not interpret any of this as any sort of financial advice__. Use at your own discretion.


######Model accuracies as of July 29, 2019:
AAPL (Apple): 73.67%
AMZN (Amazon): 75.00%
F (Ford): 63.68%
GOOGL (Google): 65.62%
KO (Coca-Cola): 59.11%
MSFT (Microsoft): 60.76%
NVDA (Nvidia): 68.24%
SBUX (Starbucks): 91.46%
TSLA (Tesla): 90.62%
UPS (United Parcel Services): 67.72%


###Have fun!
Side-note: I originally wanted to incorporate the sentiment analysis stuff into the RNN's, but I couldn't find any databases with enough data on companies' daily sentiments. Maybe if i left a computer on for 10 years getting daily sentiments, then I'd be able to use them. Oh well...
