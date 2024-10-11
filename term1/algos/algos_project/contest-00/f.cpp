#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cout.tie(0);
  std::ifstream cin("input.txt");
  std::ofstream cout("output.txt");
  int n;
  int m;
  int l;
  cin >> n >> m >> l;
  std::vector<std::vector<int> > a(n);
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < l; ++j) {
      int x;
      cin >> x;
      a[i].push_back(x);
    }
  }
  std::vector<std::vector<int> > b(m);
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < l; ++j) {
      int x;
      cin >> x;
      b[i].push_back(x);
    }
  }
  int q;
  cin >> q;
  for (int w = 0; w < q; ++w) {
    int i;
    int j;
    cin >> i >> j;
    --i;
    --j;
    int min_max = std::max(a[i][0], b[j][0]);
    int min_max_k = 0;
    for (int k = 1; k < l; ++k) {
      if (std::max(a[i][k], b[j][k]) < min_max) {
        min_max = std::max(a[i][k], b[j][k]);
        min_max_k = k;
      }
    }
    min_max_k++;
    cout << min_max_k << '\n';
  }
}