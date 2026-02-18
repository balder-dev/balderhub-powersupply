import decimal
import re

from balderhub.scpi.lib.scenario_features.scpi_transmission_feature import ScpiTransmissionFeature
from ...scenario_features.dc_power_supply_instrument import DCPowerSupplyInstrument


class SiglentSPD3303DCPowerSupplyInstrument(DCPowerSupplyInstrument):
    """
    Feature implementation for the Siglent SPD3303X / X-E Power supply instrument
    """

    scpi = ScpiTransmissionFeature()

    class Channel(DCPowerSupplyInstrument.Channel):
        """available channel for this instrument"""
        CHANNEL_1 = 1
        CHANNEL_2 = 2

    def _get_channel_string(self, of_channel: Channel) -> str:
        if of_channel == self.Channel.CHANNEL_1:
            return 'CH1'
        if of_channel == self.Channel.CHANNEL_2:
            return 'CH2'
        raise ValueError(f'unexpected value for channel: {of_channel}')

    @property
    def voltage_min_max(self) -> tuple[decimal.Decimal, decimal.Decimal]:
        return decimal.Decimal('0.00'), decimal.Decimal('32.00')

    @property
    def current_min_max(self) -> tuple[decimal.Decimal, decimal.Decimal]:
        """limitations of instrument (min/max voltage)"""
        return decimal.Decimal('0.00'), decimal.Decimal('3.20')

    @property
    def voltage_resolution(self) -> decimal.Decimal:
        """limitations of instrument: resolution of VOLTAGE in volts of the instrument"""
        return decimal.Decimal('0.01')

    @property
    def current_resolution(self) -> decimal.Decimal:
        """limitations of instrument: resolution of CURRENT in ampere of the instrument"""
        return decimal.Decimal('0.01')

    def get_configured_channel_voltage(self, of_channel: Channel) -> decimal.Decimal:
        channel_str = self._get_channel_string(of_channel)
        result = self.scpi.query_values(f"{channel_str}:VOLTAGE?".encode(self.scpi.ENCODING))
        return decimal.Decimal(result.decode(self.scpi.ENCODING))

    def get_configured_channel_current(self, of_channel: Channel) -> decimal.Decimal:
        channel_str = self._get_channel_string(of_channel)

        result = self.scpi.query_values(f"{channel_str}:CURRENT?".encode(self.scpi.ENCODING))
        return decimal.Decimal(result.decode(self.scpi.ENCODING))

    def _get_system_status(self) -> int:
        result = self.scpi.query_values("SYSTEM:STATUS?".encode(self.scpi.ENCODING))
        decoded_result = result.decode(self.scpi.ENCODING)
        if not re.match(r'^0x[0-9a-fA-F]{1,4}\n$', decoded_result):
            raise ValueError(f'received unexpected response from SCPI while asking for `SYSTEM:STATUS`: `{result}`')
        return int(decoded_result[:-1], 16)

    def get_channel_output_state(self, of_channel: Channel) -> bool:
        status = self._get_system_status()
        if of_channel == self.Channel.CHANNEL_1:
            return bool(status & (1 << 4))
        if of_channel == self.Channel.CHANNEL_2:
            return bool(status & (1 << 5))
        raise ValueError(f'unexpected value for channel: {of_channel}')

    def set_configured_channel_voltage(self, of_channel: Channel, voltage: decimal.Decimal) -> None:
        channel_str = self._get_channel_string(of_channel)

        self.scpi.write_values(f"{channel_str}:VOLTAGE {voltage}".encode('ascii'))

    def set_configured_channel_current(self, of_channel: Channel, current: decimal.Decimal) -> None:
        channel_str = self._get_channel_string(of_channel)

        self.scpi.write_values(f"{channel_str}:CURRENT {current}".encode('ascii'))

    def change_channel_output(self, of_channel: Channel, value: bool) -> None:
        channel_str = self._get_channel_string(of_channel)

        if not isinstance(value, bool):
            raise TypeError(f'expected value is from type bool, but got type {value.__class__}')
        value = 'ON' if value else 'OFF'
        self.scpi.write_values(f'OUTPUT {channel_str},{value}'.encode(self.scpi.ENCODING))
