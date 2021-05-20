.. _raster-basics:

Raster basics
=============

Opening a raster file
---------------------

.. literalinclude:: code/raster-basics_open_file.py
        :lines: 2-8

Basic information about a Raster
--------------------------------

To print information directly to your console:

.. code:: python

        print(image)

.. program-output:: $PYTHON -c "exec(open('code/raster-basics_open_file.py').read()); print(image)"
        :shell:

If you'd like to retrieve a string of information about the raster to be saved
to a variable, output to a text file etc:


.. literalinclude:: code/raster-basics_open_file.py
        :lines: 10

With added stats:

.. literalinclude:: code/raster-basics_open_file.py
        :lines: 12

Then to write a file:

.. literalinclude:: code/raster-basics_open_file.py
        :lines: 14-15

Or just print nicely to console:

.. code:: python

        print(information)

.. program-output:: $PYTHON -c "exec(open('code/raster-basics_open_file.py').read()); print(information)" 
        :shell:

Reprojecting a Raster to fit another
------------------------------------

Comparing multiple rasters can often be a burden if multiple coordinate systems, bounding boxes, and resolutions are involved.
The ``Raster`` class simplifies this using two methods: ``Raster.crop()`` and ``Raster.reproject()``.

Cropping a raster
=================
:func:`geoutils.georaster.Raster.crop`

If a large raster should be cropped to a smaller extent without changing the uncropped data, this is possible through the crop function.
