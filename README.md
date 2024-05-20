# Audire

A Package to search and get download links for songs from various platforms asynchronously.

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org/)

---
> [!NOTE]
> "Audire" is a Latin verb meaning "to hear" or "to listen." It's the root of many English words related to sound and listening, like "audit" and "auditory."


## Installation

```sh
$ pip install audire
```

## Usage Examples

### Get Supported Platforms as List :
```py
from audire import Audire

print(Audire().platforms)
```

### Search on Youtube Music :

```py
import asyncio
from audire import Audire

async def main():
    audire = Audire()
    response = await audire.search("Pedro", platform="ytm")
    print(response)

asyncio.run(main())
```

### Getting Download Link from YouTube :
```py
import asyncio
from audire import Audire

async def main():
    audire = Audire()
    response = await audire.get_download('https://www.youtube.com/watch?v=RCqvSSfsP6w', 'yt')
    print(response)

asyncio.run(main())
```

## Documentation

There is no documentation as of now.
However, you can take help from the well written docstrings this way:

```py
from audire import Audire

print(help(Audire().search))
```