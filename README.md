# stockPredictionRepo
Just exploring what I can do with LSTM RNN's and other modules people have provided.</br>

| DISCLAIMERS |
| ----------- |
| __Nothing__ in this repository is meant to be taken as __any__ sort of financial advice.
This was done purely for experimental and exploratory purposes while at an internship.
Items listed in the requirements were __NOT__ written by me. |

The `current_text.txt` file, although empty, is needed by many of the modules in the repository. __Do not delete it.__</br>

## Requirements:
* consistent internet access
* python 3
   * tested with and written in python 3.7.3
* tensorflow
   * pre 2.0.0
* pandas_datareader
* collections
* stockstats
* selenium
* datetime
* textblob
* sklearn
* random
* pandas
* numpy
* time
* csv
* os

## Important Notes:
* When creating a model for a company using `generateCompanyModel.py`, you are asked to provide the company's NASDAQ/NYSE ticker: `cur_ticker`, `seq_length`, `target_length`, and `indicator_arr`. These are written to the corresponding model's name (Ex. `LSTM_cur_ticker_seq:seq_length_target:target_length_ind:indicator_arr_copy:copy_amt.model`). The `copy_amt` simply states how many models there are with the same parameters (including itself) at the time of model generation.
* Each prediction uses the last `seq_length` days of information containing each indicator from the `indicator_arr` list all as reference data to predict whether the price will rise or fall in `target_length` days.
* When running either `getCompanyPrediction.py` or `testCompanyModel.py`, the `seq_length`, `target_length`, and `indicator_arr` variables must match a model in the `models` folder. If there is more than 1, you'll be asked to enter the `copy_amt` to indentify which model you want to use.
* All of the models in the repository, as of July 29, 2019, have `seq_length=60`, `target_length=30`, and `indicator_arr=['volume_delta', 'boll', 'macd', 'open_2_sma']` (these parameters yield the highest accuracies for whatever reason).
* Please refer to the stockstats documentation for a list of indicators to use: https://pypi.org/project/stockstats/

## How To Use:
1. Install requirements.
1. Clone this repository.
1. Go into the `stockPredictionRepo` folder.
   1. Ex: For Linux, while still in your terminal, simply run `cd stockPredictionRepo` right after cloning the repository.
1. Run `python FILENAME` using whichever python file with the name `FILENAME` you'd like to run. The table below represents all runnable python files.
</br>

| FILENAME | Description |
| -------- | ----------- |
| `generateCompanyModel.py` | Generates a model for your chosen company using the amount of epochs you entered. Saves the version of the model with the highest `val_acc` to the `models` folder. Most models took 30-50 epochs to get a good `val_acc`, and more epochs may increase the `val_acc` one tends to get (I haven't generated models using more than 50 epochs). |
| `getCompanyPrediction.py` | Uses a company's model from the `models` folder to try and predict whether the price of a particular company's stock will rise or fall `target_length` days from code execution. |
| `testCompanyModel.py` | Uses a company's model from the `models` folder to validate a particular company's most recent 5% of stock data. |
| `writeSentimentsToCSV.py` | Web-scrapes the current sentiment of your chosen companies and saves each company's current sentiment it its own CSV file (0=Bad, 1=Good). |
</br>

If you want to check how the losses and accuracies of all of the companies progressed over each epoch, type `tensorboard --logdir=logs` in your terminal while in the `stockPredictionRepo` directory. This doesn't require any previous code executed in the terminal or anything, you can do it straight from opening the terminal and entering `stockPredictionRepo`.</br>
Right click the link it gives you then open the link.</br>
When you're done, go back to your terminal and press `CTRL+C` to finish your viewing.</br>
Some of the models don't have logs; that's because I added the log functionality *after* generating some of the models.
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

__Nothing in this repository is meant to be taken as any sort of financial advice. Use at your own discretion.__</br>
#### Side Note:
I originally wanted to incorporate the sentiment analysis stuff into the LSTM RNN's, but I couldn't find any databases with enough data on companies' daily sentiments. Maybe if i left a computer on for 10 years getting daily sentiments, then I'd be able to use them. Oh well...</br>
</br>

# Have fun!
