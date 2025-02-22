#include <vector>
#include <unordered_set>

std::vector<int> arrayDiff(const std::vector<int>& a, const std::vector<int>& b) {
    // creating set with elements of `b for quick looku
    std::unordered_set<int> bSet(b.begin(), b.end());

    // Use a cetor to store the result with unique elements, preserving order
    std::vector<int> result;
    std::unordered_set<int> seen;
    for (int num : a) {
        if(bSet.find(num) == bSet.end() && seen.find(num) == seen.end()) {
            result.push_back(num);
            seen.insert(num);
        }
    }
    return result;
}