program AiSD_C2_Z1;
uses CRT, math, sysUtils;
var a,b,c,d,x1,x2: real;
begin
  writeln('rownanie ax^2+bx+c=0');
  write('a = '); readln(a);
  write('b = '); readln(b);
  write('c = '); readln(c);
  if abs(a) < 1e-12 then
  begin
    if abs(b) < 1e-12 then
      if abs(c) < 1e-12 then writeln('nieskonczona liczba rozwiazan')
      else writeln('rownanie sprzeczne')
    else writeln('jedno rozwiazanie x = ', -c/b:0:4)
  end
  else
  begin
    d := b*b - 4*a*c;
    if d < 0 then writeln('brak rozwiazan rzeczywistych')
    else if abs(d) < 1e-12 then writeln('jedno rozwiazanie podwojne x = ', -b/(2*a):0:4)
    else
    begin
      x1 := (-b - sqrt(d))/(2*a);
      x2 := (-b + sqrt(d))/(2*a);
      writeln('x1 = ', x1:0:4, ' x2 = ', x2:0:4);
    end;
  end;
  readln;
end.
