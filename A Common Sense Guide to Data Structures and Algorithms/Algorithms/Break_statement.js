function intersection(firstArray, secondArray) {
  let result = [];

  for (let i = 0; i < firstArray.length; i++) {
    for (let j = 0; j < secondArray.length; j++) {
      if (firstArray[i] == secondArray[j]) {
        result.push(firstArray[i]);
      }
    }
  }

  return result;
}

//All we have to do is add a break statement to the inner loop,
//and the function will stop iterating needlessly after it already finds
//a duplicate value. This will make our function much more efficient.

function intersection(firstArray, secondArray) {
  let result = [];

  for (let i = 0; i < firstArray.length; i++) {
    for (let j = 0; j < secondArray.length; j++) {
      if (firstArray[i] == secondArray[j]) {
        result.push(firstArray[i]);
        break;
      }
    }
  }

  return result;
}
