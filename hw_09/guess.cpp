#include <iostream>
#include <stdlib.h>
#include <ctime>

int main(){
  int x;
  int guess = 50;
  int high = 100;
  int low = 0;
  int max = 100;
  int res;
  int range;
  bool loop = 1;

  srand(time(NULL));  

  std::cout << "Please enter a number between 0 and 99: ";
  std::cin >> x;

  while(loop == 1){
    guess = rand() % max + low;
    std::cout << "Is " << guess << " your number?: ";
    std::cin >> res;
    if(res == 0){
      loop = 0;
      }
    else if(res == 1){
      low = guess + 1;
      }
    else if(res == -1){
      high = guess;
      }
    max = high - low;
  }  
  std::cout << "Your number is " << guess << std::endl;
  return 0;
} 

