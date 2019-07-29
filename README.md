# stockPredictionRepo
Just exploring what I can do with RNN's and other modules people have provided.
</br>
</br>
</br>

## DISCLAIMER
Nothing in this repository is meant to give you any sort of financial advice. This was done purely for experimental and exploratory purposes while at an internship.
</br>
</br>

__Requires Python 3__
* Tested with and written in Python 3.7.3.
</br>

## Required modules:
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
</br>
</br>

## How to use:
1. Install requirements.
1. Clone this repository.
1. Go into the stockPredictionRepo folder.
   1. Ex: For Linux, simply run `cd stockPredictionRepo` right after cloning the repository in your terminal.
1. Run `python FILENAME` using whichever python file with the name `FILENAME` you'd like to run. Here's a list of runnable files:

| FILENAME | Description |
| --- | --- |
| `generateCompanyModel.py` | Generates a model for each epoch and puts it in the models folder. Pick the model you like most, rename it to `RNN_NAMEOFCOMPANY.model` (Ex. `RNN_Yelp.model`), then move it to the `best_models` folder. |
| `getCompanyPrediction.py` | Tries to predict whether the price of a particular company's stock will go up or down in the next 30 days. |
| `testCompanyModel.py` | Uses your chosen model from the `best_models` folder to validate that particular company's most recent 5% of stock data. Just make sure that the company name you entered matches one of the models in the `best_models` folder. |
| `writeSentimentToCSV.py` | Web-scrapes the current sentiment of a company and saves it in a unique CSV file. |
</br>
</br>
</br>

Models generated using this repo are of a specific form: each prediction uses the last 60 days of information as reference data to predict whether the price will rise or fall in 30 days.
</br>
</br>

Again, please __do not interpret any of this as any sort of financial advice__. Use at your own discretion.
</br>
</br>
</br>

| Company | Model Accuracy as of July 29, 2019 |
| ------- | ---------------------------------- |
| Apple | 73.67% |
| Amazon | 75.00% |
| Ford | 63.68% |
| Google | 65.62% |
| Coca-Cola | 59.11% |
| Microsoft | 60.76% |
| Nvidia | 68.24% |
| Starbucks | 91.46% |
| Tesla | 90.62% |
| UPS | 67.72% |
</br>
</br>

### Have fun!
Side-note: I originally wanted to incorporate the sentiment analysis stuff into the RNN's, but I couldn't find any databases with enough data on companies' daily sentiments. Maybe if i left a computer on for 10 years getting daily sentiments, then I'd be able to use them. Oh well...
