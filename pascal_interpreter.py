def run(self, code):
    self.variables = {}
    self.output = []
    lines = code.strip().split('\n')
    in_begin = False
    body_lines = []

    # flatten into list of statements
    statements = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('{'):
            continue
        if stripped.lower() == 'begin':
            in_begin = True
            continue
        if stripped.lower() in ('end.', 'end'):
            break
        if in_begin:
            statements.append(stripped)

    # process statements
    i = 0
    while i < len(statements):
        stmt = statements[i]
        if stmt.lower().startswith('for'):
            # collect loop body until we hit next statement
            parts = stmt[3:].strip()
            var_part, to_part = parts.split(':=', 1)
            var = var_part.strip()
            to_parts = to_part.upper().split('TO')
            start = int(self.eval_expr(to_parts[0].strip()))
            end_do = to_parts[1].strip().split('DO')
            end = int(self.eval_expr(end_do[0].strip()))
            # next line is the body
            i += 1
            if i < len(statements):
                body = statements[i]
                for j in range(start, end + 1):
                    self.variables[var] = j
                    self.execute(body)
        else:
            self.execute(stmt)
        i += 1

    return '\n'.join(self.output)