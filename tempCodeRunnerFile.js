const findMedian = (arr) => {
  arr = arr.sort((a, b) => a - b);
  console.log(arr);

  mid = Math.floor(arr.length / 2);
  console.log(mid);

  if (arr.length % 2 == 0) {
    return (arr[mid] + arr[mid - 1]) / 2;
  } else {
    return arr[mid];
  }
};

console.log(findMedian([11, 2, 30, 4, 5, 7]));
console.log(5/2);