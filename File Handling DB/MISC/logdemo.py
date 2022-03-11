import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(levelno)s %(message)s',
                    filemode='a',
                    level=logging.DEBUG)

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
#logger.setLevel(logging.DEBUG)

# Test messages


