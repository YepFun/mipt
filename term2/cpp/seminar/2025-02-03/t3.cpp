#include <iostream>

int Fibonacci(int n) {
  if (n < 0) {
    std::cerr << "Error: Fibonacci number is not valid\n";
    return 0;
  }
  if (n == 0) {
    return 1;
  }
  if (n == 1) {
    return 1;
  }
  return Fibonacci(n - 2) + Fibonacci(n - 1);
}

int main() { 
  int n;
  std::cin >> n;
  std::cout << Fibonacci(n) << '\n';
  return 0;
}
