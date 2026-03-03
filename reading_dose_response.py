import pickle
import os
import numpy as np

# Read the pickle file
file_path = "data/data/nci_synergy_dose_response.pickle"

# Check if file exists
if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
    print(f"Current working directory: {os.getcwd()}")
    exit(1)

# Load the pickle file
with open(file_path, 'rb') as handle:
    dose_response_data = pickle.load(handle)

# Print the type and basic info
print(f"Type of loaded data: {type(dose_response_data)}")
print(f"Number of entries: {len(dose_response_data)}")
print("\n" + "="*80)

# Get the columns (keys in the nested dictionary)
# Check the first entry to see its structure
if len(dose_response_data) > 0:
    first_key = list(dose_response_data.keys())[0]
    print(f"First key: {first_key}")
    first_value = dose_response_data[first_key]
    
    print(f"\nColumns (keys in nested dictionary):")
    if isinstance(first_value, dict):
        for col in first_value.keys():
            print(f"  - {col}")
    else:
        print(f"  Value type: {type(first_value)}")
    
    print("\n" + "="*80)
    print("\nFirst 2 entries with full matrix and dose arrays:\n")
    
    # Print first 2 entries with full details
    for i, (key, value) in enumerate(list(dose_response_data.items())[:2]):
        print(f"Entry {i+1}:")
        print(f"  Key: {key}")
        if isinstance(value, dict):
            # Print matrix
            if 'matrix' in value:
                matrix = value['matrix']
                print(f"  matrix (shape {matrix.shape}):")
                print(f"    {matrix}")
            
            # Print x1_dose
            if 'x1_dose' in value:
                x1_dose = value['x1_dose']
                print(f"  x1_dose (shape {x1_dose.shape}):")
                print(f"    {x1_dose}")
            
            # Print x2_dose
            if 'x2_dose' in value:
                x2_dose = value['x2_dose']
                print(f"  x2_dose (shape {x2_dose.shape}):")
                print(f"    {x2_dose}")
        else:
            print(f"  Value: {value}")
        print()


"""
OUTPUT : 
Type of loaded data: <class 'dict'>
Number of entries: 284954

================================================================================

Columns (keys in nested dictionary):
  - matrix
  - x1_dose
  - x2_dose

================================================================================

First 5 entries:

Entry 1:
  Key: 2-Fluoro Ara-A_7-Ethyl-10-hydroxycamptothecin_786-0
  Value (dictionary):
    matrix: numpy array with shape (4, 4)
      First element: 100.0
    x1_dose: numpy array with shape (4,)
      First element: 0.0
    x2_dose: numpy array with shape (4,)
      First element: 0.0

Entry 2:
  Key: 2-Fluoro Ara-A_Abiraterone_786-0
  Value (dictionary):
    matrix: numpy array with shape (4, 4)
      First element: 100.0
    x1_dose: numpy array with shape (4,)
      First element: 0.0
    x2_dose: numpy array with shape (4,)
      First element: 0.0

Entry 3:
  Key: 2-Fluoro Ara-A_Allopurinol_786-0
  Value (dictionary):
    matrix: numpy array with shape (4, 4)
      First element: 100.0
    x1_dose: numpy array with shape (4,)
      First element: 0.0
    x2_dose: numpy array with shape (4,)
      First element: 0.0

Entry 4:
  Key: 2-Fluoro Ara-A_Altretamine_786-0
  Value (dictionary):
    matrix: numpy array with shape (4, 4)
      First element: 100.0
    x1_dose: numpy array with shape (4,)
      First element: 0.0
    x2_dose: numpy array with shape (4,)
      First element: 0.0

Entry 5:
  Key: 2-Fluoro Ara-A_Amifostine_786-0
  Value (dictionary):
    matrix: numpy array with shape (4, 4)
      First element: 100.0
    x1_dose: numpy array with shape (4,)
      First element: 0.0
    x2_dose: numpy array with shape (4,)
      First element: 0.0
"""

"""
OUTPUT :
First 2 entries with full matrix and dose arrays:

Entry 1:
  Key: 2-Fluoro Ara-A_7-Ethyl-10-hydroxycamptothecin_786-0
  matrix (shape (4, 4)):
    [[100.          98.52643585  95.75150299  39.93150711]
 [101.75115204  98.48000336 100.63999939  93.73000336]
 [101.93579102 100.87999725 101.19000244  68.04000092]
 [100.23220825 102.59999847 101.37999725  58.13000107]]
  x1_dose (shape (4,)):
    [0.0 6e-08 6e-07 6e-06]
  x2_dose (shape (4,)):
    [0.0 1e-10 1e-09 1e-08]

Entry 2:
  Key: 2-Fluoro Ara-A_Abiraterone_786-0
  matrix (shape (4, 4)):
    [[100.         101.61766815 100.30366516  80.66749573]
 [101.75115204 102.15799713 100.44000244  56.51499939]
 [101.93579102 104.34799957 102.82900238  77.60299683]
 [100.23220825 100.07700348  85.1210022   58.53499985]]
  x1_dose (shape (4,)):
    [0.0 6e-08 6e-07 6e-06]
  x2_dose (shape (4,)):
    [0.0 5e-08 5e-07 5e-06] 
"""