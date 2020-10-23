Datetime
========

Create a range of dates
-----------------------

Creating a range of dates in a list of datetime.date objects. For instance ['2019-09-30', '2019-10-01', '2019-10-02', '2019-10-03', '2019-10-04'].

.. code-block:: python

   import datetime

   start_date = datetime.date(2019, 9 , 30)
   number_of_days = 5
   date_list = [(start_date + datetime.timedelta(days = day)).isoformat() \
                for day in range(number_of_days)]


