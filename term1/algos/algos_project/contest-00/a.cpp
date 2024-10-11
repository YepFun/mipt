#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cout.tie(0);
  std::ifstream cin("input.txt");
  std::ofstream cout("output.txt");
  int n;
  cin >> n;
  std::vector<int> a(n);
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  std::vector<int> min_left(n);
  min_left[0] = a[0];
  for (int i = 1; i < n; ++i) {
    min_left[i] = (min_left[i - 1] < a[i]) ? min_left[i - 1] : a[i];
  }
  std::vector<int> min_right(n);
  min_right[n - 1] = a[n - 1];
  for (int i = n - 2; i >= 0; --i) {
    min_right[i] = (min_right[i + 1] < a[i]) ? min_right[i + 1] : a[i];
  }
  int q;
  cin >> q;
  for (int i = 0; i < q; ++i) {
    int l;
    int r;
    cin >> l >> r;
    int result = (min_left[l - 1] < min_right[r - 1]) ? min_left[l - 1]
                                                      : min_right[r - 1];
    cout << result << '\n';
  }
  cin.close();
  cout.close();
  return 0;
}
