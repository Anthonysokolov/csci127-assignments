#include <iostream>

int a = 2;
int b = 12;


int sumofsquares(int a, int b){
  int sum = 0;
  while(a <= b){
    sum += a*a;
    a ++;
  }
  return sum;
}


int main(){
  std::cout << "a = " << a << "\nb = " << b << std::endl;
  int x = sumofsquares(a,b);
  std::cout << "Sum of squares: " << x << std::endl;
  return 0;
}


