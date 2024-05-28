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


async def get_download(url: str) -> dotdict.DotDict:
    """
    Gets Download link for given URL.

    Parameters:
        url (str): URL of the song to download

    Returns:
        DotDict (dotdict): DotDict which you can access with dot notation.
    """
    api = "https://co.wuk.sh/api/json"
    headers = {"accept": "application/json", "content-type": "application/json"}
    payload = {
        "url": url,
        "filenamePattern": "basic",
        "isAudioOnly": "true",
    }

    async with aiohttp.request(
        "POST", url=api, json=payload, headers=headers
    ) as response:
        response = await response.json()
        dlurl = response.get("url")
        if not url:
            raise errors.NoDownloadsFoundError
        data = {"download_url": dlurl}
        return dotdict.DotDict(data)
