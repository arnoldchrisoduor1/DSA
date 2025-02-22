function arrayDiff(a, b) {
    const filteredArray = a.filter(element => !b.includes(element));

    // using set to remove the duplicates.
    return [ ...new Set(filteredArray)]
  }
  
console.log(arrayDiff([1, 2, 2, 3, 3, 4, 4], [2, 3]));

module.exports = arrayDiff;