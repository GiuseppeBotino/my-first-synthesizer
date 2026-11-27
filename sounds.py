import numpy as np

def note_to_freq(note: int, A4: float=440.0) -> float:
    """Convert a MIDI note number into frequency

    Args:
        note: MIDI note number.
        A4: Reference frequency of A4 in Hz.
            Defaults to 440.0

    Returns:
        Frequency in Hz.
    """
    return A4 * 2 ** ((note - 69)/12)

def check_phi(phi: np.ndarray) -> None:
    """Validate the phase array.

    Args:
        phi: NumPy array containing phase values.

    Raises:
        TypeError: If phi is not a NumPy array.
        ValueError: if phi is empty or contains values outside the interval [0, 1).
    """
    if not isinstance(phi, np.ndarray):
        raise TypeError("the type of phi must be NumPy.ndarray")

    if len(phi) == 0:
        raise ValueError("phi is empty")

    if not np.all((0 <= phi) & (phi < 1)):
        raise ValueError("elements of phi must be non-negative number less than 1")

def triangle(phi: np.ndarray) -> np.ndarray:
    """Generate a triangle waveform from phase values.

    Args:
        phi: NumPy array containing phase values.

    Returns:
        NumPy array containing the generated triangle wave form.
    """
        
    check_phi(phi)
    return np.abs(-4 * phi + 2) - 1
    
def square(phi: np.ndarray) -> np.ndarray:
    """Generate a square wave from phase values.

    Args:
        phi: NumPy array containing phase values.

    Returns:
        NumPy array containing the generated square wave form.
    """
    check_phi(phi)
    return np.where(phi < 0.5, 1, -1)

def sawtooth(phi: np.ndarray) -> np.ndarray:
    """Generate a sawtooth waveform from phase values.

    Args:
        phi: NumPy array containing phase values.

    Returns:
        NumPy array containing the generated sawtooth wave form.
    """
    check_phi(phi)
    return 2 * phi - 1

rng = np.random.default_rng()

def white_noise(phi: np.ndarray) -> np.ndarray:
    """Generate an array of zeros representing silence.

    Args:
        phi: NumPy array containing phase values.

    Returns:
        NumPy array containing the generated white noise wave form.
    """
    check_phi(phi)
    return rng.uniform(-1, 1, size=len(phi))    

def no_sound(phi: np.ndarray) -> np.ndarray:
    """Generate the phase array of no sound wave.

    Args:
        phi: NumPy array containing phase values.

    Returns:
        NumPy array containing the generated no sound wave form.
    """
    check_phi(phi)
    return np.zeros(len(phi))

tone_funcs ={
    "triangle":triangle,
    "square":square,
    "sawtooth":sawtooth,
    "white_noise":white_noise,
    "no_sound":no_sound
}

def create_wave(
    f: float=440.0,
    initial_phi: float=0.0,
    tone: str="triangle",
    buf: int=256,
    sample_rate: int=44100
    ) -> np.ndarray:
    """Generate a waveform for a specified frequency.

    Args:
        f: Frequency in Hz. Defaults to 440.0.
        initial_phi: Initial phase. Defaults to 0.
        tone: Name of the waveform function. Defaults to "triangle".
        buf: Number of samples to generate. Defaults to 256
        sample_rate: Number of samples per second. Defaults to 44100.

    Returns:
        NumPy array containing the generated waveform.
    """
    func = tone_funcs[tone]
    t = np.arange(buf) / sample_rate
    phi = np.mod(f * t + initial_phi, 1)

    return func(phi)

# test

if __name__ == "__main__":
    import sounddevice as sd
    sample_rate = 44100

    tones = ["no_sound", "triangle", "square", "sawtooth", "white_noise"]
    pitches = {
        "a" : note_to_freq(60),
        "w" : note_to_freq(61),
        "s" : note_to_freq(62),
        "e" : note_to_freq(63),
        "d" : note_to_freq(64),
        "f" : note_to_freq(65),
        "t" : note_to_freq(66),
        "g" : note_to_freq(67),
        "y" : note_to_freq(68),
        "h" : note_to_freq(69),
        "u" : note_to_freq(70),
        "j" : note_to_freq(71),
        "k" : note_to_freq(72),
    }

    tone = "triangle"
    running = True

    while running:
        com = input(">>>")

        match com:
            case "q":
                running = False
            case "tones":
                for t in tones:
                    print(t, end = " ")
                print("")
            case _ if com in tones:
                tone = com
                print(f"mode is changed : {com}")
            case _ if com in pitches:
                wave = 0.5 * create_wave(f=pitches[com], tone=tone, buf=22050)
                sd.play(wave, sample_rate)
                sd.wait()
            case _:
                print(f"{com} can't be accepted") 
