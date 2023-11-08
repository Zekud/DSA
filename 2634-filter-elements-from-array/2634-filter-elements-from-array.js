/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let array2 = []
    for(let i=0;i<arr.length;++i){
        if(fn(arr[i],i))
            array2.push(arr[i])
    }
    return array2;
};