import os


def getFileName(fileName):
    fullname = os.path.basename(fileName)
    name, ext = os.path.splitext(fullname)
    return name, ext


def changePhotoNamePostGallery(instance, file):
    name, ext = getFileName(file)
    new_name = f"{instance.id}-{instance.blog_post.title}{ext}"
    return f"BlogGallery/{new_name}"


def changePhotoNameBlogImage(instance, file):
    name, ext = getFileName(file)
    new_name = f"{instance.id}-{instance.title}{ext}"
    return f"Blog/{new_name}"
