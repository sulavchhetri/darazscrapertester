from quantitytester.total import *


def test_quantitytester():
    # Pass case
    assert quantitygen(
        "Wai Wai Zing Hot & Spicy Instant Noodle, 5 Packs, Free BowlS") == 5
    assert quantitygen("Maggi Veg Atta Noodles Masala 290 gm") == None
    assert quantitygen(
        "Yashoda Foods Current Noodles Hot 'n' Spicy Chilli + Pepper 100gm Carton 20 Pieces") == 20
    assert quantitygen(
        "Samyang Single Spicy Hot Chicken Ramen- 140gm* 5 pcs") == 5
    assert quantitygen("Current 2X Spicy Noodles (Pack of 5 X 100 gm)") == 5
    return "Passed"


def test_remove_punctuation():
    assert remove_punctuation("What are you doing?") == "What are you doing"
    assert remove_punctuation(
        "Samyang Single Spicy Hot Chicken Ramen- 140gm* 5 pcs") == "Samyang Single Spicy Hot Chicken Ramen 140gm 5 pcs"
    return "Passed"


def test_stopwordremover():
    assert stopwordsremover(
        "CG Wai Wai Quick Masala Curry Instant Noodle 60gm Pack of 5") == "CG Wai Wai Quick Masala Curry Instant Noodle 60gm Pack 5"
    assert stopwordsremover(
        "Wai Wai Chicken Bhujia Curry 750g") == "Wai Wai Chicken Bhujia Curry 750g"
    return "Passed"


def test_ngramcreator():
    assert ngramcreator("Hot Pot Gourmet Spicy Vegetable Noodles 100G", 2) == [
        'Hot Pot', 'Pot Gourmet', 'Gourmet Spicy', 'Spicy Vegetable', 'Vegetable Noodles', 'Noodles 100G']
    assert ngramcreator("Samyang Buldak Jjajang Hot Chicken Flavor Ramen(Pack of 5)",2) == [
        'Samyang Buldak', 'Buldak Jjajang', 'Jjajang Hot', 'Hot Chicken', 'Chicken Flavor', 'Flavor RamenPack', 'RamenPack 5']
    assert ngramcreator("Spartan Egg Chowmein 360G",1) == ["Spartan","Egg","Chowmein","360G"]
    return "Passed"

def test_scrape():
    #Initially no scraping is done, so there is no file called noodlesprice.csv
    assert filechecker("noodlesprice.csv") == "File not found"
    
    #Fail Case, no file is created because of a bad url
    scrape("randomthing")
    assert filechecker("randomthingprice.csv") == "File not found"
    
    #Pass Case, the scraped data is stored in a csv file
    scrape("noodles")
    assert filechecker("noodlesprice.csv")== "Not Empty"
    return "Passed"

def test_csvquantity():
    assert filechecker("noodlesquantity.csv") == "Not Empty"
    assert filechecker("wrongfile.csv") == "File not found"
    return "Passed"

def test_main():
    main("noodles")
    assert filechecker("noodlesquantity.csv") == "Not Empty"
    return "Passed"


if __name__ == "__main__":
    print(test_remove_punctuation())
    print(test_quantitytester())
    print(test_stopwordremover())
    print(test_ngramcreator())
    print(test_scrape())
    print(test_csvquantity())
    print(test_main())