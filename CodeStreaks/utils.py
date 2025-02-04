def load_handles(file_path):
    handles = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                handle = line.strip()
                if handle:
                    handles.append(handle)
    except FileNotFoundError:
        print(f"Handles file {file_path} not found. Please add user handles to the file.")
    return handles