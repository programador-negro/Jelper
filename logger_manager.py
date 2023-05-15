import logging

# now we will Create and configure logger
logging.basicConfig(filename="test.log",
                    format='%(filename)s %(funcName)s %(lineno)s %(name)s %(levelname)s %(asctime)s %(message)s',
                    filemode='a')

# Let us Create an object
logger = logging.getLogger()

# Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# some messages to test
# logger.debug("This is just a harmless debug message")
logger.info("This is just an information for you")
# logger.warning("OOPS!!!Its a Warning")
# logger.error("Have you try to divide a number by zero")
# logger.critical("The Internet is not working....")
