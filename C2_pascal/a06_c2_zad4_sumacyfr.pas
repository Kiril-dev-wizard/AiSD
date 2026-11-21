{$mode objfpc}
program AiSD_C2_Z4;
uses CRT, math, sysUtils;
function ReadNumber: integer;
begin write('L = '); readln(Result); end;
function DigitSum(L: integer): integer;
var S: integer;
begin
  L := abs(L); S := 0;
  while L > 0 do begin S := S + (L mod 10); L := L div 10; end;
  DigitSum := S;
end;
procedure PrintResult(L,S: integer);
begin writeln('L=',L,' suma cyfr S=',S); end;
procedure Run;
var L: integer;
begin L := ReadNumber; PrintResult(L, DigitSum(L)); end;
begin Run; readln; end.
