# Credit-Card-Fraud-Detection-PGDCLOUD-2022-AWS
 Cloud Machine Learning (PGDCLOUD_SEP) 2022


Balazs Barcza 
 x19190638  
Christoph Kratz 
 x21111898  
Wislan Alandes De Lima Arruda 
 x21126151 
 

Abstract—Credit card fraud has been a problem for businesses and financial institutions for decades, resulting, in recent years, in billions of dollars in losses on a yearly basis. To take on the large amount of data generated around financial transactions, large computing resources will be required. Additionally, to review large numbers of transactions in an efficient and timely manner, human review would not be suitable. Therefore, to address these challenges machine learning in the cloud seems to be the solution. With this project, we cover many aspects of fraudulent transactions, as well as a model based on supervised learning techniques such as Decision Tree (DT), and Logistic Regression (LR). It makes use of the Simulated Credit Card Transactions generated using Sparkov. It simulates the transactions of 1000 customers doing transactions with a pool of 800 merchants that was run from the duration 1st Jan 2019 to 31st Dec 2020. The purpose of this study is to predict the likelihood of transactions being fraudulent using machine learning models and deploy it to the cloud. The findings show that Decision Tree Model achieves the best recall and accuracy scores (94%). 

Keywords—credit card, fraud, cloud computing, machine learning, Amazon Web Services (AWS) 

This project has the following components:

a) IEEE style Paper in PDF format

b) Jupyter Notebook walking through machine learning tests conducted. You can run view and run them yourself. Included are also comments, reasoning, and figures. For your convenience I have included a copy of the original dataset [1] in this git repo, however please refer to the original source for the most up-to-date version.

Installation
Clone the project:

$ git clone https://github.com/Balays33/Credit-Card-Fraud-Detection-PGDCLOUD-2022-AWS.git

Pip-install dependencies. For example using a virtualenv:

$ virtualenv env && source env/bin/activate && pip install -r requirements.txt


Usage
a) Read the Paper (PDF):

credit_card_fraud_detection.pdf

b) Run the Jupyter Notebook:

find the the dataset:
$ https://www.kaggle.com/datasets/kartik2112/fraud-detection/code

Generate a balanced dataset using ADASYN resampling (this will take several minutes):
$ python app.py

Run the notebook:
$ jupyter notebook
