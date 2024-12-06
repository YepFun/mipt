#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void Merge(std::vector<int>& a, std::vector<int>& b, std::vector<int>& to) {
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
    }
  }
}

void MergeSort(std::vector<int>& a) {
  if (a.size() <= 1) {
    return;
  }
  int k = a.size() / 2;
  std::vector<int> l(a.begin(), a.begin() + k);
  std::vector<int> r(a.begin() + k, a.end());
  MergeSort(l);
  MergeSort(r);
  Merge(l, r, a);
}
