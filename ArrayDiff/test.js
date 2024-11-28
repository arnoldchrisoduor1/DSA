const assert = require('assert');
const arrayDiff = require('./arrayDiff');

describe('arrayDiff', function() {
    it('should return [2] when a = [1, 2] and b = [1]', function() {
        assert.deepStrictEqual(arrayDiff([1, 2], [1]), [2])
    })
    it('should return [1, 3] when a = [1, 2, 2, 2, 2, 3] and b = [2]', function() {
        assert.deepStrictEqual(arrayDiff([1, 2, 2, 2, 3], [2]), [1, 3]);
    });
    it('should return [] when a = [1, 2] and b = [1, 2]', function() {
        assert.deepStrictEqual(arrayDiff([1, 2], [1, 2]), []);
    })
    it('should return [2] when a = [1, 2, 2] and b = [1]', function() {
        assert.deepStrictEqual(arrayDiff([1, 2, 2], [1]), [2]);
    })
    it('should return the same array if b is empty', function(){
        assert.deepStrictEqual(arrayDiff([1, 2, 3], []), [1, 2, 3]);
    })
});