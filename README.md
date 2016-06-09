# pyspark-ide-starter

Basic Python project to run PySpark on your IDE

Clone this repository and follow the provided steps to work with a local PySpark on your IDE (IntelliJ Idea or PyCharm).

## Required downloads and installations

### Anaconda

Anaconda is a complete Python distribution embarking automatically the most common packages, and allowing an easy installation of new packages.

Download and install Anaconda (https://www.continuum.io/downloads).

### PyCharm or IntelliJ Idea

IntelliJ Idea is a complete IDE with, between others, Java, Scala and Python pluggins. PyCharm is an equivalent IDE, but with Python as only pluggin (therefore lighter).

Download one of those two IDEs (community edition)
* PyCharm: https://www.jetbrains.com/pycharm/download/
* IntelliJ Idea: https://www.jetbrains.com/idea/download/

If you choose IntelliJ Idea, you must install the Python pluggin, which is not incorporated by default.

### Spark

Download the latest, pre-built for Hadoop 2.6, version of Spark.
* Go to http://spark.apache.org/downloads.html
* Choose a release (prendre la dernière)
* Choose a package type: Pre-built for Hadoop 2.6 and later
* Choose a download type: Direct Download
* Click on the link in Step 4
* Once downloaded, unzip the file and place it in a directory of your choice

## IDE settings to work with PySpark

### Anaconda Interpreter

One first needs to add specific PySpark paths to the ones of the Anaconda Interpreter
* Open your chosen IDE
* Open the cloned Python project with the Anaconda Interpreter
* (IntelliJ only) File -> Project Structure -> SDKs -> your Anaconda interpreter
* (PyCharm only) File -> Default Settings -> Project Interpreter -> your Anaconda interpreter
* (PyCharm only) Click on the "..." icon on the right of your interpreter path, then on "More...", your project interpreter, and finally on the last icon on the bottom right ("Show paths for the selected interpreter")
* Click on "+"
* Select your_path_to_spark/spark-X.X.X-bin-hadoopX.X/python
* "OK"
* Click once again on "+"
* Select your_path_to_spark/spark-X.X.X-bin-hadoopX.X/python/lib/py4j-X.X-src.zip
* Cliquer sur OK
* OK -> Apply -> OK

### Project's environment variables

Finally, we have to set the specific PySpark environment variables to be able to run it in local.

* Run -> Edit Configurations -> Defaults -> Python
* In the "Environment variables" section, click on "...", then on "+"
* Cliquer sur l'icône "+"
* Name: PYTHONPATH 
* Value: your_path_to_spark/spark-X.X.X-bin-hadoopX.X/python:your_path_to_spark/spark-X.X.X-bin-hadoopX.X/python/lib/py4j-X.X-src.zip
* Click again on "+"
* Name: SPARK_HOME
* Value: your_path_to_spark/spark-X.X.X-bin-hadoopX.X
* OK -> Apply
* Add the same paths for each test module you will use (Python tests - Unittests for example). Add them for every test module to not have any problem later
* OK

The PySpark imports in your code should now be recognized, and the code should be able to run without any error.
