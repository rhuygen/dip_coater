| Type | Name                                        | AP Variable                | Description                                                                                                                                                                                                                                                                                                                      | Data Type | Mask         | Min                  | Default  | Max        | Unit     | Access |
|------|---------------------------------------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|--------------|----------------------|----------|------------|----------|--------|
| 0    | Target position                             | TargetPosition             | The desired target position in position mode.                                                                                                                                                                                                                                                                                    | Signed    |              | -2147483648          | 0        | 2147483647 | [µsteps] | RW     |
| 1    | Actual position                             | ActualPosition             | The actual position of the motor. Stop the motor before overwriting it. Should normally only be overwritten for reference position setting.                                                                                                                                                                                      | Signed    |              | -2147483648          | 0        | 2147483647 | [µsteps] | RW     |
| 2    | Target speed                                | TargetVelocity             | The desired speed in velocity mode. Not valid in position mode.                                                                                                                                                                                                                                                                  | Signed    |              | -131072              | 0        | 131072     | [pps]    | RW     |
| 3    | Actual speed                                | ActualVelocity             | The actual speed of the motor.                                                                                                                                                                                                                                                                                                   | Signed    |              | -131072              | 0        | 131072     | [pps]    | R      |
| 4    | Maximum speed                               | MaxVelocity                | The maximum speed used for positioning ramps.                                                                                                                                                                                                                                                                                    | Unsigned  |              | 0                    | 51200    | 131072     | [pps]    | RW     |
| 5    | Maximum acceleration                        | MaxAcceleration            | Maximum acceleration in positioning ramps. Acceleration and deceleration value in velocity mode.                                                                                                                                                                                                                                 | Unsigned  |              | 0                    | 51200    | 2147483647 | [pps²]   | RW     |
| 6    | Maximum current                             | MaxCurrent                 | Motor current used when motor is running. Where 0 = 3.125% up to 31 = 100% of maximum module current. Calculated by: maximum module current * (value + 1)/ 32.                                                                                                                                                                   | Unsigned  |              | 0                    | 24       | 31         |          | RW     |
| 7    | Standby current                             | StandbyCurrent             | The current used when the motor is not running. Where 0 = 3.125% up to 31 = 100% of maximum module current. Calculated by: maximum module current * (value + 1)/ 32. This value should be as low as possible so that the motor can cool down when it is not moving. Please see also parameter 214.                               | Unsigned  |              | 0                    | 3        | 31         |          | RW     |
| 8    | Position reached flag                       | PositionReachedFlag        | This flag is always set when target position and actual position are equal. 0 - Target position not reached, 1 - Target position reached                                                                                                                                                                                         | Bool      |              | 0                    | 0        | 1          |          | R      |
| 29   | Measured Speed                              | MeasuredSpeed              | Current speed value measured from the TMC2660 current position or from encoder.                                                                                                                                                                                                                                                  | Signed    |              | -2147483648          | 0        | 2147483647 |          | R      |
| 50   | StepDir source                              | StepDirSource              | StepDir interface source. 0 - internal, 1 - external                                                                                                                                                                                                                                                                             | Choice    |              | 0                    | 0        | 1          |          | RW     |
| 51   | StepDir frequency                           | StepDirFrequency           | The maximum frequency of the StepDir interface. This is limiting velocity and acceleration.                                                                                                                                                                                                                                      | Unsigned  |              | 0                    | 131072   | 2147483647 | [Hz]     | RW     |
| 140  | Microstep Resolution                        | MicrostepResolution        | Microstep resolutions per full step: 1 - fullstep, 2 - halfstep, 4 - 4 microsteps, 8 - 8 microsteps, 16 - 16 microsteps, 32 - 32 microsteps, 64 - 64 microsteps, 128 - 128 microsteps, 256 - 256 microsteps                                                                                                                      | Choice    |              | 1                    | 256      | 256        |          | RW     |
| 160  | Microstep Interpolation                     | Intpol                     | Interpolation of the current microstep resolution to 256 microsteps: 0 - Disable STEP pulse interpolation, 1 - Enable STEP pulse multiplication by 16.                                                                                                                                                                           | Bool      |              | 0                    | 1        | 1          |          | RWE    |
| 161  | Double Edge Steps                           | DoubleEdgeSteps            | Step impulse at each step edge to reduce step frequency requirement. 0 - Rising edge active, falling inactive. 1 - Both edges active.                                                                                                                                                                                            | Bool      |              | 0                    | 0        | 1          |          | RWE    |
| 162  | Chopper blank time                          | ChopperBlankTime           | Selects the comparator blank time. This time needs to safely cover the switching event and the duration of the ringing on the sense resistor. Normally leave at the default value.                                                                                                                                               | Unsigned  |              | 0                    | 0        | 3          |          | RW     |
| 163  | Constant TOff Mode                          | ConstantTOffMode           | Selection of the chopper mode. 0 - spread cycle, 1 - classic constant off time                                                                                                                                                                                                                                                   | Bool      |              | 0                    | 0        | 1          |          | RW     |
| 164  | Disable fast decay comparator               | DisableFastDecayComparator | See parameter 163. For "classic const. off time", setting this parameter to "1" will disable current comparator usage for termination of fast decay cycle. 0 - enable comparator, 1 - disable comparator                                                                                                                         | Bool      |              | 0                    | 0        | 1          |          | RW     |
| 165  | Chopper hysteresis end / fast decay time    | ChopperHysteresisEnd       | See parameter 163. For "spread cycle" chopper mode this parameter will set / return the hysteresis end setting (hysteresis end value after a number of decrements). For "classic const. off time" chopper mode this parameter will set / return the fast decay time.                                                             | Unsigned  |              | 0                    | 0        | 15         |          | RW     |
| 166  | Chopper hysteresis start / sine wave offset | ChopperHysteresisStart     | See parameter 163. For "spread cycle" chopper mode this parameter will set / return the Hysteresis start setting (please note that this value is an offset to the hysteresis end value). For "classic const. off time" chopper mode this parameter will set / return the sine wave offset.                                       | Unsigned  |              | 0                    | 0        | 8          |          | RW     |
| 167  | Chopper off time                            | TOff                       | The off time setting controls the minimum chopper frequency. An off time within the range of 5us to 20us will fit. Off time setting for constant t Off chopper: NCLK = 12 + 32 tOFF (Minimum is 64 clocks) Setting this parameter to zero completely disables all driver transistors and the motor can freewheel.                | Unsigned  |              | 0                    | 0        | 15         |          | RW     |
| 168  | smartEnergy current minimum (SEIMIN)        | SEIMIN                     | Sets the lower motor current limit for coolStep operation by scaling the maximum current (see axis parameter 6) value. 0 - 1/2 of CS, 1 - 1/4 of CS                                                                                                                                                                              | Bool      |              | 0                    | 0        | 1          |          | RW     |
| 169  | smartEnergy current down step               | SECDS                      | Sets the number of stallGuard2 readings above the upper threshold necessary for each current decrement of the motor current. Number of stallGuard2 measurements per decrement: Scaling: 0. . . 3: 32, 8, 2, 1. 0: slow decrement, 3: fast decrement                                                                              | Unsigned  |              | 0                    | 0        | 3          |          | RW     |
| 170  | smartEnergy hysteresis                      | smartEnergyHysteresis      | Sets the distance between the lower and the upper threshold for stallGuard2 reading. Above the upper threshold the motor current becomes decreased. Hysteresis: ([AP172] + 1) * 32. Upper stallGuard threshold: ([AP172] + [AP170] + 1) * 32                                                                                     | Unsigned  |              | 0                    | 0        | 15         |          | RW     |
| 171  | smartEnergy current up step                 | SECUS                      | Sets the current increment step. The current becomes incremented for each measured stallGuard2 value below the lower threshold see smartEnergy hysteresis start). Current increment step size: Scaling: 0. . . 3: 1, 2, 4, 8. 0: slow increment, 3: fast increment / fast reaction to rising load                                | Unsigned  |              | 0                    | 0        | 3          |          | RW     |
| 172  | smartEnergy hysteresis start                | smartEnergyHysteresisStart | The lower threshold for the stallGuard2 value (see smart Energy current up step).                                                                                                                                                                                                                                                | Unsigned  |              | 0                    | 0        | 15         |          | RW     |
| 173  | stallGuard2 filter enable                   | SG2FilterEnable            | Enables the stallGuard2 filter for more precision of the movement. If set, reduces the measurement frequency to one measurement per four fullsteps. In most cases it is expedient to set the filtered mode before using coolStep. Use the standard mode for step loss detection. 0 - standard mode, 1 - filtered mode            | Bool      |              | 0                    | 0        | 1          |          | RW     |
| 174  | stallGuard2 threshold                       | SG2Threshold               | This signed value controls stallGuard2 threshold level for stall output and sets the optimum measurement range for readout. A lower value gives a higher sensitivity. Zero is the starting value. A higher value makes stallGuard2 less sensitive and requires more torque to indicate a stall.                                  | Signed    |              | -64                  | 0        | 63         |          | RW     |
| 175  | Slope control, high side                    | SLPH                       | In temperature compensated mode (tc), the MOSFET gate driver strength is increased if the over-temperature warning temperature is reached. This compensates for temperature dependency of high-side slope control. 0 - Minimum, 1 - Minimum temperature compensation mode, 2 - Medium temperature compensation mode, 3 - Maximum | Choice    |              | 0                    | 0        | 3          |          | RW     |
| 176  | Slope control, low side                     | SLPL                       | In temperature compensated mode (tc), the MOSFET gate driver strength is increased if the over-temperature warning temperature is reached. This compensates for temperature dependency of low-side slope control. 0 - Minimum, 1 - Minimum temperature compensation mode, 2 - Medium temperature compensation mode, 3 - Maximum  | Choice    |              | 0                    | 0        | 3          |          | RW     |
| 177  | Short to Ground Protection                  | ShortToGroundProtection    | Disable short to ground protection. 0 - Short to GND protection is enabled, 1 - Short to GND protection is disabled                                                                                                                                                                                                              | Bool      |              | 0                    | 0        | 1          |          | RW     |
| 178  | Short-to-ground detection timer             | (Not available in AP)      | Timing for the short-to-ground detection. 0 - 3.2 us, 1 - 1.6 us, 2 - 1.2 us, 3 - 0.8 us                                                                                                                                                                                                                                         | Choice    |              | 0                    | 0        | 3          |          | RW     |
| 179  | VSense                                      | VSense                     | Sense resistor voltage-based current scaling. (Full-scale refers to a current setting of 31 and a DAC value of 255.) 0 - Full-scale sense resistor voltage is 305mV. 1 - Full-scale sense resistor voltage is 165mV.                                                                                                             | Bool      |              | 0                    | 0        | 1          |          | RW     |
| 180  | smartEnergy actual current                  | smartEnergyActualCurrent   | This status value provides the actual motor current setting as controlled by coolStep. The value goes up to the CS value and down to the portion of CS as specified by SEIMIN. Actual motor current scaling factor: 0. . . 31: 1/32, 2/32, . . . 32/32                                                                           | Unsigned  |              | 0                    | 0        | 31         |          | R      |
| 181  | smartEnergy stall velocity                  | smartEnergyStallVelocity   | Velocity from which stop on stall feature is active                                                                                                                                                                                                                                                                              | Unsigned  |              | 0                    | 0        | 2147483647 | [pps]    | RW     |
| 182  | smartEnergy threshold speed                 | smartEnergyThresholdSpeed  | Above this speed coolStep becomes enabled.                                                                                                                                                                                                                                                                                       | Unsigned  |              | 0                    | 0        | 7999774    | [pps]    | RW     |
| 183  | Disable step/dir interface                  | SDOFF                      | Disable step/dir interace and use SPI interface to move the motor. 0 - Enable step/dir, 1 - Disable step/dir                                                                                                                                                                                                                     | Bool      |              | 0                    | 0        | 1          |          | RW     |
| 184  | Random TOff mode                            | RandomTOffMode             | Enable / disable random TOff mode. 0 - Chopper off time is fixed, 1 - Chopper off time is random                                                                                                                                                                                                                                 | Bool      |              | 0                    | 0        | 1          |          | RW     |
| 206  | Load value                                  | LoadValue                  | Actual current control                                                                                                                                                                                                                                                                                                           | 208       | Status Flags | TMC262 status flags. | Unsigned |            | 0        | 0      | 255        |          | R      |
| 208  | Status Flags                                | DrvStatusFlags             | TMC262 status flags.                                                                                                                                                                                                                                                                                                             | Unsigned  |              | 0                    | 0        | 255        |          | R      |
| 214  | Power Down Delay                            | PowerDownDelay             | Standstill period before the current will be ramped down to standby current. The standard value is 200 (which means 2000ms).                                                                                                                                                                                                     | Signed    |              | 0                    | 0        | 65535      | [10 ms]  | RW     |