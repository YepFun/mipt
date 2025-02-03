#include <iostream>

int main() { 
  int n;
  std::cin >> n;
  double mean = 0;
  for (int i = 0; i < n; ++i) {
    int x;
    std::cin >> x;
    mean += x;
  }
  std::cout << mean / n << '\n';
  return 0;
}
