Below is a **professional GitHub README.md** you can use directly for your repository after completing the HMS lab using **Odoo 19**.

---

# 🏥 HMS – Hospital Management System (Odoo 19)

## 📌 Overview

**HMS (Hospital Management System)** is a custom Odoo 19 module developed as part of the OSD labs.
The module manages patients, departments, and doctors with business rules, access control, and automated behaviors following real-world hospital workflows.

---

## 🚀 Features

### 👤 Patient Management

* Create and manage patient records
* Patient information includes:

  * First Name *(required)*
  * Last Name *(required)*
  * Birth Date
  * Age *(computed)*
  * Address
  * Email *(validated & unique)*
  * History *(HTML field – conditionally visible)*
  * CR Ratio *(float)*
  * Blood Type *(selection)*
  * PCR *(boolean)*
  * Image *(upload)*

---

### 🏥 Department Management

* Create and manage hospital departments
* Department fields:

  * Name
  * Capacity *(integer)*
  * Is Opened *(boolean)*
  * Patients *(one2many)*
* Closed departments cannot be selected by patients

---

### 👨‍⚕️ Doctor Management

* Create and manage doctors
* Doctor fields:

  * First Name
  * Last Name
  * Image
* Patients can be linked to multiple doctors *(many2many tags)*

---

## 🔗 Relationships

* Patients are linked to:

  * One Department
  * Multiple Doctors
* Selected department capacity is displayed on the patient form
* Doctors field remains **readonly** until a department is selected

---

## 📝 Patient Log History

* Automatic log creation for patient state changes
* Log record includes:

  * Created By
  * Date
  * Description
* Patient states:

  * Undetermined
  * Good
  * Fair
  * Serious
* Each state change creates a log entry:

  ```
  State changed to NEW_STATE
  ```

---

## ⚙️ Business Rules & Validations

* First name and last name are mandatory
* Email must be **valid and unique**
* If **PCR is checked**, **CR Ratio becomes mandatory**
* History field is hidden if patient age is **less than 50**
* PCR is automatically checked if age is **below 30**

  * A warning message is shown to the user
* Patients cannot be assigned to closed departments

---

## 🔐 Security & Access Rights

### 👥 User Groups

Two custom security groups are implemented:

#### 👤 HMS User

* Create / Read / Update **own** patient records
* Read-only access to:

  * Departments
  * Doctors
* Cannot:

  * View doctors field in patient form
  * Access doctors menu

#### 👨‍💼 HMS Manager

* Full access *(CRUD)* to:

  * Patients
  * Departments
  * Doctors
* Can:

  * View doctors field in patient form
  * Access doctors menu

---

## 📂 Module Structure

```
hms/
├── models/
│   ├── patient.py
│   ├── department.py
│   └── doctor.py
├── views/
│   ├── patient_views.xml
│   ├── department_views.xml
│   └── doctor_views.xml
├── security/
│   ├── ir.model.access.csv
│   └── hms_groups.xml
├── data/
│   └── sequences.xml
├── __init__.py
└── __manifest__.py
```

---

## 🛠️ Requirements

* Odoo **19**
* Python 3.x
* PostgreSQL

---

## ▶️ Installation

1. Clone the repository into your custom addons directory:

   ```bash
   git clone https://github.com/your-username/hms.git
   ```
2. Restart the Odoo server
3. Activate **Developer Mode**
4. Install the **HMS** module from Apps

---

## 📄 License

This project is developed for educational purposes as part of ITI Open Source labs.

---
