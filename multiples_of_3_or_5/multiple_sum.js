// List all natural numbers that are mutiples of 3 or 5 and sum them

function multiple_sum(num) {

    num_list = [];
    sum = 0;

    if(num < 0) {
        return 0;
    }

    for(i = 1; i < num; i++) {
        if (i % 3 == 0) {
            num_list.push(i);
        }
        if (i % 5 == 0) {
            num_list.push(i);
        }
    }

    // chekcing for similar values using the filter method.
    let uniqueNumbers = num_list.filter((value, index, self) => {
        return self.indexOf(value) == index;
    })


    for(i = 0; i < uniqueNumbers.length; i++) {
        sum = sum + uniqueNumbers[i];
    }

    console.log("The number list",num_list);
    console.log("The unique list", uniqueNumbers);
    return sum;
}

console.log(multiple_sum(20));

module.exports = multiple_sum;
