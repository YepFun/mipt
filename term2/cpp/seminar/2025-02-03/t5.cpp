#include <iostream>

int main() {
  int x;
  std::cin >> x;
  int summ = 0;
  while (x != 0) {
    summ += x;
    std::cin >> x;
  }
  std::cout << summ << '\n';
  return 0;
}
