//Program 8
// Horspool  program for pattern mathching

#include<stdio.h>
#include<string.h>
#define MAX 500
int t[MAX];
void shifttable(char p[])
{
 	int i,j,m;
	m=strlen(p);
 	for(i=0;i<MAX;i++)
 		 t[i]=m;
 	for(j=0;j<m-1;j++)
 		t[p[j]]=m-1-j;
}


int horspool(char txt[],char p[])
{
	 int i,j,k,m,n;
	 n=strlen(txt);
	 m=strlen(p);
	 printf("\nLength of text=%d",n);
	 printf("\n Length of pattern=%d",m);
	 i=m-1;
 	while(i<n)
 	{
 		k=0;
 		while((k<m)&&(p[m-1-k]==txt[i-k]))
  			k++;
  		if(k==m)
 			return(i-m+1);
  		else
  			i+=t[txt[i]];
 	}
	return(-1);
}


void main()
{
 	char txt[100],p[100];
 	int pos;
 	//clrscr();
 	printf("Enter the text in which pattern is to be searched:\n");
 	gets(txt);   //Replace this with scanf if gets does not work
 	printf("Enter the pattern to be searched:\n");
 	gets(p);   //Replace this with scanf if gets does not work
 	shifttable(p);
 	pos=horspool(txt,p);
 	if(pos>=0)
 		 printf("\n The desired pattern was found starting from position %d",pos+1);
	 else
 		 printf("\n The pattern was not found in the given text");
}
