/* A program to perform Euclid s Algorithm to compute gcd. */
int gcd(int u, int v) {
    if (v == 0) {
        return u;
    } else {
        return gcd(v, u-u/v*v);
    }
    /* u-u/v*v* == u mod v */
}

int main() {
    int x;
    int y;
    x = 34;
    y = 16;
    output(gcd(x, y));
    return 0;
}