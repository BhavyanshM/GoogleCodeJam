// g++ -std=c++11 -O2 -Wall test.cpp -o test

#include <bits/stdc++.h>

#define PRINT(arr) for(ull n : arr) cout << n << " "; cout << endl;
#define PRINT2(arr) for(vector<ull> v : arr) {for(ull n : v) cout << n << " "; cout << endl;} cout<<endl;

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

ull fib(ull n, vector<ull>& memo){
	// PRINT(memo,n)
	if (n==0){memo[n] = 0;return 0;}
	if (n==1) {memo[n] = 1;return 1;}
	if (memo[n]!=-1) return memo[n];
	memo[n] = fib(n-1,memo) + fib(n-2,memo);
	return memo[n];
}

ull nCr(ull n, ull r){
	ull final = 1;
	for (ull i = n; i>n-r; i--){
		final *= i;
	}
	for (ull k = r; k>0; k--){
		final /= k;
	}
	return final;
}

ull nPr(ull n, ull r){
	ull final = 1;
	for (ull i = n; i>n-r; i--){
		final *= i*(i-(n-r));
	}
	for (ull k = r; k>0; k--){
		final /= k;
	}
	return final;
}

ull nCr(ull n, ull r, vector<vector<ull>>& memo){
	// PRINT2(memo);
	if (n==0) {return 0;}
	if (n==1) {memo[n][r] = 1;return 1;}
	if (r==n) {memo[n][r] = 1;return 1;}
	if (r==0) {memo[n][r] = 1;return 1;}
	if (memo[n][r]) return memo[n][r];
	memo[n][r] = nCr(n-1,r-1,memo) + nCr(n-1,r,memo);
	return memo[n][r];
}

int main(){

#ifndef ONLINE_JUDGE
	FILE* fin = freopen("input.txt","r",stdin);
	// FILE* fout = freopen("output.txt","w",stdout);
#endif

	ios::sync_with_stdio(0);
	cin.tie(0);


	int N;
	cin >> N;

	// Recursive Fibonacci Sequence Using Memoization
	// vector<ull> memo(100,-1);
	// for(ll k = 0; k<100; k++)cout << k << " " << fib(k,memo) << endl;
	
	// Iterative Permutations and Combinations
	// ull n = 6,r = 2;
	// cout << nPr(n,r) << " " << nCr(n,r) << endl;

	// Recursive Combinations with Memoization (Pascal Triangle)
	// ull n = 6, r = 3;
	// vector<vector<ull>> memo(n+1,vector<ull> (n+1,0));
	// cout << "ANS: " << nCr(n,r,memo) << endl;


	return 0;
}  
