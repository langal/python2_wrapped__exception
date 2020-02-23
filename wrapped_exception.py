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
        raise type(self), self.exception, self.exc_info[2]

"""
Verify that we can catch and re-raise a Key Violation Exception
as a "WrappedException".
"""
try:
    try:
        an_array = []
        an_array[9]
    except Exception as e:
        wrap_exc = WrappedException(e)
        wrap_exc.throw()
except WrappedException:
    print("CAUGHT A WRAPPED EXCEPTION")

print("\n===============\n")

"""
Just to see the behavior of uncuaght WrappedExceptions.
"""
try:
    an_array = []
    an_array[9]
except Exception:
    wrap_exc = WrappedException()
    wrap_exc.throw()
