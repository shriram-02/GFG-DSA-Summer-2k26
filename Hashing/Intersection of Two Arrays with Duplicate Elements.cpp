class Solution {
public:
    vector<int> intersectionWithDuplicates(vector<int>& a, vector<int>& b) {
        unordered_map<int, int> mp;
        vector<int> ans;

        for (int x : a)
            mp[x]++;

        for (int x : b) {
            if (mp[x] > 0) {
                ans.push_back(x);
                mp[x]--;
            }
        }

        return ans;
    }
};