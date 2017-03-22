# airflow-zip-operator-plugin

## Description

A plugin to Apache Airflow (Documentation: https://pythonhosted.org/airflow/, Source Code: https://github.com/apache/incubator-airflow) to allow you to run Zip and UnZip commands as an Operator from Workflows

## TODO List

* Complete the ZipOperator
* Complete the UnzipOperator
* Test extensively

## How do Deploy
 
1. Copy the zip_operator_plugin.py file into the Airflow Plugins directory

    * The Airflow Plugins Directory is defined in the airflow.cfg file as the variable "plugins_folder"
    
    * The Airflow Plugins Directory is, by default, ${AIRFLOW_HOME}/plugins
    
    * You may have to create the Airflow Plugins Directory folder as it is not created by default
 
2. Restart the Airflow Services

3. Your done!

## ZipOperator - TO BE COMPLETED

### Operator Definition

class **airflow.operators.ZipOperator**(input_file_path, output_file_path, *args, **kwargs)

Bases: **airflow.operators.BaseOperator**

An operator which takes in a path to a file and zips the contents to a location you define. 

Parameters:

* **input_file_path** (string) - Full path to the file you want to Zip
* **output_file_path** (string) - Full path to where you want to save the Zip file

### Example

    ```
    from airflow.operators import ZipOperator
    ```

## UnzipOperator - TO BE COMPLETED


### Operator Definition

class **airflow.operators.UnzipOperator**(input_file_path, output_file_path, *args, **kwargs)

Bases: **airflow.operators.BaseOperator**

An operator which takes in a path to a zip file and unzips the contents to a location you define. 

Parameters:

* **input_file_path** (string) - Full path to the zip file you want to Unzip
* **output_file_path** (string) - Full path to where you want to save the contents of the Zip file you're Unzipping

### Example

    ```
    from airflow.operators import UnzipOperator
    ```
