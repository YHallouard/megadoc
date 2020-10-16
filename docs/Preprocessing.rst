Prepocessing
============

Train test split
################

Split your dataset into train and test part.

.. code-block:: python

   from sklearn.model_selection import train_test_split

   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

If you want to conserve target balancement between classes (in classification), you should use stratify parameter.

.. code-block:: python

   X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2)