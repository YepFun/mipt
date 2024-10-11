#include <iostream>

int main() {
  int x = 5;
  int y = 7;
  char c = 'a';
  std::cout << &x << ' ' << &y << '\n'; // Adress of variable
  // при разных запусках программы значения будут различными — мы не обязаны выделять один и тот же объем памяти
  int* p = &x;
  std::cout << p << ' ' << *p << '\n';
  // p += n  n * sizeof(T) 
  // int - 4 double - 8
  p += 5; // += 20 численно
  
  --p;

  // указатель с числом сложить можно, два указателя нельзя

  std::cout << *p; // Dereference (Разименование) — возвращает указателю то, что под ним
  // Undefined Behaiviour — компилятор не обязан записывать числа в соседние куски памяти

  int x = 5;
  int y = 7;

  int* p = &x;
  ++p;

  *p = 7;

  int** pp = &p;
  // &: T -> T*
  std::cout << &y << " " << pp << '\n';
  return 0;
}