def pass_test():
    raise NotImplementedError

def pass_performance():
    raise NotImplementedError

def parse_problems(problems):
    """
    """
    input = 0
    output = 0
    dependencies = 0

    return input, output, dependencies

def build_from_template(function_template, dependencies):
    pass

def pick_function_template():
    pass

def abstract_data():
    pass

def compose_solution(problem,pick_function_template,abstract_data):
    input, output, dependencies = parse_problems(problem)
    test_passed = pass_test()
    performance_passed = pass_performance()
    data_structure = abstract_data(input, dependencies)

    while test_passed and performance_passed:
        function_template = pick_function_template(data_structure, dependencies)
        solution = build_from_template(function_template, dependencies)

    return solution
    
if __name__ == "__main__":
    problem = "Two Sum"
    soltuion = compose_solution(
        problem=problem, 
        pick_function_template=pick_function_template, 
        abstract_data=abstract_data
    )





