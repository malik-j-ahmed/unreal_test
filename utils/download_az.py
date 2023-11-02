"""Author: Japa
   Organization: Umlaut Part of Accenture
   Project: Metaverese Launcher

   This software is intended to download unreal packages from Azure Blob Storage to the Client Machine. Important
   Auth data are embedded in the code till MSAL is online. The function: download_package with parameter file name
   should be called from the ui whenever a download need to be initiated .

"""

import os
from azure.cli.core import get_default_cli
from azure.storage.blob import BlobServiceClient
from utils.logger import get_logger_service
from utils.extractor import extract_file


class AzureDownload:
    # The Main Class wraps the essential methods
    # TODO: Implement MSAL auth for download api once its running

    def __init__(self):
        self.container = None
        self.logger = get_logger_service()
        self.path = os.path.join('./data')
        self.blob_client = None
        self.container_name = 'unrealpackages'
        self.connection_string = 'DefaultEndpointsProtocol=https;AccountName=azeu1engmetal;AccountKey=A1bmkCUZHg//9/0TdJgC6tiQ4OGZAaJKFwhiztebJ1xW0TfNI+xJeuve8kchPrtZ+xoPFAt6Qo1u+AStzYRDgA==;EndpointSuffix=core.windows.net'  # top secret
        self.key = 'A1bmkCUZHg//9/0TdJgC6tiQ4OGZAaJKFwhiztebJ1xW0TfNI+xJeuve8kchPrtZ+xoPFAt6Qo1u+AStzYRDgA=='  # top Secret
        self.storage_account = 'azeu1engmetal'
        self.azure_bin = 'az'
        self.blobs = None
        self.files = []

    def auth(self):
        self.logger.info("Attempting Auth")
        self.blob_client = BlobServiceClient.from_connection_string(self.connection_string)

    def list_files(self):
        self.container = self.blob_client.get_container_client(container=self.container_name)
        self.blobs = self.container.list_blobs()
        for blob in self.blobs:
            self.files.append(blob)

    def download_package(self, filename):
        """

        :param filename:
        :return:

        This module acts as the main entry for the download from UI. While calling this function, make sure that an
        asynchronous method should be used to call else the UI will be blocked till the download finish
        """
        exist = os.path.exists(self.path)
        if not exist:
            os.mkdir(self.path)
        self.logger.info('Starinting Download of package {}'.format(filename))
        cli = get_default_cli()
        out_put_file = os.path.join(self.path, filename)
        response = cli.invoke(
            ['storage', 'blob', 'download', '--account-key', self.key, '--account-name', self.storage_account,
             '--container-name', self.container_name, '-f', out_put_file, '-n', filename])
        self.logger.info(response)
        extract_file(self.path,os.path.join(self.path,filename))


"""-----------------------------------------------------------------Unit Testing Module START---------------------------------------------------------------------"""
if __name__ == "__main__":
    ad = AzureDownload()
    ad.auth()
    ad.list_files()
    ad.download_package('22-09-01-Hafex-V1.7z')

"""-----------------------------------------------------------------Unit Testing Module END---------------------------------------------------------------------"""
