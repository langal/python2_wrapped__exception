import sys
import traceback

class WrappedException(Exception):

    def __init__(self, exception):
        super(WrappedException, self).__init__(exception.message)
        self.exc_info = sys.exc_info()

    def print_stacktrace(self):
        traceback.print_tb(self.exc_info[2])

    def get_stacktrace(self):
        return traceback.format_tb(self.exc_info[2])

    def get_core_exception(self):
        return self.exc_info[1]

try:
    raise Exception("HELLOW WORLD")
except Exception as e:
    w_exception = WrappedException(e)
    w_exception.print_stacktrace()
    print(w_exception.get_stacktrace())
