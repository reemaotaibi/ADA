# ADA - BASIC Interpreter
# Preserving computer culture, one language at a time

class BasicInterpreter:
    def __init__(self):
        self.variables = {}
        self.lines = {}
        self.output = []

    def load(self, code):
        self.lines = {}
        for line in code.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
            parts = line.split(' ', 1)
            try:
                num = int(parts[0])
                self.lines[num] = parts[1] if len(parts) > 1 else ''
            except ValueError:
                pass

    def run(self):
        self.output = []
        self.variables = {}
        sorted_lines = sorted(self.lines.keys())
        idx = 0

        while idx < len(sorted_lines):
            linenum = sorted_lines[idx]
            statement = self.lines[linenum].strip()
            result = self.execute(statement, sorted_lines, idx)

            if result == 'END':
                break
            elif isinstance(result, int):
                if result in self.lines:
                    idx = sorted_lines.index(result)
                else:
                    break
            else:
                idx += 1

        return '\n'.join(self.output)

    def execute(self, statement, sorted_lines, idx):
        statement = statement.strip()

        # PRINT
        if statement.upper().startswith('PRINT'):
            expr = statement[5:].strip()
            if expr.startswith('"') and expr.endswith('"'):
                self.output.append(expr[1:-1])
            else:
                try:
                    self.output.append(str(self.eval_expr(expr)))
                except:
                    self.output.append(expr)

        # LET
        elif statement.upper().startswith('LET'):
            parts = statement[3:].strip().split('=', 1)
            varname = parts[0].strip()
            value = self.eval_expr(parts[1].strip())
            self.variables[varname] = value

        # IF...THEN
        elif statement.upper().startswith('IF'):
            parts = statement[2:].upper().split('THEN')
            condition = parts[0].strip()
            then_part = parts[1].strip() if len(parts) > 1 else ''
            if self.eval_condition(condition):
                return self.execute(then_part, sorted_lines, idx)

        # GOTO
        elif statement.upper().startswith('GOTO'):
            target = int(statement[4:].strip())
            return target

        # FOR loop (basic)
        elif statement.upper().startswith('FOR'):
            parts = statement[3:].strip().split('=')
            var = parts[0].strip()
            range_parts = parts[1].upper().split('TO')
            start = int(self.eval_expr(range_parts[0].strip()))
            end = int(self.eval_expr(range_parts[1].strip()))
            self.variables[var] = start
            self.variables[f'__for_{var}_end'] = end

        # NEXT
        elif statement.upper().startswith('NEXT'):
            var = statement[4:].strip()
            self.variables[var] += 1
            if self.variables[var] <= self.variables.get(f'__for_{var}_end', 0):
                for i, ln in enumerate(sorted_lines):
                    if self.lines[ln].upper().startswith(f'FOR {var}'):
                        return sorted_lines[i + 1]

        # END
        elif statement.upper() == 'END':
            return 'END'

        return None

    def eval_expr(self, expr):
        expr = expr.strip()
        for var, val in self.variables.items():
            expr = expr.replace(var, str(val))
        try:
            return eval(expr)
        except:
            return expr

    def eval_condition(self, condition):
        for var, val in self.variables.items():
            condition = condition.replace(var, str(val))
        condition = condition.replace('=', '==').replace('>==', '>=').replace('<==', '<=')
        try:
            return eval(condition)
        except:
            return False


# Test it
if __name__ == "__main__":
    interpreter = BasicInterpreter()

    test_program = """
10 PRINT "Hello from ADA!"
20 LET X = 5
30 LET Y = 10
40 LET Z = X + Y
50 PRINT Z
60 FOR I = 1 TO 5
70 PRINT I
80 NEXT I
90 END
"""
    interpreter.load(test_program)
    output = interpreter.run()
    print("--- ADA Output ---")
    print(output)