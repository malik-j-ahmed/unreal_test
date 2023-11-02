"""
Author :japa
Description: Package Extractor utility
"""


from pyunpack import Archive
from utils.logger import get_logger_service

logger = get_logger_service()

def extract_file(data_path,file):

   logger.info("Extracting Package {}".format(file))
   try:

      Archive(file).extractall(data_path)
      logger.info('Extracted Package {}'.format(file))
      
   except (FileNotFoundError,PermissionError)as e:
      logger.error('Package Extraction Failed {}'.format(file))


if __name__ == "___main__":
    extract_file(r'C:\Users\japa\Documents\PROJECTS\Metaverse_launcher\Metaverse%20Launcher\src\data',r'C:\Users\japa\Documents\PROJECTS\Metaverse_launcher\Metaverse%20Launcher\src\data\22-09-01-Hafex-V1.7z')