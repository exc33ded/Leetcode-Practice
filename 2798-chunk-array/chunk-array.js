/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const chunkarr = []

        for(let i = 0; i<arr.length; i+=size){

            var subarr = arr.slice(i, i+size);

            chunkarr.push(subarr);

        }

        return chunkarr;
};
