# PyPresence Stock Updater

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A python command line app that adds live stock quotes to your discord presence!

![my presence](https://github.com/alexng353-new/pypresence-stock-updater/blob/main/assets/example.png)

## Guide on use and installation:

Create a discord developer RPC application [here](https://discord.com/developers/applications) and copy your `application ID` from the `General Information` page.

![discord dev portal](https://github.com/alexng353-new/pypresence-stock-updater/blob/main/assets/dev%20portal.png)


Install pypresence:
### `pip install pypresence`

Create and edit your `config.ini` in this format:

```
[config]
clientID = 123456789012345678 ; (your application ID)

[stocks]
stock1 = btc-usd
```

Add the two images for the stocks you want to track, or use [this image](https://github.com/alexng353-new/pypresence-stock-updater/tree/main/assets/stonk.jpg) for single-rpc and a custom image of your choice.

![upload images](https://github.com/alexng353-new/pypresence-stock-updater/blob/main/assets/upload%20images.png)

Make sure to name your custom the same as your Yahoo Finance Symbol (btc-usd, eth-usd). You can search for your stock's symbol at [Yahoo Finance](https://finance.yahoo.com).

I have included the images for [BTC-CAD](https://github.com/alexng353-new/pypresence-stock-updater/tree/main/assets/btc-cad.png) and [ETH-CAD](https://github.com/alexng353-new/pypresence-stock-updater/tree/main/assets/eth-cad.png)

Stock Updater supports up to 2 stocks at a time, [single-rpc.py](https://github.com/alexng353-new/pypresence-stock-updater/blob/main/single-rpc.py) and [double-rpc.py](https://github.com/alexng353-new/pypresence-stock-updater/blob/main/double-rpc.py) respectively.

Have fun with your new stock quoting presence!