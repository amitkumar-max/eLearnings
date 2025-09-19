from django.shortcuts import render
import numpy as np

def student_dashboard(request):
    # Example: NumPy ka use karke dummy data generate karna
    marks = np.random.randint(50, 100, size=5).tolist()  # random marks
    subjects = ["Math", "Physics", "Chemistry", "CS", "English"]

    context = {
        "subjects": subjects,
        "marks": marks,
    }
    return render(request, "dashboard.html", context)
