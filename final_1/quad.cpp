#include <iostream>
#include <math.h>

int a1 = 3;
int b1 = 7;
int c1 = 2;
int a2 = 4;
int b2 = 8;
int c2 = 9;

int discrim(int a, int b, int c){
  int out = b*b - (4*a*c);
  return out;
}


double quadsolve(int a, int b, int c){
  int d = discrim(a,b,c);
  if(d >= 0){
    double z = (sqrt(d) - b)/(2*a);
    return z;
  }
  else{
    return 0;
  }
}


int main(){
  std::cout << "a = " << a1 << "\nb = " << b1 << "\nc = " << c1 << std::endl;
  int d1 = discrim(a1,b1,c1);
  std::cout << "Discriminant = " << d1 << std::endl;
  double root1 = quadsolve(a1,b1,c1);
  std::cout << "Root = " << root1 << std::endl;

  std::cout << "********************" << std::endl;

  std::cout << "a = " << a2 << "\nb = " << b2 << "\nc = " << c2 << std::endl;
  int d2 = discrim(a2,b2,c2);
  std::cout << "Discriminant = " << d2 << std::endl;
  double root2 = quadsolve(a2,b2,c2);
  std::cout << "Root = " << root2 << std::endl;

  return 0;
}





