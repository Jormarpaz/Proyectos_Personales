#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}person;



int main(void)
{

    person people[3];

    people[0].name = "Carter";
    people[0].number = "+3463005088";

    people[1].name = "David";
    people[1].number = "+34699230923";

    people[2].name = "John";
    people[2].number = "+34628931567";

    string name = get_string("Name: ");
    for (int i = 0; i <3; i++)
    {
        if (strcmp(people[i].name,name)==0)
        {
            printf("Found %s\n",people[i].number);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;

}
