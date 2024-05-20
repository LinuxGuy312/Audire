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

from audire import dotdict, errors
from audire.helpers import youtube


class Audire:
    """
    Audire class search and get download links for music across various platforms.

    Attributes:
        platforms (list): List of supported Platforms.
    """

    def __init__(self):
        self.platforms = [
            "yt",  # YouTube
            "ytm",  # YouTube Music
        ]

    async def search(
        self, query: str,
        platform: str = "ytm",
        limit: int = 10
    ) -> dotdict.DotDict:
        """
        Audire Search Function.

        Parameters:
            query (str): Query to search.
            platform (str, optional): Platform to search on. Defaults to "ytm" (YouTube Music)
            limit (int, optional): Limit the results. Defaults to 10
        Returns:
            DotDict (dotdict): DotDict which you can access with dot notation.
        """

        if platform not in self.platforms:
            raise errors.PlatformNotSupportedError

        if platform == "yt":
            return await youtube.search(query, False, limit)

        if platform == "ytm":
            return await youtube.search(query, True, limit)

    async def get_download(self, url: str, platform: str) -> dotdict.DotDict:
        """
        Returns An Object.

        Parameters:
            url (str): URL of song.
            platform (str): Platform of download.

        Returns:
            DotDict (dotdict): DotDict which you can access with dot notation.
        """

        if platform not in self.platforms:
            raise errors.PlatformNotSupportedError

        if platform in ("yt", "ytm"):
            return await youtube.get_download(url)
