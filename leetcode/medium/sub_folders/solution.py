# 1233. Remove Sub-Folders from the Filesystem
# we don't like sub folders in this
# implementation:
# go through array and create dictionaries using the root of each folder sequence given
# for each array of values associated with the keys we loop through and if one key is contained in another key the other key is removed
# the result is then stored back in the dictionary

def remove_subfolders(folder):
    folder_dict = create_folder_dict(folder)
    for key in folder_dict.keys():
        similar_paths = folder_dict[key]
        for path in similar_paths:
            for test_path in similar_paths:
                print(path, test_path, path in test_path and path != test_path)
                if len(path) > len(test_path):
                    continue
                if path in test_path and path != test_path:
                    if double_check(path, test_path) and (test_path in folder):
                        folder.remove(test_path)
    print(folder)
    return folder

def double_check(path, test_path):
    arr = path.split('/')
    arr2 = test_path.split('/')
    iterator = min(len(arr),len(arr2))
    i = 0
    while i < iterator:
        if arr[i] != arr2[i]:
            return False
        i += 1
    return True

def create_folder_dict(folder_arr):
    folder_dict = {}
    for path in folder_arr:
        root = path[1]
        # print(path, root)
        if root in folder_dict:
            # print("inside dictionary")
            folder_dict[root].append(path)
        else:
            # print("outside dictionary")
            folder_dict[root] = [path]
    print(folder_dict)
    return folder_dict

# folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# folder = ["/a","/a/b/c","/a/b/d"]
# folder = ["/a/b/c","/a/b/ca","/a/b/d"]
folder = ["/aa/ab/ac/ae","/aa/ab/af/ag","/ap/aq/ar/as","/ap/aq/ar","/ap/ax/ay/az","/ap","/ap/aq/ar/at","/aa/ab/af/ah","/aa/ai/aj/ak","/aa/ai/am/ao"]
remove_subfolders(folder)