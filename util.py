def navigate_directories(directory, files):
    for path in directory.iterdir():
        if path.is_dir():
            navigate_directories(path, files)
        else:
            files.append(path)
    return files
