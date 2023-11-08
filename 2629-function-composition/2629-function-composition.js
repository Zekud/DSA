/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
	return function(x) {
        if(functions.length == 0){
            return x
        }else{
            let i=functions.length-1
            let val = functions[i](x);
            --i;
            while(i>=0){
                val = functions[i](val);
                 --i;
            }
            return val;
        }
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */