#include <fstream>
#include <iostream>
#include <vector>

bool BinarySearch(int b, std::vector<int>& a) {
  int left_border = 0;
  int right_border = a.size() - 1;
  while (left_border <= right_border) {
    int m = (left_border + right_border) / 2;
    if (a[m] == b) {
      return true;
    }
    if (a[m] < b) {
      left_border = m + 1;
    } else {
      right_border = m - 1;
    }
  }
  return false;
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
  std::vector<int> a(n);
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  for (int i = 0; i < k; ++i) {
    int b;
    cin >> b;
    bool found = BinarySearch(b, a);
    if (found) {
      cout << "YES\n";
    } else {
      cout << "NO\n";
    }
  }
  return 0;
}
