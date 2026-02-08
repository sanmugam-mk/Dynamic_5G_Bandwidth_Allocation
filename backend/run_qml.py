import numpy as np
from app.allocation.optimizer import quantum_optimize

INPUT_FILE = "gnuradio_input.bin"
OUTPUT_FILE = "amplitudes.bin"

SAMPLE_RATE = 32000


def generate_signal(amplitudes):
    t = np.arange(0, 1, 1 / SAMPLE_RATE)

    signal = np.zeros(len(t))

    base_freq = 500

    for i, amp in enumerate(amplitudes):
        f = base_freq + i * 200
        signal += amp * np.cos(2 * np.pi * f * t)

    return signal.astype(np.float32)


def write_for_gnuradio(amplitudes):
    signal = generate_signal(amplitudes)
    signal.tofile(OUTPUT_FILE)


def main():
    data = np.fromfile(INPUT_FILE, dtype=np.float32)

    if len(data) == 0:
        print("No data yet")
        return

    optimized = quantum_optimize(data, total_prbs=50)

    write_for_gnuradio(optimized)

    print("Updated amplitudes.bin")


if __name__ == "__main__":
    main()