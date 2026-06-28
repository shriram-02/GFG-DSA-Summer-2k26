class Solution {
  public:
    vector<int> linearProbing(int hashSize, int arr[], int N) {
        vector<int> hash(hashSize, -1);

        for (int i = 0; i < N; i++) {
            int idx = arr[i] % hashSize;
            int start = idx;

            while (hash[idx] != -1 && hash[idx] != arr[i]) {
                idx = (idx + 1) % hashSize;
                if (idx == start) break;
            }

            if (hash[idx] == -1)
                hash[idx] = arr[i];
        }

        return hash;
    }
};