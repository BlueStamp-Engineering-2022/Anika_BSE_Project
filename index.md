# Face Recognition Door Lock
The Face Recognition Door Lock uses the faces of saved images stored in AWS to open a door lock. It can also greet guests, tell you who is at the door, save multiple guests and more. It sends an email with a live picture captured when an unrecognized guest is at the door. Using Rasperry Pi, Arduino, a servo, Python, IDE, and AWS this door lock is fully functional.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Anika Karvat | Saratoga High School | Mechanical Engineering | Incoming Sophomore

![Headstone Image](https://lh3.googleusercontent.com/pw/AM-JKLUdOuU9Q6jJW24ISIrUQ86stBQrCDxvoC6gCmYYJBYLRuTZ0KuYGIkEr4aPZzd6wEQgvUS3nlK2IZbWJMW13zeNAtBtXtwrCLN6D4wDYT2vPBLwp_yU01ss2ku1Mu6appCKLMp1psU20Tl-z7ugj-Xs=s1290-no?authuser=0)
  
# Final Milestone
My final milestone was adding modifications. I added LED lights, one green and one red. The green light flashes for a second when a person is allowed in. When a person is not allowed in/ a new guest it will flash red for a second. Another modification I added was with the email function. I changed it so when a specific person is at the door it will also send an email. Before, it only sent an email when the person was unknown, now it sends when they are unknown and when a person you want to id at your door. I also attatched all components onto a piece of acrylic so it can easily be moved. 

[![Final Milestone](https://img.youtube.com/vi/LYExreLvghs/hqdefault.jpg )](https://www.youtube.com/watch?v=LYExreLvghs "Final Milestone")

# Second Milestone
My second milestone is fully finishing the lock. Now it is a fully functional lock with a few add-ons. I connected the Arduino and the Rasperry Pi with serial connection and downloaded IDE on the Rasperry Pi. I also finished writing all my code, it now sends an email with a picture when an unrecognized guest is at the door. When the lock opens it opens for five seconds then locks again. Using my guest search function, it can identify who is at the door by pulling the RekognitionID from my AWS bucket. I also connected a red and green LED, when the door is opened by a recognized guest the green light will flash, when a guest is locked out it will flash red then send me an email.

[![Second Milestone](https://img.youtube.com/vi/f14yofIJps4/hqdefault.jpg)](https://www.youtube.com/watch?v=f14yofIJps4 "Second Milestone")
# First Milestone
  

My first milestone is setting up the hardware. This consists of the Raspberry Pi, Arduino, and the lock that contains the servo. I uploaded code to the arduino connected it to the servo and got it to open and close. Some places I struggled in was setting up my Rasperry Pi with AWS. Configuring the image bucket and the guest collection table was tricky. It took a while to set up all the different locations. Building the 3-d printed lock went smoothly and connecting that to the arduino was also easily accomplished.   

[![First Milestone](https://img.youtube.com/vi/C8MUmDBtJec/sddefault.jpg)](https://www.youtube.com/watch?v=C8MUmDBtJec "First Milestone")


# Starter Project
My Starter Project was the Useless Machine. When the switch is hit the arm will come up and hit it back then rotate down again. The board consists of two switches, an LED, two resistors, and a terminal that connects to the wires of the motor and battery pack. The motor is under the board and has the arm attatched to it. The battery pack has 3 AA batteries. All three parts fit inside the plastic box where only the switch pokes out and the door opens and closes.

[![Starter Project](https://img.youtube.com/vi/2e7--Mj_rL8/sddefault.jpg)](https://www.youtube.com/watch?v=2e7--Mj_rL8)

#  Diagrams
![arduino circuit](https://user-images.githubusercontent.com/107944844/176942366-9e5cb216-ffaf-4a28-8fcd-653d68950203.jpg)
![schematics](https://hackster.imgix.net/uploads/attachments/437788/block1_ioWGCtJDGN.jpg)
