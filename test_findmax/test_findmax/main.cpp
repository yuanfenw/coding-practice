//
//  main.cpp
//  test_findmax
//
//  Created by Yuanfeng Wang on 3/21/13.
//  Copyright (c) 2013 Yuanfeng Wang. All rights reserved.
//

#include <iostream>
#include <deque>
#include <string>
using namespace std;

void maxInWindow(int* arr, int k)
{
    std::deque<int> Qi(k);
    std::cout<< "size of pointer:"<<sizeof(arr)<<std::endl;
    int i;
    for(i = 0; i < k; i++)
    {
        while(!Qi.empty() && arr[i] >= arr[Qi.back()])
        {
            Qi.pop_back();
        }
        Qi.push_back(i);
    }
    
    for( ; i < sizeof(arr); i++)
    {
        std::cout << arr[Qi.front()] << std::endl;
        while(!Qi.empty() && i - k >= Qi.front())
        {
            }
        
        while(!Qi.empty() && arr[i] >= arr[Qi.back()])
        {
            Qi.pop_back();
        }
        Qi.push_back(i);
    }
    std::cout << arr[Qi.front()] << std::endl;
}

string IntToString(int a){
    string b = "";
    while(a){
        b += a%10+'0';
        a /= 10;
    }
    return b;
}

int main(){
    //int a[] = {3,4,5,6,8, 7 ,9};
    //int k = 3;
   // maxInWindow(a,k);
    
    int a = -1093;
    string b = IntToString(a);
    std::cout <<b;
    
    
}