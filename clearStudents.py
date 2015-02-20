#pickle test
import pickle

students = []

with open('students.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(students, f, pickle.HIGHEST_PROTOCOL)
