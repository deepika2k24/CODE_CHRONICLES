#include<stdio.h>
#include<time.h>

int bin_search(int a[],int n,int key);

int main()
{
        int n,i,a[100],key,f;
        double clk;
        clock_t starttime,endtime;

        printf("\n\t\t\t Binary search \n");
        printf("\n Enter number of elements");
        scanf("%d",&n);

        for(i=0;i<n;i++)
	     	a[i]=rand()%100;
	 
	  printf("Enetr the key to be searched:");
	  scanf("%d",&key); 	
        
  	  starttime=clock(); 
 	  f=bin_search(a,n,key);
     	  endtime=clock();
                
        if(f==-1)
           printf("\nThe element %d is not found",key);
        else
           printf("The element %d is found in position %d",key,f);

        clk=(double)(endtime-starttime)/CLOCKS_PER_SEC;
        printf("\nThe run time is %f\n",clk);
 }
  

int bin_search(int a[],int n,int key)
{
int low,mid,high;
low=0, high=n-1;
while(low<=high)
{
	mid=(low+high)/2;
	if(key==a[mid])
	    return(mid);
	else if(key<a[mid])
	    high=mid-1;
      else
	    low=mid+1;
}
return(-1);
}

  
