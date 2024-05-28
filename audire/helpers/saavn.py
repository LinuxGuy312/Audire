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

import aiohttp

from audire import dotdict, errors


async def search(query: str, limit: int) -> dotdict.DotDict:
    """
    Searches JioSaavn for given query.

    Parameters:
        query (str): Query to search for.
        limit (int): Limit the results.
    Returns:
        DotDict (dotdict): DotDict which you can access with dot notation.
    """
    api = "https://saavn.dev/api/search/songs"
    params = {"query": query, "limit": limit}

    async with aiohttp.request("GET", url=api, params=params) as response:
        response = await response.json()
        resp = response["data"].get("results")
        if not resp:
            raise errors.NoResultsFoundError
        result = {"results": resp}
        return dotdict.DotDict(result)


async def get_download(url: str) -> dotdict.DotDict:
    """
    Gets Download link for given URL.

    Parameters:
        url (str): URL of the song to download

    Returns:
        DotDict (dotdict): DotDict which you can access with dot notation.
    """
    api = "https://saavn.dev/api/songs"
    params = {"link": url}

    async with aiohttp.request("GET", url=api, params=params) as response:
        response = await response.json()
        if not response["success"]:
            raise errors.NoDownloadsFoundError
        data = {"data": response["data"][0]["downloadUrl"]}
        return dotdict.DotDict(data)
