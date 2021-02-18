Pipeline
========

Union pipeline
--------------

Using sklego to create different pipeline for categorical and numerical features.

.. code-block:: python

    from sklearn.pipeline import make_union, make_pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.impute import SimpleImputer

    from sklego.preprocessing import PandasTypeSelector


    cat_features_preprocessing = make_pipeline(PandasTypeSelector(exclude='number'),
                                               SimpleImputer(strategy='constant', fill_value='unknown'),
                                               OneHotEncoder(categories=[['normal', 'sth', 'fixed']], handle_unknown='ignore'))

    num_features_preprocessing = make_pipeline(PandasTypeSelector(include='number'),
                                               SimpleImputer(strategy='median'),
                                               StandardScaler())

    preprocessor = make_union(cat_features_preprocessing, num_features_preprocessing)

