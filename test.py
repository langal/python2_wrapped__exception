from wrapped_exception import WrappedException

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
    pass
else:
    assert(False)

try:
    try:
        an_array = []
        an_array[9]
    except Exception:
        WrappedException().throw()
except WrappedException:
    pass
else:
    assert(False)
