Classification
==============

Unbalance Dataset
-----------------

Multiclasse Classification
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Sklearn utils

.. code-block:: python

    from sklearn.utils import class_weight
    class_weight = class_weight.compute_class_weight('balanced,
                                                     np.unique(y_train),
                                                     y_train)
    model = LogisticRegression(class_weight = class_weight)
    model.fit(X_train, y_train)

- Counts to Length. #(TODO : fill when used)
- Smoothen Weights. #(TODO : fill when used)
- Sample Weight Strategy, for XGBoost #(TODO : fill when used)
