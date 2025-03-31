#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <fstream>
#include <functional>

long long MeasureTime(std::function<void(std::vector<int>&)> SortFunction, std::vector<int>& arr, int cIterations) {
  long long average_time = 0;
  for (int i = 0; i < cIterations; ++i) {
    auto begin = std::chrono::steady_clock::now();
    for (unsigned cnt = 5; cnt != 0; --cnt) {
      SortFunction(arr);
    }
    auto end = std::chrono::steady_clock::now();
    average_time += std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count();
  }
  return average_time / cIterations;
}

std::vector<int> GenerateRandomVector(int size) {
  int random_values[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  unsigned seed = 1001;
  std::default_random_engine rng(seed);
  std::uniform_int_distribution<unsigned> random_distribution(0, 9);
  std::vector<int> arr(size);
  for (int i = 0; i < size; ++i) {
    arr[i] = random_values[random_distribution(rng)];
  }
  return arr;
}

void BubbleSort(std::vector<int>& arr, long long& swaps) {
  swaps = 0;
  bool swapped;
  for (size_t i = 0; i < arr.size(); ++i) {
    swapped = false;
    for (size_t j = 0; j + 1 < arr.size() - i; ++j) {
      if (arr[j] > arr[j + 1]) {
          std::swap(arr[j], arr[j + 1]);
          swaps++;
          swapped = true;
      }
    }
    if (!swapped) {
      break; 
    }
  }
}

void ForwardStep(std::vector<int>& arr, unsigned begin_idx, unsigned end_idx, long long& swaps) {
  for (unsigned i = begin_idx; i < end_idx; ++i) {
    if (arr[i] > arr[i + 1]) {
      std::swap(arr[i], arr[i + 1]);
      swaps++;
    }
  }
}

void BackwardStep(std::vector<int>& arr, unsigned begin_idx, unsigned end_idx, long long& swaps) {
  for (unsigned i = end_idx; i > begin_idx; --i) {
    if (arr[i] < arr[i - 1]) {
      std::swap(arr[i], arr[i - 1]);
      swaps++;
    }
  }
}

void ShakerSort(std::vector<int>& arr, unsigned begin_idx, unsigned end_idx, long long& swaps) {
  while (begin_idx < end_idx) {
    ForwardStep(arr, begin_idx, end_idx, swaps);
    --end_idx;
    BackwardStep(arr, begin_idx, end_idx, swaps);
    ++begin_idx;
  }
}

void CombSort(std::vector<int>& arr, long long& swaps) {
  int gap = arr.size();
  bool swapped = true;
  while (gap > 1 || swapped) {
    gap = std::max(1, (int)(gap / 1.3));
    swapped = false;
    for (size_t i = 0; i + gap < arr.size(); ++i) {
      if (arr[i] > arr[i + gap]) {
        std::swap(arr[i], arr[i + gap]);
        swapped = true;
        swaps++;
      }
    }
  }
}

std::vector<int> GenerateShellGaps(int n) {
  std::vector<int> gaps;
  for (int gap = n; gap > 1; gap /= 2) {
    gaps.push_back(gap);
  }
  gaps.push_back(1);
  return gaps;
}

std::vector<int> GenerateHibbardGaps(int n) {
  std::vector<int> gaps;
  int k = 1;
  while ((1 << k) - 1 <= n) {
    gaps.push_back((1 << k) - 1);
    k++;
  }
  std::reverse(gaps.begin(), gaps.end());
  return gaps;
}

std::vector<int> GenerateReverseFibonacciGaps(int n) {
  std::vector<int> gaps;
  int a = 1, b = 1;
  while (b <= n) {
    gaps.push_back(b);
    int temp = a + b;
    a = b;
    b = temp;
  }
  std::reverse(gaps.begin(), gaps.end());
  return gaps;
}

void ShellSort(std::vector<int>& arr, std::vector<int> gaps, long long& swaps) {
  for (size_t gap : gaps) {
    for (size_t i = gap; i < arr.size(); ++i) {
      int temp = arr[i];
      size_t j;
      for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
        arr[j] = arr[j - gap];
        swaps++;
      }
      arr[j] = temp;
    }
  }
}

void TestSortingAlgorithms() {
  std::ofstream file("data/results.csv");
  file << "Size,CombSortTime,CombSortSwaps,ShakerSortTime,ShakerSortSwaps,ShellSortHibbardTime,ShellSortHibbardSwaps,ShellSortStandardTime,ShellSortStandardSwaps,ShellSortFibTime,ShellSortFibSwaps\n";

  for (size_t size = 1000; size <= 100000; size += 1000) {
    std::vector<int> arr = GenerateRandomVector(size);
    std::vector<int> arr_comb = arr, arr_shaker = arr, arr_shell_hibbard = arr, arr_shell_standard = arr, arr_shell_fib = arr;
    long long swaps_comb, swaps_shaker, swaps_shell_hibbard, swaps_shell_standard, swaps_shell_fib;

    long long comb_sort_time = MeasureTime([&](std::vector<int>& arr) { CombSort(arr, swaps_comb); }, arr_comb, 10);
    long long shaker_sort_time = MeasureTime([&](std::vector<int>& arr) { ShakerSort(arr, 0, arr.size() - 1, swaps_shaker); }, arr_shaker, 10);
    long long shell_sort_hibbard_time = MeasureTime([&](std::vector<int>& arr) { ShellSort(arr, GenerateHibbardGaps(arr.size()), swaps_shell_hibbard); }, arr_shell_hibbard, 10);
    long long shell_sort_standard_time = MeasureTime([&](std::vector<int>& arr) { ShellSort(arr, GenerateShellGaps(arr.size()), swaps_shell_standard); }, arr_shell_standard, 10);
    long long shell_sort_fib_time = MeasureTime([&](std::vector<int>& arr) { ShellSort(arr, GenerateReverseFibonacciGaps(arr.size()), swaps_shell_fib); }, arr_shell_fib, 10);

    file << size << ","
         << comb_sort_time << "," << swaps_comb << ","
         << shaker_sort_time << "," << swaps_shaker << ","
         << shell_sort_hibbard_time << "," << swaps_shell_hibbard << ","
         << shell_sort_standard_time << "," << swaps_shell_standard << ","
         << shell_sort_fib_time << "," << swaps_shell_fib << "\n";

    std::cout << size << ","
              << comb_sort_time << "," << swaps_comb << ","
              << shaker_sort_time << "," << swaps_shaker << ","
              << shell_sort_hibbard_time << "," << swaps_shell_hibbard << ","
              << shell_sort_standard_time << "," << swaps_shell_standard << ","
              << shell_sort_fib_time << "," << swaps_shell_fib << "\n";
  }

  file.close();
}

int main() {
  TestSortingAlgorithms();
  return 0;
}
