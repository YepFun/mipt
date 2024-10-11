#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

void Merge(std::vector<int>& a, std::vector<int>& b, std::vector<int>& to,
           long long& inversions) {
  size_t i = 0;
  size_t j = 0;
  to.resize(a.size() + b.size());
  while (i < a.size() || j < b.size()) {
    if (j == b.size() || (i < a.size() && a[i] <= b[j])) {
      to[i + j] = a[i];
      ++i;
    } else {
      to[i + j] = b[j];
      ++j;
      inversions += a.size() - i;
    }
  }
}

void MergeSort(std::vector<int>& a, long long& inversions) {
  if (a.size() <= 1) {
    return;
  }
  int k = a.size() / 2;
  std::vector<int> l(a.begin(), a.begin() + k);
  std::vector<int> r(a.begin() + k, a.end());
  MergeSort(l, inversions);
  MergeSort(r, inversions);
  Merge(l, r, a, inversions);
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cout.tie(0);
  std::ifstream cin("input.txt");
  std::ofstream cout("output.txt");
  int n;
  cin >> n;
  std::vector<int> a(n);
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  long long inversions = 0;
  MergeSort(a, inversions);
  cout << inversions << '\n';
  return 0;
}
