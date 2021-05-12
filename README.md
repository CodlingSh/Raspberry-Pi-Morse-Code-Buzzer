A super simple, yet really fun little project I made awhile back to familiarize myself with using the GPIO pins on a Raspberry Pi. When run the program will ask the user for a string, and then convert the string to morse code and then flash a light or buzz a buzzer in the pattern.

To use this program, simply hook up a circuit comprising of a LED with a 1kΩ resistor along with another circuit comprising of just a piezo buzzer. By default, these circuits should connect to GPIO pin 17 and 25 (11 and 22 if you are going by the BCM numbering), but this can easily be changed by altering the values of the pin1 and pin2 variables on line 135 and 136 respectivly. You also need to make sure that you have the RPi.GPIO library installed.

Here is a video of the program in action:
<iframe width="560" height="315" src="https://www.youtube.com/embed/u2toeC-oG1M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
