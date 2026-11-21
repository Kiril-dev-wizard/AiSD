program AiSD_C2_Z2;
uses CRT, math, sysUtils;
var L0,n,i: integer; S: int64;
begin
  write('L0 = '); readln(L0);
  write('n = '); readln(n);
  S := 0;
  for i := 0 to n-1 do S := S + sqr(L0+i);
  writeln('L0=',L0,' n=',n,' S=',S);
  readln;
end.
