// List all natural numbers that are mutiples of 3 or 5 and sum 

// ============== OPTIMIZED CODE ======================

function multiple_sum_op(number) {
    let sum = 0;

    if(number < 0) {
        return 0;
    }

    for (let i = 1; i < number; i++) {
        // Add to sum if the number is divisible by 3 or 5
        if(i % 3 === 0 || i % 5 === 0) {
            sum += i;
        }
    }
    return sum;
}

// ================= Clever Solution =========================

function solution(number) {
    return Number < 1 ? 0 : [...new Array(number).keys()].filter(n => n % 3 === 0 || n % 5 === 0).reduce((a, b) => a + b)
}

// ============= First Solution =================

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
