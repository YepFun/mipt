#include <iostream>

int Collatz(int x) {
  int i = 0;
  while (x != 1) {
    if (x % 2 == 0) {
      x /= 2;
    }
    else {
      x = 3 * x + 1;
    }
    ++i;
  }
  return i;
}

int main() { 
  int x;
  std::cin >> x;
  std::cout << Collatz(x) << '\n';
  return 0;
}
