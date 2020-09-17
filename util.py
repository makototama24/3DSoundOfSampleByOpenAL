import ffmpeg
import pyogg
from openal import *


AUDIO_1 = 'create.wav'

# Write absolute path of the music file
USE_AUDIO = './Music/wav_Sound/create.wav'

# Write absolute path of the figure file
FIGURE = ''

WINDOW_WIDTH, WINDOW_HEIGHT = 650, 450
WINDOW_TITLE = 'OpenAL Sample'
WINDOW_INITSIZE = '350x250'

COORDINATE_FONTSIZE = 20

BUTTON_FONTSIZE = 15
BUTTON_WIDTH, BUTTON_HEIGHT = 10, 2
CANVAS_WIDTH, CANVAS_HEIGHT = 450, 350

ENTRY_SIZE = 3
ENTRY_INIT_x = ENTRY_INIT_y = ENTRY_INIT_z = 0
ENTRY_ipadx = ENTRY_ipady = 10
ENTRY_padx = 20
