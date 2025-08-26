/* 

Dictionary can be implemented using binary search tree.  A binary search tree is a binary tree such that each node stores a key of a dictionary. Key 'k' of a node is always greater than the keys present in its left sub tree. Similarly, key 'k' of a node is always lesser than the keys present in its right sub tree.
Design, Develop and Implement a menu driven Program in C  to perform the  following operations using  Binary Search Tree (BST).
a.	Create a dictionary of words 
b.	Traverse the dictionary  in Inorder, Preorder and Post Order
c.	Search the dictionary for a given word (KEY) and display the appropriate message
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct node
{
char  info[20];
struct node *left;
struct node *right;
};

typedef struct node *NODEPTR;
NODEPTR maketree(char word[]);
NODEPTR createtree(char word[]);
void setleft(NODEPTR p,char word[]);
void setright(NODEPTR p,char word[]);
void intrav(NODEPTR p);
void pretrav(NODEPTR p);
void posttrav(NODEPTR p);
void search(NODEPTR p,char key[]);


void main()
{
	NODEPTR ptree;
	NODEPTR p,q;
	char word[20],key[20];
	int opt,f;
        do{

	printf("\n1->CREATE DICTIONARY  2->TRAVERSE 3->SEARCH  4->EXIT ");
	printf("\nEnter your option:");
	scanf("%d",& opt);
	switch(opt)
	{
	case 1: printf("\nEnter a word :");
	        scanf("%s",word);
	        ptree=maketree(word);
		while(strcmp(word,"END")!=0)
		{
			printf("\nEnter a word(Type END to stop):");
			scanf("%s",word);
			if(strcmp(word,"END")==0)
			break;
			p=q=ptree;
			while((strcmp(word,p->info)!=0)  && q!=NULL)
			{
				p=q;
				if(strcmp(word,p->info)<0)
					q=p->left;
				else
					q=p->right;
			}
		if(strcmp(word,p->info)<0)
			setleft(p,word);
		else if(strcmp(word,p->info)>=0)
			setright(p,word);
		}
		printf("\n DICTIONARY CREATED SUCCESSFULLY");
		break;
	case 2 : printf("\n PREORDER TRAVERSAL OF THE DICTIONARY IS:");
		pretrav(ptree);
                
		printf("\n INORDER TRAVERSAL OF THE DICTIONARY IS:");
		intrav(ptree);
	
		printf("\n POSTORDER TRAVERSAL OF THE DICTIONARY IS:");
		posttrav(ptree);
		break;
	case 3: printf("\n Enter the key to search in the dictionary:");
		scanf("%s",key);
		search(ptree,key);
		//if(f==-1)
		//	printf("\n Key %s is not found in the dictionary");
		//else
		//	printf("\n Key %s is found in the dictionary");
        break;
	case 4: printf("\nEXITING BINARY TREE");
		exit(1);
	}
        }while(opt!=4);

}
NODEPTR maketree(char w[])
{
	NODEPTR t;
	t=(NODEPTR)malloc(sizeof(struct node));
	if(t==NULL)
	{
		printf("\n Node allocation failed");
		exit(0);
	}
		strcpy(t->info,w);
		t->left=NULL;
		t->right=NULL;
		return(t);
}

void setleft(NODEPTR p,char w[])
{
	if(p==NULL)
		printf("Void Insertion");
	else if(p->left!=NULL)
		printf("Invalid Insertion");
	else
		p->left=maketree(w);
}

void setright(NODEPTR p,char w[])
{
	if(p==NULL)
		printf("Void Insertion");
	else if(p->right!=NULL)
		printf("Invalid Insertion");
	else
		p->right=maketree(w);
}

void intrav(NODEPTR tree)
{
	if(tree!=NULL)
	{
		intrav(tree->left);
		printf("%s\t",tree->info);
		intrav(tree->right);
	}
}

void pretrav(NODEPTR tree)
{
	if(tree!=NULL)
	{
		printf("%s\t",tree->info);
		pretrav(tree->left);
		pretrav(tree->right);
	}
}

void posttrav(NODEPTR tree)
{
	if(tree!=NULL)
	{
		posttrav(tree->left);
		posttrav(tree->right);
		printf("%s\t",tree->info);
	}
}

void search(NODEPTR tree,char key[])
{
 NODEPTR p,q;
 p=q=tree;
 while((strcmp(key,p->info)!=0)  && q!=NULL)
   {
	p=q;
	if(strcmp(key,p->info)<0)
		q=p->left;
	else
		q=p->right;
   }
     if(strcmp(key,p->info)==0)
	printf("\n Key %s is found in the dictionary",key);
    else
	printf("\n Key %s is not found in the dictionary",key);
}

/*Sample output


1->CREATE DICTIONARY  2->TRAVERSE 3->SEARCH  4->EXIT 
Enter your option:1  

Enter a word :table

Enter a word(Type END to stop):chair

Enter a word(Type END to stop):lamp

Enter a word(Type END to stop):laptop

Enter a word(Type END to stop):mouse

Enter a word(Type END to stop):keyboard

Enter a word(Type END to stop):vase

Enter a word(Type END to stop):water

Enter a word(Type END to stop):cup

Enter a word(Type END to stop):steel

Enter a word(Type END to stop):umbrella

Enter a word(Type END to stop):van

Enter a word(Type END to stop):END

 DICTIONARY CREATED SUCCESSFULLY
1->CREATE DICTIONARY  2->TRAVERSE 3->SEARCH  4->EXIT 
Enter your option:2

 PREORDER TRAVERSAL OF THE DICTIONARY IS:
table  chair   lamp    keyboard        cup     laptop  mouse   steel   vase      umbrella        van     water

 INORDER TRAVERSAL OF THE DICTIONARY IS:
chair   cup     keyboard        lamp    laptop  mouse   steel   table   umbrella  van     vase    water

 POSTORDER TRAVERSAL OF THE DICTIONARY IS:
cup   keyboard        steel   mouse   laptop  lamp    chair   van     umbrella  water   vase    table

1->CREATE DICTIONARY  2->TRAVERSE 3->SEARCH  4->EXIT 
Enter your option:3

 Enter the key to search in the dictionary:mouse

 Key mouse is found in the dictionary
1->CREATE DICTIONARY  2->TRAVERSE 3->SEARCH  4->EXIT 
Enter your option:3

 Enter the key to search in the dictionary:cable

 Key cable is not found in the dictionary
1->CREATE DICTIONARY  2->TRAVERSE 3->SEARCH  4->EXIT 
Enter your option:END
*/