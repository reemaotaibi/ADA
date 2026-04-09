# Ada Language Interpreter
# Named after Ada Lovelace, 1815-1852
# "The first programmer who ever lived"

class AdaInterpreter:
    def __init__(self):
        self.variables = {}
        self.output = []
        self.in_loop = False
        self.loop_body = []

    def run(self, code):
        self.variables = {}
        self.output = []
        lines = code.strip().split('\n')
        in_begin = False

        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith('--'):
                continue
            if stripped.lower() == 'begin':
                in_begin = True
                continue
            if stripped.lower().startswith('end') and not stripped.lower().startswith('end loop'):
                break
            if in_begin:
                self.execute(stripped)

        return '\n'.join(self.output)

    def execute(self, stmt):
        upper = stmt.upper().strip()
        
        if self.in_loop and not upper.startswith('END LOOP'):
            self.loop_body.append(stmt)
            return

        stmt = stmt.rstrip(';').strip()
        upper = stmt.upper()

        if upper.startswith('PUT_LINE') or upper.startswith('ADA.TEXT_IO.PUT_LINE'):
            content = stmt[stmt.index('(')+1:stmt.rindex(')')]
            content = content.strip()
            if content.startswith('"') and content.endswith('"'):
                self.output.append(content[1:-1])
            else:
                self.output.append(str(self.eval_expr(content)))

        elif upper.startswith('PUT') or upper.startswith('ADA.TEXT_IO.PUT'):
            content = stmt[stmt.index('(')+1:stmt.rindex(')')]
            content = content.strip()
            if content.startswith('"') and content.endswith('"'):
                if self.output:
                    self.output[-1] += content[1:-1]
                else:
                    self.output.append(content[1:-1])
            else:
                val = str(self.eval_expr(content))
                if self.output:
                    self.output[-1] += val
                else:
                    self.output.append(val)

        elif upper.startswith('NEW_LINE') or upper.startswith('ADA.TEXT_IO.NEW_LINE'):
            self.output.append('')

        elif ':=' in stmt:
            var, expr = stmt.split(':=', 1)
            var = var.strip()
            if ':' in var:
                var = var.split(':')[0].strip()
            self.variables[var] = self.eval_expr(expr.strip())

        elif upper.startswith('FOR'):
            rest = stmt[3:].strip()
            if 'IN' in rest.upper() and 'LOOP' in rest.upper():
                var_part = rest[:rest.upper().index('IN')].strip()
                range_part = rest[rest.upper().index('IN')+2:rest.upper().index('LOOP')].strip()
                if '..' in range_part:
                    start, end = range_part.split('..')
                    self.loop_var = var_part
                    self.loop_start = int(self.eval_expr(start.strip()))
                    self.loop_end = int(self.eval_expr(end.strip()))
                    self.in_loop = True
                    self.loop_body = []

        elif upper.startswith('END LOOP'):
            if self.in_loop:
                self.in_loop = False  # turn OFF before executing body!
                body = self.loop_body[:]
                self.loop_body = []
                for i in range(self.loop_start, self.loop_end + 1):
                    self.variables[self.loop_var] = i
                    for body_stmt in body:
                        self.execute(body_stmt)

        elif upper.startswith('IF'):
            if 'THEN' in upper:
                cond_part = stmt[2:stmt.upper().index('THEN')].strip()
                then_part = stmt[stmt.upper().index('THEN')+4:].strip()
                if self.eval_condition(cond_part):
                    self.execute(then_part)

    def eval_expr(self, expr):
        expr = expr.strip().strip('"')
        for var, val in self.variables.items():
            expr = expr.replace(var, str(val))
        try:
            return eval(expr)
        except:
            return expr

    def eval_condition(self, condition):
        for var, val in self.variables.items():
            condition = condition.replace(var, str(val))
        condition = condition.replace('=', '==').replace('>==','>=').replace('<==','<=').replace('/=','!=')
        try:
            return eval(condition)
        except:
            return False