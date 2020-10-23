Image
=====

Load Images
-----------

.. code-block:: python

    from PIL import Image
    im = Image.open("bride.jpg")

Resize an Image
---------------

.. code-block:: python

    from PIL import Image
    im = im.resize((160,300),Image.ANTIALIAS)
