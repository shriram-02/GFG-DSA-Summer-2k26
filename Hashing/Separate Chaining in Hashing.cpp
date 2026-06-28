class Solution{
  public:
    vector<vector<int>> separateChaining(int hashSize, int arr[], int N){
        vector<vector<int>> hash(hashSize);

        for(int i = 0; i < N; i++){
            hash[arr[i] % hashSize].push_back(arr[i]);
        }

        return hash;
    }
};