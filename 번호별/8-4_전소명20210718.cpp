#include <set>
#include <vector>
#include <iostream>
using namespace std; 

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> s;
        for(int i : nums) s.insert(i);
        nums.clear();
        for(int i : s) nums.push_back(i);
        return s.size();
    }
};