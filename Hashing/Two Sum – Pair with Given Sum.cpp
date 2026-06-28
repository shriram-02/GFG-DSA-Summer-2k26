class Solution {
public:
    bool twoSum(vector<int>& arr, int target) {
        unordered_set<int> st;

        for (int x : arr) {
            if (st.count(target - x))
                return true;
            st.insert(x);
        }

        return false;
    }
};