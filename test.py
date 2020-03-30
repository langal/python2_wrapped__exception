import sys
import traceback

from wrapped_exception import WrappedException


def test_catch_raise():
    """Verify that we can catch and re-raise a Key Violation Exception as a "WrappedException"."""
    try:
        try:
            _my_bad_code()
        except Exception as e:
            wrap_exc = WrappedException(e)
            wrap_exc.throw()
    except WrappedException as e:
        assert(isinstance(e.exception, IndexError))
        trace_back = sys.exc_info()

        # verify that the bad code ('an_array[9') is in the stack trace
        # stacktraces are a tuple (file, line number, function name, line)
        assert('an_array[9]' == traceback.extract_tb(trace_back[2])[-1][-1])

        # also verify that the stored trace_back in the Wrapped Exception works
        assert('an_array[9]' == traceback.extract_tb(e.trace_back)[-1][-1])
    else:
        raise Exception("Failed to catch WrappedException")

    # test that wrapped exception captures sys.exc_info
    try:
        try:
            _my_bad_code()
        except Exception:
            WrappedException().throw()
    except WrappedException as e:
        assert(isinstance(e.exception, IndexError))
        trace_back = sys.exc_info()
        assert('an_array[9]' == traceback.extract_tb(trace_back[2])[-1][-1])
        assert('an_array[9]' == traceback.extract_tb(e.trace_back)[-1][-1])
    else:
        raise Exception("Failed to catch WrappedException")

# this is a function that just throws an IndexError
def _my_bad_code():
    # force a builtin exception
    an_array = []
    an_array[9]


if __name__ == "__main__":
    test_catch_raise()
