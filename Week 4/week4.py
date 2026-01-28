students = [
  {
    "name": "Huy",
    "age": "20",
    "grade": {"math": 9, "english": 7}
  },
  {
    "name": "Huy",
    "age": "11",
    "grade": {"math": 8, "english": 8}
  }, 
  {
    "name": "Hy",
    "age": "2",
    "grade": {"math": 7, "english": 9}
  }
]

# List All Student Names
students["name"]

# Calculate Average Grade Using Lambda
average = lambda a, b: (a + b) / 2
average(students[0]["grade"]["math"], students[0]["grade"]["english"])

# Find Top Students

# Use Tuples to Store Constants
# Filter Students Based on Criteria
# Demonstrate Local and Global Variables