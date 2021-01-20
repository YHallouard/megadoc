Vizualisation
=============

Saving a figure
###############

.. code-block:: python

   import matplotlib.pyplot as plt

   fig = plt.figure()
   plt.plot(range(10))
   fig.savefig('temp.png', dpi=fig.dpi)

Improve Plotting
################

.. code-block:: python

    %matplotlib inline
    %config InlineBackend.figure_format='retina'
