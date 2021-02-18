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

    sns.set(style='whitegrid', palette='muted', font_scale=1.2)

    HAPPY_COLORS_PALETTE = ["#01BEFE", "#FFDD00", "#FF7D00", "#FF006D", "#ADFF02", "#8F00FF"]

    sns.set_palette(sns.color_palette(HAPPY_COLORS_PALETTE))

    rcParams['figure.figsize'] = 12, 8
