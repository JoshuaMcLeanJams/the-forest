init python:
    channel_list = [
        "lead",
        "lead2",
        "harmony",
        "harmony2",
        "accomp",
        "accomp2",
        "drums",
        "drums2"
    ]
    audio_file = dict.fromkeys(channel_list, None)

    for channel in channel_list:
        renpy.music.register_channel(channel, "music", True, True, True)

label audio_set(channel, file):
    $audio_file[channel] = file
    return

label audio_stop_all():
    for channel in channel_list:
        renpy.music.stop(channel)
    return

label audio_toggle(channel, file):
    python:
        if audio_file[channel] is None:
           call audio_toggle(channel, file)
        else:
           audio_file[channel] = None
    return

label audio_update:
    python:
        for channel in channel_list:
            renpy.music.stop(channel)
            if audio_file[channel] is not None:
                renpy.play(audio_file[channel], channel)
    return
