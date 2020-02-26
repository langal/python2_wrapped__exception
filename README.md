# python2_wrapped__exception

This is basically an Exception class that would be used to wrap raised Exceptions.

The common use case is when one wants to present a custom exception class to a downstream caller.

One would typically do this:

try:
&nbsp;&nbsp;&nbsp;&nbsp;doStuffTHatTHrowsAnException()
except Exception as e:
&nbsp;&nbsp;&nbsp;&nbsp;raise MyCustomException(e.message)
    
However, the above code causes the execution stack at the time of the first exception to be lost.

The WrappedException allows us to do this:

try:
&nbsp;&nbsp;&nbsp;&nbsp;doStuffTHatTHrowsAnException()
except Exception:
&nbsp;&nbsp;&nbsp;&nbsp;WrappedException.throw()
    
Callers can now catch "WrappedException" and still have the original execution stack.

Alternatively, they can do this:

try:
&nbsp;&nbsp;&nbsp;&nbsp;doStuffTHatTHrowsAnException()
except Exception as e:
&nbsp;&nbsp;&nbsp;&nbsp;WrappedException(e.message, another_parameter, etc.).throw()
    
As WrappedException would typically be subclassed with a "business" exception.
    
 

