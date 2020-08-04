from DeliveryDroneStateMachine import DroneStateMachine
from DeliveryDroneStates import Idle


class DeliveryDrone(DroneStateMachine):
    def __init__(self, initial_state):
        super().__init__(initial_state)
        self.set_context('max_total_jobs', 10)
        self.set_context('max_consecutive_jobs', 3)
        self.set_context('total_jobs', 0)
        self.set_context('jobs_since_maintenance', 0)


drone = DeliveryDrone(Idle)
drone.run()
