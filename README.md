Electrum-server for the Electrum client
=========================================

  * Author: Thomas Voegtlin (ThomasV on the bitcointalk forum)
  * Language: Python


Note
----

  This code is now unmaintained. The replacement code for electrum
  server is ElectrumX: https://github.com/spesmilo/electrumx


Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires ferrited, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of Ferrite addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'electrum-fec-server' script



License
-------

Electrum-server is made available under the terms of the MIT License.
See the included `LICENSE` for more details.
