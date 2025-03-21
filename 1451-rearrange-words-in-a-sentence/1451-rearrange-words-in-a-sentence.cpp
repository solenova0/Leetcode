 class Solution {
 public:
  string arrangeWords(string text) {
    if (text.empty()) return "";
     text.front() = tolower(text.front());
    istringstream iss(text);
    string ret, s;
    vector<pair<string, int>> words;
    int i = 0;
    while (iss >> s) words.emplace_back(s, ++i);
    sort(words.begin(), words.end(), [](pair<string, int> p1, pair<string, int> 
p2) {
      if (p1.first.size() == p2.first.size()) {
        return p1.second < p2.second;
      }
      return p1.first.size() < p2.first.size();
    });
    bool first = true;
    for (auto& w : words) {
      if (first) {
        first = false;
        ret += w.first;
      } else {
        ret += " ";
        ret += w.first;
      }
    }
    ret.front() = toupper(ret.front());
    return ret;
  }
 };