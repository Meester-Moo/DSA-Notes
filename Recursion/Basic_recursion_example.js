function countdown(number) {
  console.log(number);

  if (number === 0) {
    // number being 0 is the base case
    return;
  } else {
    countdown(number - 1);
  }
}
