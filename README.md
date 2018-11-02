# Kaggle Home Credit Default Risk Competition
*Using feature engineering and LightGBM to build a bronze medal solution to the [Kaggle Home Credit Default Risk competition](https://www.kaggle.com/c/home-credit-default-risk).*

<img src="https://github.com/jamesdellinger/kaggle_home_credit_default_risk_competition/blob/master/images/thumb76_76.png" height="140">

## My Competition Solution
* [Notebook](http://nbviewer.jupyter.org/github/jamesdellinger/kaggle_home_credit_default_risk_competition/blob/master/kernel_home_credit_putting_all_the_steps_together_v10.ipynb)

## Final Leaderboard Result:
* 561st place solo-submission (out of 7,198 teams total); top 8%
* `0.79506` [private LB score](https://www.kaggle.com/c/home-credit-default-risk/leaderboard).
* My best performing kernel is [here on kaggle](https://www.kaggle.com/jamesdellinger/home-credit-putting-all-the-steps-together), and in the notebook just above.

## My Solution's Key Components
* LightGBM: https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree
* Feature engineering by hand/intuition, and through various aggregations
* Target encoding
* Mean rank prediction blending

## Background
* I participated in the [Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk) kaggle competition during June of 2018 in order to complete my [final project](https://github.com/jamesdellinger/machine_learning_nanodegree_capstone_project) for Udacity's Machine Learning Engineer nanodegree. At this time I earned a public leaderboard score of `0.74111`.
* I continued to refine my algorithm over the next two months, and was ultimately able to achieve a final private leaderboard score of `0.79506` when the competition ended on August 29, 2018.

## Competition Summary
* The goal of the [Home Credit Default Risk competition](https://www.kaggle.com/c/home-credit-default-risk) on Kaggle is the creation of a machine learning algorithm that is able to predict the likelihood that a loan applicant will make at least one late payment when repaying their loan. 
* The competition is sponsored by [Home Credit](http://www.homecredit.net), whose mission is to provide a positive and safe borrowing experience to groups of people that traditional, mainstream banks and financial institutions typically refuse to serve.

## Dependencies
* [requirements.txt](https://github.com/jamesdellinger/kaggle_home_credit_default_risk_competition/blob/master/requirements.txt)

* [environment.yml](https://github.com/jamesdellinger/kaggle_home_credit_default_risk_competition/blob/master/exploration.ipynb)