# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 Cooper Dalrymple
#
# SPDX-License-Identifier: Unlicense

import ulab.numpy as np

import synthwaveform

SIZE = 8
TYPE = np.float

print(synthwaveform.sine(size=SIZE, dtype=TYPE))
print(synthwaveform.triangle(size=SIZE, dtype=TYPE))
print(synthwaveform.saw(size=SIZE, dtype=TYPE))
print(synthwaveform.square(size=SIZE, dtype=TYPE))
print(synthwaveform.noise(size=SIZE, dtype=TYPE))
print(
    synthwaveform.mix(
        synthwaveform.sine(size=SIZE, dtype=TYPE), (synthwaveform.noise(size=SIZE, dtype=TYPE), 0.5)
    )
)
print(synthwaveform.from_wav("test.wav", SIZE))
