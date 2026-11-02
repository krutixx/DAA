#include <iostream>
using namespace std;

int main() {

    int n, W;

    cout << "Enter number of items: ";
    cin >> n;

    int value[n], weight[n];

    cout << "Enter values of items:\n";
    for (int i = 0; i < n; i++)
        cin >> value[i];

    cout << "Enter weights of items:\n";
    for (int i = 0; i < n; i++)
        cin >> weight[i];

    cout << "Enter knapsack capacity: ";
    cin >> W;

    // DP table
    int dp[n + 1][W + 1];

    // Initialize first row and column to 0
    for (int i = 0; i <= n; i++)
        dp[i][0] = 0;

    for (int w = 0; w <= W; w++)
        dp[0][w] = 0;

    // Fill DP table
    for (int i = 1; i <= n; i++) {

        for (int w = 1; w <= W; w++) {

            if (weight[i - 1] <= w) {

                int take = value[i - 1] +
                           dp[i - 1][w - weight[i - 1]];

                int notTake = dp[i - 1][w];

                dp[i][w] = max(take, notTake);
            }

            else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    cout << "\nMaximum value = " << dp[n][W] << endl;

    return 0;
}