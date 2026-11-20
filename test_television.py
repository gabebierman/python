from television import Television


def test_init():
    tv = Television()
    #status, channel, volume values
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    #tv is off
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #tv is on
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_mute():
    #tv is on, vol increased once, then tv muted
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    #tv is on and unmuted
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    #tv is off and muted
    tv.mute()
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #tv is off an unmuted
    tv = Television()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_up():
    #tv is off and channel is increased
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #tv is on an channel has increased
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    #tv is on and channel is increased past max channel
    for x in range(Television.MAX_CHANNEL + 1):
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_channel_down():
    #tv is off and channel is decreased
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #tv is on and channel is increased
    tv.power()
    tv.channel_up()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    #tv is on and channel is decreased past min channel
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_volume_up():
    #tv is off and volume is increased
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #tv is on an volume is increased
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    #tv is on, mute is on, and volume is increased
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    #volume is at max volume and is increased
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    #tv is off and volume is decreased
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    #tv is on an volume is decreased
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    #tv is on, mute is on, and volume is decreased
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    #volume is at min volume and is decreased
    tv.volume_down()
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
