import os
def save_uploaded_file(uploaded_file):

    save_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return save_path


def get_file_extension(file_path):

    return file_path.split(".")[-1].lower()