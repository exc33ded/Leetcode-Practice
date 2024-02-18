#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int count = 0;
        unordered_set<char> allowedSet(allowed.begin(), allowed.end());

        for (const auto& word : words) {
            bool consistent = true;
            for (char w : word) {
                if (allowedSet.find(w) == allowedSet.end()) {
                    consistent = false;
                    break;
                }
            }
            if (consistent) {
                count++;
            }
        }

        return count;
    }
};