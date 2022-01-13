from behave import given, when, then
from calculate import denominators

@given(u'we call the add function')
def step_impl(context):
    pass

@when(u'we give the function an argumentof size {num}')
def step_impl(context,num: str):
    context.results = denominators.add(int(num))

@then(u'we should get {results}')
def step_impl(context, results: str):
    assert(context.results == int(results))

#________________________________________________________


@given(u'we call the div function')
def step_impl(context):
    pass

@when(u'we give arguments {num1} and {num2}')
def step_impl(context, num1:str,num2:str):
    context.results = denominators.div(int(num1), int(num2))
    print(context.results)

@then(u'we get {results}')
def step_impl(context, results:str):
    assert(context.results == int(results))