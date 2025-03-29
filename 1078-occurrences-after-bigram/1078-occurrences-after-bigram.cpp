class Solution {
 public:
  vector<string> findOcurrences(string text, string first, string second) {
    vector<string> ret;
    istringstream iss(text);
    string w1, w2, w3;

    if (!(iss >> w1)) return ret; // Read first word
    if (!(iss >> w2)) return ret; // Read second word

    while (iss >> w3) {  // Read third word and process
      if (w1 == first && w2 == second) {
        ret.push_back(w3);
      }
      w1 = w2; // Shift words forward
      w2 = w3;
    }
    
    return ret;
  }
};
