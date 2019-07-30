# stockPredictionRepo
Just exploring what I can do with RNN's and other modules people have provided.</br>

| DISCLAIMER |
| ---------- |
| Nothing in this repository is meant to give you any sort of financial advice.
This was done purely for experimental and exploratory purposes while at an internship. |

The `current_text.txt` file, although empty, is needed by the `currentCompanySentiment.py` module. Do not delete it.</br>

## Requirements:
* consistend internet access
* python 3
   * tested with and written in Python 3.7.3
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
* csv
* os

### Important Notes:
* When first creating a model for a company using `generateCompanyModel.py`, you are asked to provide the company's name, `seq_length`, and `target_length`. These are appended to the `company_lengths.csv` file located in the repository after the model has been finished.
* Each prediction uses the last `seq_length` days of information as reference data to predict whether the price will rise or fall in `target_length` days.
* When running either `getCompanyPrediction.py` or `testCompanyModel.py`, the `seq_length` and `target_length` variables are taken from the row of the corresponding company in the `company_lengths.csv` file.
* All of the models in the repository, as of July 29, 2019, have `seq_length=60` and `target_length=30` (these lengths yield the highest accuracies for whatever reason).

## How To Use:
1. Install requirements.
1. Clone this repository.
1. Go into the stockPredictionRepo folder.
   1. Ex: For Linux, while still in your terminal, simply run `cd stockPredictionRepo` right after cloning the repository.
1. Run `python FILENAME` using whichever python file with the name `FILENAME` you'd like to run. The table below represents all runnable python files.
</br>

| FILENAME | Description |
| -------- | ----------- |
| `generateCompanyModel.py` | Generates a model for your chosen company. Saves the version of the model with the highest `val_acc` to the `models` folder. |
| `getCompanyPrediction.py` | Uses a company's model from the `models` folder to try and predict whether the price of a particular company's stock will rise or fall `seq_length` days from execution. Make sure that the `COMPANYNAME` you entered matches one of the models in the `models` folder (Ex. `LSTM_COMPANYNAME.model`). |
| `testCompanyModel.py` | Uses a company's model from the `models` folder to validate a particular company's most recent 5% of stock data. Make sure that the `COMPANYNAME` you entered matches one of the models in the `models` folder (Ex. `LSTM_COMPANYNAME.model`). |
| `writeSentimentToCSV.py` | Web-scrapes the current sentiment of a company and saves it in a unique CSV file (0=Bad, 1=Good). |
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

Again, please __do not interpret any of this as any sort of financial advice__. Use at your own discretion.</br>

#### Side Note:
I originally wanted to incorporate the sentiment analysis stuff into the RNN's, but I couldn't find any databases with enough data on companies' daily sentiments. Maybe if i left a computer on for 10 years getting daily sentiments, then I'd be able to use them. Oh well...</br>
</br>

### Have fun!
