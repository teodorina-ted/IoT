import tkinter as tk
import paho.mqtt.client as mqtt

# --- QUESITO 4: EXCHANGE SYSTEM ---
# MQTT allows us to add a smartphone later without changing this code.
BROKER = "localhost" 
TOPIC_TEMP = "chamber/temperature"
TOPIC_ALARM = "chamber/alarms"

# --- QUESITO 3: REMOTE CONTROL SYSTEM LOGIC ---
def remote_logic(temp_value):
    # Mutually exclusive logic based on requirements 
    if 0 <= temp_value <= 10:
        return "L1" # 0-10 L1 Range 
    elif 10 < temp_value <= 20:
        return "L2" # 10-20 Range 
    elif temp_value > 20:
        return "L3" # Oltre 30: Range 20 to 50 as i understand
    return "OFF"

# --- QUESITO 1: GUI IMPLEMENTATION ---
class ClimateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Climate Chamber - Teodorina Lungu")

        # 1.1 Slider 
        tk.Label(root, text="Temperature Slider (Simulated)").pack()
        self.slider = tk.Scale(root, from_=0, to=50, orient='horizontal', length=300, command=self.update)
        self.slider.pack(pady=10)

        # 1.2 Visualizers L1, L2, L3 
        self.l1 = tk.Label(root, text="L1", bg="grey", width=15)
        self.l2 = tk.Label(root, text="L2", bg="grey", width=15)
        self.l3 = tk.Label(root, text="L3", bg="grey", width=15)
        self.l1.pack(); self.l2.pack(); self.l3.pack()

        # MQTT Setup
        self.client = mqtt.Client()
        self.client.connect(BROKER, 1883)
        self.client.loop_start()

    def update(self, val):
        temp = float(val)
        alarm = remote_logic(temp)
        
        # Update GUI colors
        self.l1.config(bg="green" if alarm == "L1" else "grey")
        self.l2.config(bg="yellow" if alarm == "L2" else "grey")
        self.l3.config(bg="red" if alarm == "L3" else "grey")
        
        # Send data to broker (Quesito 4)
        self.client.publish(TOPIC_TEMP, temp)

# QUESITO 2: DBMS Suggestion 
# Type: InfluxDB (Time-series)
# Structure: { "time": timestamp, "temp": value, "alarm": status }

if __name__ == "__main__":
    root = tk.Tk()
    app = ClimateApp(root)
    root.mainloop()