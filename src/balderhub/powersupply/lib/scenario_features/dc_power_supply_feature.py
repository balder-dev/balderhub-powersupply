import decimal
import balder


class DCPowerSupplyFeature(balder.Feature):
    """
    Power Supply Feature that is independent of the device type. It even does not need to be a Programmable Power
    Supply, because you could use any device that can be controlled and provide the functionality below.
    """

    def get_configured_voltage(self) -> decimal.Decimal:
        """
        returns the current configured voltage

        :return: the configured VOLTAGE
        """
        raise NotImplementedError

    def get_configured_current(self) -> decimal.Decimal:
        """
        returns the current configured CURRENT

        :return: the configured CURRENT
        """
        raise NotImplementedError

    def is_enabled(self) -> bool:
        """
        :return: returns True if the output is activated, False otherwise
        """
        raise NotImplementedError

    def set_configured_voltage(self, voltage: decimal.Decimal):
        """
        Sets the current configured VOLTAGE

        :param voltage: the VOLTAGE in volts that should be set to the channel
        """
        raise NotImplementedError

    def set_configured_current(self, current: decimal.Decimal):
        """
        Sets the current configured CURRENT

        :param current: the CURRENT in ampere that should be set
        """
        raise NotImplementedError

    def power_on(self) -> None:
        """
        enables the power supply output
        """
        raise NotImplementedError

    def power_off(self):
        """
        disable the power supply output
        """
        raise NotImplementedError
