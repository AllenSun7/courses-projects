# -*- coding: utf-8 -*-
import math

def andness_geo (n):
    #calculator geometric mean andness for various value of n
    #ag = (n/(n-1))-(n+1)/(n-1) * (n/(n+1))^n
    total = 1000000000000000
    ag = (n/(n-1)) - (n+1)/(n-1) * (n/(n+1))**n
    ag_total = (total/(total-1)) - (total+1)/(total-1) * (total/(total+1))**total
    print("ag[G;%.2f] = %.8f" %(n, ag))
    print("ag[G;%.2f] = %.8f" %(total, ag_total))
    print("ag[G;%.2f]/ag[G;%d] = %.8f" %(n, total, ag/ag_total))
    return 

def andness_indicator(n, total):
    pass

def weight_geo(n):
    #calculator geometric mean weights for various value of n
    #wg = (n+1)/(n-1) * (n/(n+1))^n - (1/(n-1))
    wg = (n+1)/(n-1) * (n/(n+1))**n - (1/(n-1))
    print("ag[G;%.2f] = %.8f" %(n, wg))

def main():
    andness_geo(2.0)

if __name__ == "__main__":
    main()