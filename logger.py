import logging

def configure_logger():
    """ Configures logger used throughout the application
        To get an instance of the configured logger from any module, simply call:
            `logger = logging.getLogger(__name__)`
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
        handlers=[
            logging.FileHandler("out.log"),
            logging.StreamHandler()
        ]
    )

#configure_logger
configure_logger()

#logger = logging.getLogger(__name__)
#logger.info("Starting code")
#logger.info("Ending code")