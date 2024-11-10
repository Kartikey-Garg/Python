import Dice_Rolling_Simulator
def test_pos():
    assert Dice_Rolling_Simulator.usr(5) == True
def test_neg():
    assert Dice_Rolling_Simulator.usr('f') == False