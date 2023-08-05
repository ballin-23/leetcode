// part of the 30 days of js => write a function that splits an array into chunks of size n
/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    new_arr = []
    if (size > 1) {
        chunk_arr = []
        for(let i = 0; i < arr.length; i++) {
            if ((i+1) % size == 0) {
                chunk_arr.push(arr[i])
                new_arr.push(chunk_arr)
                chunk_arr = []
            } else {
                chunk_arr.push(arr[i])
            }
        }
        if (chunk_arr.length > 0) {
            new_arr.push(chunk_arr)
        }
        return new_arr
    }
    else {
        if (arr) {
            arr.forEach((item) => {
                new_arr.push([item])
            })
        }
        return new_arr
    }
};