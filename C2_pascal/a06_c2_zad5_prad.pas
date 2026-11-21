program AiSD_C2_Z5;
uses CRT, math, sysUtils;
const P_INST = 3.0; DURATION = 10;
procedure PrintResults(E1c,E2c,E1b,E2b,MaxP: real);
begin
  writeln('E1_active=',E1c:0:8,' kWh');
  writeln('E2_active=',E2c:0:8,' kWh');
  writeln('E1_reactive=',E1b:0:8,' kWh');
  writeln('E2_reactive=',E2b:0:8,' kWh');
  writeln('Max_power=',MaxP:0:4,' kW');
end;
procedure Simulate(out E1c,E2c,E1b,E2b,MaxP: real);
var t: integer; H: longint; Active,Reactive: real; TariffI: boolean;
begin
  E1c:=0; E2c:=0; E1b:=0; E2b:=0; MaxP:=0;
  for t := 0 to DURATION-1 do
  begin
    H := (6 + t div 3600) mod 24;
    Active := P_INST*(1+sin(t))/2;
    Reactive := 0.1*Active;
    TariffI := ((H>=6) and (H<13)) or ((H>=15) and (H<22));
    if TariffI then begin E1c:=E1c+Active/3600; E1b:=E1b+Reactive/3600; end
    else begin E2c:=E2c+Active/3600; E2b:=E2b+Reactive/3600; end;
    if Active > MaxP then MaxP := Active;
  end;
end;
procedure Control;
var E1c,E2c,E1b,E2b,MaxP: real;
begin Simulate(E1c,E2c,E1b,E2b,MaxP); PrintResults(E1c,E2c,E1b,E2b,MaxP); end;
begin Control; readln; end.
