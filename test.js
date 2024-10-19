
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
const createhashtag = (str) => {
    if (str.length > 280 || str.trim().length === 0) {
        return false;
    }
    split_arr = str.split(" ");
    
    strarr = split_arr.map((cur_elem) =>  (cur_elem.replace(cur_elem[0],cur_elem[0].toUpperCase())) );
    // console.log(strarr);
    
    finalstr=`#${strarr.join("")}`
    console.log(finalstr);
    
}

console.log(createhashtag("Hello my name is Sayan"));
