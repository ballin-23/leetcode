input = [2,0,2,1,1,0]

def sort_colors(nums):
    color_dictionary = {}
    for i in range(len(nums)):
        if nums[i] in color_dictionary.keys():
            color_dictionary[nums[i]].append(i)
        else:
            color_dictionary.update({nums[i]: [i]})
    sorted_color_dictionary = dict(sorted(color_dictionary.items(), key=lambda x:x[0]))
    counter = 0
    for num in sorted_color_dictionary:
        indices = sorted_color_dictionary[num]
        for index in indices:
            nums[counter] = num
            counter += 1



sort_colors(input)