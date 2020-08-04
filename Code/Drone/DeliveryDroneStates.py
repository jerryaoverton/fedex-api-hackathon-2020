from DeliveryDroneStateMachine import DroneState


class Idle(DroneState):
    @staticmethod
    def run(context):
        print("drone is idle")

    @staticmethod
    def next_state(context):
        if context['total_jobs'] >= context['max_total_jobs']:
            return Retired()
        else:
            return Working()


class Working(DroneState):
    @staticmethod
    def run(context):
        print("drone is working")
        context['jobs_since_maintenance'] += 1
        context['total_jobs'] += 1

    @staticmethod
    def next_state(context):
        if context['jobs_since_maintenance'] < context['max_consecutive_jobs']:
            return Working()
        else:
            return GettingMaintenance()


class GettingMaintenance(DroneState):
    @staticmethod
    def run(context):
        print("drone is getting maintenance")
        context['jobs_since_maintenance'] = 0

    @staticmethod
    def next_state(context):
        return PayingForMaintenance()


class PayingForMaintenance(DroneState):
    @staticmethod
    def run(context):
        print("drone is paying for maintenance")

    @staticmethod
    def next_state(context):
        return Idle()


class Retired(DroneState):
    @staticmethod
    def run(context):
        print("drone is retired")
