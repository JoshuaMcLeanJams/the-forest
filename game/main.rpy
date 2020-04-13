define e = Character("Eileen", kind=nvl, color="#C8FFC8")
define narrator = nvl_narrator
define menu = nvl_menu

define audio.bass = "audio/running_genesis_bass.ogg"
define audio.bass2 = "audio/running_genesis_bass2.ogg"
define audio.drum = "audio/running_genesis_drum.ogg"
define audio.pulse1 = "audio/running_genesis_pulse1.ogg"
define audio.pulse2 = "audio/running_genesis_pulse2.ogg"
define audio.wave = "audio/running_genesis_wave.ogg"

label start:
    scene bg room
    nvl show
    jump main

label main:
    nvl clear
    menu:
        "What shall we toggle?"

        "Bass":
            call audio_toggle('accomp', audio.bass)
        "Bass 2":
            call audio_toggle('accomp2', audio.bass2)
        "Drum":
            call audio_toggle('drums', audio.drum)
        "Pulse 1":
            call audio_toggle('harmony', audio.pulse1)
        "Pulse 2":
            call audio_toggle('harmony2', audio.pulse2)
        "Wave":
            call audio_toggle('lead', audio.wave)
        "I'm outta here":
            jump end

    call audio_update()
    jump main

label end:
    "The End"
    call audio_stop_all()
    return
