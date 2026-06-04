# coding:utf-8
import ast
import base64
import copy
import json
from django.http import JsonResponse
from django.apps import apps

from util.codes import *
from util import message as mes


def _encode_token_payload(payload):
    return base64.b64encode(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).decode("utf-8")


def _decode_token_payload(token):
    decoded = base64.b64decode(token).decode("utf-8")
    try:
        return json.loads(decoded)
    except json.JSONDecodeError:
        legacy_payload = decoded.replace('"null"', '""').replace("null", '""')
        return ast.literal_eval(legacy_payload)


class Auth(object):
    def authenticate(self, model, req_dict):
        """
        用户登录，登录成功返回token；登录失败返回失败原因
        :param username:账号
        :param password:密码
        :return: json
        """
        msg = {'code': normal_code, 'msg': mes.normal_code, 'data': {}}
        tablename = model.__tablename__
        encode_dict = {"tablename": tablename, "params": req_dict}

        msg['data']["id"] = req_dict.get("id")
        msg["id"] = req_dict.get("id")
        msg["username"] = req_dict.get("username")
        msg['token'] = _encode_token_payload(encode_dict)
        return JsonResponse(msg)

    def get_token(self, model, req_dict):
        tablename=model.__tablename__
        encode_dict = {"tablename":tablename, "params": req_dict}

        return _encode_token_payload(encode_dict)

    def identify(self, request):
        """
        用户鉴权
        :param request:本次请求对象
        :return: list
        """

        msg = {'code': normal_code, 'msg': mes.normal_code, 'data': {}}
        # django的header被处理过了
        token = request.META.get('HTTP_TOKEN')

        if token  and token !="null":

            auth_token = copy.deepcopy(token)

            decode_dict = _decode_token_payload(auth_token)

            tablename2 = decode_dict.get("tablename")

            params2 = decode_dict.get("params",{})

            datas=None
            allModels = apps.get_app_config('main').get_models()
            for model in allModels:
                if model.__tablename__ == tablename2:
                    datas = model.getbyparams(model, model, params2)

            if not datas:
                msg['code'] = 401
                msg['msg'] = '找不到该用户信息'
                result = msg
            else:
                request.session['tablename'] = tablename2
                request.session['params'] = params2
                msg['msg'] = '身份验证通过。'
                result = msg
        else:
            msg['code'] = 401
            msg['msg'] = 'headers未包含认证信息。'
            result = msg
        return result

    def getTokenInfo(self, request):
        try:
            token = request.META.get('HTTP_TOKEN')
            return _decode_token_payload(token)
        except:
            return {}
