import RPi.GPIO as GPIO                                                                         #import the RPi.GPIO module to allow us use the board GPIO pins.
import pyrebase                                                                                 #import the pyrebase module which allows us to communicate with the firebase servers.
from time import sleep                                                                          #import the time modulde to allow us do the delay stuff.

config = {                                                              #define a dictionary named config with several key-value pairs that configure the connection to the database.
  "apiKey": "AIzaSyBNhQMH700fEAMJorLNnRC1rt6ZzsXKANE",
  "authDomain": "pearlhacks2021.firebaseapp.com",
  "databaseURL": "https://pearlhacks2021-default-rtdb.firebaseio.com",
  "storageBucket": "pearlhacks2021.appspot.com"
}

firebase = pyrebase.initialize_app(config)                              #initialize the communication with the "firebase" servers using the previous config data.

redLED = 12                                                                                    
blueLED = 19                                                                                   
greenLED = 18                                                                                 
servo = 25

GPIO.setmode(GPIO.BCM)                                                                         
GPIO.setwarnings(False)                                                                        

GPIO.setup(redLED,GPIO.OUT)                                                                    
GPIO.setup(blueLED,GPIO.OUT)                                                                   
GPIO.setup(greenLED,GPIO.OUT)                                                                 
GPIO.setup(servo,GPIO.OUT)

red_pwm = GPIO.PWM(redLED,1000)                                                                
blue_pwm = GPIO.PWM(blueLED,1000)                                                              
green_pwm = GPIO.PWM(greenLED,1000)                                                            
pwm=GPIO.PWM(servo, 50)

red_pwm.start(0)                                                                               
blue_pwm.start(0)                                                                              
green_pwm.start(0)                                                                             
pwm.start(0)

print("Starting now! Press CTRL+C to exit")                                       



def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(servo, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(servo, False)
	pwm.ChangeDutyCycle(0)

def openDispenserServo():
    db=firebase.database()
    SetAngle(90)
    sleep(1)
    SetAngle(0)
    data = "No"
    db.child("pearlHacks_tabLetTab").child("access").set(data)
    print("Done")

def distract():
    print("Success")
    


try:
    while True:                                                                              

        database = firebase.database()                                            
        openDispenser = database.child("hardware")                            

        database = firebase.database()                                         
        openDispenser = database.child("hardware")                        
        controlDispenser = openDispenser.child("pill okay").get().val()  
        print(str(controlDispenser))

        database = firebase.database()                                         
        distractionAttempt = database.child("pearlHacks_tabLetTab")                        
        distraction = distractionAttempt.child("Distraction attempted").get().val()  
        print(str(distraction))
        #openDispenserServo()
 
        database = firebase.database()                                         
        distractionAttempt = database.child("pearlHacks_tabLetTab")                        
        access = distractionAttempt.child("access").get().val()  
        print(str(access))

        if "Yes" in controlDispenser and "yes" in access:
            openDispenserServo()
        
        if "\"Distract\"" in distraction:
            distract()

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    red_pwm.stop() # stop red PWM
    blue_pwm.stop() # stop blue PWM
    green_pwm.stop() # stop green PWM
    GPIO.cleanup() # cleanup all GPIO
