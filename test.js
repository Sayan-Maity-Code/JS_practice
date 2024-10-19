
const findlongestword = (str) => {
    if (str.trim().length === 0) {
        return false;
    };
    strarr = str.split(" ");
    strarr = strarr.sort((a, b) => a.length - b.length);
console.log(strarr.at(-1));
    
};

console.log(findlongestword("Longest word is the lastwordsurely"));
