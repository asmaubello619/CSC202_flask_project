from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from models import Patient, ClinicQueue

app = Flask(__name__)
clinic_queue = ClinicQueue()

CLINIC_NAME = "Sunrise Health Clinic"  # Clinic name

@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        staff_name = request.form['staff_name']
        return redirect(url_for('dashboard', staff_name=staff_name))
    return render_template('welcome.html', clinic_name=CLINIC_NAME)

@app.route('/dashboard/<staff_name>', methods=['GET', 'POST'])
def dashboard(staff_name):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        age_unit = request.form['age_unit']
        timestamp = datetime.now().strftime("%H:%M %p")
        patient = Patient(name, age, age_unit, timestamp)
        clinic_queue.add_patient(patient)
        return redirect(url_for('dashboard', staff_name=staff_name))

    waiting = clinic_queue.get_waiting_patients()
    served = clinic_queue.get_served_patients()
    return render_template('dashboard.html',
                           staff_name=staff_name,
                           patients=waiting,
                           served=served,
                           clinic_name=CLINIC_NAME)

@app.route('/next/<staff_name>')
def next_patient(staff_name):
    clinic_queue.next_patient()
    return redirect(url_for('dashboard', staff_name=staff_name))

@app.route('/logout')
def logout():
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)