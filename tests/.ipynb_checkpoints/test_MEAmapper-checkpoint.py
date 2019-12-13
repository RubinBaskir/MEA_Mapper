from MEAmapper import MEAmap

def test_MEAmap():
    usa = MEAmap('St. Louis', 'New York')
    assert usa.iloc[0,0] == 'Hawaii'