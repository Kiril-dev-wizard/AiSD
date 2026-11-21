program AiSD_C3_Z5;
uses CRT, math, sysUtils;
var a: real;
function PowerIter(a: real; n: integer; var counter: integer): real;
var i: integer; result: real;
begin result:=1; counter:=0; for i:=1 to n do begin result:=result*a; counter:=counter+1; end; PowerIter:=result; end;
function PowerRec(a: real; n: integer; var counter: integer): real;
begin
  if n=0 then begin counter:=0; Result:=1; end
  else begin Result:=a*PowerRec(a,n-1,counter); counter:=counter+1; end;
end;
function PowerSquareIter(a: real; n: integer; var counter: integer): real;
var result,factor: real; e: integer;
begin
  result:=1; factor:=a; e:=n; counter:=0;
  while e>0 do
  begin
    if (e and 1)=1 then begin result:=result*factor; counter:=counter+1; end;
    factor:=factor*factor; counter:=counter+1; e:=e shr 1;
  end;
  if n>0 then counter:=counter-1;
  PowerSquareIter:=result;
end;
function PowerSquareRec(a: real; n: integer; var counter: integer): real;
var half,square: real; c1,c2: integer;
begin
  if n=0 then begin counter:=0; Result:=1; end
  else
  begin
    half:=PowerSquareRec(a,n div 2,c1);
    square:=half*half; c2:=c1+1;
    if (n mod 2)=0 then begin Result:=square; counter:=c2; end
    else begin Result:=square*a; counter:=c2+1; end;
  end;
end;
procedure PrintTable(a: real);
var n,ci,cr,csi,csr: integer; vi,vr,vsi,vsr: real;
begin
  writeln('a=',a:0:2);
  writeln(' n | iter      |mul| rec        |mul| sq-iter    |mul| sq-rec     |mul');
  for n:=0 to 15 do
  begin
    vi:=PowerIter(a,n,ci); vr:=PowerRec(a,n,cr);
    vsi:=PowerSquareIter(a,n,csi); vsr:=PowerSquareRec(a,n,csr);
    writeln(n:3,' | ',vi:10:0,' | ',ci:3,' | ',vr:10:0,' | ',cr:3,
            ' | ',vsi:10:0,' | ',csi:3,' | ',vsr:10:0,' | ',csr:3);
  end;
end;
procedure Run;
begin a:=2.0; PrintTable(a); end;
begin Run; readln; end.
