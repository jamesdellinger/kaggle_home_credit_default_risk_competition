## Competition Data Overview
Home Credit needs an algorithm that will take as inputs various personal and alternative financial information originally taken from a loan applicant's profile, and then determine a probability of the applicant eventually becoming delinquent. This probability will be in the range [0.0, 1.0], where 1.0 represents a 100\% certainty that the applicant will make at least one late payment and 0.0 indicates that there is zero chance that the applicant will ever be delinquent. The algorithm will be tested on a set of 48,744 individuals who previously borrowed from Home Credit. A CSV file must be produced that contains one header row, and 48,744 prediction rows, where each prediction row contains both a user ID, the `SKI_ID_CURR` column, and the probability, the `TARGET` column, of that user repaying their loan. The file must be formatted as follows:

```
SK_ID_CURR,TARGET
100001,0.1
100005,0.9
100013,0.2
etc.
```

Home Credit knows which borrowers ultimately made at least one late payment, and which ones were never delinquent. A good algorithm will need to predict a high probability of delinquency for the majority of borrowers who did make a late payment. This algorithm will also need to predict a low probability of delinquency for the majority of borrowers who always paid on time.

The scoring metric for submissions is area under the [ROC curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic). The best performing submissions are ranked on the competition's [leaderboard](https://www.kaggle.com/c/home-credit-default-risk/leaderboard).

## Competition Data Tables
https://www.kaggle.com/c/home-credit-default-risk/data

In order to reproduce my results, the following eight CSV files must be downloaded and unzipped inside this `/data` directory:

<img src="https://github.com/jamesdellinger/kaggle_home_credit_default_risk_competition/blob/master/images/homecredit.png" height="700">

1. [application_test.csv.zip](https://www.kaggle.com/c/9120/download/application_test.csv.zip)
2. [application_train.csv.zip](https://www.kaggle.com/c/9120/download/application_train.csv.zip)
3. [bureau.csv.zip](https://www.kaggle.com/c/9120/download/bureau.csv.zip)
4. [bureau_balance.csv.zip](https://www.kaggle.com/c/9120/download/bureau_balance.csv.zip)
5. [credit_card_balance.csv.zip](https://www.kaggle.com/c/9120/download/credit_card_balance.csv.zip)
6. [installments_payments.csv.zip](https://www.kaggle.com/c/9120/download/installments_payments.csv.zip)
7. [POS_CASH_balance.csv.zip](https://www.kaggle.com/c/9120/download/POS_CASH_balance.csv.zip)
8. [previous_application.csv.zip](https://www.kaggle.com/c/9120/download/previous_application.csv.zip)
