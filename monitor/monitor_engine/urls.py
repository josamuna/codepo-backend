from django.urls import path
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    # All path related to devices
    path('device/show/all', views.getAllDevices),
    path('device/show/<int:pk>', views.getDeviceById),
    path('device/save', views.createDevice),
    path('device/update/<int:pk>', views.updateDevice),
    path('device/delete/<int:pk>', views.deleteDevice),
    path('device/statistic/count', views.getNumberDevice),
    path('device/publish', views.publish_mqtt),
    path('device/position/show/all', views.getDeviceData),
    path('device/history/show/all', views.getLocationHistory),
    path('device/history/show/<int:pk>', views.getDeviceHistory),
    path('device/restore/<int:pk>', views.restoreDevice),
    path('device/force/delete/<int:pk>', views.permanentlyDeleteDevice),
    path('device/deleted/show/all', views.getAllDeletedDevices),
    path('device/follow', views.followDevice),
    path('device/follow/show', views.getFollowedDevices),
    # path('device/notification/save', views.saveNotification),

    # All path related to users
    path('user/show/all', views.getAllUsers),
    path('user/show/<int:pk>', views.getUserById),
    path('user/save', views.createUser),
    path('user/update/<int:pk>', views.updateUser),
    path('user/delete/<int:pk>', views.deleteUser),
    path('user/login', views.loginUser),
    path('user/statistic/count', views.getNumberUser),
    path('user/restore/<int:pk>', views.restoreUser),
    path('user/force/delete/<int:pk>', views.permanentlyDeleteUser),
    path('user/deleted/show/all', views.getAllDeleteUsers),
    path('user/color/save', views.saveColorPreference),
    path('user/color/preference/show/<int:pk>', views.getColorPreference),
    path('user/notification/show/<int:pk>', views.getUserNotification),
    path('user/notification/read/<int:pk>', views.alreadyRead),
    path('user/mail/send', views.sendMail),

    # All path related to commands
    path('command/show/all', views.getAllCommands),
    path('command/show/<int:pk>', views.getCommandById),
    path('command/save', views.createCommand),
    path('command/update/<int:pk>', views.updateCommand),
    path('command/delete/<int:pk>', views.deleteCommand),
    path('command/search/<str:element>', views.searchCommand),
    path('command/restore/<int:pk>', views.restoreCommand),
    path('command/force/delete/<int:pk>', views.permanentlyDeleteCommand),
    path('command/deleted/show/all', views.getAllDeletedCommands),

    # All path related to token
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
