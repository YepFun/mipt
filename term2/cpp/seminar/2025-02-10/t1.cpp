#include <iostream>

unsigned gcd(unsigned a, unsigned b) {
  if (a == 0 && b == 0) {
    return 1;
  }
  while (a != 0 && b != 0) {
    if (a >= b) {
      a -= b;
    } else {
      b -= a;
    }
  } 
  return a + b;
}

int main() {
  unsigned a, b;
  std::cin >> a >> b;
  std::cout << gcd(a, b) << '\n';
  return 0;
}
