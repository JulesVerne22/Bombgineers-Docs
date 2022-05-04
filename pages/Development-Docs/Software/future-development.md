---
layout: page
title: Future Software Dev
permalink: /dev-docs/software/future-software-dev/
---

# Future Software Development

This page is dedicated to things that will need to be adjusted or added in software. 

## Carpet Bomb Accuracy

Currently the simulation takes the location of the first bomb dropped to calculate the accuracy. However, it should be taking the closest of all bombs dropped in order to calculate the accuracy.

## Course Correction due to Wind

When adding wind, there must also be a change in the direction the plane is facing in order to maintain realism. If there is a 90 degree crosswind at half the speed of the plane, the plane would have to turn into the wind in order to cancel that extra acceleration sideways. This could be done by changing the planes rotation value by a calculated amount based on wind speed.

## Bomb Drop Adjustments due to Wind and Gusts

Similar to the above phenomenon, the bomb's trajectory will also be changed by the wind and therefore more adjustments will need to be made to the bombsight calculations.

## Plane Speed and Altitude Randomness

It was asked that we introduce randomness into the options set in the options menu. However, we were unable to achieve this due to time constraints. It is a fairly simple solution though. Simply take the selected value and use a random number function with a speicified range and add that value to the specified variables.

## Scaling and the Fudge Factor Fixes

After almost completing the functional basics of the simulation, it was found that the units in the Unreal Engine crid were not the assumed 1 meter, rather they represent 1cm. So, all calculations and variables are based on that assumption. To offset this, we created a fudge factor which scales these said variables to the proper values or by any scalar for that matter. However, if set to the proper scale, the map will need to be expanded drastically which we did not have time to implement.
