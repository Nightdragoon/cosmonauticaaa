#include <bits/stdc++.h>
#include<cpr/cpr.h>
#include <nlohmann/json.hpp>
using json = nlohmann::json;
using namespace std;
int main(int, char**){
    auto x = cpr::Get(cpr::Url{"http://localhost:8090/cosmos"});
    auto r = json::parse(x.text);
    cout << r["message"] << endl;
}
