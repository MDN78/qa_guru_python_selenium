# 1 Повторить код из урока и отрефакторить  
возможно коректируя селекторы   
Отрефакторить рабочий код до версии

```python
driver.get('https://ecosia.org')
query = '[name=q]'
type(query, value='selene' + Keys.ENTER)
driver.back()
type(query, value=' yashaka' + Keys.ENTER)
click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=4)
driver.quit()
```  


