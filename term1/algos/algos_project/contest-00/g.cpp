#include <fstream>
#include <iomanip>
#include <iostream>

int HowManyTrucks(int n, int k) {
  int box = n;
  if (box <= k) {
    return 1;
  }
  if (box % 2 == 0) {
    return HowManyTrucks(box / 2, k) * 2;
  }
  return HowManyTrucks(box / 2, k) + HowManyTrucks(box / 2 + 1, k);
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cout.tie(0);
  std::ifstream cin("input.txt");
  std::ofstream cout("output.txt");
  int n;
  int k;
  cin >> n >> k;
  cout << HowManyTrucks(n, k) << '\n';
  return 0;
}