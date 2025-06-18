# Python-CRUD-Application-for-Hospital

## Hospital Patient Management System
A command-line application for managing hospital patient records with create, read, update, and delete (CRUD) functionality and statistical reporting.

### Target Users
This application is designed for hospital administrators, nurses, and medical staff within healthcare organizations to facilitate their daily tasks related to patient data management.

## Features
### Patient Management
- **Create**: Add new patient records with validation
- **Read**: Search by:
  - Patient ID
  - Name (partial match supported)
  - Department/Poli
- **Update**: Modify any patient field
- **Delete**: Secure record removal (admin-only)

### Statistics Module
- Age, weight, and height distribution (min/max/avg)
- Diagnosis frequency reports

### Security
- Admin authentication system
- Attempt limits (5 tries)

### Input Validation
- Patient ID must be unique
- Age, weight, height must be numeric
- Gender must be "male" or "female"
- Menu selection is restricted to valid choices

## How to Run
- Make sure Python 3 is installed
- Save the Python file
- Run the application using terminal pr command prompt

## Data Structure
```python
{
    'ID Pasien': 'PE1',           # Unique ID
    'Nama': 'Jane Doe',           # Patient name
    'Usia': 35,                   # Age
    'Jenis Kelamin': 'L',         # Gender (L/P)
    'Domisili': 'Jakarta',        # Address
    'Berat Badan': 70,            # Weight (kg)
    'Tinggi Badan': 175,          # Height (cm)
    'Poli': 'Cardiology',         # Department
    'Diagnosis': 'Hypertension',  # Medical condition
    'Tindak Lanjut': 'Routine'    # Treatment plan
}
