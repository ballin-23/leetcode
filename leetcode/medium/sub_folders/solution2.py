def remove_subfolders(folder):
    folder.sort()  # Sort the folder array in lexicographical order
    result = []
    result.append(folder[0])  # Add the first folder to the result list
    # print(result)
    prev_folder = folder[0]  # Add a trailing slash for comparison

    for i in range(1, len(folder)):
        current_folder = folder[i]  # Add a trailing slash for comparison
        # print(current_folder, "--" ,prev_folder, current_folder.startswith(prev_folder))
        if not current_folder.startswith(prev_folder):
            print(result)
            result.append(folder[i])  # Add the folder to the result list
            prev_folder = current_folder  # Update the previous folder

    # print(result)
    return result

# folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# folder = ["/a","/a/b/c","/a/b/d"]
# folder = ["/a/b/c","/a/b/ca","/a/b/d"]
folder = ["/aa/ab/ac/ae","/aa/ab/af/ag","/ap/aq/ar/as","/ap/aq/ar","/ap/ax/ay/az","/ap","/ap/aq/ar/at","/aa/ab/af/ah","/aa/ai/aj/ak","/aa/ai/am/ao"]
remove_subfolders(folder)