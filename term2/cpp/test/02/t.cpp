#include <iostream>
#include <cstdint>

uint64_t gcd(uint64_t a, uint64_t b) {
  if (b == 0) {
    return a;
  }
  return gcd(b, a % b);
}

uint64_t lcm(uint64_t a, uint64_t b) {
    return a / gcd(a, b) * b;
}

unsigned long long digit_sum(unsigned long long a) {
  unsigned long long sum = 0;
  while(a != 0) {
    sum += a % 10;
    a /= 10;
  }
  return sum;
}

unsigned long long redux(unsigned long long a) {
  unsigned long long t = a;
  while (digit_sum(t) > 9) {
    t = digit_sum(t);
  }
  return digit_sum(t);
}

unsigned long long collatz_conjecture_count(unsigned long long a) {
    unsigned long long cnt = 0;
    while (a > 1) {
      if (a % 2 == 0) {
        a /= 2;
      } else {
        a = 3 * a + 1;
      }
      ++cnt;
    }
    return cnt;
}

bool is_powerof2(uint64_t a) {
  while (a > 0) {
    if (a % 2 != 0 && a != 1) {
      return false;
    }
  }
  return true;
}

uint64_t align(uint64_t U, uint8_t P) {
    if (U == 0) {
        return 0; 
    }
    uint64_t factor = 1 << P; 
    uint64_t result = (U + factor - 1) / factor * factor; 
    return result;
}

uint64_t count_bits(uint64_t number) {
    uint64_t count = 0;
    while (number) {
        count += number & 1;   
        number >>= 1;           
    }
    return count;
}

uint64_t align(uint64_t U, uint8_t P) {
    if (U == 0) {
        return 0;
    }
    uint64_t powerOfTwo = 1ULL << P;
    uint64_t W = (U + powerOfTwo - 1) / powerOfTwo * powerOfTwo;
    if (W < U) {
        return UINT64_MAX; 
    }
    return W;
}

int main() {
  uint64_t a = 12;
  uint64_t b = 18;
  std::cout << '\n';
  return 0;
}


