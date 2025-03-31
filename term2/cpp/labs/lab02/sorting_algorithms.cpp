#include <iostream>
#include <vector>
#include <chrono>

using namespace std;

void ForwardStep(vector<unsigned>& arr, unsigned begin_idx, unsigned end_idx) {
  for (unsigned i = begin_idx; i < end_idx; ++i) {
    if (arr[i] > arr[i + 1]) {
      swap(arr[i], arr[i + 1]);
    }
  }
}

void BackwardStep(vector<unsigned>& arr, unsigned begin_idx, unsigned end_idx) {
  for (unsigned i = end_idx; i > begin_idx; --i) {
    if (arr[i] < arr[i - 1]) {
      swap(arr[i], arr[i - 1]);
    }
  }
}

void ShakerSort(vector<unsigned>& arr, unsigned begin_idx, unsigned end_idx) {
  while (begin_idx < end_idx) {
    ForwardStep(arr, begin_idx, end_idx);
    --end_idx;
    BackwardStep(arr, begin_idx, end_idx);
    ++begin_idx;
  }
}

// Функция проверки порядка элементов с заданным шагом для сортировки расчёской
bool CombPass(vector<unsigned>& arr, int gap) {
  bool swapped = false;
  for (size_t i = 0; i + gap < arr.size(); ++i) {
    if (arr[i] > arr[i + gap]) {
      swap(arr[i], arr[i + gap]);
      swapped = true;
    }
  }
  return swapped;
}

// Сортировка расчёской
void CombSort(vector<unsigned>& arr) {
  int gap = arr.size();
  const double shrink = 1.3;
  bool swapped = true;
  while (gap > 1 || swapped) {
    if (gap > 1) gap /= shrink;
    swapped = CombPass(arr, gap);
  }
}

// Сортировка Шелла
void ShellSort(vector<unsigned>& arr, vector<int> gaps) {
  for (int gap : gaps) {
    for (size_t i = gap; i < arr.size(); ++i) {
      unsigned temp = arr[i];
      size_t j;
      for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
        arr[j] = arr[j - gap];
      }
      arr[j] = temp;
    }
  }
}

vector<int> GenerateHibbardGaps(int n) {
  vector<int> gaps;
  for (int i = 1; (1 << i) - 1 <= n; ++i) {
    gaps.insert(gaps.begin(), (1 << i) - 1);
  }
  return gaps;
}

vector<int> GenerateFibonacciGaps(int n) {
  vector<int> gaps;
  int a = 1, b = 1;
  while (b <= n) {
    gaps.insert(gaps.begin(), b);
    int temp = a + b;
    a = b;
    b = temp;
  }
  return gaps;
}

int main() {
  return 0;
}
