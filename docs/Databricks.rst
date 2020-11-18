DataFrame
=========

Column function
---------------

.. code-block:: python

    from pyspark.sql.functions import col

Create a datatype schema
------------------------

.. code-block:: python

    from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, BooleanType
    from pyspark.sql.functions import from_json, unix_timestamp

    schema = StructType([
      StructField("channel", StringType(), True),
      StructField("comment", StringType(), True),
      StructField("delta", IntegerType(), True),
      StructField("flag", StringType(), True),
      StructField("geocoding", StructType([                 # (OBJECT): Added by the server, field contains IP address geocoding information for anonymous edit.
        StructField("city", StringType(), True),
        StructField("country", StringType(), True),
        StructField("countryCode2", StringType(), True),
        StructField("countryCode3", StringType(), True),
        StructField("stateProvince", StringType(), True),
        StructField("latitude", DoubleType(), True),
        StructField("longitude", DoubleType(), True),
      ]), True),
      StructField("isAnonymous", BooleanType(), True),      # (BOOLEAN): Whether or not the change was made by an anonymous user
      StructField("isNewPage", BooleanType(), True),
      StructField("isRobot", BooleanType(), True),
      StructField("isUnpatrolled", BooleanType(), True),
      StructField("namespace", StringType(), True),         # (STRING): Page's namespace. See https://en.wikipedia.org/wiki/Wikipedia:Namespace
      StructField("page", StringType(), True),              # (STRING): Printable name of the page that was edited
      StructField("pageURL", StringType(), True),           # (STRING): URL of the page that was edited
      StructField("timestamp", StringType(), True),         # (STRING): Time the edit occurred, in ISO-8601 format
      StructField("url", StringType(), True),
      StructField("user", StringType(), True),              # (STRING): User who made the edit or the IP address associated with the anonymous editor
      StructField("userURL", StringType(), True),
      StructField("wikipediaURL", StringType(), True),
      StructField("wikipedia", StringType(), True),         # (STRING): Short name of the Wikipedia that was edited (e.g., "en" for the English)
    ])


Start a Stream
--------------

For parquet source file:

.. code-block:: python

   # TODO
    dataPath = "/mnt/training/asa/flights/2007-01-stream.parquet/"

    parquetSchema = "DepartureAt timestamp, FlightDate string, DepTime string, CRSDepTime string, ArrTime string, " + \
    "CRSArrTime string, UniqueCarrier string, FlightNum integer, TailNum string, ActualElapsedTime string," + \
    " CRSElapsedTime string, AirTime string, ArrDelay string, DepDelay string, Origin string, Dest string, " + \
    "Distance string, TaxiIn string, TaxiOut string, Cancelled integer, CancellationCode string, Diverted integer," + \
    "CarrierDelay string, WeatherDelay string, NASDelay string, SecurityDelay string, LateAircraftDelay string"

    # Configure the shuffle partitions to match the number of cores
    spark.conf.set("spark.sql.shuffle.partitions", sc.defaultParallelism)

    streamDF = (spark                   # Start with the SparkSesion
      .readStream                       # Get the DataStreamReader
      .format('parquet')                # Configure the stream's source for the appropriate file type
      .schema(parquetSchema)            # Specify the parquet files' schema
      .option("maxFilesPerTrigger", 1)  # Restrict Spark to processing only 1 file per trigger
      .load(dataPath)                # Load the DataFrame specifying its location with dataPath
    )

Kafka Stream
~~~~~~~~~~~~

.. code-block:: python

    from pyspark.sql.functions import col
    spark.conf.set("spark.sql.shuffle.partitions", sc.defaultParallelism)

    kafkaServer = "server1.databricks.training:9092"   # US (Oregon)
    # kafkaServer = "server2.databricks.training:9092" # Singapore

    editsDF = (spark.readStream                        # Get the DataStreamReader
      .format("kafka")                                 # Specify the source format as "kafka"
      .option("kafka.bootstrap.servers", kafkaServer)  # Configure the Kafka server name and port
      .option("subscribe", "en")                       # Subscribe to the "en" Kafka topic
      .option("startingOffsets", "earliest")           # Rewind stream to beginning when we restart notebook
      .option("maxOffsetsPerTrigger", 1000)            # Throttle Kafka's processing of the streams
      .load()                                          # Load the DataFrame
      .select(col("value").cast("STRING"))             # Cast the "value" column to STRING
    )

Stop Streams
------------

.. code-block:: python

    for s in spark.streams.active: # Iterate over all active streams
      s.stop()                     # Stop the stream


Configure Suffle Partition
--------------------------

Configure the shuffle partitions to match the number of cores

.. code-block:: python

   spark.conf.set("spark.sql.shuffle.partitions", sc.defaultParallelism)


Unqued delayed event in stream
------------------------------

Ignore any events delayed by X minutes or more. And slidding windows.

.. code-block:: python

    from pyspark.sql.functions import col, window

    countsDF = (streamDF  # Start with the DataFrame
      .withWatermark("DepartureAt", "300 minutes")             # Specify the watermark
      .groupBy(col("UniqueCarrier"),
               window(col("DepartureAt"), "30 minutes"))            # Aggregate the data
      .count()            # Produce a count for each aggreate
      .select(col("window.start").alias("start"), # Elevate field to column
              col("count"),                       # Include count
              col("UniqueCarrier"))            # Add the column "hour", extracting it from "window.start"
    )

Train/Test Split in DataBricks
------------------------------

.. code-block:: python

    trainDF, testDF = preprocessedDF.randomSplit(
    [0.7, 0.3],  # 70-30 split
    seed=42)     # For reproducibility

