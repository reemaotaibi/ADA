class CobolInterpreter:
    def __init__(self):
        self.variables = {}
        self.output = []

    def run(self, code):
        self.variables = {}
        self.output = []
        lines = code.strip().split('\n')
        in_procedure = False

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            if 'PROCEDURE DIVISION' in stripped.upper():
                in_procedure = True
                continue
            if 'DATA DIVISION' in stripped.upper() or \
               'WORKING-STORAGE SECTION' in stripped.upper() or \
               'IDENTIFICATION DIVISION' in stripped.upper() or \
               stripped.upper().startswith('PROGRAM-ID'):
                continue
            if stripped.upper().startswith('01 ') or \
               stripped.upper().startswith('77 '):
                self.parse_data(stripped)
                continue
            if in_procedure:
                self.execute(stripped)

        return '\n'.join(self.output)

    def parse_data(self, stmt):
        parts = stmt.split()
        if len(parts) >= 4 and 'PIC' in [p.upper() for p in parts]:
            varname = parts[1].upper()
            if 'VALUE' in [p.upper() for p in parts]:
                val_idx = [p.upper() for p in parts].index('VALUE')
                val = parts[val_idx + 1].strip('"\'').rstrip('.')
                try:
                    self.variables[varname] = int(val)
                except:
                    try:
                        self.variables[varname] = float(val)
                    except:
                        self.variables[varname] = val
            else:
                self.variables[varname] = 0

    def execute(self, stmt):
        stmt = stmt.rstrip('.').strip()
        upper = stmt.upper()

        if upper.startswith('DISPLAY'):
            content = stmt[7:].strip()
            parts = content.split()
            result = []
            for p in parts:
                if p.startswith('"') or p.startswith("'"):
                    result.append(p.strip('"\''))
                elif p.upper() in self.variables:
                    result.append(str(self.variables[p.upper()]))
                elif p.upper() not in ('UPON', 'CONSOLE'):
                    result.append(p)
            self.output.append(' '.join(result))

        elif upper.startswith('MOVE'):
            parts = stmt.split()
            if 'TO' in [p.upper() for p in parts]:
                to_idx = [p.upper() for p in parts].index('TO')
                val = ' '.join(parts[1:to_idx]).strip('"\'')
                target = parts[to_idx + 1].upper()
                try:
                    self.variables[target] = int(val)
                except:
                    try:
                        self.variables[target] = float(val)
                    except:
                        self.variables[target] = val

        elif upper.startswith('ADD'):
            parts = stmt.split()
            if 'TO' in [p.upper() for p in parts]:
                to_idx = [p.upper() for p in parts].index('TO')
                val = self.eval_expr(parts[1])
                target = parts[to_idx + 1].upper()
                self.variables[target] = self.variables.get(target, 0) + val

        elif upper.startswith('SUBTRACT'):
            parts = stmt.split()
            if 'FROM' in [p.upper() for p in parts]:
                from_idx = [p.upper() for p in parts].index('FROM')
                val = self.eval_expr(parts[1])
                target = parts[from_idx + 1].upper()
                self.variables[target] = self.variables.get(target, 0) - val

        elif upper.startswith('MULTIPLY'):
            parts = stmt.split()
            if 'BY' in [p.upper() for p in parts]:
                by_idx = [p.upper() for p in parts].index('BY')
                val = self.eval_expr(parts[1])
                target = parts[by_idx + 1].upper()
                self.variables[target] = self.variables.get(target, 0) * val

        elif upper.startswith('STOP'):
            return

    def eval_expr(self, expr):
        expr = expr.strip().strip('"\'')
        if expr.upper() in self.variables:
            return self.variables[expr.upper()]
        try:
            return int(expr)
        except:
            try:
                return float(expr)
            except:
                return expr