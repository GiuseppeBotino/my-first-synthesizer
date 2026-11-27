# My First Synthesizer

A simple waveform synthesizer written in Python using NumPy and sounddevice.

This project is the first step toward my goal of developing a Digital Audio Workstation (DAW).

## Features

- Generate triangle waves.
- Generate square waves.
- Generate sawtooth waves.
- Generate white noise.
- Generate silence.
- Play musical notes by entering keyboard commands in the terminal.

## Requirements

- Python
- NumPy
- sounddevice

## Installation

Install the required packages:

```bash
pip install numpy sounddevice
```

## Usage

Run the program:

```bash
python3 sounds.py
```

Enter a command and press Enter to execute it.

Available commands:

- `a` to `k`: Play musical notes.
- `triangle`: Select triangle wave.
- `square`: Select square wave.
- `sawtooth`: Select sawtooth wave.
- `white_noise`: Select white noise.
- `no_sound`: Select silence.
- `tones`: Display available waveforms.
- `q`: Quit the program.

## Keyboard Mapping

| Key | MIDI Note | Pitch |
|:---:|:---:|:---:|
| A | 60 | C4 |
| W | 61 | C#4 |
| S | 62 | D4 |
| E | 63 | D#4 |
| D | 64 | E4 |
| F | 65 | F4 |
| T | 66 | F#4 |
| G | 67 | G4 |
| Y | 68 | G#4 |
| H | 69 | A4 |
| U | 70 | A#4 |
| J | 71 | B4 |
| K | 72 | C5 |

## Project Status

This project is currently in its early development stage.

The long-term goal is to develop a DAW with a synthesizer, note recording, note editing, and audio export.

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
