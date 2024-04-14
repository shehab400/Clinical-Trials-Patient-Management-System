import pandas as pd
import numpy as np
import os

def generate_patient_csv(file_path):
    # Define the list of possible values for each attribute
    sex_options = ['Male', 'Female']
    diseases = ['Diabetes', 'Hypertension', 'Asthma', 'Cancer', 'Heart Disease', 'Arthritis']
    ages = list(range(18, 90))  # Patient ages from 18 to 89

    

    # Create a dictionary of sample patient data
    data = {
        'sex': [],
        'age': [],
        'disease': [],

    }

    # Generate sample data for a number of patients
    num_patients = 100  # Adjust this value to control the number of patients in the CSV file
    for _ in range(num_patients):
        # Select random values for each attribute
        sex = np.random.choice(sex_options)
        age = np.random.choice(ages)
        disease = np.random.choice(diseases)
        

        # Append the values to the data dictionary
        data['sex'].append(sex)
        data['age'].append(age)
        data['disease'].append(disease)
        

    # Create a DataFrame from the data dictionary
    df = pd.DataFrame(data)

    # Check if the directory exists; if not, create it
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    print(f'CSV file saved to {file_path}')

# Define the file path to save the CSV file
file_path = 'Assets/patients.csv'  # Use a full path to specify where to save the file

# Call the function to generate the CSV file
generate_patient_csv(file_path)
