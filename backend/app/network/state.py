import time

class NetworkState:
    def __init__(self):
        self.state = {}
    
    def update(self, demands: dict, allocation: dict) -> dict:
        self.state = {
            "timestamp": time.time(),
            "users": {
                user: {
                    "demand": demands[user],
                    "allocated": allocation[user]
                }
                for user in demands
            }
        }   
        return self.state