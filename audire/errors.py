"""
Audire
Copyright (c) 2024 Eren

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class BaseError(Exception):
    """
    The base class for all errors raised within this package.

    Attributes:
        error_message (str, optional): The specific error message.
    """

    message = "An error occurred."

    def __init__(self, error_message=None):
        self.error_message = error_message or self.message

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return f"<{self.__class__.__name__} error_message='{self.error_message}'>"


class PlatformNotSupportedError(BaseError):
    """
    Exception raised when an unsupported platform is requested.
    """

    message = "Requested Platform is Not Supported."


class NoResultsFoundError(BaseError):
    """
    Exception raised when no results are found for a given query.
    """

    message = "No Results Found for the given query"


class NoDownloadsFoundError(BaseError):
    """
    Exception raised when no download results are found for the given URL.
    """

    message = "No Download Results Found for the given URL"
