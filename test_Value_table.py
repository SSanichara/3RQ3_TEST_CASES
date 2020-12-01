from Value_table import Valuetable


def test_reset_T():
    # if the reset is clicked then the boolean is true then from the value table should return to mainmenu
    reset_T = Valuetable()
    T_test = reset_T.reset(True)
    assert T_test == True, "reset value should be true when clicked and return to main menu from the value table"


def test_gui_size():
    # the window size is set by the camand geometry in tkinter and the size value should match "750x750"
    set_window_size = "750x750"
    window = Valuetable()
    window_size = window.GUI_size("750 x 750")
    assert window_size == set_window_size, "the window size should be 750 by 750 on all screens"


def test_previous_T():
    # if the reset is clicked then the boolean is true then from the value table should return to mainmenu
    previous_button = Valuetable()
    previous_value = previous_button.previous(True)
    assert previous_value == True, "previous value should be true when clicked and return to main menu from the value table"


def test_save_history():
    # use case values to test if the array stored in the a array is the same that is in the file testing with 2 resistors
    values_array_test = "V1=1v V2=1v VT=2v I1=1A I2=1A IT=1A R1=1ohm R2=1ohm R2=1ohm RT=2ohm"
    history = Valuetable()
    save_history = history.save_history("V1=1v V2=1v VT=2v I1=1A I2=1A IT=1A R1=1ohm R2=1ohm R2=1ohm RT=2ohm")
    assert save_history == values_array_test, "this array should be equal to the test case values"


def test_view_history():
    #using the sample string values in the file this test should pass if the value array written in the history is the same
    values_array_test = "V1=1v V2=1v VT=2v I1=1A I2=1A IT=1A R1=1ohm R2=1ohm R2=1ohm RT=2ohm"
    history_file = open(r"testfile", "r+")
    history=history_file.read()
    print(history)
    assert history==values_array_test,"this should read the same values from the test file"

def test_Knowvariable():
    values=len(["2","2"])
    requiredknownvariables=values
    know=Valuetable()
    number_of_known=know.Knowvariable(2)
    assert number_of_known==requiredknownvariables,"The user is required to provide 2 known variables per set"