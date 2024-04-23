from behave import given, when, then

@given('eu tenho dois números: {num1:d} e {num2:d}')
def step_impl(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('eu realizo a média dos dois números')
def step_impl(context):
    context.resultado = round((context.num1 + context.num2) / 2, 1)

@then('o resultado deve ser {resultado:d}')
def step_impl(context, resultado):
    assert context.resultado == resultado, f"resultado incorreto. Esperando: {resultado}. Obtido: {context.resultado}"
