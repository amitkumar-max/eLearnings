import os

BASE_DIR = "app/lessons/content"

deleted = 0
for course in os.listdir(BASE_DIR):
    course_path = os.path.join(BASE_DIR, course)
    if not os.path.isdir(course_path):
        continue

    files = os.listdir(course_path)
    base_names = {}

    for file_name in files:
        name, ext = os.path.splitext(file_name)
        if ext.lower() not in [".html", ".txt"]:
            continue

        name_lower = name.lower()
        base_names.setdefault(name_lower, []).append((file_name, ext.lower()))

    for base, variants in base_names.items():
        # if both HTML and TXT exist → delete TXT
        html_exists = any(v[1] == ".html" for v in variants)
        txt_files = [v[0] for v in variants if v[1] == ".txt"]

        if html_exists and txt_files:
            for txt in txt_files:
                os.remove(os.path.join(course_path, txt))
                deleted += 1
                print(f"🗑️ Deleted TXT duplicate: {course}/{txt}")

        # remove extra "(1)" or "(copy)" files
        for file_name, _ in variants:
            if "(copy" in file_name.lower() or "(1)" in file_name.lower():
                os.remove(os.path.join(course_path, file_name))
                deleted += 1
                print(f"🧹 Removed copy file: {course}/{file_name}")

print(f"\n✅ Cleanup complete! {deleted} files removed.")
