import numpy as np
import requests
import json

class User:
    def __init__(self, user_id, traffic_type):
        self.user_id = user_id
        self.traffic_type = traffic_type
        self.data_rate = 0
        self.buffer = 0

    def generate_traffic(self):
        if (self.traffic_type.lower() == "video"):
            self.data_rate = np.random.uniform(2,5)
        elif (self.traffic_type.lower() == "browsing"):
            self.data_rate = np.random.exponential(1.5)
        elif (self.traffic_type.lower() == "chat"):
            self.data_rate = np.random.uniform(0.05, 0.2)
        elif (self.traffic_type.lower() == "gaming"):
            self.data_rate = np.random.uniform(0.1, 0.3)
        self.buffer += self.data_rate
        return self.data_rate
    
    def calculate_prb_demand(self, prb_capacity=1.0):
        return int(np.ceil(self.data_rate / prb_capacity))
    
class BaseStation:
    def __init__(self, total_prbs):
        self.total_prbs = total_prbs
        
    def schedule(self, users, prb_capacity = 1.0):
        allocations = {}
        remaining_prbs = self.total_prbs
        for u in users:
            demand = u.calculate_prb_demand(prb_capacity)
            allocated = min(demand, remaining_prbs)

            # Serve buffer
            served_data = allocated * prb_capacity
            u.buffer = max(0, u.buffer - served_data)
            allocations[u.user_id] = {
                    "demand_prbs": demand,
                    "allocated_prbs": allocated,
                    "remaining_buffer": round(u.buffer,2)
                }

            remaining_prbs -= allocated
            if remaining_prbs <= 0:
                break

        return allocations

users = []
types = ["video","browsing","chat","gaming"]

for i in range(1, 101):
    users.append(User(i, np.random.choice(types)))

bs = BaseStation(total_prbs = 50)

for t in range(1000):
    for u in users:
        u.generate_traffic()
    
    allocation = bs.schedule(users)

#json_output = json.dumps(allocation)
requests.post("http://localhost:8080/json_output", json={"allocations": allocation})