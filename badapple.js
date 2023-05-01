function trackChord () {
    for (let index = 0; index < 2; index++) {
        loopMelody2()
        music.playTone(156, music.beat(BeatFraction.Half))
        music.playTone(185, music.beat(BeatFraction.Quarter))
        music.playTone(156, music.beat(BeatFraction.Quarter))
        music.playTone(208, music.beat(BeatFraction.Half))
        music.playTone(185, music.beat(BeatFraction.Quarter))
        music.playTone(208, music.beat(BeatFraction.Quarter))
        loopMelody2()
        music.playTone(208, music.beat(BeatFraction.Half))
        music.playTone(185, music.beat(BeatFraction.Quarter))
        music.playTone(208, music.beat(BeatFraction.Quarter))
        music.playTone(185, music.beat(BeatFraction.Half))
        music.playTone(156, music.beat(BeatFraction.Quarter))
        music.playTone(185, music.beat(BeatFraction.Quarter))
    }
    for (let index = 0; index < 3; index++) {
        loopMelody3()
    }
    loopMelody2()
    music.playTone(156, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    music.playTone(156, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Quarter))
    for (let index = 0; index < 2; index++) {
        // 낮은 시
        music.playTone(123.47, music.beat(BeatFraction.Half))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        music.rest(music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        // 낮은 라#
        music.playTone(116.54, music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
    }
    music.playTone(139, music.beat(BeatFraction.Half))
    music.playTone(139, music.beat(BeatFraction.Half))
    music.playTone(156, music.beat(BeatFraction.Half))
    music.playTone(156, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(175, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Half))
    for (let index = 0; index < 3; index++) {
        loopMelody4()
    }
    for (let index = 0; index < 2; index++) {
        // 낮은 시
        music.playTone(123.47, music.beat(BeatFraction.Half))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        music.rest(music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        // 낮은 라#
        music.playTone(116.54, music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
    }
    music.playTone(139, music.beat(BeatFraction.Half))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(123.47, music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Half))
    music.playTone(165, music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(185, music.beat(BeatFraction.Half))
    music.playTone(165, music.beat(BeatFraction.Quarter))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    loopMelody2()
    music.playTone(208, music.beat(BeatFraction.Whole))
    music.playTone(185, music.beat(BeatFraction.Whole))
    playChord = false
}
function sndDrum (duration: number, repeat: number) {
    for (let index = 0; index < repeat; index++) {
        music.playTone(100, 10)
        music.rest(duration)
    }
}
// Chord용 반복 1
function loopMelody2 () {
    for (let index = 0; index < 3; index++) {
        music.playTone(156, music.beat(BeatFraction.Half))
        music.playTone(156, music.beat(BeatFraction.Quarter))
        music.playTone(156, music.beat(BeatFraction.Quarter))
        music.rest(music.beat(BeatFraction.Quarter))
        music.playTone(156, music.beat(BeatFraction.Quarter))
        music.playTone(139, music.beat(BeatFraction.Quarter))
        music.playTone(156, music.beat(BeatFraction.Quarter))
    }
}
input.onButtonPressed(Button.A, function () {
    isPlaying = 1
    playBadApple()
})
function loopMelody1 () {
    music.playTone(622, music.beat(BeatFraction.Half))
    music.playTone(698, music.beat(BeatFraction.Half))
    music.playTone(740, music.beat(BeatFraction.Half))
    music.playTone(831, music.beat(BeatFraction.Half))
    music.playTone(932, music.beat(BeatFraction.Whole))
    music.playTone(1244, music.beat(BeatFraction.Half))
    music.playTone(1108, music.beat(BeatFraction.Half))
    music.playTone(932, music.beat(BeatFraction.Whole))
    music.playTone(622, music.beat(BeatFraction.Whole))
    music.playTone(932, music.beat(BeatFraction.Half))
    music.playTone(831, music.beat(BeatFraction.Half))
    music.playTone(740, music.beat(BeatFraction.Half))
    music.playTone(698, music.beat(BeatFraction.Half))
    music.playTone(622, music.beat(BeatFraction.Half))
    music.playTone(698, music.beat(BeatFraction.Half))
    music.playTone(740, music.beat(BeatFraction.Half))
    music.playTone(831, music.beat(BeatFraction.Half))
    music.playTone(932, music.beat(BeatFraction.Whole))
    music.playTone(831, music.beat(BeatFraction.Half))
    music.playTone(740, music.beat(BeatFraction.Half))
}
function trackBeat () {
    for (let index = 0; index < 2; index++) {
        for (let index = 0; index < 3; index++) {
            sndDrum(music.beat(BeatFraction.Whole), 3)
            sndDrum(music.beat(BeatFraction.Quarter), 4)
            sndDrum(music.beat(BeatFraction.Whole), 3)
            sndDrum(music.beat(BeatFraction.Half), 2)
        }
        sndDrum(music.beat(BeatFraction.Whole), 3)
        sndDrum(music.beat(BeatFraction.Quarter), 4)
        sndDrum(music.beat(BeatFraction.Whole), 4)
    }
    playBeat = false
}
// Chord용 반복 2
function loopMelody3 () {
    loopMelody2()
    music.playTone(156, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    music.playTone(156, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Quarter))
    for (let index = 0; index < 2; index++) {
        // 낮은 시
        music.playTone(123.47, music.beat(BeatFraction.Half))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        music.rest(music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        // 낮은 라#
        music.playTone(116.54, music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
    }
    music.playTone(139, music.beat(BeatFraction.Half))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(123.47, music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(156, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    music.playTone(156, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Quarter))
}
// Chord용 반복 3
function loopMelody4 () {
    for (let index = 0; index < 2; index++) {
        // 낮은 시
        music.playTone(123.47, music.beat(BeatFraction.Half))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        music.rest(music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
        // 낮은 라#
        music.playTone(116.54, music.beat(BeatFraction.Quarter))
        music.playTone(123.47, music.beat(BeatFraction.Quarter))
    }
    music.playTone(139, music.beat(BeatFraction.Half))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.rest(music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(123.47, music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Half))
    music.playTone(165, music.beat(BeatFraction.Quarter))
    music.playTone(139, music.beat(BeatFraction.Quarter))
    music.playTone(185, music.beat(BeatFraction.Half))
    music.playTone(165, music.beat(BeatFraction.Quarter))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    loopMelody2()
    music.playTone(156, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    music.playTone(156, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Half))
    music.playTone(185, music.beat(BeatFraction.Quarter))
    music.playTone(208, music.beat(BeatFraction.Quarter))
}
input.onButtonPressed(Button.AB, function () {
    trackChord()
})
function trackMain () {
    for (let index = 0; index < 2; index++) {
        loopMelody1()
        music.playTone(698, music.beat(BeatFraction.Half))
        music.playTone(622, music.beat(BeatFraction.Half))
        music.playTone(698, music.beat(BeatFraction.Half))
        music.playTone(740, music.beat(BeatFraction.Half))
        music.playTone(698, music.beat(BeatFraction.Half))
        music.playTone(622, music.beat(BeatFraction.Half))
        music.playTone(587, music.beat(BeatFraction.Half))
        music.playTone(698, music.beat(BeatFraction.Half))
        loopMelody1()
        music.playTone(698, music.beat(BeatFraction.Whole))
        music.playTone(740, music.beat(BeatFraction.Whole))
        music.playTone(831, music.beat(BeatFraction.Whole))
        music.playTone(932, music.beat(BeatFraction.Whole))
    }
    for (let index = 0; index < 3; index++) {
        for (let index = 0; index < 2; index++) {
            music.playTone(1108, music.beat(BeatFraction.Half))
            music.playTone(1244, music.beat(BeatFraction.Half))
            music.playTone(932, music.beat(BeatFraction.Half))
            music.playTone(831, music.beat(BeatFraction.Half))
            music.playTone(932, music.beat(BeatFraction.Whole))
            music.playTone(831, music.beat(BeatFraction.Half))
            music.playTone(932, music.beat(BeatFraction.Half))
        }
        music.playTone(831, music.beat(BeatFraction.Half))
        music.playTone(740, music.beat(BeatFraction.Half))
        music.playTone(698, music.beat(BeatFraction.Half))
        music.playTone(554, music.beat(BeatFraction.Half))
        music.playTone(622, music.beat(BeatFraction.Whole))
        music.playTone(554, music.beat(BeatFraction.Half))
        music.playTone(622, music.beat(BeatFraction.Half))
        music.playTone(698, music.beat(BeatFraction.Half))
        music.playTone(740, music.beat(BeatFraction.Half))
        music.playTone(831, music.beat(BeatFraction.Half))
        music.playTone(932, music.beat(BeatFraction.Half))
        music.playTone(622, music.beat(BeatFraction.Whole))
        music.playTone(831, music.beat(BeatFraction.Half))
        music.playTone(932, music.beat(BeatFraction.Half))
    }
    music.playTone(1108, music.beat(BeatFraction.Half))
    music.playTone(1244, music.beat(BeatFraction.Half))
    music.playTone(932, music.beat(BeatFraction.Half))
    music.playTone(831, music.beat(BeatFraction.Half))
    music.playTone(932, music.beat(BeatFraction.Whole))
    music.playTone(831, music.beat(BeatFraction.Half))
    music.playTone(932, music.beat(BeatFraction.Half))
    music.playTone(1108, music.beat(BeatFraction.Half))
    music.playTone(1244, music.beat(BeatFraction.Half))
    music.playTone(932, music.beat(BeatFraction.Half))
    music.playTone(831, music.beat(BeatFraction.Half))
    music.playTone(932, music.beat(BeatFraction.Whole))
    music.playTone(1244, music.beat(BeatFraction.Half))
    music.playTone(1396, music.beat(BeatFraction.Half))
    music.playTone(1479, music.beat(BeatFraction.Half))
    music.playTone(1396, music.beat(BeatFraction.Half))
    music.playTone(1244, music.beat(BeatFraction.Half))
    music.playTone(1108, music.beat(BeatFraction.Half))
    music.playTone(932, music.beat(BeatFraction.Whole))
    music.playTone(831, music.beat(BeatFraction.Half))
    music.playTone(932, music.beat(BeatFraction.Half))
    music.playTone(831, music.beat(BeatFraction.Half))
    music.playTone(740, music.beat(BeatFraction.Half))
    music.playTone(698, music.beat(BeatFraction.Half))
    music.playTone(554, music.beat(BeatFraction.Half))
    music.playTone(622, music.beat(BeatFraction.Whole))
}
input.onButtonPressed(Button.B, function () {
    if (isPlaying == 1) {
        isPlaying = 2
        while (isPlaying == 2) {
            music.stopMelody(MelodyStopOptions.All)
            basic.clearScreen()
        }
    }
    if (isPlaying == 2) {
        isPlaying = 1
        music.setVolume(150)
        while (isPlaying == 1) {
            basic.showString("BADAPPLE")
        }
    }
})
function playBadApple () {
    playBeat = true
    for (let index = 0; index < 8; index++) {
        music.rest(music.beat(BeatFraction.Breve))
    }
    playChord = true
    for (let index = 0; index < 8; index++) {
        music.rest(music.beat(BeatFraction.Breve))
    }
    trackMain()
}
let playChord = false
let playBeat = false
let isPlaying = 0
music.setTempo(138)
music.setBuiltInSpeakerEnabled(true)
music.setVolume(150)
isPlaying = 0
playBeat = false
playChord = false
basic.showIcon(IconNames.Yes)
basic.pause(500)
basic.clearScreen()
basic.forever(function () {
    while (isPlaying == 1) {
        basic.showString("BADAPPLE")
    }
})
basic.forever(function () {
    while (playBeat == true) {
        trackBeat()
    }
})
basic.forever(function () {
    while (playChord == true) {
        trackChord()
    }
})
