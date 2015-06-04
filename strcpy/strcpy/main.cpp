//
//  main.cpp
//  strcpy
//
//  Created by Yuanfeng Wang on 4/18/13.
//  Copyright (c) 2013 Yuanfeng Wang. All rights reserved.
//

#include <iostream>
using namespace std;

int main()
{

    // insert code here...
    char string[32] = "hello, world";
    char* pstr1 = "hello, new world";;
    cout << (pstr1)<<endl;
    cout<< strlen(string) <<endl;
    pstr1 = strcpy(pstr1, string);
    cout << (pstr1)<<endl;
    return 0;
}

char* strcpy(char * pstr1, const char * pstr2)
{
    pstr1 = new char[strlen(pstr2)];
    while (*(pstr2) !='/0'){
        *(++pstr1) = *(++pstr2)
    }
    //for (int i=0 ; i<strlen(pstr2); ++i) pstr1[i] = pstr2[i];
    return pstr1;
}