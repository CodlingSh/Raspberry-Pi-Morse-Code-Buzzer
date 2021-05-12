# SHELDON'S MORSE CODE PROGRAM

import RPi.GPIO as GPIO, time

def main():
    wordToTranslate = ""
    
    wordToTranslate = input("Please enter a word to translate into Morse Code: ")
    
    beep(wordToTranslate)

def beep(word):
    chars = []
    

    for let in word.lower():
        if let == "a":
            chars.append(".-")
            chars.append(" ")
        elif let == "b":
            chars.append("-...")            
            chars.append(" ")            
        elif let == "c":
            chars.append("-.-.")
            chars.append(" ")
        elif let == "d":
            chars.append("-..")
            chars.append(" ")            
        elif let == "e":
            chars.append(".")
            chars.append(" ")            
        elif let == "f":
            chars.append("..-.")
            chars.append(" ")            
        elif let == "g":
            chars.append("--.")
            chars.append(" ")            
        elif let == "h":
            chars.append("....")
            chars.append(" ")            
        elif let == "i":
            chars.append("..")
            chars.append(" ")            
        elif let == "j":
            chars.append(".---")
            chars.append(" ")            
        elif let == "k":
            chars.append("-.-")
            chars.append(" ")            
        elif let == "l":
            chars.append(".-..")
            chars.append(" ")            
        elif let == "m":
            chars.append("--")
            chars.append(" ")            
        elif let == "n":
            chars.append("-.")
            chars.append(" ")            
        elif let == "o":
            chars.append("---")
            chars.append(" ")            
        elif let == "p":
            chars.append(".--.")
            chars.append(" ")            
        elif let == "q":
            chars.append("--.-")
            chars.append(" ")            
        elif let == "r":
            chars.append(".-.")
            chars.append(" ")            
        elif let == "s":
            chars.append("...")
            chars.append(" ")                        
        elif let == "t":
            chars.append("-")
            chars.append(" ")            
        elif let == "u":
            chars.append("..-")
            chars.append(" ")            
        elif let == "v":
            chars.append("...-")
            chars.append(" ")            
        elif let == "w":
            chars.append(".--")
            chars.append(" ")            
        elif let == "x":
            chars.append("-..-")
            chars.append(" ")            
        elif let == "y":
            chars.append("-.--")
            chars.append(" ")            
        elif let == "z":
            chars.append("--..")
            chars.append(" ")            
        elif let == ".":
            chars.append(".....")
            chars.append(" ")
        elif let == "!":
            chars.append("--..--")
            chars.append(" ")
        elif let == " ":
            chars.append("  ")            

    print("".join(chars))

    for codePiece in chars:
        for symbol in codePiece:
            if symbol == ".":
                GPIO.output(pin1, GPIO.HIGH)
                GPIO.output(pin2, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(pin1, GPIO.LOW)
                GPIO.output(pin2, GPIO.LOW)
                time.sleep(0.1)
            elif symbol == "-":
                GPIO.output(pin1, GPIO.HIGH)
                GPIO.output(pin2, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(pin1, GPIO.LOW)
                GPIO.output(pin2, GPIO.LOW)
                time.sleep(0.1)
            elif symbol == " ":
                time.sleep(0.1)
    main()

def setup():
    # SET UP THE GPIO PINS
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)

if __name__ == '__main__':
    pin1 = 11
    pin2 = 22

    setup()
    print("Make sure you are connected to the pins marked \"GPIO17\" and \"GPIO25\". \nPress Ctrl + c to exit.\n")
    try:
        main()
    except KeyboardInterrupt: # EXIT THE PROGRAM WHEN PRESSING CONTROL + C
        print("\nGood bye!")
        GPIO.cleanup()
