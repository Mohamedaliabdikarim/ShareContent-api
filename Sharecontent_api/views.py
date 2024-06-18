from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE, JWT_AUTH_SECURE)


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my Sharecontent API!"
    }
    )
    @api_view(['POST'])
    def logout_route(request):
        response = Response()
        response.set_cookie(
            key=JWT_AUTH_COOKIE,
            value='',
            httponly=True
            exists ='Thu,01 jan 1970 00:00:00 GMT',
            max=0,
            samesite= JWT_AUTH_SAMESITE
            secure = JWT_AUTH_SECURE
        )
        response.set_cookie(
            key=JWT_AUTH_REFRESH_COOKIE,
            value='',
            httponly=True,
            expires='Thu,01 jan 1970 00:00:00 GMT',
            samesite= = JWT_AUTH_SAMESITE,
            secure = JWT_AUTH_SECURE,

        )
        return response

