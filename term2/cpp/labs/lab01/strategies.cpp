#include <algorithm>
#include <chrono>
#include <fstream>
#include <iostream>
#include <random>
#include <vector>

int F(std::vector<int>& arr, int x) {
  int cnt = 0;
  while (cnt < arr.size() && arr[cnt] != x) {
    ++cnt;
  }
  if (cnt == arr.size()) {
    return -1;
  }
  return cnt;
}

void StrategyA (std::vector<int>& arr, int n, int x) {
  if (F(arr, x) != -1 && arr[0] != x) {
    std::swap(arr[0], arr[F(arr, x)]);
  }
}

void StrategyB (std::vector<int>& arr, int n, int x) {
  if (F(arr, x) != -1 && arr[0] != x) {
    int index = F(arr, x);
    std::swap(arr[index - 1], arr[index]);
  }
}

void StrategyC(std::vector<int>& arr, int n, int x) {
    std::vector<int> cnt(arr.size(), 0);
    int index = F(arr, x);
    if (index != -1) {
        ++cnt[index];
    }
    if (index != -1 && arr[0] != x && arr[index] > arr[0]) {
        std::swap(arr[index], arr[0]);
        std::swap(cnt[index], cnt[0]);
    }
}

int main() {
  int search_values[] = {-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  int random_values[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  const int cIterations = 100;
  const int cMax_size = 25000;
  
  std::ofstream file("data/data_strategy.txt");
  file << "StrategyA StrategyB StrategyC\n";

  for (int size = 10; size < cMax_size; size += 10) {
    int array_size = size;
    unsigned seed = 1001;
    std::default_random_engine rng(seed);
    std::uniform_int_distribution<unsigned> random_distribution(0, 9);

    std::vector<int> data_array(array_size);
    for (int i = 0; i < array_size; ++i) {
      data_array[i] = random_values[random_distribution(rng)];
    }

    file << size << " ";
    std::cout << size << " ";
    
    long long average_time = 0;
    for (int i = 0; i < cIterations; ++i) {
      auto start_time = std::chrono::steady_clock::now();
      for (unsigned cnt = 100000; cnt != 0; --cnt) {
        int target = search_values[random_distribution(rng)];
        StrategyA(data_array, array_size, target);
      }
      auto end_time = std::chrono::steady_clock::now();
      average_time += std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();
    }
    file << average_time / cIterations << " ";
    std::cerr << average_time / cIterations << " ";

    // Strategy B
    for (unsigned i = 0; i < array_size; ++i) {
      data_array[i] = random_values[random_distribution(rng)];
    }
    average_time = 0;
    for (int i = 0; i < cIterations; ++i) {
      auto start_time = std::chrono::steady_clock::now();
      for (unsigned count = 100000; count != 0; --count) {
        int target = search_values[random_distribution(rng)];
        StrategyB(data_array, array_size, target);
      }
      auto end_time = std::chrono::steady_clock::now();
      average_time += std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();
    }
    file << average_time / cIterations << " ";
    std::cout << average_time / cIterations << " ";

    // Strategy C
    for (unsigned i = 0; i < array_size; ++i) {
      data_array[i] = random_values[random_distribution(rng)];
    }
    average_time = 0;
    for (int i = 0; i < cIterations; ++i) {
      auto start_time = std::chrono::steady_clock::now();
      for (unsigned count = 100000; count != 0; --count) {
        int target = search_values[random_distribution(rng)];
        StrategyC(data_array, array_size, target);
      }
      auto end_time = std::chrono::steady_clock::now();
      average_time += std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();
    }
    file << average_time / cIterations << '\n';
    std::cout << average_time / cIterations << '\n';
  }
  file.close();
  return 0;
}
