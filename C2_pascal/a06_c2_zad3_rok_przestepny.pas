program AiSD_C2_Z3;
uses CRT, math, sysUtils;
function ReadYear: integer;
begin write('R = '); readln(Result); end;
function IsLeap(R: integer): boolean;
begin Result := ((R mod 4 = 0) and (R mod 100 <> 0)) or (R mod 400 = 0); end;
procedure PrintResult(R: integer; Leap: boolean);
begin
  if Leap then writeln('Rok ',R,' jest przestepny')
  else writeln('Rok ',R,' nie jest przestepny');
end;
procedure Run;
var R: integer;
begin R := ReadYear; PrintResult(R, IsLeap(R)); end;
begin Run; readln; end.
