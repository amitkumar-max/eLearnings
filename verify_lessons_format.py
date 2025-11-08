import os, collections

BASE_DIR = "app/lessons/content"
for course in os.listdir(BASE_DIR):
    path = os.path.join(BASE_DIR, course)
    if not os.path.isdir(path):
        continue
    files = [os.path.splitext(f)[0].lower() for f in os.listdir(path) if f.endswith(('.html', '.txt'))]
    dupes = [f for f, c in collections.Counter(files).items() if c > 1]
    if dupes:
        print(f"⚠️ {course} has duplicate base files: {dupes}")
