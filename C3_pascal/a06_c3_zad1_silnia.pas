{$mode objfpc}
program AiSD_C3_Z1;
uses CRT, math, sysUtils;
function ReadNumber: int64;
begin write('n = '); readln(Result); end;
function FactorialRecursive(n: int64): int64;
begin if n <= 1 then Result := 1 else Result := n * FactorialRecursive(n-1); end;
function FactorialIterative(n: int64): int64;
var i: int64;
begin Result := 1; for i := 2 to n do Result := Result * i; end;
procedure PrintResults(n, Iter, Rec: int64);
begin
  writeln('Silnia iteracyjnie:  ', Iter);
  writeln('Silnia rekurencyjnie:', Rec);
end;
procedure Run;
var n: int64;
begin n := ReadNumber; PrintResults(n, FactorialIterative(n), FactorialRecursive(n)); end;
begin Run; readln; end.
