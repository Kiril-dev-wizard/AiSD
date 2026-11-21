#!/usr/bin/env bash
# AiSD Pascal — реальные прогоны скомпилированных программ
cd "$(dirname "$0")/pascal_build"
out=../pascal_test_results.txt
: > "$out"
{
echo "=== AiSD Pascal compile & run (FPC 3.2.2, Linux x86_64) ==="
echo "DATA: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo
echo "--- C2 Z1: quadratic (1 -5 6) ---"
printf '1\n-5\n6\n' | ./a06_c2_zad1_rownanie | head -5
echo "--- C2 Z1: (1 0 1) no roots ---"
printf '1\n0\n1\n' | ./a06_c2_zad1_rownanie | head -5
echo "--- C2 Z2: sum squares L0=1 n=3 ---"
printf '1\n3\n' | ./a06_c2_zad2_suma_kwadratow | head -5
echo "--- C2 Z3: leap 2000 / 1900 ---"
printf '2000\n' | ./a06_c2_zad3_rok_przestepny | head -3
printf '1900\n' | ./a06_c2_zad3_rok_przestepny | head -3
echo "--- C2 Z4: digit sum 258 ---"
printf '258\n' | ./a06_c2_zad4_sumacyfr | head -5
echo "--- C2 Z5: electricity (10 s) ---"
./a06_c2_zad5_prad | head -8
echo "--- C3 Z1: factorial 18 ---"
printf '18\n' | ./a06_c3_zad1_silnia | head -5
echo "--- C3 Z2: timing 18! x 100000 ---"
printf '18\n100000\n' | ./a06_c3_zad2_time_silnia | head -10
echo "--- C3 Z4: digit sum 258 both methods ---"
printf '258\n' | ./a06_c3_zad4_sumacyfr | head -5
echo "--- C3 Z5: power a=2 n=0..15 (selected rows) ---"
./a06_c3_zad5_potega | head -9
} | tee "$out"
