

# Clinical Trials Patient Management System

This project is a Clinical Trials Patient Management System that allows you to manage patient data efficiently. It uses PyQt5 for the GUI and Pandas for handling CSV data. The system enables you to add new patients, search for patients based on certain criteria, and load patient data from a CSV file.

## Features

- Add new patients to the database.
- Search for patients based on criteria such as sex, age range, and disease.
- Load patient data from a CSV file.
- Display search results in a styled message box.
- Customizable GUI and application icon.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or later
- PyQt5
- Pandas

You can install the required Python packages using pip:

```bash
pip install pyqt5 pandas
```

## Getting Started

To run the project, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/clinical-trials.git
    ```

2. Navigate to the project directory:

    ```bash
    cd clinical-trials
    ```

3. Ensure that the `GUI` directory contains the `Gui.ui` file and `Assets` contains the necessary images, such as `patient.png`.

4. Run the main script:

    ```bash
    python main.py
    ```

The application window will open, allowing you to add and search for patients.

## Usage

- **Add Patient**: Use the provided fields in the GUI to enter a new patient's sex, age, and disease. Click the "Add Patient" button to add the patient to the database.
  
- **Search for Patients**: Use the filters in the GUI to specify criteria such as sex, age range, and disease. Click the "Search Patient" button to search for patients matching the criteria. The results will be displayed in a styled message box.
  
- **Load CSV File**: To load patient data from a CSV file, go to `File > Load CSV` and select the CSV file to import.

## Customization

- You can customize the GUI by modifying the `.ui` file in the `GUI` directory.
  
- Update the `Assets/images/patient.png` path to point to the desired icon image for the application.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or pull request.

## Acknowledgments

- The project uses PyQt5 for the GUI and Pandas for data handling.
- Thank you to all open-source contributors and maintainers.

---

Replace the GitHub repository URL in the "Clone this repository" section with the URL of your own GitHub repository. You may also want to add additional sections such as "Acknowledgments," "License," and "Contributing" depending on the nature of your project and community guidelines. Let me know if there's anything else I can help you with!
