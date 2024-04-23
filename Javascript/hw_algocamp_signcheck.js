function getSign(number) {
    if (typeof number !== 'number' || isNaN(number)) {
        return NaN; // Not-a-Number, indicating an invalid input
    } else if (Object.is(number, 0)) {
        return Object.is(number, -0) ? -0 : +0; // Return -0 or +0
    } else {
        return number > 0 ? 1 : -1; // Positive or negative
    }
}

// Example usage:
console.log(getSign(5)); // Output: 1 (positive)
console.log(getSign(-3)); // Output: -1 (negative)
console.log(getSign(0)); // Output: +0 (zero)
console.log(getSign(-0)); // Output: -0 (negative zero)
console.log(getSign(+0)); // Output: +0 (positive zero)
console.log(getSign("hello")); // Output: NaN (invalid input)