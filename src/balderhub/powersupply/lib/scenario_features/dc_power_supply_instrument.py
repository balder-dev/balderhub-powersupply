import decimal
import enum
import balder


class DCPowerSupplyInstrument(balder.Feature):
    """raw implementation of a programmable power supply instrument"""

    class Channel(enum.Enum):
        """enum holding all available channels of this instrument"""

    @property
    def voltage_min_max(self) -> tuple[decimal.Decimal, decimal.Decimal]:
        """limitations of instrument (min/max voltage)"""
        raise NotImplementedError

    @property
    def current_min_max(self) -> tuple[decimal.Decimal, decimal.Decimal]:
        """limitations of instrument (min/max voltage)"""
        raise NotImplementedError

    @property
    def voltage_resolution(self) -> decimal.Decimal:
        """limitations of instrument: resolution of VOLTAGE in volts of the instrument"""
        raise NotImplementedError

    @property
    def current_resolution(self) -> decimal.Decimal:
        """limitations of instrument: resolution of CURRENT in ampere of the instrument"""
        raise NotImplementedError

    def get_configured_channel_voltage(self, of_channel: Channel) -> decimal.Decimal:
        """
        returns the current configured voltage for the given channel

        :param of_channel: the channel to get the configuration for
        :return: the configured VOLTAGE for the requested channel
        """
        raise NotImplementedError

    def get_configured_channel_current(self, of_channel: Channel) -> decimal.Decimal:
        """
        returns the current configured current for the given channel

        :param of_channel: the channel to get the configuration for
        :return: the configured CURRENT for the requested channel
        """
        raise NotImplementedError

    def get_channel_output_state(self, of_channel: Channel) -> bool:
        """
        Returns the current channel output state (True means activated, False means deactivated)

        :param of_channel: the channel to get the configuration for
        :return: True, when the channel output is activated, False otherwise
        """
        raise NotImplementedError


    def set_configured_channel_voltage(self, of_channel: Channel, voltage: decimal.Decimal) -> None:
        """
        Sets the current configured voltage for the given channel

        :param of_channel: the channel to set the configuration for
        :param voltage: the VOLTAGE in volts that should be set to the channel
        """
        raise NotImplementedError

    def set_configured_channel_current(self, of_channel: Channel, current: decimal.Decimal) -> None:
        """
        Sets the current configured CURRENT for the given channel

        :param of_channel: the channel to set the configuration for
        :param current: the CURRENT in ampere that should be set to the channel
        """
        raise NotImplementedError

    def change_channel_output(self, of_channel: Channel, value: bool) -> None:
        """
        Sets the current channel output state (True means activated, False means deactivated)

        :param of_channel: the channel to set the configuration for
        :param value: True if the output should be enabled, False otherwise
        """
        raise NotImplementedError
