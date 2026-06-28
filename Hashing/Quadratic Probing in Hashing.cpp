class Solution{
public:
    vector<int> quadraticProbing(int hashSize, int arr[], int N){
        vector<int> hash(hashSize, -1);

        for(int i = 0; i < N; i++){
            int key = arr[i];
            int h = key % hashSize;

            if(hash[h] == -1){
                hash[h] = key;
                continue;
            }

            for(int j = 1; j < hashSize; j++){
                int idx = (h + j * j) % hashSize;
                if(hash[idx] == -1){
                    hash[idx] = key;
                    break;
                }
            }
        }

        return hash;
    }
};