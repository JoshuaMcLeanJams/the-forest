class AudioLayer:
        is_playing = False
        layer_dict = {}

        def __init__(self, file):
                self.enabled = False
                self.file = file

        @classmethod
        def disable(cls, channel):
                cls.layer_dict[channel].enabled = False
                renpy.music.set_volume(0.0, 0, channel)
                return

        @classmethod
        def disable_all(cls):
                for channel in cls.layer_dict.keys():
                        cls.disable(channel)

        @classmethod
        def enable(cls, channel):
                cls.layer_dict[channel].enabled = True
                renpy.music.set_volume(1.0, 0, channel)
                return

        @classmethod
        def enable_all(cls):
                for channel in cls.layer_dict.keys():
                        cls.enable(channel)

        @classmethod
        def toggle(cls, channel):
                if cls.layer_dict[channel].enabled:
                        cls.disable(channel)
                else:
                        cls.enable(channel)
                return

        @classmethod
        def toggle_all(cls):
                for channel in cls.layer_dict.keys():
                        cls.toggle(channel)

        @classmethod
        def set(cls, channel, file):
                if cls.is_playing:
                        return
                if channel not in cls.layer_dict.keys():
                        renpy.music.register_channel(channel, "music", True, True, True)
                cls.layer_dict[channel] = AudioLayer(file)
                return

        @classmethod
        def start(cls):
                if cls.is_playing:
                        return
                for channel in cls.layer_dict.keys():
                        if channel is not None:
                                renpy.music.play(cls.layer_dict[channel].file, channel)
                                cls.disable(channel)
                cls.is_playing = True
                return

        @classmethod
        def stop(cls):
                if not cls.is_playing:
                        return
                for channel in cls.layer_dict.keys():
                        renpy.music.stop(channel)
                is_playing = True
