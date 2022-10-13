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
### Onshape
* [Onshape_Assignment_Template](#Onshape_Assignment_Template)

&nbsp;

## LED_blinky.py

### Assignment Description

I wrote code that tells the Raspberry Pi to blink the LED that is built into it. When the code is running, the LED turns on for one second before turning off for one second and looping.

### Evidence 

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/LED_blinky.png">

### Code

[LED_blinky.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/launch_countdown.py)

### Reflection

This was a pretty simple assignment. The only thing I had trouble with was getting the code to run. I would constantly get an error saying that it couldn't find import board but eventually I got it to work by literally just waiting.

&nbsp;

## Launch_Pad_Part_1

### Assignment Description

I wrote code that displays a countdown from 10 to 0 ("liftoff") in the terminal using a for loop. 

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/LaunchCountdown.png">

### Code

[launch_countdown.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/launch_countdown.py)

### Reflection

There wasn't much to do for this one once again. After trying to run the code without 3 different numbers in the for loop, I realized I needed to add a -1 so it would actually count down.

&nbsp;

## Launch_Pad_Part_2

### Assignment Description

Adding on to the part 1 code, I connected 2 LEDs to my arduino using a breadboard. One of the LEDs was red and one was green. During the countdown, the red LED would blink every second until the message "LIFTOFF" was printed onto the terminal, at which point the red LED would stop blinking and the green LED would turn on for 10 seconds.

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/ezgif.com-gif-maker%20(1).gif" width="350">

### Code

[launch_countdown.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/launch_countdown.py)

### Wiring

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/Launch2.png">

### Reflection

For this assignment, I had a lot of trouble understanding how the wiring works. Turns out everyone else was overcomplicating it and it is much easier than it seemed. 

&nbsp;

## Launch_Pad_Part_3

### Assignment Description

I connected a button to the previous part so that when it is pressed, the countdown begins and the red LED starts blinking.

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/ezgif.com-gif-maker%20(2).gif" width="350">

### Code

[launch_countdown.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/launch_countdown.py)

### Wiring

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/Launch3.png">

### Reflection

This part was really easy and fun because all I had to do was put all of the original for loop into a while true if button pressed loop and then it would work.

&nbsp;

## Launch_Pad_Part_4

### Assignment Description

For this part of the Launch Pad assignments I had to get a servo motor to spin when the timer reaches 0. I got the servo motor to spin 180 degrees clockwise once the green light came on, then 2 seconds later it would turn 180 degrees counterclockwise.

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/ezgif.com-gif-maker%20(4).gif">

### Code

[launch_countdown.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/launch_countdown.py)

### Wiring

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/Launch4.png">

### Reflection

The only slightly challenging part of this assignment was adding the library to my Raspberry Pi Pico. To do that I had to download all of the python libraries and then indevidually extract the adafruit_motor library and add it to my circuit python "lib" folder. After that all I did was imported the library and added a for angle in range loop so that the motor would turn 180 degrees when the green light turns on and then turn back 180 degrees 2 seconds later.

&nbsp;

## Crash_Avoidance_Part_1

### Assignment Description

The goal for this assignment was to connect an accelerometer to my Raspberyy Pi Pico and show the X, Y, and Z values on the terminal.

### Evidence

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/ezgif.com-gif-maker%20(5).gif">

### Code

[crash_avoidance.py](https://github.com/Scrusse/Engineering_4_Notebook/blob/main/raspberry-pi/crash_avoidance.py)

### Wiring

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/CrashAvoidance1.png">

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

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[hot moms of cville](https://www.hotmomsofcville.com/)

### Test Image

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/images/WideMace.png">

### Test GIF

<img src="https://github.com/Scrusse/Engineering_4_Notebook/blob/main/images/NegativeEthicalBilby-max-1mb.gif">
