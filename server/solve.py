from sympy import solve, simplify
from latex2sympy2_extended import latex2sympy
from pix2text import Pix2Text
import re

config = {
    "analyzer": {
        "model_name": "mfd",        
        "model_type": "yolov10",    
        "threshold": 0.55           
    },
    "text": {"use_fast": True},
    "formula": {"use_fast": True}
}

p2t = Pix2Text.from_config(config=config)

def process_and_solve(img_path):
    latex_str = p2t.recognize(img_path)
    # using regular expressions to clean up whitespaces between digits
    clean_latex = latex2sympy(re.sub(r'(?<=\d)\s+(?=\d)', '', latex_str.strip()))
    
    try:
        found_variables = list(clean_latex.free_symbols)
        
        if not found_variables:
            calculated_result = simplify(clean_latex)
            
            return {
                "status": "success",
                "type": "arithmetic",
                "parsed_expression": str(clean_latex),
                "result": str(calculated_result),
                "float_result": float(calculated_result.evalf())
            }
        
        solutions = solve(clean_latex, found_variables)
        
        return {
            "status": "success",
            "type": "algebra",
            "parsed_equation": str(clean_latex),
            "variables_found": [str(v) for v in found_variables],
            "solutions": [str(sol) for sol in solutions] if isinstance(solutions, list) else str(solutions)
        }
        
    except Exception as e:
        return {
            "status": "error", 
            "message": f"Could not parse or solve this LaTeX structure. Error: {str(e)}"
        }
    