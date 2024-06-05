// ΨΔΣL345ΨΘL
#include <bits/stdc++.h>
using namespace std;
#define nl "\n"
#define pb push_back
#define lsb(x) (x & -x) 
#define sp(x) fixed<<setprecision(x)
#define all(x) x.begin(),x.end()
#define fore(it,i,f) for(auto it=i;it<f;++it)
#define fastIO ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll,ll>par;
typedef vector<ll>vll;
typedef vector<vector<ll>>vvll;
typedef vector<bool>vb;

/*'A' = 65 'Z' = 90
  'a' = 97 'z' = 122
  '0' = 48 '9' = 57 */

int main(){
    fastIO;
    
    unordered_map<string,ll>dias;
    unordered_map<ll,string>dias_;
    
    dias["LUNES"] = 0;
    dias["MARTES"] = 1;
    dias["MIERCOLES"] = 2;
    dias["JUEVES"] = 3;
    dias["VIERNES"] = 4;
    dias["SABADO"] = 5;
    dias["DOMINGO"] = 6;
    
    dias_[0] = "LUNES";
    dias_[1] = "MARTES";
    dias_[2] = "MIERCOLES";
    dias_[3] = "JUEVES";
    dias_[4] = "VIERNES";
    dias_[5] = "SABADO";
    dias_[6] = "DOMINGO";

    ll n;
    cin>>n;
    
    fore(i,0,n){
        ll A;
        string S;
        cin>>S>>A;
        ll numeroDia = dias[S];
        cout<<dias_[(numeroDia+A)%7]<<nl;
    }
  
    return 0;
}
