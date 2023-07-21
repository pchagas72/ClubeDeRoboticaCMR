#include <stdio.h>

int solve(int limit) {

  int multiples_sum = 0;
  for (int i = 0; i < limit; i++){
    if (i % 3 ==0 || i % 5 == 0){
      multiples_sum++;
      }
  }
  return multiples_sum;
}

int main(){

  int solution = solve(1000);
  printf("%d\n", solution);
  return 0;
}
