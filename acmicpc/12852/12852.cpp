#include <cstdio>
int d[1000001],p[1000001];
// d[n] = d[n-1]+1 or d[n/2]+1 or d[n/3]+1
// p[n] = n-1 or n/2 or n/3
int main(){
  int k;
  scanf("%d",&k);
  d[1]=0;
  for(int n=2;n<=k;n++){
    d[n]=d[n-1]+1;
    p[n]=n-1;
    if(n%2==0){
      if(d[n]>d[n/2]+1){
        d[n]=d[n/2]+1;
        p[n]=n/2;
      }
    }
    if(n%3==0){
      if(d[n]>d[n/3]+1){
        d[n]=d[n/3]+1;
        p[n]=n/3;
      }
    }
  }
  printf("%d\n",d[k]);
  while(k>0){
    printf("%d ",k);
    k=p[k];
  }
}
