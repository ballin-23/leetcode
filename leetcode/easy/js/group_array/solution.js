/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const myMap = new Map()
    this.forEach(item => {
        if (myMap.has(fn(item))) {
            existing = myMap.get(fn(item))
            existing.push(item)
            myMap.set(fn(item), existing)
        } else {
            myMap.set(fn(item), [item])
        }
    })
    const obj = {}
    myMap.forEach((value, key) => {
        obj[key] = value
    })
    return obj
};