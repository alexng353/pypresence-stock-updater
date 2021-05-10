# PyPresence Stock Updater

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

##Guide on use and installation:

Create a discord developer RPC application [here](https://discord.com/developers/applications) and copy your `client ID` from the `General Information` page.

![discord dev portal](assets/dev\ portal.png)



Install pypresence:
### `pip install pypresence`

Create and edit your `config.ini`
Example:

```[config]
clientID = 123456789012345678

[stocks]
stock1 = btc-usd```

Stock Updater supports up to 2 stocks at a time, single-rpc.py and double-rpc.py respectively.
