/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let result = []
    for(let i = 0; i<nums.length; ++i){
       for(let j = 0; j<nums.length; ++j){
           if(nums[i] + nums[j] == target && i != j ){
                result.push(i);
                 result.push(j);
           }
       }
   }
    let unique = [...new Set(result)]
    return unique;
    
};