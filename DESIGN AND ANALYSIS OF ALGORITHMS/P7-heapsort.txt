PART B
Program 10
“Sunshine” a job search portal is looking for engineering graduates, they need to sort the candidate’s resume based on their ranking(Average Percentage). Ranking should be generated randomly. Design and develop a program in C to sort the resumes by using heap sort algorithm. Determine the time required to sort the elements. Repeat the experiment for different values of n and plot a graph of the time taken versus n.(n=no of elements).
Note : This is only basic program- You have to make modifications to accommodate the problem statement appropriately
#include<stdio.h>
#include<time.h>
#define TRUE
#define FALSE

void heapbottomup(int h[],int n)
{
   	int i,heap,v,j,k;
   	for(i=n/2;i>0;i--)
	{
		k=i;
		v=h[k];
		heap=FALSE;
		while(!heap && (2*k)<=n)
		{
			j=2*k;
			if(j<n)
   	  		if(h[j]<h[j+1])
			j=j+1;
      		if(v>=h[j])
			heap=TRUE;
			else
			{
				h[k]=h[j];
				k=j;
			}
	}
}

void heapsort(int h[],int n)
{    
	int i,temp,last=n;
	if(n<=1)
      return;
     else
   {
		heapbottomup(h,n);
		temp=h[last];
		h[last]=h[1];
		h[1]=temp;
		last--;
      	heapsort(h,n-1);
	}
}


main()
{
// Write driver function here
}
