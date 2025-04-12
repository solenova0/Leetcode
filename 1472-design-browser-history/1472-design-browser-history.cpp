 class BrowserHistory {
 private:
  list<string> history;
  int x;
 
public:
  BrowserHistory(string homepage) {
    history.push_back(homepage);
    x = 0;
  }
 
  void visit(string url) {
    history.erase(next(history.begin(), x + 1), history.end());
    history.push_back(url);
    ++x;
  }
 
  string back(int steps) {
 
    x = steps > x ? 0 : x - steps;
    return *next(history.begin(), x);
  }
 
  string forward(int steps) {
    int n = history.size();
    x = steps > n - 1 - x ? n - 1 : x + steps;
    return *next(history.begin(), x);
  }
 };