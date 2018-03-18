from selenium import webdriver

def test_hello():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    
    driver.get('http://localhost:8080/hello')
    assert "Hello" in driver.page_source
