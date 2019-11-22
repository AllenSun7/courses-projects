#include <math.h>
#include <iostream>
using namespace std;
//compile and run c++
// g++ filename.cpp
// ./a.out

double urn(void) {return double(rand())/RAND_MAX;}

double ANDNESS(double (*F)(double, double))
{
    int Total=1000000, Below, i ;
    for(Below=i=0; i<Total; i++)
        if(urn() < F(urn(), urn())) Below++;
    return 2.- Below*3.0/Total;
}

double A2(double a, double b) {return (a+b)/2.;}
double G2(double a, double b) {return sqrt(a*b);}
double PM2(double a, double b) 
{
    double r = -0.860138; 
    return pow(((pow(a,r)+pow(b,r))/2), 1/r);
}

int main(void)
{
    cout << "A: " << ANDNESS(A2) << "\n";
    cout << "G: " << ANDNESS(G2) << "\n";
    cout << "PM: " << ANDNESS(PM2) << "\n";
    return 0;
}


