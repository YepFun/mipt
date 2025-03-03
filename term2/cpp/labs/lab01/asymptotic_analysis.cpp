#include <chrono>
#include <fstream>
#include <iostream>
#include <random>
#include <vector>

bool LinearSearch(const std::vector<int>& arr, int target) {
  for (int num : arr) {
    if (num == target) {
      return true;
    }
  }
  return false;
}

bool BinarySearch(const std::vector<int>& arr, int target) {
  int left = 0;
  int right = arr.size() - 1;
  while (left <= right) {
    int mid = (left + right) / 2;
    if (arr[mid] == target) {
      return true;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return false;
}

long long MeasureTime (std::function<bool(const std::vector<int>&, int)> SearchFunction, const std::vector<int>& arr, int target, int cIterations) {
  long long average_time = 0;
  for (int i = 0; i < cIterations; ++i) {
    auto begin = std::chrono::steady_clock::now();
    for (unsigned cnt = 100000; cnt != 0; --cnt) {
      SearchFunction(arr, target);
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

/* std::vector<int> GenerateRandomVector(int size) {
  std::vector<int> arr(size);
  // unsigned seed = 1001;
  std::random_device rd; // seed
  std::default_random_engine rng(rd());  
  std::uniform_int_distribution<int> dstr(0, 100);  
  for (int i = 0; i < size; ++i) {
    arr[i] = dstr(rng);  
  }
  return arr;
}*/

std::vector<int> GenerateRandomSortedVector(int size) {
  std::vector<int> arr = GenerateRandomVector(size);
  std::sort(begin(arr), end(arr));
  return arr;
}

bool FindPair(const std::vector<int>& arr, int sum) {
  for (size_t i = 0; i < arr.size(); ++i) {
    for (size_t j = i + 1; j < arr.size(); ++j) {
      if (arr[i] + arr[j] == sum) {
        return true;
      }
    }
  }
  return false;
}

bool FindPairSorted(const std::vector<int>& arr, int sum) {
  int left = 0;
  int right = arr.size() - 1;
  while (left < right) {
    int current_sum = arr[left] + arr[right];
    if (current_sum == sum) {
      return true;
    } else if (current_sum < sum) {
      left++;
    } else {
      right--;
    }
  }
  return false;
}

int main() {
  int search_values[] = {-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  int random_values[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  const int cIterations = 25;
  const int cMax_size = 25000;

  // std::vector<int> sizes = {100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000}; 

  std::ofstream file_search("data/data_search.txt");
  file_search << "N Linear_Avg Linear_Worst Binary_Avg Binary_Worst\n";
  
  // for (int size : sizes) {  
  /* for (int size = 100; size < cMax_size; size += 100) {
    std::vector<int> arr = GenerateRandomVector(size);
    std::vector<int> sorted_arr = GenerateRandomSortedVector(size);

    std::random_device rd; // seed
    std::default_random_engine gen(rd());  
    std::uniform_int_distribution<int> dstr(0, size - 1);

    long long linear_avg_time = MeasureTime(LinearSearch, arr, arr[dstr(gen)], cIterations);
    long long binary_avg_time = MeasureTime(BinarySearch, sorted_arr, sorted_arr[dstr(gen)], cIterations);

    int target = -1; 
    long long linear_worst_time = MeasureTime(LinearSearch, arr, target, cIterations);
    long long binary_worst_time = MeasureTime(BinarySearch, sorted_arr, target, cIterations);

    std::cerr << size << " " << linear_avg_time << " " << linear_worst_time << " " << binary_avg_time << " " << binary_worst_time << "\n"; 

    file_search << size << " " << linear_avg_time << " " << linear_worst_time << " " << binary_avg_time << " " << binary_worst_time << "\n";
  }
  file_search.close();
  */

  std::ofstream file_pair("data/data_pair.txt");
  file_pair << "N FindPair_Avg FindPair_Worst FindPairSorted_Avg FindPairSorted_Worst\n";
  
  for (int size = 5; size < cMax_size; size += 5) {
    // std::cout << "Size: " << size << '\n';
    std::vector<int> arr = GenerateRandomVector(size);
    std::vector<int> sorted_arr = GenerateRandomSortedVector(size);

    std::random_device rd; // seed
    std::default_random_engine gen(rd());  
    std::uniform_int_distribution<int> dstr(0, size - 1);

    long long find_pair_avg_time = MeasureTime(FindPair, arr, arr[dstr(gen)] + arr[dstr(gen)], cIterations);
    long long find_pair_sorted_avg_time = MeasureTime(FindPairSorted, sorted_arr, sorted_arr[dstr(gen)] + sorted_arr[dstr(gen)], cIterations);

    int target = -1; 
    long long find_pair_worst_time = MeasureTime(FindPair, arr, target, cIterations);
    long long find_pair_sorted_worst_time = MeasureTime(FindPairSorted, sorted_arr, target, cIterations);

    std::cerr << size << " " << find_pair_avg_time << " " << find_pair_worst_time << " " << find_pair_sorted_avg_time << " " << find_pair_sorted_worst_time << "\n";

    file_pair << size << " " << find_pair_avg_time << " " << find_pair_worst_time << " " << find_pair_sorted_avg_time << " " << find_pair_sorted_worst_time << "\n";
  }
  file_pair.close();

  return 0;
}

