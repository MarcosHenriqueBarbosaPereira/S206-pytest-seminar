from s206_seminar.src.hospital_app.patient import Patient


class Doctor:

    def __init__(self, name):
        self.name = name
        self.working = False
        self.consulting = False
        self.current_patient = None
        self.patients = []

    def start_working(self):
        if self.working:
            raise ValueError("The doctor is already working.")
        self.working = True

    def stop_working(self):
        if not self.working:
            raise ValueError("The doctor is not working.")
        self.working = False

    def start_consulting(self, patient: Patient):
        if not self.working:
            raise ValueError("The doctor is not working.")
        elif self.consulting:
            raise ValueError("The doctor is already consulting a patient.")
        elif patient.consulting:
            raise ValueError("The patient is already consulting a doctor.")
        elif patient not in self.patients:
            raise ValueError("The patient is not in the doctor's list of patients.")

        self.consulting = True
        self.current_patient = patient
        patient.start_consulting()

    def stop_consulting(self):
        if not self.consulting:
            raise ValueError("The doctor is not consulting a patient.")
        self.consulting = False
        self.current_patient.stop_consulting()
        self.current_patient = None

    def add_patient(self, patient: Patient):
        if patient in self.patients:
            raise ValueError("The patient is already in the doctor's list of patients.")
        self.patients.append(patient)
