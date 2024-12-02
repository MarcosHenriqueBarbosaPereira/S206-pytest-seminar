class Patient:

    def __init__(self, name):
        self.name = name
        self.consulting = False

    def start_consulting(self):
        if self.consulting:
            raise ValueError("The patient is already consulting a doctor.")
        self.consulting = True

    def stop_consulting(self):
        if not self.consulting:
            raise ValueError("The patient is not consulting a doctor.")
        self.consulting = False
