import urllib3

def test_homepage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/')
    assert 200 == r.status

def test_aboutpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/about')
    assert 200 == r.status

def test_shopsummerclothespage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/shopclothes')
    assert 200 == r.status



def test_shopwinterclothespage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/shopclotheswinter')
    assert 200 == r.status

def test_contactpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/contact')
    assert 200 == r.status

def test_registerpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/register/')
    assert 200 == r.status

def test_loginpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/login/')
    assert 200 == r.status

def test_crudpage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/crud')
    assert 200 == r.status
  
def test_nopage():
    http = urllib3.PoolManager()
    r = http.request('GET','http://35.246.41.188:5000/crudoperation')
    assert 404 == r.status
  