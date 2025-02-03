#include <iostream>

bool PrimeNumber (int n) { 
  bool prime_number = true;
  for (int i = 2; i * i < n + 1; ++i) { 
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

int main() { 
  int n;
  std::cin >> n;
  std::cout << PrimeNumber(n) << '\n';
  return 0;
}
