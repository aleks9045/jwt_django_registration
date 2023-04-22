# Регистрация с помощью jwt токена
Сайт доступен по адресу
# 85.192.41.43
Все пути:</br>
admin/ </br>
auth/ ^users/$ [name='user-list']</br>
auth/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']</br>
auth/ ^users/activation/$ [name='user-activation']</br>
auth/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='user-activation']</br>
auth/ ^users/me/$ [name='user-me']</br>
auth/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='user-me']</br>
auth/ ^users/resend_activation/$ [name='user-resend-activation']</br>
auth/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='user-resend-activation']</br>
auth/ ^users/reset_password/$ [name='user-reset-password']</br>
auth/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']</br>
auth/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']</br>
auth/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']</br>
auth/ ^users/reset_username/$ [name='user-reset-username']</br>
auth/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username']</br>
auth/ ^users/reset_username_confirm/$ [name='user-reset-username-confirm']</br>
auth/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username-confirm']</br>
auth/ ^users/set_password/$ [name='user-set-password']</br>
auth/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='user-set-password']</br>
auth/ ^users/set_username/$ [name='user-set-username']</br>
auth/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$ [name='user-set-username']</br>
auth/ ^users/(?P<id>[^/.]+)/$ [name='user-detail']</br>
auth/ ^users/(?P<id>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']</br>
auth/ ^$ [name='api-root']</br>
auth/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']</br>
auth/ ^jwt/create/? [name='jwt-create']</br>
auth/ ^jwt/refresh/? [name='jwt-refresh']</br>
auth/ ^jwt/verify/? [name='jwt-verify']</br>
^static/(?P<path>.*)$</br>
^media/(?P<path>.*)$</br>
</br>
