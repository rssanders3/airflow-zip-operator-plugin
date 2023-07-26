# airflow-zip-operator-plugin

## Description

A plugin to Apache Airflow (Documentation: https://pythonhosted.org/airflow/, Source Code: https://github.com/apache/incubator-airflow) to allow you to run Zip and UnZip commands as an Operator from Workflows

## TODO List

* Print out metrics about zip file (compression, size, etc)
* Test extensively

## How do Deploy

1. Copy the zip_operator_plugin.py file into the Airflow Plugins directory

    * The Airflow Plugins Directory is defined in the airflow.cfg file as the variable "plugins_folder"
    
    * The Airflow Plugins Directory is, by default, ${AIRFLOW_HOME}/plugins
    
    * You may have to create the Airflow Plugins Directory folder as it is not created by default
    
    * quick way of doing this:
    
        $ cd {AIRFLOW_PLUGINS_FOLDER}
        $ wget https://raw.githubusercontent.com/rssanders3/airflow-zip-operator-plugin/master/zip_operator_plugin.py
 
2. Restart the Airflow Services

3. Create or Deploy DAGs which utilize the Operator

4. Your done!

## ZipOperator

### Operator Definition

class **zip_operator_plugin.ZipOperator**(input_file_path, output_file_path, *args, **kwargs)

Bases: **airflow.operators.BaseOperator**

An operator which takes in a path to a file and zips the contents to a location you define. 

Parameters:

* **path_to_file_to_zip** (string) - Full path to the file you want to Zip
* **path_to_save_zip** (string) - Full path to where you want to save the Zip file

### Example

    ```
    from zip_operator_plugin import ZipOperator
    
    zip_task = ZipOperator(
        task_id='zip_task',
        path_to_file_to_zip="/path/to/file",
        path_to_save_zip="/path/to/file.zip",
        dag=dag)
    ```

## UnzipOperator


### Operator Definition

class **zip_operator_plugin.UnzipOperator**(input_file_path, output_file_path, *args, **kwargs)

Bases: **airflow.operators.BaseOperator**

An operator which takes in a path to a zip file and unzips the contents to a location you define. 

Parameters:

* **path_to_zip_file** (string) - Full path to the zip file you want to Unzip
* **path_to_unzip_contents** (string) - Full path to where you want to save the contents of the Zip file you're Unzipping

### Example

    ```
    from zip_operator_plugin import UnzipOperator
    
    unzip_task = UnzipOperator(
        task_id='unzip_task',
        path_to_zip_file="/path/to/file.zip",
        path_to_unzip_contents="/path/to/unzip/to/",
        dag=dag)
    ```
