
class Solution {
    public boolean isPalindrome(int x) {
        int r,s=0,number=x;
        if(number<0){
            return false;
        }
        while (number!=0){
            r=number%10;
            s= s*10 +r;
            number/=10;
        }
        if (s==x){
            return true;
        }
        else {
            return false;
        }
    }
}