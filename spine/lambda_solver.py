def pass_test():
    raise NotImplementedError

def pass_complexity():
    raise NotImplementedError

def parse_into_trees(problems):
    """
    Returns
        #    Dependency
        #
        #Input         Output
    """
    input = 0
    output = 0
    dependencies = 0

    return input, output, dependencies

def specify_template(function_template, dependencies):
    pass

def pick_function_template():
    pass

def abstract_data():
    pass

def compose_solution(problem,pick_function_template,abstract_data):
    input, output, dependencies = parse_into_trees(problem)
    
    data_structure = abstract_data(input, output, dependencies)
    function_templates =  function_template = pick_function_template(
        data_structure, dependencies
    )

    solutions = [specify_template(func_template) 
        for func_template in function_templates
    ]
    judged_solutions = {s:[pass_test(s), pass_complexity(s)] 
        for s in solutions
    }
    
    passed_solutions = []
    for key, value in judged_solutions.items():
        if value == [True, True]:
            passed_solutions.append(key)

    return passed_solutions
    
if __name__ == "__main__":
    problem = "Two Sum"
    soltuion = compose_solution(
        problem=problem, 
        pick_function_template=pick_function_template, 
        abstract_data=abstract_data
    )





