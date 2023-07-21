#include <stdio.h>

int fibonacci(int x){
	if (x <= 1){
        	return x;
    	}else {
    		return fibonacci(x-1) + fibonacci(x - 2);
    	}
}

int solve() { 
	int sum = 0;
	int value = 0;
	int counter = 0;
	while (value < 4000000){	
		value = fibonacci(counter);
		if (value % 2 == 0) {
			sum += value;
		}
		counter++;
	}
	return sum;
}

int main(){
	printf("%d\n", solve());
}

		
