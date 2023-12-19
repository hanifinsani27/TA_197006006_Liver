#!/usr/bin/env python3

# Liver Prediction Using Support Vector Machine
import pickle
import os
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# For training
def train():
    dataset = pd.read_csv('liver.csv')
    # X = dataset[['Total_Protiens', 'Albumin', 'Alkaline_Phosphotase']]
    # Y = dataset[['Dataset']]

    # mengganti nilai 0 dengan nan
    data_modified = dataset.copy(deep=True)
    data_modified[["Albumin_and_Globulin_Ratio"]] = data_modified[
        ["Albumin_and_Globulin_Ratio"]].replace(0, np.NaN)

    # mengganti nilai nan dengan mean dan median
    data_modified["Albumin_and_Globulin_Ratio"].fillna(data_modified["Albumin_and_Globulin_Ratio"].mean(), inplace=True)

    x = data_modified[['Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio']]
    y = data_modified[['Dataset']]

    # train test split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=12)

    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier(criterion = "entropy", random_state = 0, splitter=best, max_depth = 3)
    svc = model.fit(x_train, y_train)

    # Save Model Menjadi Pickle
    with open('tree.pkl', 'wb') as m:
        pickle.dump(svc, m)
    test(x_test, y_test)

# Test accuracy model
def test(x_test, y_test):
    with open('tree.pkl', 'rb') as mod:
        p = pickle.load(mod)

    pre = p.predict(x_test)
    print(accuracy_score(y_test, pre))  # Prints the accuracy of the model


def find_data_file(filename):
    if getattr(sys, "frozen", False):
        # The application is frozen.
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen.
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)


def check_input(data) -> int:
    df = pd.DataFrame(data=data, index=[0])
    with open(find_data_file('tree.pkl'), 'rb') as model:
        p = pickle.load(model)
    op = p.predict(df)
    return op[0]


if __name__ == '__main__':
    train()
