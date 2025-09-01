#include<stdio.h>
#include<time.h>
void dfs(int n, int a[10][10], int u, int t[10][10], int visited[10]);
int main()
{
        int n,i,j,u,a[10][10],visited[10],t[10][10];
        double clk;
        clock_t starttime,endtime;
        printf("\n\t\t\t DEPTH FIRST SEARCH \n");
        printf("\n Enter number of vertices:");
        scanf("%d",&n);
        printf("\n Enter the adjacency matrix (Enter 0/1)\n");
	    for(i=0;i<n;i++)
	     for(j=0;j<n;j++)
	    	scanf("%d",&a[i][j]);
	   	printf("\n Enter the source vertex:");
        scanf("%d",&u);
    	for(i=0;i<n;i++)
       {	
          	visited[i]=0;
       }
       dfs(n,a,u,t,visited);
       for(i=0;i<n;i++)  
            if(visited[i]==1)
                 printf("%d is reachable",i);
            else
                printf("%d is not reachable",i);
                
                printf("DFS traversal : Edges visited\n");
                for(i=0;i<n-1;i++)
                printf("%d %d\n",t[i][0],t[i][1]);
                
       
}

void dfs(int n, int a[10][10], int u, int t[10][10], int visited[10])
{
    int v;
    static int k=0;
    visited[u]=1;
    for(v=0;v<n;v++)
    {
        if(a[u][v]==1 && visited[v]==0)
        {
         t[k][0]=u;
         t[k][1]=v;
         k++;
         dfs(n,a,v, t, visited);
        }
    }
}
