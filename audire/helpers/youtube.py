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


async def search(query: str, ytmusic: bool, limit: int) -> dotdict.DotDict:
    """
    Searches YouTube or YouTube Music for given query.

    Parameters:
        query (str): Query to search for.
        ytmusic (bool): Whether to search on YouTube Music.
        limit (int): Limit the results.
    Returns:
        DotDict (dotdict): DotDict which you can access with dot notation.
    """
    api = "https://editorchoice-api-vq4j.onrender.com/"

    if ytmusic:
        path = "ytmsearch"
    else:
        path = "ytsearch"

    param = {"query": query}

    async with aiohttp.request("GET", url=api + path, params=param) as response:
        response = await response.json()
        resp = response.get("result") or response.get("results")
        if not resp:
            raise errors.NoResultsFoundError
        result = {"results": resp[:limit]}
        return dotdict.DotDict(result)


async def get_download(url: str) -> dotdict.DotDict:
    """
    Gets Download link for given Video ID.

    Parameters:
        video_id (str): Video ID of the song to download

    Returns:
        DotDict (dotdict): DotDict which you can access with dot notation.
    """
    api = "https://co.wuk.sh/api/json"
    headers = {"accept": "application/json", "content-type": "application/json"}
    payload = {
        "url": url,
        "filenamePattern": "basic",
        "isAudioOnly": "true",
        "disableMetadata": "true",
    }

    async with aiohttp.request(
        "POST", url=api, json=payload, headers=headers
    ) as response:
        response = await response.json()
        dlurl = response.get("url")
        if not url:
            raise errors.NoResultsFoundError
        data = {"download_url": dlurl}
        return dotdict.DotDict(data)
