from dip_coater.config.config_base import *

# TMC2660 specific settings

# Current settings (in mA)
DEFAULT_CURRENT = 2000
DEFAULT_CURRENT_STANDSTILL = 100
MIN_CURRENT = 74    # Minimum current that can be sensed by the TMC2660 (with 350 mV full scale VSENSE)
MAX_CURRENT = 2000  # Absolute max limit for TMC2660 !

# Other motor settings
INVERT_MOTOR_DIRECTION = False

