#include <bits/stdc++.h>
using namespace std;
//---- MACROS ------
#define ll long long
#define pb push_back
#define mp make_pair
#define mineq(a,n) a = min((a), (n)) 
#define maxeq(a,n) a = max((a), (n))
#define forn(i,a,n) for (int i = a; i < n; ++i) 
#define forn2(i,a,n) for (int i = a; i < n; i+=2) 
#define fornn(i,n,a) for (int i = n; i >= a; --i) 
#define matrix(a) vector<vector<a>>
#define inf INT32_MAX
//-----------------
void coutVector(vector<auto>& v) {
    cout << "[";
    forn(i, 0, v.size()) {
        cout << v[i];
        if(i < v.size()-1) cout << ", ";
    };
    cout << "]" << endl; 
}


void coutMatrix(matrix(auto)& m) {
    // cout << "---------------------------" << endl;
    cout << "[" << endl;
    for(auto v : m) {
        cout << "    ";
        coutVector(v);
    }
    cout << "]" << endl;
    // cout << "---------------------------" << endl << endl;
} 

//----------------------------------------------------------------------

//----------------------------------------------------------------------
typedef int resultado; // cambiar int por el tipo deseado

struct parametros {
    vector<int> v;
    int n;
    int m;
};

parametros createTest(){
    parametros p = {};
    p.n = 10;
    p.m = 20;
    forn(i, 0, p.n) p.v.pb(rand() % p.m + 10); // rango: [10, m)
    return p;
}
//----------------------------------------------------------------------

//----------------------------------------------------------------------
resultado solve1(parametros p){  // mi solucion
    resultado res1 = 0;
    return res1;
} 
resultado solve2(parametros p){  // una solucion correcta
    resultado res2 = 0;
    return res2;
} 
//----------------------------------------------------------------------

//----------------------------------------------------------------------
int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);

    ll t; cin >> t;
    forn(tt, 0, t) {
        parametros p = createTest();
        resultado res1 = solve1(p);
        resultado res2 = solve2(p);

        if( res1 != res2) {
            cout << "se rompio todo" << endl;
            cout << "mi caca: " << res1 << endl;
            cout << "la posta: " << res2 << endl;
            
            // print parametros
            cout << "n: " << p.n << endl;
            cout << "m: " << p.m << endl;
            cout << "m: " << p.m << endl;
        }
    }
    cout << "terminaron los tests" << endl;
}
//----------------------------------------------------------------------
