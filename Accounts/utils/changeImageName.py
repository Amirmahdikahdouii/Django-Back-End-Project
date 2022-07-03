import os


def getFileName(fileName):
    fullname = os.path.basename(fileName)
    name, ext = os.path.splitext(fullname)
    return name, ext


def changeProfilePictureName(instance, file):
    name, ext = getFileName(file)
    new_name = f"{instance.id}-{instance.user.username}{ext}"
    return f"UserProfileImages/{new_name}"
