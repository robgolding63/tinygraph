from django.conf.urls.defaults import *
from piston.resource import Resource
from api.views.definitions import DataObjectHandler, PackageHandler, \
    MibUploadHandler, PackageMembershipHandler

data_object_handler = Resource(DataObjectHandler)
package_handler = Resource(PackageHandler)
mib_upload_handler = Resource(MibUploadHandler)
package_membership_handler = Resource(PackageMembershipHandler)

urlpatterns = patterns('',
    url(r'^data-object/$', data_object_handler, name='data_objects'),
    url(r'^data-object/(?P<id>\d+)/$', data_object_handler, name='data_object'),
    
    url(r'^package/$', package_handler, name='packages'),
    url(r'^package/(?P<id>\d+)/$', package_handler, name='package'),
    
    url(r'^package-membership/$', package_membership_handler, name='package_memberships'),
    url(r'^package-membership/(?P<id>\d+)/$', package_membership_handler, name='package_membership'),
)