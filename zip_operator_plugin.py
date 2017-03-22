__author__ = 'rssanders3'

from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
from airflow.utils import apply_defaults
import logging


class ZipOperator(BaseOperator):
    """
    An operator which takes in a path to a file and zips the contents to a location you define.

    :param input_file_path: Full path to the file you want to Zip
    :type input_file_path: string
    :param output_file_path: Full path to where you want to save the Zip file
    :type output_file_path: string
    """

    template_fields = ('input_file_path', 'output_file_path')
    template_ext = []
    ui_color = '#ffffff'  # ZipOperator's Main Color: white  # todo: find better color

    @apply_defaults
    def __init__(
            self,
            input_file_path,
            output_file_path,
            *args, **kwargs):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def execute(self, context):
        logging.info("Executing ZipOperator.execute(context)")

        logging.warning("Action still needs to be implemented")

        logging.info("Finished executing ZipOperator.execute(context)")


class UnzipOperator(BaseOperator):
    """
    An operator which takes in a path to a zip file and unzips the contents to a location you define.

    :param input_file_path: Full path to the zip file you want to Unzip
    :type input_file_path: string
    :param output_file_path: Full path to where you want to save the contents of the Zip file you're Unzipping
    :type output_file_path: string
    """

    template_fields = ('input_file_path', 'output_file_path')
    template_ext = []
    ui_color = '#ffffff'  # UnzipOperator's Main Color: white  # todo: find better color

    @apply_defaults
    def __init__(
            self,
            input_file_path,
            output_file_path,
            *args, **kwargs):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def execute(self, context):
        logging.info("Executing UnzipOperator.execute(context)")

        logging.warning("Action still needs to be implemented")

        logging.info("Finished executing UnzipOperator.execute(context)")


# Defining the plugin class
class ZipOperatorPlugin(AirflowPlugin):
    name = "zip_operator_plugin"
    operators = [ZipOperator, UnzipOperator]
    flask_blueprints = []
    hooks = []
    executors = []
    admin_views = []
    menu_links = []
