import logging
# create logger
lgr = logging.getLogger('myapp')
lgr.setLevel(logging.DEBUG)
# add a file handler
fh = logging.FileHandler('myapp.log')
fh.setLevel(logging.WARNING)
# create a formatter and set the formatter for the handler.
frmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(frmt)
# add the Handler to the logger
lgr.addHandler(fh)
# You can now start issuing logging statements in your code
lgr.debug('debug message') # This won't print to myapp.log
lgr.info('info message') # Neither will this.
lgr.warn('Checkout this warning.') # This will show up in the log file.
lgr.error('An error goes here.') # and so will this.
lgr.critical('Something critical happened.') # and this one too.
