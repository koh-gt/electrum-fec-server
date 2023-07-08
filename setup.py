from setuptools import setup

setup(
    name="electrum-fec-server",
    version="1.0",
    scripts=['run_electrum_fec_server.py','electrum-fec-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumfecserver':'src'
        },
    py_modules=[
        'electrumfecserver.__init__',
        'electrumfecserver.utils',
        'electrumfecserver.storage',
        'electrumfecserver.deserialize',
        'electrumfecserver.networks',
        'electrumfecserver.blockchain_processor',
        'electrumfecserver.server_processor',
        'electrumfecserver.processor',
        'electrumfecserver.version',
        'electrumfecserver.ircthread',
        'electrumfecserver.stratum_tcp'
    ],
    description="Ferrite Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://github.com/koh-gt/electrum-fec-server/",
    long_description="""Server for the Electrum Lightweight Ferrite Wallet"""
)
