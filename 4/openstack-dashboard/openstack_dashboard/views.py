# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django import shortcuts
from django.views.decorators import vary
from django.shortcuts import render

import horizon

from openstack_auth import views

#huoqu yonghuming , panduan yonghu quanxian ,yongyu shezhi tiaozhuanjiemian

def get_user_home(user):
    if user.is_superuser:
        return horizon.get_dashboard('admin').get_absolute_url()
    return horizon.get_dashboard('project').get_absolute_url()


@vary.vary_on_cookie
#huoqu denglu jiemian de yonghuming he mima , yanzheng tongguo ze panduan yonghuquanxian, fouze shuaxin
def splash(request):
    if request.user.is_authenticated():
       return shortcuts.redirect(get_user_home(request.user))
#       return shortcuts.render(request, "admin")
    form = views.Login(request)
    request.session.clear()
    request.session.set_test_cookie()
    return shortcuts.render(request, 'splash.html', {'form': form})

def index(request):
    return render(request,'index.html')
