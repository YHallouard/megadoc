Regression
==========

Linear Regression
-----------------

Train
~~~~~

.. code-block:: python

   from sklearn.linear_model import LinearRegression
   X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
   # y = 1 * x_0 + 2 * x_1 + 3
   y = np.dot(X, np.array([1, 2])) + 3
   reg = LinearRegression().fit(X, y)
   reg.score(X, y)

Get Parameters
~~~~~~~~~~~~~~
.. code-block:: python

   reg.coef_
   reg.intercept_

Predict
~~~~~~~
.. code-block:: python

   reg.predict(np.array([[3, 5]]))