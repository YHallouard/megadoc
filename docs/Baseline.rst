Baseline
========

Classifier
----------

.. code-block:: python

   import numpy as np
   from sklearn.dummy import DummyClassifier

   dummy_clf = DummyClassifier(strategy="most_frequent")
   dummy_clf.fit(X_train, y_train)

   dummy_clf.predict(X_test)
   dummy_clf.score(X_test, y_test)



Regressor
---------

.. code-block:: python

   import numpy as np
   from sklearn.dummy import DummyRegressor

   dummy_regr = DummyRegressor(strategy="mean")
   dummy_regr.fit(X_train, y_train)

   dummy_regr.predict(X_test)
   dummy_regr.score(X_test, y_test)
