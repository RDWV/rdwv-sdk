API Reference
=============

Implemented coins
*****************

BTC
---

BTC class supports lightning out of the box.
For lightning methods to work, it must be enabled from the daemon
(enabled by default and edited by ``BTC_LIGHTNING`` environment variable).
If lightning is disabled, ``LightningDisabledError`` is raised when
calling lightning methods.

.. autoclass:: rdwv.coins.btc.BTC
    :members:
    :show-inheritance:
    :undoc-members:

BCH
---

BCH supports Schnorr signatures, they are enabled out of the box

.. autoclass:: rdwv.coins.bch.BCH
    :members:
    :show-inheritance:
    :undoc-members:

XMR
---

XMR support is based on our custom daemon implementation which tries to follow electrum APIs as closely as possible

.. autoclass:: rdwv.coins.xmr.XMR
    :members:
    :show-inheritance:
    :undoc-members:

ETH
---

ETH support is based on our custom daemon implementation which tries to follow electrum APIs as closely as possible

.. autoclass:: rdwv.coins.eth.ETH
    :members:
    :show-inheritance:
    :undoc-members:

BNB
---

BNB support is based on our custom daemon implementation which tries to follow electrum APIs as closely as possible

.. autoclass:: rdwv.coins.bnb.BNB
    :members:
    :show-inheritance:
    :undoc-members:

SmartBCH
--------

SmartBCH support is based on our custom daemon implementation which tries to follow electrum APIs as closely as possible

.. autoclass:: rdwv.coins.sbch.SBCH
    :members:
    :show-inheritance:
    :undoc-members:

Polygon (MATIC)
---------------

Polygon (MATIC) support is based on our custom daemon implementation which tries to follow electrum APIs as closely as possible

.. autoclass:: rdwv.coins.matic.MATIC
    :members:
    :show-inheritance:
    :undoc-members:

TRON (TRX)
----------

TRON (TRX) support is based on our custom daemon implementation which tries to follow electrum APIs as closely as possible

.. autoclass:: rdwv.coins.trx.TRX
    :members:
    :show-inheritance:
    :undoc-members:

XRG
---

XRG supports Schnorr signatures, they are enabled out of the box

.. autoclass:: rdwv.coins.xrg.XRG
    :members:
    :show-inheritance:
    :undoc-members:

LTC
---

LTC class supports lightning out of the box.
For lightning methods to work, it must be enabled from the daemon
(enabled by default and edited by ``LTC_LIGHTNING`` environment variable).
If lightning is disabled, ``LightningDisabledError`` is raised when
calling lightning methods.

.. autoclass:: rdwv.coins.ltc.LTC
    :members:
    :show-inheritance:
    :undoc-members:

BSTY
----

BSTY class supports lightning out of the box.
For lightning methods to work, it must be enabled from the daemon
(enabled by default and edited by ``BSTY_LIGHTNING`` environment variable).
If lightning is disabled, ``LightningDisabledError`` is raised when
calling lightning methods.

.. autoclass:: rdwv.coins.bsty.BSTY
    :members:
    :show-inheritance:
    :undoc-members:

GRS
---

GRS class supports lightning out of the box.
For lightning methods to work, it must be enabled from the daemon
(enabled by default and edited by ``GRS_LIGHTNING`` environment variable).
If lightning is disabled, ``LightningDisabledError`` is raised when
calling lightning methods.

.. autoclass:: rdwv.coins.grs.GRS
    :members:
    :show-inheritance:
    :undoc-members:

Utilities
*****************

.. automodule:: rdwv.utils
    :members:
    :show-inheritance:
    :undoc-members:
    :exclude-members: CustomJSONEncoder
