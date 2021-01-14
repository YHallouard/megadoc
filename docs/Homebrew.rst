HomeBrew
=========

Change python version
---------------------
Print the list of python version installed:

.. code-block:: bash
    brew list | grep python

Switch python version

.. code-block:: bash
    brew unlink python@3.9
    brew link --force python@3.8



