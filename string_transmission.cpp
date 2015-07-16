#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;
typedef long long ll;
const int MOD = 1000000007;
ll add(ll a, ll b) { return (a + b) % MOD; }
ll mul(ll a, ll b) { return a * b % MOD; }
ll sub(ll a, ll b) { return (a + MOD - b) % MOD; }
char msg[1024];
int N, T, K;
ll dp[1024], Next[1024];
int num[2][1024];
ll period(int d) {
    // initialie num
    int m = N / d;
    memset(num, 0, sizeof(num));
    for (int i = 0; i < N; ++ i) num[msg[i] - '0'][i % m]++;

    //initialize dp table
    memset(dp, 0, sizeof(dp));
    dp[0] = 1;

    for (int i = 1; i <= m; ++ i) {
        for (int j = 0; j <= K; ++ j) {
            Next[j] = 0;
            if (j >= num[0][i - 1]) Next[j] = add(Next[j], dp[j - num[0][i - 1]]);
            if (j >= num[1][i - 1]) Next[j] = add(Next[j], dp[j - num[1][i - 1]]);
        }
        memcpy(dp, Next, sizeof(ll) * (K + 1));
    }

    ll ans = 0;
    for (int k = 0; k <= K; ++ k) ans = add (ans, dp[k]);
    return ans;
}

int main() {
    scanf ("%d", &T);
    while (T --) {
//        cout << "--------------------" << endl;
        scanf ("%d %d %s", &N, &K, msg);
        vector<int> fac;
        int tN = N;
        for (int i = 2; i <= tN; ++ i) if (tN % i == 0) {
            fac.push_back(i);
            while (tN % i == 0) tN /= i;
        }
        ll ans = 0;
        int maxstate = (1 << fac.size());
        for (int mask = 0; mask < maxstate; ++ mask) {
            int bit = 0, d = 1;
            for (int i = 0; i < (int)fac.size(); ++ i)
                if ((mask >> i) & 1) {
                    d *= fac[i]; bit++;
                }

            if (bit & 1) ans = sub(ans, period(d));
            else ans = add(ans, period(d));
//            cout << bit << " " << d << " " << period(d) << endl;
        }

        cout << ans << endl;
    }
    return 0;
}
