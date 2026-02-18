import decimal
from ..scenario_features import DCPowerSupplyInstrument
from ..scenario_features.dc_power_supply_feature import DCPowerSupplyFeature


class DirtyDcPowerSupplyChannel(DCPowerSupplyFeature):
    """
    Dirty helper feature that can be assigned directly to the device
    """

    instrument = DCPowerSupplyInstrument()

    @property
    def channel(self) -> DCPowerSupplyInstrument.Channel:
        """
        :return: returns the channel that should be used for the feature (defaults to 1)
        """
        return self.instrument.Channel(1)

    def set_configured_voltage(self, voltage: decimal.Decimal):
        self.instrument.set_configured_channel_voltage(self.channel, voltage)

    def set_configured_current(self, current: decimal.Decimal):
        self.instrument.set_configured_channel_current(self.channel, current)

    def get_configured_voltage(self) -> decimal.Decimal:
        return self.instrument.get_configured_channel_voltage(self.channel)

    def get_configured_current(self) -> decimal.Decimal:
        return self.instrument.get_configured_channel_current(self.channel)

    def is_enabled(self) -> bool:
        return self.instrument.get_channel_output_state(self.channel)

    def power_on(self):
        return self.instrument.change_channel_output(self.channel, True)

    def power_off(self):
        return self.instrument.change_channel_output(self.channel, False)
