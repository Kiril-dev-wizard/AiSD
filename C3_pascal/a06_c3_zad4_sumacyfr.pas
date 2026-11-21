program AiSD_C3_Z4;
uses CRT, math, sysUtils;
function ReadNumber: integer;
begin write('L = '); readln(Result); end;
function DigitSumIterative(L: integer): integer;
var S: integer;
begin L:=abs(L); S:=0; while L>0 do begin S:=S+(L mod 10); L:=L div 10; end; DigitSumIterative:=S; end;
function DigitSumRecursive(L: integer): integer;
begin
  L := abs(L);
  if L = 0 then Result := 0
  else Result := (L mod 10) + DigitSumRecursive(L div 10);
end;
procedure PrintResults(L, Iter, Rec: integer);
begin
  writeln('Suma cyfr iteracyjnie:  ',Iter);
  writeln('Suma cyfr rekurencyjnie:',Rec);
end;
procedure Run;
var L: integer;
begin L:=ReadNumber; PrintResults(L,DigitSumIterative(L),DigitSumRecursive(L)); end;
begin Run; readln; end.
