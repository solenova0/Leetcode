 class Solution {
public:
    int findComplement(int num) {
        int ret = 0, bits = 0;
        while (num) {
            if (!(num & 1)) { 
                ret += (1 << bits);
            }
            num >>= 1; 
            ++bits;
        }
        return ret;
    }
};
