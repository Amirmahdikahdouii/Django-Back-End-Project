import os


def getFileName(fileName):
    fullname = os.path.basename(fileName)
    name, ext = os.path.splitext(fullname)
    return name, ext


def changePhotoNameMiniProjects(instance, file):
    name, ext = getFileName(file)
    new_name = f"{instance.id}-{instance.name}{ext}"
    return f"miniProjectList/{new_name}"
