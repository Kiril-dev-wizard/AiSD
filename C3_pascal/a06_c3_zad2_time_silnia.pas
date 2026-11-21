{$mode objfpc}
program AiSD_C3_Z2;
uses CRT, math, sysUtils;
function FactorialRecursive(n: int64): int64;
begin if n <= 1 then Result := 1 else Result := n * FactorialRecursive(n-1); end;
function FactorialIterative(n: int64): int64;
var i: int64;
begin Result := 1; for i := 2 to n do Result := Result * i; end;
function ReadArg(maxArg: int64): int64;
var v: int64;
begin
  repeat
    write('n (0..',maxArg,') = '); readln(v);
    if (v < 0) or (v > maxArg) then writeln('Blad: podaj wartosc z zakresu.');
  until (v >= 0) and (v <= maxArg);
  Result := v;
end;
procedure MeasureIter(n, reps: int64; out value: int64; out seconds: real);
var T0,T1: real; i: longint;
begin
  T0 := Time*24*60*60;
  for i := 1 to reps do value := FactorialIterative(n);
  T1 := Time*24*60*60;
  seconds := T1-T0;
end;
procedure MeasureRec(n, reps: int64; out value: int64; out seconds: real);
var T0,T1: real; i: longint;
begin
  T0 := Time*24*60*60;
  for i := 1 to reps do value := FactorialRecursive(n);
  T1 := Time*24*60*60;
  seconds := T1-T0;
end;
procedure Run;
var n,reps,vi,vr: int64; ti,tr: real;
begin
  n := ReadArg(20);
  write('Liczba powtorzen = '); readln(reps);
  MeasureIter(n,reps,vi,ti);
  MeasureRec(n,reps,vr,tr);
  writeln('Argument silni: ',n);
  writeln('Liczba powtorzen: ',reps);
  writeln('Silnia iteracyjnie: ',vi,' czas: ',ti:0:4,' s');
  writeln('Silnia rekurencyjnie: ',vr,' czas: ',tr:0:4,' s');
end;
begin Run; readln; end.
