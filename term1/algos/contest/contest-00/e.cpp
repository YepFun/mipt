#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

bool AbleToCover(std::vector<int>& x, int& k, long long& length) {
  int segment_number = 0;
  size_t i = 0;
  while (i < x.size()) {
    int segment_start = x[i];
    segment_number++;
    while (i < x.size() && x[i] <= segment_start + length) {
      ++i;
    }
  }
  return (segment_number <= k);
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cout.tie(0);
  std::ifstream cin("input.txt");
  std::ofstream cout("output.txt");
  int n;
  int k;
  cin >> n >> k;
  std::vector<int> x(n);
  for (int i = 0; i < n; ++i) {
    cin >> x[i];
  }
  sort(x.begin(), x.end());
  long long min_length = 0;
  long long max_length = x[n - 1] - x[0];
  while (min_length < max_length) {
    long long m = (min_length + max_length) / 2;
    if (AbleToCover(x, k, m)) {
      max_length = m;
    } else {
      min_length = m + 1;
    }
  }
  cout << min_length << '\n';
}
