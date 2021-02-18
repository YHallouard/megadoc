Metrics
=======

Distances
---------

Wasserstein
~~~~~~~~~~~

In mathematics, the `Wasserstein`_ distance or Kantorovich–Rubinstein metric is a distance function defined between probability distributions on a given metric space
M.

.. _Wasserstein: https://en.wikipedia.org/wiki/Wasserstein_metric

.. code-block:: python

   from scipy.stats import wasserstein_distance, beta

   wasserstein_distance([1,2,3,4],[1,2,3,4,4])
   x = np.linspace(0, 1, 100)
   dist1 = stats.beta.pdf(x,5,5)
   dist2 = stats.beta.pdf(x,8,5)
   ws_distance = wasserstein_distance(dist1,dist2)


Sklearn Metrics
~~~~~~~~~~~~~~~
To import or get the short name of all metrics in sklearn.

.. code-block:: python

    from sklearn.metrics import SCORERS
    SCORERS.keys()
