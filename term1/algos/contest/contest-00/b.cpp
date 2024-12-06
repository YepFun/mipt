#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

const int cPrecision = 10;
const long double cZero = 0.0L;

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cout.tie(0);
  std::ifstream cin("input.txt");
  std::ofstream cout("output.txt");
  int n;
  cin >> n;
  std::vector<long double> a(n);
  std::vector<long double> ln_a(n);
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    ln_a[i] = log(a[i]);
  }
  std::vector<long double> ln_sum(n);
  ln_sum[0] = ln_a[0];
  for (int i = 1; i < n; ++i) {
    ln_sum[i] = ln_sum[i - 1] + ln_a[i];
  }
  int q;
  cin >> q;
  for (int i = 0; i < q; ++i) {
    int l;
    int r;
    cin >> l >> r;
    long double ln_sum_l;
    if (l > 0) {
      ln_sum_l = ln_sum[l - 1];
    } else {
      ln_sum_l = cZero;
    }
    long double final_ln_sum = ln_sum[r] - ln_sum_l;
    long double result = exp(final_ln_sum / (r - l + 1));
    cout << std::fixed << std::setprecision(cPrecision) << result << '\n';
  }
  return 0;
}
