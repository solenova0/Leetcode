 class Solution {
 public:
  int maxDiff(int num) {
    string s1 = to_string(num);
    string s2 = to_string(num);
    char c, t;
    bool found = false;
    int n = s1.size();
    for (int i = 0; i < n; ++i) {
      if (!found && s1[i] != '9') {
        c = s1[i];
        s1[i] = '9';
        found = true;
      } else if (found && s1[i] == c) {
        s1[i] = '9';
      }
    }
    found = false;
    for (int i = 0; i < n; ++i) {
      if (!found) {
        if (s2[0] != '1') {
          c = s2[0];
          t = '1';
          s2[0] = '1';
          found = true;
        } else {
          if (i > 0 && s2[i] != s2[0] && s2[i] != '0') {
            c = s2[i];
            t = '0';
            s2[i] = '0';
            found = true;
          }
        }
      } else {
        if (s2[i] == c) {
          s2[i] = t;
        }
      }
    }
    return stoi(s1) - stoi(s2);
  }
 };