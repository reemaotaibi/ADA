class FortranInterpreter:
    def __init__(self):
        self.variables = {}
        self.output = []

    def run(self, code):
        self.variables = {}
        self.output = []
        lines = code.strip().split('\n')

        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('!') or stripped.upper().startswith('C ') or stripped.upper().startswith('PROGRAM'):
                continue
            self.execute(stripped)

        return '\n'.join(self.output)

    def execute(self, stmt):
        stmt = stmt.strip()
        upper = stmt.upper()

        if upper.startswith('PRINT') or upper.startswith('WRITE'):
            if ',' in stmt:
                content = stmt[stmt.index(',')+1:].strip()
            else:
                content = stmt[5:].strip()
            parts = [p.strip() for p in content.split(',')]
            result = []
            for p in parts:
                p = p.strip("'\"* ")
                if p.upper() in self.variables:
                    result.append(str(self.variables[p.upper()]))
                elif p:
                    result.append(p)
            self.output.append(' '.join(result))

        elif upper.startswith('INTEGER') or upper.startswith('REAL') or upper.startswith('CHARACTER'):
            pass

        elif upper.startswith('DO'):
            parts = stmt[2:].strip()
            if '=' in parts:
                var_part, range_part = parts.split('=', 1)
                var = var_part.strip().upper()
                range_vals = [r.strip() for r in range_part.split(',')]
                start = int(self.eval_expr(range_vals[0]))
                end = int(self.eval_expr(range_vals[1]))
                step = int(self.eval_expr(range_vals[2])) if len(range_vals) > 2 else 1
                for i in range(start, end + 1, step):
                    self.variables[var] = i

        elif upper.startswith('END DO') or upper.startswith('ENDDO'):
            pass

        elif upper.startswith('STOP') or upper == 'END':
            return

        elif '=' in stmt and '==' not in stmt:
            var, expr = stmt.split('=', 1)
            self.variables[var.strip().upper()] = self.eval_expr(expr.strip())

    def eval_expr(self, expr):
        expr = expr.strip()
        for var, val in self.variables.items():
            expr = expr.replace(var, str(val))
        try:
            return eval(expr)
        except:
            return expr