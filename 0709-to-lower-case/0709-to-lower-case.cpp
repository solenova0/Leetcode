class Solution {
 public:
  string toLowerCase(string str) {
     for (char& x : str) { 
        x = tolower(x); 
    } 
    return str;
  }
 };