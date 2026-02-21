Examples
********

This BalderHub project can be used with any kind of power controlling devices. The most common way to work with it, is
by using the `balderhub-scpi <https://hub.balder.dev/projects>`_ project to communicate with programmable power supply
devices.

Use a ready-to-use instrument implementation
============================================

This BalderHub project provides ready-to-use feature implementation for some kind of devices. Checkout the
:ref:`Setup Features <Setup Features>` section to see the available devices.

Most of them using the SCPI interface for communication. For example using a Siglent SPD3303X/X-E, you can add the
following features to your setup device:

.. code-block:: python

    # file `setup_features.py`
    from balderhub.scpi.lib.setup_features import SocketScpiFeature


    class ScpiOfSiglentSPD3303X(SocketScpiFeature):

        @property
        def ip_address(self) -> str:
            return '192.168.0.81'

And within your setup:

.. code-block:: python

    # file `setup_example.py`

    import balder
    import balderhub.powersupply.lib.setup_features

    from lib.setup_features import ScpiOfSiglentSPD3303X

    class SetupExample(balder.Setup):

        class Instrument(balder.Device):
            scpi = ScpiOfSiglentSPD3303X()
            ps_inst = balderhub.powersupply.lib.setup_features.siglent.SiglentSPD3303DCPowerSupplyInstrument()
            # use the first channel directly (without splitting up instrument device and channel device)
            channel = balderhub.powersupply.lib.setup_features.DirtyDcPowerSupplyChannel()

            ...


Use it in a Scenario
====================

If you want to write test that using Power-Supply functionality, just use the most common scenario-level feature
:class:`balderhub.powersupply.lib.scenario_features.DCPowerSupplyFeature`:

.. code-block:: python

    # file `scenario_example.py`

    import balder
    import balderhub.powersupply.lib.scenario_features


    class ScenarioExample(balder.Scenario):

        class PowerSupply(balder.Device):
            ps = balderhub.powersupply.lib.scenario_features.DCPowerSupplyFeature()

        ...

        def test_do_something(self):
            ...
