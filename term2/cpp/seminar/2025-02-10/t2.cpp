#include <iostream>

void binary(int a) {
  if (a > 1) {
    binary(a / 2);
  }
  std::cout << a % 2;
  return;
}

int main() {
  int a;
  std::cin >> a;
  binary(a);
  return 0;
}
