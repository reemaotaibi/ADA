EXAMPLES = {
    "BASIC": """10 PRINT "Hello from BASIC!"
20 LET X = 1
30 FOR I = 1 TO 5
40 LET X = X * 2
50 PRINT X
60 NEXT I
70 END""",

    "Pascal": """program HelloADA;
begin
  writeln('Hello from Pascal!');
  writeln('ADA preserves the past.');
  for i := 1 to 5 do
    writeln(i);
end.""",

    "COBOL": """IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO-ADA.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-NAME PIC X(20) VALUE "ADA".
01 WS-NUM  PIC 9(3)  VALUE 0.
PROCEDURE DIVISION.
    DISPLAY "Hello from COBOL!".
    DISPLAY "Program: " WS-NAME.
    MOVE 42 TO WS-NUM.
    DISPLAY "Answer: " WS-NUM.
    STOP RUN.""",

    "Fortran": """      PROGRAM HELLO
      INTEGER I, X
      PRINT *, 'Hello from Fortran!'
      X = 1
      DO I = 1, 5
        X = X * 2
        PRINT *, X
      END DO
      STOP
      END""",

    "Ada": """-- Ada program, named after Ada Lovelace
-- The first programmer, 1815

with Ada.Text_IO;
procedure Hello is
begin
   Put_Line("Ada Lovelace, 1815.");
   Put_Line("The first programmer who ever lived.");
   Put_Line("This language carries her name.");
   for I in 1 .. 5 loop
      Put_Line(I);
   end loop;
end Hello;""",

}
