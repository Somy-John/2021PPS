#include <stdio.h>

int main(void) {
  int k,n,h,i,j,sum,num;// k층 n 호
  int tmp[15];
  scanf(" %d",&num);
  for(h=0;h<num;h++){
    scanf(" %d %d",&k,&n);
    for(i=1;i<=n;i++){
      for(j=0;j<=k;j++){
        if(i==1) tmp[j]=1;
        else if(j==0) tmp[j] = i;
        else{
          tmp[j] = tmp[j-1]+tmp[j];
        }
      }
    }
    sum = tmp[k];
    printf("%d\n",sum);
  }
  return 0;
}