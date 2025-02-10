#include <iostream>
#include <cmath>

double f(double x) {
  return cos(x) - x;
}
double df(double x) {
  return - sin(x) - 1;
}
double bisection_method(double a, double b) {
  int iterations = 0;
  while (fabs(a - b) > 1e-5) {
    double m = (a + b) / 2.0;
    if (f(a) * f(m) < 0) {
      b = m;
    } else {
      a = m;
    }
  }
  return a;
  std::cout << "Number of iterations (bisection method): " << iterations << '\n';
}
/* double Newtons_method(double a, double b) {

} */

int main() {
  double a = 0.0;
  double b = 1.0;
  std::cout << bisection_method(a, b) << '\n';
  // std::cout << Newtons_method(a, b) << '\n';
  return 0;
}