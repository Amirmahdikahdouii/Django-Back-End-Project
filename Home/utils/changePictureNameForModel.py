import os


def getFileName(fileName):
    fullname = os.path.basename(fileName)
    name, ext = os.path.splitext(fullname)
    return name, ext


def changePhotoName(instance, file):
    name, ext = getFileName(file)
    new_name = f"{instance.id}-{instance.title}{ext}"
    return f"carouselImage/{new_name}"