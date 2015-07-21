import logging
import sys
logger = logging.getLogger('info')
print logger.level
logger.setLevel(logging.INFO)
print logger.level
logger.addHandler(logging.StreamHandler(stream=sys.stdout))
logger.debug('debug message')
