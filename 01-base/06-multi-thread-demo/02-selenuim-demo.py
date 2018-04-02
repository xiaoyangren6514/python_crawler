from selenium import webdriver


def main():
    browser = webdriver.PhantomJS(executable_path='./phantomjs')
    browser.get("https://www.qiushibaike.com/8hr/page/1/")
    print(browser.page_source)


if __name__ == '__main__':
    main()

