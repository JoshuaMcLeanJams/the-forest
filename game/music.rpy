define audio.bass = "audio/running_genesis_bass.ogg"
define audio.bass2 = "audio/running_genesis_bass2.ogg"
define audio.drum = "audio/running_genesis_drum.ogg"
define audio.pulse1 = "audio/running_genesis_pulse1.ogg"
define audio.pulse2 = "audio/running_genesis_pulse2.ogg"
define audio.wave = "audio/running_genesis_wave.ogg"

init python:
    AudioLayer.set('drum', audio.drum)
    AudioLayer.set('bass', audio.bass)
    AudioLayer.set('bass2', audio.bass2)
    AudioLayer.set('pulse1', audio.pulse1)
    AudioLayer.set('pulse2', audio.pulse2)
    AudioLayer.set('wave', audio.wave)

