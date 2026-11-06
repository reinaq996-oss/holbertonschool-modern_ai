#!/usr/bin/env python3
"""Encode customer features and return fitted target and ordinal encoders."""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Return an encoded copy and fitted churn, binary, and tenure encoders."""
    encoded = df.copy()
    churn_le = preprocessing.LabelEncoder()
    encoded['Churn'] = churn_le.fit_transform(encoded['Churn'])

    binary_columns = ['Partner', 'Dependents', 'PaperlessBilling',
                      'SeniorCitizen']
    binary_oe = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])
    binary_oe.fit(encoded[binary_columns].to_numpy().reshape(-1, 1))
    for column in binary_columns:
        encoded[column] = binary_oe.transform(
            encoded[[column]].to_numpy()
        ).ravel().astype('int64')

    tenure_oe = preprocessing.OrdinalEncoder()
    encoded[['TenureGroup']] = tenure_oe.fit_transform(
        encoded[['TenureGroup']]
    ).astype('int64')

    one_hot_columns = ['Contract', 'PaymentMethod']
    one_hot = preprocessing.OneHotEncoder(drop='first', dtype='int64')
    values = one_hot.fit_transform(encoded[one_hot_columns]).toarray()
    dummy_columns = pd.DataFrame(
        values, index=encoded.index,
        columns=one_hot.get_feature_names_out(one_hot_columns)
    )
    encoded = pd.concat(
        [encoded.drop(columns=one_hot_columns), dummy_columns], axis=1
    )
    return encoded, churn_le, binary_oe, tenure_oe
