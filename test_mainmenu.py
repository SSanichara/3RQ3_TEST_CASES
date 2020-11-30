from mainmenu import Mainmenu


def test_next_button_unclicked():
    # TESTS IF THE BUTTON IS NOT CLICK WILL RETURN A FALSE VALUE
    button_F = False
    button = Mainmenu()
    button_TF = button.Next_button(False)
    assert button_TF == button_F, "This should be True until the button is clicked"


def test_next_button_clicked():
    # TESTS IF THE BUTTON IS CLICKED IT WILL RETURN A TRUE VALUE AFTER CLICKED
    button_T = True
    button = Mainmenu()
    button_TF = button.Next_button(True)
    assert button_TF == button_T, "This should be True after the button is clicked"


def test_calculation_choice_S():
    # the user will pick series and this test will confirm that series calculations will be used
    C_series = "series"
    calculation = Mainmenu()
    choice = calculation.Calculation_type("series")
    assert choice == C_series, "This will be True if the user chooses series circuit calculations"


def test_calculation_choice_P():
    # the user will pick parallel and this test will confirm that parallel calculations will be used
    C_parallel = "parallel"
    calculation = Mainmenu()
    choice = calculation.Calculation_type("parallel")
    assert choice == C_parallel, "This will be true if the user chooses parallel circuit calculations"


def test_resistor_over_limit():
    # the upper limit of resistors is 10 so if the user chooses a higher value then 10 a error will occure this test should fail
    overlimit = 10
    resistor = Mainmenu()
    number_over_resistors = resistor.Number_of_resistorso(11)
    assert number_over_resistors <= overlimit, "11 resistors or more is not allowed"


def test_resistor_under_limit():
    # the lower limit of resistors is 0 so if the user chooses a lower value then 0 a error will occure this test should fail
    underlimit = 0
    resistor = Mainmenu()
    number_under_resistors = resistor.Number_of_resistorsl(-1)
    assert number_under_resistors >= underlimit, "less than 0 resistors is not allowed"
