import decimal

import balder

from .dc_power_supply_feature import DCPowerSupplyFeature
from .dc_power_supply_instrument import DCPowerSupplyInstrument


class DCPowerSupplyInstrumentChannel(DCPowerSupplyFeature):
    """
    Implementation of :class:`balderhub.powersupply.lib.scenario_features.DCPowerSupplyFeature` and uses a channel of an
    :class:`balderhub.powersupply.lib.scenario_features.DCPowerSupplyInstrument`
    """

    class Instrument(balder.VDevice):
        """vdevice representing the power supply instrument"""
        inst = DCPowerSupplyInstrument()

    @property
    def channel(self) -> DCPowerSupplyInstrument.Channel:
        """
        :return: returns the channel identifier this feature represents
        """
        raise NotImplementedError

    def get_configured_voltage(self) -> decimal.Decimal:
        return self.Instrument.inst.get_configured_channel_voltage(self.channel)

    def get_configured_current(self) -> decimal.Decimal:
        return self.Instrument.inst.get_configured_channel_current(self.channel)

    def is_enabled(self) -> bool:
        return self.Instrument.inst.get_channel_output_state(self.channel)

    def set_configured_voltage(self, voltage: decimal.Decimal):
        self.Instrument.inst.set_configured_channel_voltage(self.channel, voltage)

    def set_configured_current(self, current: decimal.Decimal):
        self.Instrument.inst.set_configured_channel_current(self.channel, current)

    def power_on(self):
        return self.Instrument.inst.change_channel_output(self.channel, True)

    def power_off(self):
        return self.Instrument.inst.change_channel_output(self.channel, False)
