# Weekday

* Author: Ruslan Dolovaniuk (Ukraine)


Additional functions for working with date and time

## List of hotkeys:
* All hotkeys are bound to NVDA+W. Different functions depend on the selected mode;
* NVDA+ALT+W: switches operating modes;
* NVDA+SHIFT+W: in countdown and alarm modes, switches between time measurements (hours, minutes, seconds);
* NVDA+SHIFT+W: in day of the week, stopwatch and time signal modes, saves the settings of all modes;

## Mode Day of the week
* NVDA+W: pronounces the day of the week;

## Stopwatch mode
* NVDA+W: single press turns on the stopwatch if it is not running;
* NVDA+W: Double click starts the stopwatch if it is not running or pauses it if it is running. Also restores its operation if it was suspended;
* NVDA+W: Triple click disables running stopwatch;

## Countdown mode
The initial selection turns on the mode setting. It contains the following combinations:
* NVDA+SHIFT+W: Switches settings units (hours, minutes, seconds);
* NVDA+W: A single press switches the time selection for installation, for hours in steps of 1 hour, for minutes and seconds - in steps of 5 units;
* NVDA+W: double click sets the selected interval;
* NVDA+W: triple pressing starts the countdown;

When running, the following combinations:
* NVDA+W: a single press tells how much time is left until the designated period;
* NVDA+W: double-clicking pauses the countdown if it was running, or restores it back if it was paused;
* NVDA+W: triple pressing stops the countdown;

## Alarm mode
The initial selection turns on the mode setting. It contains the following combinations:
* NVDA+SHIFT+W: Switches settings units (hours, minutes, seconds);
* NVDA+W: A single press switches the time selection for installation, for hours in steps of 1 hour, for minutes and seconds - in steps of 5 units;
* NVDA+W: double click sets the selected time;
* NVDA+W: triple pressing starts the alarm;

When running, the following combinations:
* NVDA+W: a single press tells you how much time is left until the appointed time;
* NVDA+W: triple pressing stops the alarm;

## Time signal mode
* NVDA+W: switches the signal period time (60, 30, 15, 0) minutes. Default 0 - signal disabled;

##List of changes:
###Version 0.5.2
* added saving settings;

###Version 0.5.0
* added alarm mode;

###Version 0.4.5
* added Time Signal mode;

###Version 0.4.0
* redesigned component architecture;
* added countdown timer;
* the control system has been changed and modes have been introduced;

###Version 0.3.0
* Added stopwatch;
