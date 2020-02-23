import sys
import traceback

class WrappedException(Exception):

    def __init__(self, exception):
        super(WrappedException, self).__init__(exception.message)
        self.exc_info = sys.exc_info()
        self.core_exception = exception

    def print_core_stacktrace(self):
        traceback.print_tb(self.exc_info[2])

    def get_core_stacktrace(self):
        return traceback.format_tb(self.exc_info[2])

    def get_core_exception(self):
        return self.core_exception

try:
    raise Exception("HELLOW WORLD")
except Exception as e:
    w_exception = WrappedException(e)
    w_exception.print_core_stacktrace()
    print(w_exception.get_core_stacktrace())
