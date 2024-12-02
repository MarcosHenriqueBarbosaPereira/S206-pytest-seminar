import pytest

from s206_seminar.src.hospital_app.patient import Patient
from s206_seminar.src.hospital_app.doctor import Doctor


class TestHospitalApp:

    def setup_method(self, _):
        self.patient1 = Patient("Alice")
        self.patient2 = Patient("Luke")
        self.doctor1 = Doctor("Bob")
        self.doctor2 = Doctor("Eve")

    def test_start_consulting_success(self):
        self.doctor1.start_working()
        self.doctor1.add_patient(self.patient1)
        self.doctor1.start_consulting(self.patient1)

        assert self.patient1.consulting == True
        assert self.doctor1.consulting == True
        assert self.doctor1.current_patient == self.patient1

    def test_start_consulting_doctor_not_working(self):
        self.doctor1.add_patient(self.patient1)
        with pytest.raises(ValueError) as excinfo:
            self.doctor1.start_consulting(self.patient1)
        assert str(excinfo.value) == "The doctor is not working."

    def test_start_consulting_doctor_already_consulting(self):
        self.doctor1.start_working()
        self.doctor1.add_patient(self.patient1)
        self.doctor1.add_patient(self.patient2)
        self.doctor1.start_consulting(self.patient1)
        with pytest.raises(ValueError) as excinfo:
            self.doctor1.start_consulting(self.patient2)
        assert str(excinfo.value) == "The doctor is already consulting a patient."

    def test_start_consulting_patient_already_consulting(self):
        self.doctor1.start_working()
        self.doctor1.add_patient(self.patient1)
        self.doctor2.start_working()
        self.doctor2.add_patient(self.patient1)
        self.doctor1.start_consulting(self.patient1)
        with pytest.raises(ValueError) as excinfo:
            self.doctor2.start_consulting(self.patient1)
        assert str(excinfo.value) == "The patient is already consulting a doctor."

    def test_start_consulting_patient_not_in_doctor_list(self):
        self.doctor1.start_working()
        with pytest.raises(ValueError) as excinfo:
            self.doctor1.start_consulting(self.patient1)
        assert str(excinfo.value) == "The patient is not in the doctor's list of patients."

    def test_stop_consulting_success(self):
        self.doctor1.start_working()
        self.doctor1.add_patient(self.patient1)
        self.doctor1.start_consulting(self.patient1)
        self.doctor1.stop_consulting()

        assert self.patient1.consulting == False
        assert self.doctor1.consulting == False
        assert self.doctor1.current_patient == None

    def test_stop_consulting_doctor_not_consulting(self):
        self.doctor1.start_working()
        self.doctor1.add_patient(self.patient1)
        with pytest.raises(ValueError) as excinfo:
            self.doctor1.stop_consulting()
        assert str(excinfo.value) == "The doctor is not consulting a patient."

    def test_stop_consulting_patient_not_consulting(self):
        self.doctor1.start_working()
        self.doctor1.add_patient(self.patient1)
        self.doctor1.start_consulting(self.patient1)
        self.patient1.stop_consulting()
        with pytest.raises(ValueError) as excinfo:
            self.doctor1.stop_consulting()
        assert str(excinfo.value) == "The patient is not consulting a doctor."

    def test_start_and_stop_working(self):
        self.doctor1.start_working()
        assert self.doctor1.working == True
        self.doctor1.stop_working()
        assert self.doctor1.working == False
    