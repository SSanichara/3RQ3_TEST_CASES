from calculation import Calculationfunction


def test_VIR_S():
    # test values to check V=IR SERIES
    voltage = 6
    # current=2
    # resitance=3
    values = Calculationfunction()
    VoltageV = values.series_calculation_VIR(6)
    assert VoltageV == voltage, "the voltage should be equal to 6V in test case for V=IR in series"


def test_VIR_P():
    # test values to check V=IR
    voltage = 6
    # current=2
    # resitance=3
    valuep = Calculationfunction()
    VoltageV = valuep.parallel_calulations_VIR(6)
    assert VoltageV == voltage, "the voltage should be equal to 6V in test case for V=IR in parallel"


def test_IVR_S():
    # test values to check I=V/R SERIES
    # voltage=6
    current = 2
    # resitance=3
    values = Calculationfunction()
    currentV = values.series_calculation_IVR(2)
    assert currentV == current, "the current should be equal to 2A in test case for I=V/R in series"


def test_IVR_P():
    # test values to check I=V/R
    # voltage = 6
    current = 2
    # resitance=3
    valuep = Calculationfunction()
    currentV = valuep.parallel_calulations_IVR(2)
    assert currentV == current, "the current should be equal to 2A in test case for I=V/R in parallel"


def test_RVI_S():
    # test values to check I=V/R SERIES
    # voltage=6
    # current = 2
    resitance = 3
    values = Calculationfunction()
    resitanceV = values.series_calculation_RVI(3)
    assert resitanceV == resitance, "the resistance should be equal to 3ohms in test case for R=V/I in series"


def test_RVI_P():
    # test values to check R=V/I
    # voltage = 6
    # current = 2
    resitance = 3
    valuep = Calculationfunction()
    resitanceV = valuep.parallel_calulations_RVI(3)
    assert resitanceV == resitance, "the resistance should be equal to 3ohms in test case for I=V/R in parallel"


def test_voltage_total_series():
    # test values to check V1+V2=VT
    # Voltage1 = 1
    # Voltage2 = 2
    VoltageTotal = 3
    values = Calculationfunction()
    Calculated_V_Total = values.series_voltage_total(3)
    assert Calculated_V_Total == VoltageTotal, "Using the test case values voltage total should be 3 Volts for series circuit"


def test_resitance_total_series():
    # test values to check R1+R2=RT
    # resitance1 = 1
    # resitance2 = 2
    resitanceTotal = 3
    values = Calculationfunction()
    Calculated_r_Total = values.series_resistance_total(3)
    assert Calculated_r_Total == resitanceTotal, "Using the test case values resistance total should be 3 ohms for series circuit"


def test_current_total_parallel():
    # test values to check I1+I2=IT
    # current1 = 1
    # current2 = 2
    currentTotal = 3
    valuep = Calculationfunction()
    Calculated_I_Total = valuep.parallel_current_total(3)
    assert Calculated_I_Total == currentTotal, "Using the test case values current total should be 3 A for parallel circuit"


def test_resitance_total_parallel():
    # test values to check 1/r1+1/r2=IT
    # resitance1 = 1
    # resitance2 = 2
    resitanceTotal = 1.5
    valuep = Calculationfunction()
    Calculated_R_Total = valuep.parallel_resistance_total(1.5)
    assert Calculated_R_Total == resitanceTotal, "Using the test case values resistance total should be 1.5 ohm for parallel circuit"

def test_scientific_units_KV():
    # test if the value entered is in kilovolts 5kv=5000V
    voltage_scientific = 5000
    scientific_value = Calculationfunction()
    Calculated_scientific_voltage = scientific_value.Scientific_Unit_KV(5000)
    assert Calculated_scientific_voltage == voltage_scientific, "using the test case of 5KV it should equal 5000 volts"

def test_scientific_units_mA():
    # test if the value entered is in kilovolts 3mA=0.003A
    Current_scientific = 0.003
    scientific_value = Calculationfunction()
    Calculated_scientific_current = scientific_value.Scientific_Unit_mA(0.003)
    assert Calculated_scientific_current == Current_scientific, "using the test case of 3mA it should equal 0.003Amps"
