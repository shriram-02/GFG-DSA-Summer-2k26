class Solution {
  public:
    vector<int> removeDuplicate(vector<int>& arr) {
        unordered_set<int> st;
        vector<int> ans;

        for (int x : arr) {
            if (st.find(x) == st.end()) {
                st.insert(x);
                ans.push_back(x);
            }
        }

        return ans;
    }
};