
// const findlongestword = (str) => {
//     if (str.trim().length === 0) {
//         return false;
//     };
//     strarr = str.split(" ");
//     strarr = strarr.sort((a, b) => a.length - b.length);
// console.log(strarr.at(-1));
    
// };

// console.log(findlongestword("Longest word is the lastwordsurely"));



// ---------------------------
// const createhashtag = (str) => {
//     if (str.length > 280 || str.trim().length === 0) {
//         return false;
//     }
//     split_arr = str.split(" ");
    
//     strarr = split_arr.map((cur_elem) =>  (cur_elem.replace(cur_elem[0],cur_elem[0].toUpperCase())) );
//     // console.log(strarr);
    
//     finalstr=`#${strarr.join("")}`
//     console.log(finalstr);
    
// }

// createhashtag("Hello my name is Sayan");
// ---------------------------------------

// 3rd problem
// Count occurances of character

// const count_number = (word, Letter) => {
//     word = word.trim().toLowerCase();
//     Letter = Letter.toLowerCase();
    
//     let totalcount = word.split("").reduce((accum, curr) => {
//         if (curr === Letter) {
//             accum++;
//         }
//         return accum;
//     }, 0)
//     console.log(totalcount);
    
    
    
// }
// count_number("Sayan","A")


// const sot_asc = (x) => {
//     sort_x = x.sort((a, b) => a - b)
//     return sort_x[sort_x.length-1];
// }
// console.log(sot_asc([5,6,4,2,11,98]));
 
// DataFetchingComponent.js


// function Calculate_avg(arr) {
//     avg_arr = arr.reduce((accum, cur_elem) => accum + cur_elem, 0
//     );
//     console.log(avg_arr);
    
//     avg_arr = avg_arr / arr.length;
//     return avg_arr;
// }

// console.log(Calculate_avg([1,2,3,4,5]));

// function checkequal(arr1,arr2) {
//     return arr1.every((curVal,index)=>curVal===arr2[index])
    
   
// }
// console.log(checkequal([1,2,3],[1,2,3]));

// const removeDuplicate = (arr) => {
//     newArr = [...new Set(arr)]
//     return newArr;
// }
// console.log(removeDuplicate([1,2,22,8,2,1,66,5,4]));

const countVowels = (arr) => {
    let count = 0;
    vwl = ['a', 'e', 'i', 'o', 'u'];
    new_arr = arr.split("");
    console.log(new_arr);
    // for (let char in new_arr) {
    //     if (vwl.includes(new_arr[char].toLowerCase())) {
    //       count++;
    //     }
    // ----------can also be done----
    for (let char of new_arr) {
        if (vwl.includes(char.toLowerCase())) {
            count++;
        }
    }

    return count;
    
}

console.log(countVowels("fbdj wwjfhA AE dvbsdvI jju"));
