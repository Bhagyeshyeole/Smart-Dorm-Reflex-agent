"""
Dorm Room Smart Controller

made this to manage and track the environment with simple reflex AI agents for dorm room control.
It reacts to occupancy,temperature,and time of day.

Basically itsacts as digital thermostat + lights system .

"""

import random
import time
import argparse
import sys

# Ideal values for comfort.can be adjusted.
COMFORT_TEMP_LOW = 18
COMFORT_TEMP_HIGH = 28
NIGHT_START_HOUR = 19
NIGHT_END_HOUR = 6

# Simple status thing .
OFF = "OFF"
ON = "ON"

class Room:
    """Keeps track of what's going on in the dorm room"""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Back to initial conditions"""
        self.temperature = 22
        self.someone_home = False
        self.current_hour = 14
        self.lights_on = OFF
        self.ac_running = OFF
        self.heater_on = OFF
    
    def update_weather(self):
        """Randomly change conditions"""
        self.temperature = random.randint(15, 35)
        self.someone_home = random.choice([True, False])
        self.current_hour = (self.current_hour + 1) % 24

class Controller:
    """This makes decisions"""
    
    def __init__(self):
        self.room = Room()
        self.steps_taken = 0
        
        # Pre-calculate night times.
        self.night_times = []
        for h in range(NIGHT_START_HOUR, 24):
            self.night_times.append(h)
        for h in range(0, NIGHT_END_HOUR + 1):
            self.night_times.append(h)
    
    def should_lights_be_on(self):
        """Check if it is dark outside"""
        return ON if self.room.current_hour in self.night_times else OFF
    
    def check_temperature(self):
        """Decide AC, heat or nothing"""
        temp = self.room.temperature
        
        if temp > COMFORT_TEMP_HIGH:
            return ON, OFF    # AC time
        elif temp < COMFORT_TEMP_LOW:
            return OFF, ON    # Brrr, heat
        else:
            return OFF, OFF   # Just right
    
    def do_one_cycle(self):
        """One full cycle"""
        self.steps_taken += 1
        
        print("\n" + "="*55)
        print(f"Step {self.steps_taken:2d}  |  "
              f"{self.room.current_hour:02d}:00  |  "
              f"{self.room.temperature}°C  |  "
              f"{'👤 Home' if self.room.someone_home else 'Empty'}")
        
        self.room.update_weather()
        
        if not self.room.someone_home:
            # Save electricity when appliance is not in use.
            self.room.lights_on = OFF
            self.room.ac_running = OFF
            self.room.heater_on = OFF
            print("   → Empty room: everything OFF")
            return
        
        lights = self.should_lights_be_on()
        ac_status, heat_status = self.check_temperature()
        
        self.room.lights_on = lights
        self.room.ac_running = ac_status
        self.room.heater_on = heat_status
        
        # what we have decided.
        if lights == ON:
            print("   → Dark outside: lights ON")
        else:
            print("   → Plenty of daylight: lights OFF")
        
        if ac_status == ON:
            print("   → Too hot: AC kicked on")
        elif heat_status == ON:
            print("   → Freezing: heater started")
        else:
            print("   → Nice temperature: climate OFF")
    
    def simulate(self, cycles=5, speed=1.0):
        """Run the whole show"""
        print(""" Dorm Smart Controller
          Sensors: motion detector, thermometer, clock
        Actuators: lights, AC unit, space heater """)
        print("-" * 55)
        
        for i in range(cycles):
            self.do_one_cycle()
            
            if i < cycles - 1:
                time.sleep(max(0.1, 1.0 / speed))
        
        print("\n All done!")

def handle_arguments():
    """follows what the user wants to do"""
    parser = argparse.ArgumentParser(description="Dorm room controller")
    
    parser.add_argument('-c', '--cycles', type=int, default=5,
                        help='How many simulation cycles (default: 5)')
    parser.add_argument('-s', '--speed', type=float, default=1.0,
                        help='Speed multiplier (2.0 = twice as fast)')
    
    return parser.parse_args()

# Main 
def main():
    try:
        options = handle_arguments()
        brain = Controller()
        brain.simulate(options.cycles, options.speed)
    except KeyboardInterrupt:
        print("\n\nStopped by user. Have a good day!")
        sys.exit(0)

if __name__ == "__main__":
    main()