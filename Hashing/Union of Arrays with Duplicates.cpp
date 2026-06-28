class Solution {
public:
    int findUnion(vector<int>& a, vector<int>& b) {
        unordered_set<int> st;

        for (int x : a)
            st.insert(x);

        for (int x : b)
            st.insert(x);

        return st.size();
    }
};