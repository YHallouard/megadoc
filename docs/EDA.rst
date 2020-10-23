Exploratory Data Analysis
=========================

Missing Values Analysis
-----------------------

Interring way tp plot missing values.

.. code-block:: python

    import missingno as msno

    missingdata_df = data.columns[data.isnull().any()].tolist()
    msno.matrix(data[missingdata_df])

Correlation Matrix
------------------

Plotting correlation Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python


    import seaborn as sns
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(15, 15))
    ax = sns.heatmap(corr, annot=False, ax=ax, cmap="Blues");
    ax.set_title("Cramer V Correlation between Variables");