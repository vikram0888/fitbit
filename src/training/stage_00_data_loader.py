import os
import sys
import shutil
from src.utility import read_params
import a

from src.utility import get_logger_object_of_training
from src.utility import clean_data_source_dir, download_file_from_cloud
from webapp.exception_layer.generic_exception.generic_exception import GenericException

log_collection_name = "data_loader"


def loader_main(config_path: str, datasource: str, is_logging_enable=True,execution_id=None,executed_by=None) -> None:
    try:
        logger = get_logger_object_of_training(config_path=config_path, collection_name=log_collection_name,
                                               execution_id=execution_id,executed_by=executed_by)
        logger.is_log_enable = is_logging_enable
        logger.log("Starting data loading operation.\nReading configuration file.")

        config = read_params(config_path)

        cloud_provider = config['cloud_provider']['name']
        status = config['cloud_provider']['is_enabled']
        downloader_path = config['data_download']['cloud_training_directory_path']
        download_path = config['data_source']['Training_Batch_Files']

        logger.log("Configuration detail has been fetched from configuration file.")
        # removing existing training and additional training files from local
        logger.log(f"Cleaning local directory [{download_path}]  for training.")
        clean_data_source_dir(download_path, logger=logger,
                              is_logging_enable=is_logging_enable)  # removing existing file from local system

        logger.log(f"Cleaning completed. Directory has been cleared now  [{download_path}]")
        # downloading traning and additional training file from cloud into local system
        logger.log("Data will be downloaded from cloud storage into local system")
        if int(status):
            download_file_from_cloud(cloud_provider=cloud_provider,
                                     cloud_directory_path=downloader_path,
                                     local_system_directory_file_download_path=download_path,
                                     logger=logger,
                                     is_logging_enable=is_logging_enable
                                     )
        else:
            for file in os.listdir(downloader_path):
                if '.dvc' in file or '.gitignore' in file:
                    continue
                print(f"Source dir: {downloader_path} file: {file} is being copied into destination dir: {download_path}"
                      f" file: {file}")
                shutil.copy(os.path.join(downloader_path,file),os.path.join(download_path,file))

        logger.log("Data has been downloaded from cloud storage into local system")

    except Exception as e:
        generic_exception = GenericException(
                "Error occurred in module [{0}] method [{1}]"
                    .format(loader_main.__module__,
                            loader_main.__name__))
        raise Exception(generic_exception.error_message_detail(str(e), sys)) from e

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default=os.path.join("config", "params.yaml"))
    args.add_argument("--datasource", default=None)
    parsed_args = args.parse_args()
    print("started")
    loader_main(config_path=parsed_args.config, datasource=parsed_args.datasource)
