class Solution {
  public:
    void sortArr(vector<string>& arr) {
        // code here
        stable_sort(arr.begin(), arr.end(), [](const string &a, const string &b) {
            return a.size() < b.size();
        });
    }
};