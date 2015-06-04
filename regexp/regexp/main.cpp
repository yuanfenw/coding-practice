//
//  main.cpp
//  regexp
//
//  Created by Yuanfeng Wang on 5/3/13.
//  Copyright (c) 2013 Yuanfeng Wang. All rights reserved.
//

#include <iostream>
using namespace std;
bool match(char *first, char * second);

int main(int argc, const char * argv[])
{

    // insert code here...
    std::cout << "Hello, World!\n";
    char str1[] = "h*lo";
    char str2[] = "hello";
    
    if (match(str1, str2)) cout << "matched";
    return 0;
}

bool match(char *first, char * second)
{
    // If we reach at the end of both strings, we are done
    if (*first == '\0' && *second == '\0')
        return true;
    
    // Make sure that the characters after '*' are present in second string.
    // This function assumes that the first string will not contain two
    // consecutive '*'
    if (*first == '*' && *(first+1) != '\0' && *second == '\0')
        return false;
    
    // If the first string contains '?', or current characters of both
    // strings match
    if (*first == '?' || *first == *second)
        return match(first+1, second+1);
    
    // If there is *, then there are two possibilities
    // a) We consider current character of second string
    // b) We ignore current character of second string.
    if (*first == '*')
        return match(first+1, second) || match(first, second+1);
    return false;
}