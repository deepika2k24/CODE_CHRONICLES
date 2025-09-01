#include<stdio.h>
  
int count,w[10],d,x[10];
  
void subset(int cs,int k,int r)
{
   int i;
   x[k]=1;
   if((cs+w[k])==d)
    {
       printf("\n Subset solution = %d\n",++count);
       for(i=0; i<=k; i++)
       {
         if(x[i]==1)
         printf("%d\n",w[i]);
       }
     }
  else if(cs+w[k]+w[k+1] <=d)
        subset(cs+w[k],k+1,r-w[k]);
    if((cs+r-w[k]>=d)&&(cs+w[k+1])<=d)
    {               
      x[k]=0;
      subset(cs,k+1,r-w[k]);
    }
}
  
int main()
{
    int sum=0,i,n;
    printf("enter no of elements\n");
    scanf("%d",&n);
    printf("Enter the elements in ascending order\n");
    for(i=0; i<n; i++)
    scanf("%d",&w[i]);
    printf("Enter the required sum\n");
    scanf("%d",&d);
    for(i=0; i<n; i++)
    sum +=w[i];
 if(sum < d)
    {
        printf("no solution exits\n");
          
    }   
    printf("The solution is\n");
    count =0;
    subset(0,0,sum);
    return 0;

}


/* Sample output 1
enter no of elements
4
Enter the elements in ascending order
1 2 3 4
Enter the required sum
7
The solution is

 Subset solution = 1
1
2
4

 Subset solution = 2
3
4


Sample output 2
enter no of elements
4
Enter the elements in ascending order
3 5 6 7
Enter the required sum
15
The solution is

 Subset solution = 1
3
5
7

*/
