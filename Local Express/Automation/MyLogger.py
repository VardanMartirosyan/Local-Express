import logging

def logger(level, message, fileName):
    logging.basicConfig(level=logging.INFO, filename=fileName, filemode="a",
                        format="%(asctime)-12s %(levelname)s %(message)s",
                        datefmt="%d-%m-%Y %H:%M:%S")
    if level == "INFO":
        logging.info(message)
        return
    if level == "DEBUG":
        logging.debug(message)
        return
    if level == "WARNING":
        logging.warning(message)
        return
    if level == "ERROR":
        logging.error(message)
        return
    if level == "CRITICAL":
        logging.critical(message)
        return
