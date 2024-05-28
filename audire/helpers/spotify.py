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

import json
import aiohttp
from bs4 import BeautifulSoup as BS

from audire import errors, dotdict


async def _get_search_token():
    url = "https://open.spotify.com/search"
    async with aiohttp.request("GET", url=url) as response:
        soup = BS(await response.text(), "html.parser").find(
            "script", {"id": "session"}
        )
    token = json.loads(soup.string)["accessToken"]
    return token


async def search(query, limit):
    """
    Returns An Object.

        Parameters:
            query (str): Query to search
            limit (int): Limit the results
        Returns:
            DotDict (dotdict): DotDict which you can access with dot notation
    """
    token = await _get_search_token()
    api = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": query, "limit": limit, "type": "track"}
    async with aiohttp.request("GET", api, params=params, headers=headers) as resp:
        response = await resp.json()
    if not response["tracks"].get("items"):
        raise errors.NoResultsFoundError
    result = {"results": response["tracks"]["items"]}
    return dotdict.DotDict(result)


async def get_download(url):
    """
    Returns An Object.

        Parameters:
            url (str): URL of the song
        Returns:
            DotDict (dotdict): DotDict which you can access with dot notation
    """
    api = "https://milanbhandari.onrender.com/spotify"
    async with aiohttp.request("GET", url=api, params={"url": url}) as response:
        data = await response.json()
    if not data.get("success"):
        raise errors.NoResultsFoundError
    return {"download_url": data["link"]}
