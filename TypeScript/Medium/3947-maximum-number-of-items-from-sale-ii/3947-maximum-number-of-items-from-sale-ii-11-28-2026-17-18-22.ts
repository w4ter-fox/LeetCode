function maximumSaleItems(items: number[][], budget: number): number {
    const n = items.length;
    const freq = new Array<number>(n + 1).fill(0);
    for (const [f] of items) {
        freq[f]++;
    }

    const multiples = new Array<number>(n + 1).fill(0);
    for (let f = 1; f <= n; f++) {
        if (freq[f] > 0){
            let count = 0;
            for (let g = f; g <= n; g += f) {
                count += freq[g];
            }
            multiples[f] = count;
        }
    }

    let m = Infinity;
    for (const [, p] of items) {
        if (p<m) {
            m = p;
        }
    }

    const bundles: [number, number][] = [];
    for (const [f, p] of items) {
        const d = multiples[f] - 1;
        if (d > 0 && p < 2 * m) {
            bundles.push([p, d]);
        }
    }

    bundles.sort((a, b) => a[0] - b[0]);

    let total = 0;
    let rem = budget;
    for (const [p, d] of bundles) {
        const t = Math.min(d, Math.floor(rem / p));
        total += 2 * t;
        rem -= t * p;
        if (t < d) {
            break;
        }
    }

    return total + Math.floor(rem / m);
};