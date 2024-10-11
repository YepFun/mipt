#include <fstream>
#include <iomanip>
#include <iostream>

const int cPrecision = 10;
const long double cValueAccuracy = 1e-10;

long double F(long double x, int a, int b, int c, int d) {
  return a * x * x * x + b * x * x + c * x + d;
}

long double FindRoot(int a, int b, int c, int d) {
  const long double cLeftBorder = -1000000000.0L;
  const long double cRightBorder = 1000000000.0L;
  long double left = cLeftBorder;
  long double right = cRightBorder;
  long double m;
  while (right - left > cValueAccuracy) {
    m = (left + right) / 2;
    if (F(m, a, b, c, d) == 0) {
      return m;
    }
    if (F(left, a, b, c, d) * F(m, a, b, c, d) < 0) {
      right = m;
    } else {
      left = m;
    }
  }
  return (left + right) / 2;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cout.tie(0);
  std::ifstream cin("input.txt");
  std::ofstream cout("output.txt");
  int a;
  int b;
  int c;
  int d;
  cin >> a >> b >> c >> d;
  double result = FindRoot(a, b, c, d);
  cout << std::fixed << std::setprecision(cPrecision) << result << '\n';
  return 0;
}
