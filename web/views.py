from multiprocessing import context
from django.shortcuts import render
import xmlrpc.client
import ssl
from django.conf import settings
# Create your views here.


def index(request):
    
    url = 'https://%s/xmlrpc/' % (settings.ODOO_HOST)
    DB = settings.ODOO_DB
    USER = settings.ODOO_USER
    api_key = settings.ODOO_API_KEY
    common_proxy = xmlrpc.client.ServerProxy(url+'common',allow_none=True,verbose=False, use_datetime=True,context=ssl._create_unverified_context())
    uid = common_proxy.login(DB,USER,api_key)
    models = xmlrpc.client.ServerProxy(url+'object',allow_none=True,verbose=False, use_datetime=True,context=ssl._create_unverified_context())
    Search_and_read = models.execute_kw(DB, uid, api_key, 'product.template', 'search_read', [[['categ_id', '=', 'main']]], {'fields': ['name', 'categ_id','list_price','image_1920'], 'limit': 5})
    context = {
        "products": Search_and_read
    }
    return render(request,'index.html',context)