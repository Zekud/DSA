/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let myMap = new Map()
    let callCount = 0;
    return function(...args) { 
        let key = JSON.stringify(args)
        if(myMap.has(key))
            return myMap.get(key)
        else{
            let result = fn(...args)
            myMap.set(key,result)
            callCount++;
            return result;
        }
            
    }
    function getCallCount(){
        return callCount;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */