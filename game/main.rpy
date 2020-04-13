define e = Character("Eileen", kind=nvl, color="#C8FFC8")
define narrator = nvl_narrator
define menu = nvl_menu

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

label start:
    $AudioLayer.start()
    scene bg room
    nvl show

label main:
    nvl clear
    menu:
        "What shall we toggle?"

        "Bass":
            $AudioLayer.toggle('bass')
        "Bass 2":
            $AudioLayer.toggle('bass2')
        "Drum":
            $AudioLayer.toggle('drum')
        "Pulse 1":
            $AudioLayer.toggle('pulse1')
        "Pulse 2":
            $AudioLayer.toggle('pulse2')
        "Wave":
            $AudioLayer.toggle('wave')
        "Enable all":
            $AudioLayer.enable_all()
        "Disable all":
            $AudioLayer.disable_all()
        "Toggle all":
            $AudioLayer.toggle_all()
        "I'm outta here":
            jump end

    jump main

label end:
    "The End"
    $AudioLayer.stop()
    return
