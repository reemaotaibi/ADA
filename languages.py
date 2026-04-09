from interpreter import BasicInterpreter
from pascal_interpreter import PascalInterpreter
from cobol_interpreter import CobolInterpreter
from fortran_interpreter import FortranInterpreter
from ada_interpreter import AdaInterpreter
from examples import EXAMPLES

INTERPRETERS = {
    "BASIC": BasicInterpreter,
    "Pascal": PascalInterpreter,
    "COBOL": CobolInterpreter,
    "Fortran": FortranInterpreter,
    "Ada": AdaInterpreter,
}