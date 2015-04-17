# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
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

"""
URL patterns for the OpenStack Dashboard.
"""

from django.conf import settings  # noqa
from django.conf.urls.defaults import include  # noqa
from django.conf.urls.defaults import patterns  # noqa
from django.conf.urls.defaults import url  # noqa
from django.conf.urls.static import static  # noqa
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # noqa

import horizon


urlpatterns = patterns('',
#    url(r'^$', 'openstack_dashboard.views.index', name='index'),
    url(r'^$', 'openstack_dashboard.views.splash', name='splash'),
#    url(r'^splash/', 'openstack_dashboard.views.splash', name='splash'),
    url(r'^auth/', include('openstack_auth.urls')),
#    url(r'^index1/', 'openstack_dashboard.views.index1', name='index1')
    url(r'', include(horizon.urls)),
)

# Development static app and project media serving using the staticfiles app.
urlpatterns += staticfiles_urlpatterns()

# Convenience function for serving user-uploaded media during
# development. Only active if DEBUG==True and the URL prefix is a local
# path. Production media should NOT be served by Django.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^500/$', 'django.views.defaults.server_error')
    )
