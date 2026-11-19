class Television:
    """Class television and functions to control basic settings"""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Method to initialize television with default settings"""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Method to turn the television on or off"""
        self.__status = not self.__status

    def mute(self) -> None:
        """Method to mute or unmute the television while it's on"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Method to increase the channel, rolls over to min channel if max channel is exceeded"""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Method to decrease the channel, rolls over to max channel if channel goes below min channel"""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Method to increase the volume when the television is on. 
        Unmute if muted. Caps at max volume, no roll over"""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Method to decrease the volume when the television is on. 
                Unmute if muted. Caps at min volume, no roll over"""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """method to return the television's current power, channel, and volume."""
        if self.__muted:
            volume= Television.MIN_VOLUME
        else:
            volume = self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'