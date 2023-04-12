"""Exceptions for marking tests as skipped or deprecated.

This module exists to provide backwards compatibility with previous
versions of xnose where skipped and deprecated tests were core
functionality, rather than being provided by plugins. It may be
removed in a future release.
"""
from xnose.plugins.skip import SkipTest
from xnose.plugins.deprecated import DeprecatedTest
