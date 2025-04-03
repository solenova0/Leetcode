 class Solution {
 public:
  double average(vector<int>& salary) {
    double avg = 0;
    int n = salary.size();
    for (auto s : salary) avg += s;
    avg -= *max_element(salary.begin(), salary.end());
    avg -= *min_element(salary.begin(), salary.end());
    return avg / (n - 2);
  }
 };