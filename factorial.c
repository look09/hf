#include <stdio.h>


int times;
int answer[times];
void factorial(int number){
	int i,tempAnswer=1;
 printf("Enter a number: ");    
  scanf("%d",&number);    
    for(i=1;i<=number;i++){    
      tempAnswer=tempAnswer*i;
		answer[i] = tempAnswer;
  }    
}

int main(){
	int i, number;
	scanf("%d", &times);
	for(i=0;i<=times;i++){
		scanf("%d", &number);
		factorial(number);
	}
	
	for(i=0;i<=times;i++){
		printf("%d", answer[i]);
	}
	return 0;
}
