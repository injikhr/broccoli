from .. import errors
from ..utils import cryptoutils
from ..models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class UserTokenResponse(APIView):

    """
    [POST] /api/user/token
    @PathVariable: nil
    @RequestParam: nil
    @RequestBody: {
        password:   string,
        keystore:   { did: string, walletAddress: string, privKey: string, pubKey: string }
    }
    """
    @staticmethod
    def gen_post_response(access_token, code=status.HTTP_200_OK, err=None):
        return Response(
            {
                "error": err,
                "access_token": access_token,
            },
            status=code,
        )

    def post(self, request):
        try:
            # Get keystore
            keystore = request.data["keystore"]

            # Generate password hash
            password = cryptoutils.hash_dict({
                "password": request.data["password"],
                "keystore": keystore,
            })

            # SELECT 1 FROM user;
            is_user_exists = User.objects.filter(
                did = keystore["did"],
                password = password,
            ).exists()

            # Validate: User not found
            if not is_user_exists:
                raise errors.AuthorizationFailedError("User not found")

            # Validate: User found
            access_token = cryptoutils.gen_JWT(keystore["did"])
            res = self.gen_post_response(access_token)
            res.set_cookie("access_token", access_token)
            return res

        # Handle all known error
        except errors.BaseError as err:
            return err.gen_response()

        except KeyError as err:
            return errors.ClientFaultError(err).gen_response()

        # Handle unhandled error
        except Exception as err:
            return errors.UnhandledError(err).gen_response()
