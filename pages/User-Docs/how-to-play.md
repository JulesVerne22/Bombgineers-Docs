---
layout: page
title: How to Play
permalink: /user-docs/how-to-play/
---

# How to play

If you have not performed the setup yet, please do so [here](setup.md)

## Start Menu

Now that you have performed the setup, you should have a start menu displayed across 3 screens. 

![Start Menu](./3-screen-start-menu.PNG)

Within the start menu, there are a few options. 

- Start
    - This will start the simulation
- Options
    - This will allow for adjustments to be made to the simulation such as plane speed, altitude, bomb-type, wind speed, etc.
![Options Menu](./options-menu.PNG)
- Credits
    - Displays the developers
![Credits Menu](./credits-menu.PNG)
- Exit
    - Exits the game

One key note is in the options menu. Please observe that the options include a selection for fullscreen or windowed. It is recommended that the windowed option is selected. This is susceptible to change if some development occurs to help with the multiscreen view.

## Simulation

After messing with the options menu, you will begin the simulation. There will be some warm up time to get things setup up (mainly changing camera angles).

Once the bombsight appears, the simulation has begun. 

![Bombsight Widget](./bombsight-widget.PNG)

Please notice that the bombsight display is on two monitors while the 3D view of the plane is on the third monitor. Also, notice that the 3D view has a drop trajectory for the bomb. 

![Side View Widget](./side-view-widget.PNG)

The bombsight view will be the main view to look at.

### Inputs into bomb tables

On the bombsight screens, there will be inputs provided such as true airspeed, bombing altitude, and bomb type. These should correlate to values within the bombing tables. 

These can be located in the upper left of the bombsight widget.

### Lining up the bombsight

The first order of business is lining up the bombsight. Essentailly, this will entail adjusting the y-axis input to center the line of sight of the bombsight onto the target. Please be aware that since the other inputs have not be correctly input, the crosshairs will begin wavering off of the target.

### Inputs to simulation

Looking through the bomb tables, values for actual time of fall and trail will be provided. With these values, twist the ATF and trail knobs until they read correctly on the bombsight view (they are in the lower right). 

### Rate Adjustment

From here, the game of correcting will be played. The user will switch from adjusting the rate knob to line up with the groundspeed of the plane (Note that in case of wind, groundspeed does not equal true airspeed). With adjusting the rate knob, the user will continuously recenter the crosshairs over the target. If the crosshairs do not waver from the target, then inputs should be correct. If the crosshairs do waver from the target, continue correcting the inputs. The rate value can be found in the lower right of the bombsight widget.

### Dropping the bomb

As per the case of the norden bombsight, the bombsight had the capability of releasing the bomb automatically based on a few factors.

First, the bombsight calculates the angle where the user is aiming there crosshair. This is not too difficult as long as the True Vertical is accurate (True Vertical references what the gyroscope thinks is vertical).

Additionally, based on the inputs from the user (i.e. ATF, Trail, and rate), the bombsight will calculate a necessary drop angle. The two angles in question can be found in the lower right of the bombsight widget.

With these two angles, as soon as the drop angle equals the line of sight angle, the bomb will drop automatically.

### After bomb drop

Now that the bomb is away, the 3D view will show the bomb trajectory as well as the bomb dropping. Watching for a few seconds will assure the bomb hits its target. Shortly after the bomb explodes, the simulation will end.

## End Menu

Now that you have blown up your target, a few stats will be displayed on the end menu. Namely, the accuracy of the drop. This details how close to the target did the bomb land. 

From the end menu, the user has two options:

- Retry
    - Will return to start menu
- Exit
    - Will exit the simulation

![End Menu](./end-menu.PNG)

