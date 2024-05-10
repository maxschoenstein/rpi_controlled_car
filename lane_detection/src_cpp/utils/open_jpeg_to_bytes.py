def openJpegToBytes(file_path):
    with open(file_path, 'rb') as f:
        return f.read()
