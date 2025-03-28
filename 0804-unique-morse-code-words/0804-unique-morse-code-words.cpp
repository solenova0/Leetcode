 class Solution {
 public:
  int uniqueMorseRepresentations(vector<string>& words) {
    unordered_set<string> morse;
    vector<string> dict{
      ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
      "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
      "..-","...-",".--","-..-","-.--","--.."
    };

    for (auto& w : words) {
      string s;
      for (auto& c : w) {
        s += dict[c - 'a'];
      }
      morse.insert(s);
    }
    return morse.size();
  }
};
