import pygame
import numpy
import math
import time
import threading

pygame.init()

bits = 16
sample_rate = 44100
channels = 8  # Ensure we use stereo

# Pre-initialize the mixer with the correct parameters
pygame.mixer.pre_init(sample_rate, -bits, channels)
pygame.mixer.init()

# Check the mixer initialization
print(f"Number of mixer channels (should be 2): {pygame.mixer.get_num_channels()}")
print(f"Mixer frequency: {pygame.mixer.get_init()[0]}")
print(f"Mixer format: {pygame.mixer.get_init()[1]}")
print(f"Mixer channels: {pygame.mixer.get_init()[2]}")

def sine_x(amp, freq, t):
    return int(round(amp * math.sin(2 * math.pi * freq * t)))

class Tone:
    @staticmethod
    def sine(freq, duration=1, speaker=None):
        num_samples = int(round(duration * sample_rate))
        sound_buffer = numpy.zeros((num_samples, channels), dtype=numpy.int16)
        amplitude = 2 ** (bits - 1) - 1

        for sample_num in range(num_samples):
            t = float(sample_num) / sample_rate
            sine_wave = sine_x(amplitude, freq, t)

            if speaker == 'r':
                sound_buffer[sample_num][1] = sine_wave
            elif speaker == 'l':
                sound_buffer[sample_num][0] = sine_wave
            else:
                sound_buffer[sample_num][0] = sine_wave
                sound_buffer[sample_num][1] = sine_wave

        # Check the shape of the sound buffer
        # print(f"Sound buffer shape: {sound_buffer.shape}")

        sound = pygame.sndarray.make_sound(sound_buffer)
        sound.set_volume(1.0)
        sound.play(loops=0, maxtime=int(duration * 1000))
        time.sleep(duration)

    @staticmethod
    def create_tone_from_freq(freq_list, duration=1):
        tone_threads = []

        for freq in freq_list:
            thread = threading.Thread(target=Tone.sine, args=[freq, duration])
            tone_threads.append(thread)
        
        for thread in tone_threads:
            thread.start()

        for thread in tone_threads:
            thread.join()