Smart Dorm Project : Simple Reflex Agent.
Course: CSA2001 — Fundamentals of AI and ML

Submitted By : Bhagyesh Amol Yeole 
Btech CSE - AIML (2025-29)
VIT Bhopal University

What is this Smart dorm reflex agent ?
This is a simple reflex agent that is built to tackle a common issue: energy waste in university dorms/hostels. This system basically automates the room lighting and temperature control using sensor data. The goal is to keep the room comfortable for students while cutting down the wasted electricity.

AI Concepts Used: 
This project applies a few core AI fundamentals concepts: 

  1.The PEAS Framework

Performance Measure: Saving energy and maintaining student comfort.
Environment: The dorm room (tracking temperature, time,and occupancy).
Actuators: Light switch, AC unit, and heater,etc.
Sensors: Motion detector, thermometer, an internal clock.

 2.Agent architecture.
It operates as a Simple Reflex Agent. It doesn't have any memory or keep track of past states; it just processes the current environment and reacts instantly using condition-action rules.

How it Works?
Smart Lighting: Lights only trigger if someone is actually present in the room AND it's dark out (between 19:00 and 06:00).
Climate Control: The AC turns on if the room gets hotter than 28°C. The heater turns on if it drops below 18°C.
Auto-Shutoff: If the motion sensor detects the room is empty, it cutoffs the power to all systems immediately, ignoring other rules.

Running the Simulation
You just need Python to run this program:

Bash
git clone: https://github.com/Bhagyeshyeole/Smart-Dorm-Reflex-agent.git
cd smart-dorm-reflex-agent
python main.py

Sample Output

  Environment Change: Time: 21:00, Temp: 32°C, Occupied: True
  [AGENT ACTION]: It's dark: Lights turned ON.
  [AGENT ACTION]: Too hot: AC turned ON.

  Environment Change: Time: 22:00, Temp: 20°C, Occupied: False
  [AGENT ACTION]: Dorm Empty: All systems powered down.