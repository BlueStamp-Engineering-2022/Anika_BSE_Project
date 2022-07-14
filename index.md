# Face Recognition Door Lock
The Face Recognition Door Lock uses the faces of saved images stored in AWS to open a door lock. It can also greet guests, tell you who is at the door, save multiple guests and more. It sends an email with a live picture captured when an unrecognized guest is at the door. Using Rasperry Pi, Arduino, a servo, Python, IDE, and AWS this door lock is fully functional.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Anika Karvat | Saratoga High School |  | Incoming Sophomore

![Headstone Image](https://lh3.googleusercontent.com/pw/AM-JKLUdOuU9Q6jJW24ISIrUQ86stBQrCDxvoC6gCmYYJBYLRuTZ0KuYGIkEr4aPZzd6wEQgvUS3nlK2IZbWJMW13zeNAtBtXtwrCLN6D4wDYT2vPBLwp_yU01ss2ku1Mu6appCKLMp1psU20Tl-z7ugj-Xs=s1290-no?authuser=0)
  
# Final Milestone
My final milestone is the increased reliability and accuracy of my robot. I ameliorated the sagging and fixed the reliability of the finger. As discussed in my second milestone, the arm sags because of weight. I put in a block of wood at the base to hold up the upper arm; this has reverberating positive effects throughout the arm. I also realized that the forearm was getting disconnected from the elbow servo’s horn because of the weight stress on the joint. Now, I make sure to constantly tighten the screws at that joint. 

[![Final Milestone](https://res.cloudinary.com/marcomontalbano/image/upload/v1612573869/video_to_markdown/images/youtube--F7M7imOVGug-c05b58ac6eb4c4700831b2b3070cd403.jpg )](https://www.youtube.com/watch?v=F7M7imOVGug&feature=emb_logo "Final Milestone")

# Second Milestone
My second milestone is finishing the base of the lock. Now it is a fully functional lock with just the basics. I connection the Arduino with the Rasperry Pi with serial connection and downloaded IDE on the Rasperry Pi. I also finished all my code for the function. It now sends an email with a picture when an unrecognized guest is at the door. When the lock opens it opens for five seconds then locks again. Using my guest search function, it can identify who is at the door by pulling the RekognitionID from my AWS bucket.

[![Second Milestone](https://img.youtube.com/vi/f14yofIJps4/hqdefault.jpg)](https://www.youtube.com/watch?v=f14yofIJps4 "Second Milestone")
# First Milestone
  

My first milestone is setting up the hardware. This consists of the Raspberry Pi, Arduino, and the lock that contains the servo. I uploaded code to the arduino connected it to the servo and got it to open and close. Some places I struggled in was setting up my Rasperry Pi with AWS. Configuring the image bucket and the guest collection table was tricky. It took a while to set up all the different locations. Building the 3-d printed lock went smoothly and connecting that to the arduino was also easily accomplished.   

[![First Milestone](https://img.youtube.com/vi/C8MUmDBtJec/sddefault.jpg)](https://www.youtube.com/watch?v=C8MUmDBtJec "First Milestone")


# Starter Project
My Starter Project was the Useless Machine. When the switch is hit the arm will come up and hit it back then rotate down again. The board consists of two switches, an LED, two resistors, and a terminal that connects to the wires of the motor and battery pack. The motor is under the board and has the arm attatched to it. The battery pack has 3 AA batteries. All three parts fit inside the plastic box where only the switch pokes out and the door opens and closes.

[![Starter Project](https://img.youtube.com/vi/2e7--Mj_rL8/sddefault.jpg)](https://www.youtube.com/watch?v=2e7--Mj_rL8)

# Circuit Diagrams
![arduino circuit](https://user-images.githubusercontent.com/107944844/176942366-9e5cb216-ffaf-4a28-8fcd-653d68950203.jpg)
