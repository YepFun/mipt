#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <utility>
#include <vector>

std::vector<std::pair<int, int> > MergeSegments(
    std::vector<std::pair<int, int> >& segments) {
  std::vector<std::pair<int, int> > result;
  int current_left = segments[0].first;
  int current_right = segments[0].second;
  for (size_t i = 0; i < segments.size(); ++i) {
    int left = segments[i].first;
    int right = segments[i].second;
    if (left > current_right) {
      result.push_back({current_left, current_right});
      current_left = left;
      current_right = right;
    } else {
      current_right = std::max(right, current_right);
    }
  }
  result.push_back({current_left, current_right});
  return result;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);
  std::cout.tie(0);
  std::ifstream cin("input.txt");
  std::ofstream cout("output.txt");
  int n;
  cin >> n;
  std::vector<std::pair<int, int> > segments(n);
  for (int i = 0; i < n; ++i) {
    cin >> segments[i].first >> segments[i].second;
  }
  sort(segments.begin(), segments.end());
  std::vector<std::pair<int, int> > result;
  result = MergeSegments(segments);
  cout << result.size() << '\n';
  for (size_t i = 0; i < result.size(); ++i) {
    cout << result[i].first << ' ' << result[i].second << '\n';
  }
  return 0;
}
