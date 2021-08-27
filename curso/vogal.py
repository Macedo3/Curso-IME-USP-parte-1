def vogal(vg):
    if vg == 'a' or vg =='e' or vg == 'i' or vg == 'o' or vg == 'u' or vg == 'A' or vg == 'E' or vg == 'I' or vg == 'O' or vg == 'U':
        return True
    else:
        return False
    
def test_vg_a():
    assert vogal('a') == True

def test_vg_E():
    assert vogal('E') == True

def test_vg_u():
    assert vogal('u') == True
    
def test_vg_r():
    assert vogal('r') == False
    
def test_vg_S():
    assert vogal('S') == False
    
def test_vg_b():
    assert vogal('b') == False