DataFrame
=========

Group by
--------

- Group a dataframe by a group of columns with different aggregations columns.

.. code-block:: python

    dataframe.groupby(['Name', 'Fruit'])['Number'].agg('sum')

- You can also use different aggregation functions on different columns.

.. code-block:: python

    dataframe.groupby(['Name', 'Fruit'])['Number, att1, att2'].agg({'Name': "count", 'att1': "sum",'att2': 'mean'})

- You can also use custom aggregation functions

.. code-block:: python

    dataframe.groupby("date").agg({"duration": np.sum, "user_id": lambda x: x.nunique()})

Aggregation Methods
~~~~~~~~~~~~~~~~~~~

- sum
- mean
- count
- nunique

MultiIndex
----------

Remove MultiIndex
~~~~~~~~~~~~~~~~~

To split multi index to columns :

.. code-block:: python

    dataframe.reset_index()


Turn that :

+------------+------------+-----------+-----------+
|                         |      att1 |      att2 |
+============+============+===========+===========+
| departement| day        |           |           |
+------------+------------+-----------+-----------+
| 1          |01/01/2020  |  0.083    | 0.083     |
+------------+------------+-----------+-----------+
|            |02/01/2020  |   0.083   |  0.083    |
+------------+------------+-----------+-----------+
|            |03/01/2020  |    0.083  | 0.083     |
+------------+------------+-----------+-----------+

To that :

+------------+------------+-----------+-----------+-----------+
|            | departement|      day  |      att1 |      att2 |
+============+============+===========+===========+===========+
|  index     |            |           |           |           |
+------------+------------+-----------+-----------+-----------+
| 1          | 1          |01/01/2020 | 0.083     | 0.083     |
+------------+------------+-----------+-----------+-----------+
| 2          | 1          |02/01/2020 |  0.083    | 0.083     |
+------------+------------+-----------+-----------+-----------+
| 3          | 1          |03/01/2020 | 0.083     | 0.083     |
+------------+------------+-----------+-----------+-----------+

Sort On
--------

DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

.. code-block:: python

    df.sort_values(by=['col1'])