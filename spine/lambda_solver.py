from parseproblems import parse_into_trees

def pass_test():
    raise NotImplementedError

def pass_complexity():
    raise NotImplementedError

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
    TwoSum = """
      Given an array of integers nums and an integer target, 
      return indices of the two numbers 
      such that they add up to target.
    """
    problem = TwoSum
    a = parse_into_trees(problem)
    print(a[2][-1])
    # soltuion = compose_solution(
    #     problem=problem, 
    #     pick_function_template=pick_function_template, 
    #     abstract_data=abstract_data
    # )

    # TODO:
    # refine regex example
    # set up python packaging

