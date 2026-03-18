class Patient:
    def __init__(self, name, age, age_unit, timestamp):
        self.name = name
        self.age = age
        self.age_unit = age_unit
        self.timestamp = timestamp
        self.status = "Waiting"

    def get_details(self):
        return f"{self.name} - {self.age} {self.age_unit} - Registered at: {self.timestamp}"

class ClinicQueue:
    def __init__(self):
        self.waiting_patients = []
        self.served_patients = []

    def add_patient(self, patient):
        self.waiting_patients.append(patient)

    def next_patient(self):
        if self.waiting_patients:
            patient = self.waiting_patients.pop(0)
            patient.status = "Served"
            self.served_patients.append(patient)
            return patient
        return None

    def get_waiting_patients(self):
        return self.waiting_patients

    def get_served_patients(self):
        return self.served_patients