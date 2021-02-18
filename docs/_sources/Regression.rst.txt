Regression
==========

Sklearn Linear Regression
-------------------------

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

Pyspark Linear Regression
-------------------------

Train
~~~~~

With train_df being a spark DataFrame.

.. code-block:: python

    from pyspark.ml.regression import LinearRegression

    lr = LinearRegression(featuresCol = 'features', labelCol='MV', maxIter=10, regParam=0.3, elasticNetParam=0.8)
    lr_model = lr.fit(train_df)

Get Parameters
~~~~~~~~~~~~~~
.. code-block:: python

    lr_model.coefficients
    lr_model.intercept

Summary
~~~~~~~

.. code-block:: python

    trainingSummary = lr_model.summary
    print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
    print("r2: %f" % trainingSummary.r2)

Predict
~~~~~~~

.. code-block:: python

    lr_predictions = lr_model.transform(test_df)
    lr_predictions.select("prediction","MV","features").show(5)

Evaluation
~~~~~~~~~~

.. code-block:: python

    from pyspark.ml.evaluation import RegressionEvaluator

    lr_evaluator = RegressionEvaluator(predictionCol="prediction", \
                     labelCol="MV",metricName="r2")
    print("R Squared (R2) on test data = %g" % lr_evaluator.evaluate(lr_predictions))
