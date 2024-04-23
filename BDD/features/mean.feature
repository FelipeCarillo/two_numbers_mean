Feature: Média de dois números 
  Scenario: Realizar a média de dois números
    Given eu tenho dois números: 6 e 6
    When eu realizo a média dos dois números
    Then o resultado deve ser 6.0
  
    Given eu tenho dois números: 10 e 17
    When eu realizo a média dos dois números
    Then o resultado deve ser 13.5