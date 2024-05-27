# Audire

A Package to search and get download links for songs from various platforms asynchronously.

![Python](https://img.shields.io/badge/made_with-python-blue?style=for-the-badge&logoColor=blue&labelColor=lightblue&link=https%3A%2F%2Fwww.python.org)
![PyPI - Version](https://img.shields.io/pypi/v/Audire?style=for-the-badge&label=Audire&link=https%3A%2F%2Fpypi.org%2Fproject%2FAudire)




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

## License
This project is licensed under the MIT License. See the [MIT](https://opensource.org/license/mit) file for details.

## Contributing
If you wish to contribute to this project, please [fork](https://github.com/LinuxGuy312/Audire/fork) and [create a pull request](https://github.com/LinuxGuy312/Audire/compare) or [submit an issue](https://github.com/LinuxGuy312/Audire/issues/new).

## Contact
For any Questions or concerns, please contact me at:
- Telegram : [@WH0907](https://t.me/WH0907)
- Email : linuxguy312@segfault.net