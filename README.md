# Engineering_4_Notebook

&nbsp;

## Table of Contents
### LED Blink
* [LED blinky](#LED_blinky.py)
### Lauch Pad
* [Launch Pad Part 1](#Launch_Pad_Part_1)
* [Launch Pad Part 2](#Launch_Pad_Part_2)
* [Launch Pad Part 3](#Launch_Pad_Part_3)
* [Launch Pad Part 4](#Launch_Pad_Part_4)
### Crash Avoidance
* [Crash Avoidance Part 1](#Crash_Avoidance_Part_1)
* [Crash Avoidance Part 2](#Crash_Avoidance_Part_2)
### Landing Area
* [Landing Area Part 1](#Landing_Area_Part_1)
### Onshape
* [FEA Beam Design Part 1](#FEA_Beam_Design_Part_1)

&nbsp;

## LED_blinky.py

### Assignment Description

I wrote code that tells the Raspberry Pi to blink the LED that is built into it. When the code is running, the LED turns on for one second before turning off for one second and looping.

### Evidence 

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/LED_blinky.png">

### Code

[LED_blinky.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/launch_countdown.py)

### Reflection

This was a pretty simple assignment. The only thing I had trouble with was getting the code to run. I would constantly get an error saying that it couldn't find import board but eventually I got it to work by literally just waiting.

&nbsp;

## Launch_Pad_Part_1

### Assignment Description

I wrote code that displays a countdown from 10 to 0 ("liftoff") in the terminal using a for loop. 

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/LaunchCountdown.png">

### Code

[launch_countdown.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/launch_countdown.py)

### Reflection

There wasn't much to do for this one once again. After trying to run the code without 3 different numbers in the for loop, I realized I needed to add a -1 so it would actually count down.

&nbsp;

## Launch_Pad_Part_2

### Assignment Description

Adding on to the part 1 code, I connected 2 LEDs to my arduino using a breadboard. One of the LEDs was red and one was green. During the countdown, the red LED would blink every second until the message "LIFTOFF" was printed onto the terminal, at which point the red LED would stop blinking and the green LED would turn on for 10 seconds.

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/ezgif.com-gif-maker%20(1).gif" width="350">

### Code

[launch_countdown.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/launch_countdown.py)

### Wiring

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/Launch2.png">

### Reflection

For this assignment, I had a lot of trouble understanding how the wiring works. Turns out everyone else was overcomplicating it and it is much easier than it seemed. 

&nbsp;

## Launch_Pad_Part_3

### Assignment Description

I connected a button to the previous part so that when it is pressed, the countdown begins and the red LED starts blinking.

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/ezgif.com-gif-maker%20(2).gif" width="350">

### Code

[launch_countdown.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/launch_countdown.py)

### Wiring

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/Launch3.png">

### Reflection

This part was really easy and fun because all I had to do was put all of the original for loop into a while true if button pressed loop and then it would work.

&nbsp;

## Launch_Pad_Part_4

### Assignment Description

For this part of the Launch Pad assignments I had to get a servo motor to spin when the timer reaches 0. I got the servo motor to spin 180 degrees clockwise once the green light came on, then 2 seconds later it would turn 180 degrees counterclockwise.

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/ezgif.com-gif-maker%20(4).gif">

### Code

[launch_countdown.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/launch_countdown.py)

### Wiring

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/Launch4.png">

### Reflection

The only slightly challenging part of this assignment was adding the library to my Raspberry Pi Pico. To do that I had to download all of the python libraries and then indevidually extract the adafruit_motor library and add it to my circuit python "lib" folder. After that all I did was imported the library and added a for angle in range loop so that the motor would turn 180 degrees when the green light turns on and then turn back 180 degrees 2 seconds later.

&nbsp;

## Crash_Avoidance_Part_1

### Assignment Description

The goal for this assignment was to connect an accelerometer to my Raspberyy Pi Pico and show the X, Y, and Z values on the terminal.

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/ezgif.com-gif-maker%20(5).gif">

### Code

[crash_avoidance.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/crash_avoidance.py)

### Wiring

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/CrashAvoidance1.png">

### Reflection

This assignment was one of the more fun ones in my opinion. I enjoy figuring out how to wire things and the satisfaction of them working after half an hour of trying and failing. The code was pretty simple and was stuff I had done before.

## Crash_Avoidance_Part_2

### Assignment Description

For this part, all I had to do was add a light that activates when the accelerometer is tilted 90 or more degrees sideways. All I had to do was detect when Z was less than 1 and then have the light turn but only when Z was less than 1. The wiring for the light was the exact same as in Launch Pad Part 1.

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/CrashAvoidance2gif.gif">

### Code

[crash_avoidance.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/crash_avoidance.py)

### Wiring

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/CrashAvoidance2.png">

### Reflection

I had no problems doing this assignment because it just combined two things I've already done before.

## Landing_Area_Part_1

### Assignment Description

For this assignment I had to write code that took 3 coordinates and found the area of the triangle made. The coordinates need to be input into the the terminal. This part didn't require any wiring, just the pico.

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/ezgif.com-gif-maker%20(5).gif">

### Code

[landing_area.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/landing_area.py)

### Reflection

This assignment was significantly more coding heavy than any of the other ones. I figured out that this is my weakness and I enjoy the wiring parts of assignments better. I tried to do this one by myself but all of the code for the equasions and stuff was too much. I got help from people like Paul Schakel (he was very helpful).

## FEA_Beam_Design_Part_1

### Assignment Description

This was a group project that involved making a beam that weighs ≤ 13g, is at least 186mm long, and can hold as much weight as possible on the end. We were given a template to work off of. This part could be thought of as the rough draft of the design as we will be optimizing it in part 2.

### Part Link 

[Beam Design](https://cvilleschools.onshape.com/documents/bf97d39192dd8226ac13c025/w/661b56d36143d290099bc165/e/fa44a3634a5c845d4172ad8b)

### Part Image

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/Engagement%20Block%20%2B%20Holder%20(1).png" width="350">

### Reflection

This part only took us around 45 minutes and was pretty simple. I think the triangle things will be very usefull because they add a lot of support without adding much weight. We will probably increase the wall height so it doesn't bend too much.

## FEA_Beam_Design_Part_3

### Assignment Description

For this part, we had to optimize the design of the beam so that it could hold as much weight as possible without breaking or bending too far. 

### Part Link

[Beam Design](https://cvilleschools.onshape.com/documents/bf97d39192dd8226ac13c025/w/661b56d36143d290099bc165/e/fa44a3634a5c845d4172ad8b)

### Part Image

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/sim2.png" width="350">

The image above is a simulation that was done before the final changes were made. The right end of the beam was thickened so it wouldn't bend nearly as much.

### Reflection

Very nice.

## Ring & Spinner

### Assignment Description

For this assignment I had to follow directions to create two of four parts for a full assembly. The two parts I made for this section were the Ring and Spinner.

### Part Link

[Ring](https://cvilleschools.onshape.com/documents/05ddfbcddb1f79cb00b6062d/w/18d4e1dd5368de9cd5e335e5/e/b1dc412b2cb9fb3ed19d906e)

[Spinner](https://cvilleschools.onshape.com/documents/05ddfbcddb1f79cb00b6062d/w/18d4e1dd5368de9cd5e335e5/e/30e46ded1856bfc6903aaef7)

### Part Image

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/Top%2C%20Ring%2C%20Key.png" width="200">
<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/Spinner%20%26%20Prop.png" width="200">

### Reflection

These parts were pretty easy. I learned a little more about helixes on the spinner.

## Key & Prop

### Assignment Description

For this section I had to add onto the already existing parts by editing in context. The parts I made this time were the Key and Prop, finishing the four needed for the full assembly.

### Part Link

[Key](https://cvilleschools.onshape.com/documents/05ddfbcddb1f79cb00b6062d/w/18d4e1dd5368de9cd5e335e5/e/b1dc412b2cb9fb3ed19d906e)

[Prop](https://cvilleschools.onshape.com/documents/05ddfbcddb1f79cb00b6062d/w/18d4e1dd5368de9cd5e335e5/e/b1dc412b2cb9fb3ed19d906e)

### Part Image

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/Top%2C%20Ring%2C%20Key%20(1).png" width="350">
<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/Spinner%20%26%20Prop%20(1).png" width="350">

### Reflection

Every tool I had to use for these parts I have already used before. Both did require a pattern of some kind, with the key using a linear pattern and the prop using circular pattern

## Assembling the Launcher

### Assignment Description

This is the final section of the Launcher. For this I had to simply assemble the four parts I had already made and mate them in a way that it could somewhat function visibly in onshape.

### Part Link

[Full Assembly](https://cvilleschools.onshape.com/documents/05ddfbcddb1f79cb00b6062d/w/18d4e1dd5368de9cd5e335e5/e/b62ee3fa91a1cdd384b0aa7f)

### Part Image

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/Images/Pull%20Copter.png" width="350">

### Reflection

This was a pretty simple assignment. It taught me more about assemblies and how to edit in context. I also learned about how to simplify parts and do it in as few instances as possible.

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[hot moms of cville](https://www.hotmomsofcville.com/)

### Test Image

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/images/WideMace.png">

### Test GIF

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/images/NegativeEthicalBilby-max-1mb.gif">
