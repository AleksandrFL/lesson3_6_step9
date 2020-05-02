import time

def test_button_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # ожидание чтобы увидеть фразу на кнопке добавления в корзину
    #time.sleep(30)
   
    #Определим список найденных элементов
    button_basket = browser.find_elements_by_css_selector(".btn-add-to-basket")
    
    #Проверим его на наличие элементов
    assert len(button_basket)>0, "Корзина не найдена"
    
    