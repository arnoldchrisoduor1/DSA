const multiple_sum = require('./multiple_sum'); // Assuming the function is exported from another file

describe('multiple_sum()', () => {
  test('should return 0 if input number is negative', () => {
    expect(multiple_sum(-5)).toBe(0);
  });

  test('should return 0 if input number is 0', () => {
    expect(multiple_sum(0)).toBe(0);
  });

  test('should return the correct sum of multiples of 3 or 5 below 10', () => {
    expect(multiple_sum(10)).toBe(23);  // Multiples: 3, 5, 6, 9 -> Sum = 23
  });

  test('should return the correct sum of multiples of 3 or 5 below 20', () => {
    expect(multiple_sum(20)).toBe(78);  // Multiples: 3, 5, 6, 9, 10, 12, 15, 18 -> Sum = 78
  });

  test('should return the correct sum of multiples of 3 or 5 below 1', () => {
    expect(multiple_sum(1)).toBe(0); // No multiples below 1
  });
});