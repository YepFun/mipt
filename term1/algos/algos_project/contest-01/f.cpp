#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

const int c8 = 8;

uint32_t cur = 0;
uint32_t NextRand24(uint32_t a, uint32_t b) {
  cur = cur * a + b;
  return cur >> c8;
}
uint32_t NextRand32(uint32_t a, uint32_t b) {
  uint32_t x = NextRand24(a, b);
  uint32_t y = NextRand24(a, b);
  return (x << c8) ^ y;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cout.tie(0);
  std::ifstream cin("input.txt");
  std::ofstream cout("output.txt");
  int n;
  cin >> n;
  int a;
  int b;
  cin >> a >> b;
  std::vector<uint32_t> x(n);
  for (int i = 0; i < n; ++i) {
    x[i] = NextRand32(a, b);
  }
  std::sort(x.begin(), x.end());
  uint32_t m = x[n / 2];
  long long result = 0;
  for (int i = 0; i < n; ++i) {
    result += (x[i] > m) ? (x[i] - m) : (m - x[i]);
  }
  cout << result << '\n';
  return 0;
}
