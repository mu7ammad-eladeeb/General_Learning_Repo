#include<iostream>
#include<windows.h>
using namespace std;
int main()
{
    int hours = 0;
    int min = 0;
    int sec = 0;
    cout<<"hours :"<<endl;
    cin>>hours;
    cout<<"min :"<<endl;
    cin>>min;
    cout<<"sec :"<<endl;
    cin>>sec;
    while(true)
    {
        system("cls"); 
        // cls refers to clear screen. It's used to clear the terminal screen
        if(sec>59)
        {
            min++;
            sec=0;
        }
        if(min>59)
        {
            hours++;
            min=0;
        }
        if(hours>23)
        {
            hours=0;
        }
         cout<<hours<<":"<<min<<":"<<sec<<endl;
         sec++;
        Sleep(1000); 
        // Notice that S is uppercase, It's used to reduce the speed of timer
        // You choose the number between ( )
        // It need the library <windows.h> and it doesn't work on any other online compiler
    }
   
    return 0;
}