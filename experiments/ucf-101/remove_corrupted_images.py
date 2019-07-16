import os
import PIL.Image as Image
from send2trash import send2trash


def is_corrupted(filename):
    try:
        img = Image.open(filename)
        return False
    except OSError:
        return True


def remove_corrupted_image_folder(dir):
    if not os.path.isdir(dir):
        print(dir, "does not exist")
        return False
    for dirpath, dirnames, filenames in os.walk(dir):
        if len(filenames) == 0:
            # Empty folder. Delete
            send2trash(dirpath)
            print("Removed", dirpath)
            return True
        else:
            for file in filenames:
                if is_corrupted(os.path.join(dirpath, file)):
                    # Corrupted images detected. Delete the whole folder.
                    send2trash(dirpath)
                    print("Removed", dirpath)
                    return True
    return False


print("Hello, world!")
l = open("/home/jiashu/Documents/I3D-Tensorflow/list/ucf_list/train_flow.list", 'r')
print("List loaded")
lines = list(l)
counter = 0

for line in lines:
    path = (line.split())[0]
    assert isinstance(path, str)

    filename_i = os.path.join(path, 'i')
    filename_x = os.path.join(path, 'x')
    filename_y = os.path.join(path, 'y')

    if remove_corrupted_image_folder(filename_i):
        send2trash(filename_x)
        send2trash(filename_y)
        counter += 1
    elif remove_corrupted_image_folder(filename_x):
        send2trash(filename_i)
        send2trash(filename_y)
        counter += 1
    elif remove_corrupted_image_folder(filename_y):
        send2trash(filename_i)
        send2trash(filename_x)
        counter += 1

print("Total number of corrupted directory is", counter)
