Doctest documentation for base convertor.
===

Summary of the Base class and it's methods.
---

Base class has three methods for conversion of a decimanl number to:
* binary number
* octagonal number
* hexagonal number

**All methods allow only int type for conversion.**

And a fourth method for checking if entered number is valid for conversion.

    >>> from base_convertor import Base

For converting a number to binary use Base.dec_to_bin() method.

    >>> Base.dec_to_bin(7) == bin(7)
    True

For converting a number to octagonal use Base.dec_to_oct() method.

    >>> Base.dec_to_oct(7) == oct(7)
    True

For converting a number to hexagonal use Base.dec_to_hex() method.

    >>> Base.dec_to_hex(7) == hex(7)
    True

Incorrect numbers will trigger ValueError.

    >>> Base.dec_to_bin(-10)
    Traceback (most recent call last):
    ...
    ValueError: Error!
    Incorrect number was entered.
