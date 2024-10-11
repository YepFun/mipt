#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>
#include <algorithm>

const int cMod = 10004321;
const int c123 = 123;
const int c45 = 45;

void GenerateVector(std::vector<int>& a) {
  for (size_t i = 2; i < a.size(); ++i) {
    a[i] = (c123 * a[i - 1] + c45 * a[i - 2]) % cMod;
  }
}

int Partition(std::vector<int>& a, int& left, int& right, int& pivot) {
  int a_pivot = a[pivot];
  std::swap(a[right], a[pivot]);
  int j = left;
  for (int i = left; i < right; ++i) {
    if (a[i] < a_pivot) {
      std::swap(a[i], a[j]);
      ++j;
    }
  }
  std::swap(a[right], a[j]);
  return j;
}

int QuickSelect(std::vector<int>& a, int left, int right, int k) {
  if (left == right) {
    return a[left];
  }
  int pivot = left + rand() * (right - left + 1);
  pivot = Partition(a, left, right, pivot); 
  if (pivot == k) {
    return a[k];
  } else if (pivot > k) {
    return QuickSelect(a, left, pivot - 1, k);
  } else {
    return QuickSelect(a, pivot + 1, right, k);
  }
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
  --k;
  std::vector<int> a(n);
  cin >> a[0] >> a[1];
  GenerateVector(a);
  cout << QuickSelect(a, 0, n - 1, k) << '\n';
  return 0;
}