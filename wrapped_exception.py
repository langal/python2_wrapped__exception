import sys
import traceback

class WrappedException(Exception):
    """
    This Exception class basically allows some Exception to be re-raised
    as another Exception type (eg. a business exception).

    Business-named exception would merely subclass this.
    """
    def __init__(self, exception=None):
        super(WrappedException, self).__init__()
        self.exc_info = sys.exc_info()
        self.exception = exception if exception else self.exc_info[1]

    def throw(self):
        if self.exc_info[0] and self.exc_info[1] and self.exc_info[2]:
            raise type(self), self.exception, self.exc_info[2]
        raise self
