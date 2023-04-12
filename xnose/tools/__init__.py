"""
Tools for testing
-----------------

xnose.tools provides a few convenience functions to make writing tests
easier. You don't have to use them; nothing in the rest of xnose depends
on any of these methods.

"""
from xnose.tools.nontrivial import *
from xnose.tools.nontrivial import __all__ as nontrivial_all
from xnose.tools.trivial import *
from xnose.tools.trivial import __all__ as trivial_all

__all__ = trivial_all + nontrivial_all
