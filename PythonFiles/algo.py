import sys
import pandas as pd
from PyQt5 import QtWidgets, uic, QtGui

class Patient:
    patient_data = []
    id_counter = 0

    def __init__(self, sex, age, disease):
        self.sex = sex
        self.age = age
        self.disease = disease
        self.id = Patient.id_counter
        Patient.id_counter += 1

    def __repr__(self):
        return f"PatientID={self.id}, sex={self.sex}, age={self.age}, disease={self.disease}"

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI/Gui.ui', self)
        self.setWindowTitle("Clinical Trials")
        self.addPatientButton.clicked.connect(self.add_patient)
        self.selectPatientButton.clicked.connect(self.select_patient)
        self.actionFile.triggered.connect(self.load_csv)
        for Box in (self.comboBox, self.comboBox_4):
            Box.addItem('Male')
            Box.addItem('Female')
        self.comboBox_4.addItem('both')
        diseases = ['Diabetes', 'Hypertension', 'Asthma', 'Cancer', 'Heart Disease', 'Arthritis']
        for disease in diseases:
            self.comboBox_3.addItem(disease)
            self.comboBox_6.addItem(disease)

    def add_patient(self):
        sex = self.comboBox.currentText()
        if self.lineEdit.text() :
            if self.lineEdit.text()=='0':
                QtWidgets.QMessageBox.information(self, 'Failed', 'Please write correct patient age.')
                return
            age = int(self.lineEdit.text())
        else:
            QtWidgets.QMessageBox.information(self, 'Failed', 'Please write the patient age.')
            return
        disease = self.comboBox_3.currentText()
        new_patient = Patient(sex, age, disease)
        Patient.patient_data.append(new_patient)
        QtWidgets.QMessageBox.information(self, 'Success', 'Patient has been successfully added to the database.')

    def select_patient(self):
        sex = self.comboBox_4.currentText()
        age_range = self.lineEdit_2.text()
        if '-' in age_range:
            age_min, age_max = map(int, age_range.split('-'))
        else:
            age_min = None
            age_max = None
            QtWidgets.QMessageBox.information(self, 'Failed', 'Please write the patients age in correct form i.e 18-40.')
            return
        disease = self.comboBox_6.currentText()
        filtered_patients = self.divide_and_conquer_search(Patient.patient_data, sex, age_min, age_max, disease)
        if not filtered_patients:
            QtWidgets.QMessageBox.information(self, 'No Results', 'No patients found with the specified criteria.')
        else:
            results = "\n\n".join(str(patient) for patient in filtered_patients)
            self.show_results(results)

    def show_results(self, results):
        msg_box = QtWidgets.QMessageBox(self)
        icon_path = 'Assets/images/patient.png'
        icon_pixmap = QtGui.QPixmap(icon_path)
        msg_box.setIconPixmap(icon_pixmap)
        msg_box.setWindowTitle('Results')
        msg_box.setText(f'Patients found:\n{results}')
        msg_box.setStyleSheet('''
            QMessageBox {
                color: #333;
                font: bold 14px;
            }
            QMessageBox QLabel {
                margin-bottom: 20px;
            }
            QMessageBox QPushButton {
                background-color: #007BFF;
                color: #fff;
                border-radius: 4px;
                padding: 5px 15px;
                font: bold 12px;
            }
            QMessageBox QPushButton:hover {
                background-color: #0056b3;
            }
        ''')
        msg_box.exec_()

    def load_csv(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Load CSV file', '', 'CSV Files (*.csv)', options=options)
        if file_path:
            df = pd.read_csv(file_path)
            for index, row in df.iterrows():
                sex = row.get('sex')
                age = row.get('age')
                disease = row.get('disease')
                new_patient = Patient(sex, age, disease)
                Patient.patient_data.append(new_patient)
            QtWidgets.QMessageBox.information(self, 'Success', 'CSV file loaded successfully.')

    def divide_and_conquer_search(self, patient_list, sex, age_min, age_max, disease):
        if not patient_list:
            return []
        mid = len(patient_list) // 2
        patient = patient_list[mid]
        filtered_patients = []
        if (
            (sex == 'both' or patient.sex == sex) and
            (age_min is None or age_min <= patient.age <= age_max) and
            (disease == '' or patient.disease == disease)
        ):
            filtered_patients.append(patient)
        left_half = patient_list[:mid]
        right_half = patient_list[mid + 1:]
        filtered_patients += self.divide_and_conquer_search(left_half, sex, age_min, age_max, disease)
        filtered_patients += self.divide_and_conquer_search(right_half, sex, age_min, age_max, disease)
        return filtered_patients
