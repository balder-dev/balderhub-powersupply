from ..scenario_features.dc_power_supply_instrument import DCPowerSupplyInstrument
from ..scenario_features.dc_power_supply_instrument_channel import DCPowerSupplyInstrumentChannel


class DCPowerSupplyInstrumentChannel1(DCPowerSupplyInstrumentChannel):
    """
    Universal DC Power Supply Setup Feature representing the Channel 1 of a Power-Supply Instrument
    """

    @property
    def channel(self) -> DCPowerSupplyInstrument.Channel:
        return self.Instrument.inst.Channel(1)
