# coding:utf-8

import logging
import importlib
import os
from django.urls import path
from main import config_v, schema_v
logger = logging.getLogger(__name__)
# from dj2.settings import dbName as schemaName
# url规则列表
urlpatterns = [
    path(r'config/page', config_v.config_page),
    path(r'config/list', config_v.config_list),
    path(r'config/save', config_v.config_save),
    path(r'config/add', config_v.config_add),
    path(r'config/info/<id_>', config_v.config_info),
    path(r'config/info', config_v.config_info_request),
    path(r'config/detail/<id_>', config_v.config_detail),
    path(r'config/update', config_v.config_update),
    path(r'config/delete', config_v.config_delete),
]
# main app的路径
mainDir = os.path.join(os.getcwd(), "main")

# 过滤文件的列表
excludeList = [
    "schema_v.py",
    "config_v.py",
]

view_modules = {}
for i in os.listdir(mainDir):
    if i not in excludeList and i[-5:] == "_v.py":
        tableName = i[:-5].replace(" ", "").strip()
        view_modules[tableName.lower()] = importlib.import_module("main.{}".format(i[:-3]))


def route_view(tableName, action):
    table_name = tableName.lower()
    return getattr(view_modules[table_name], "{}_{}".format(table_name, action))

for i in os.listdir(mainDir):
    if i not in excludeList and i[-5:] == "_v.py":
        tableName = i[:-5]
        tableName = tableName.replace(" ", "").strip()
        logger.debug("Registering generated routes for table %s", tableName)

        urlpatterns.extend(
            [
                path(r'{}/default'.format(tableName.lower()),
                     route_view(tableName, "default")),
                path(r'{}/page'.format(tableName.lower()),
                     route_view(tableName, "page")),
                path(r'{}/autoSort'.format(tableName.lower()),
                     route_view(tableName, "autoSort")),

                path(r'{}/save'.format(tableName.lower()),
                     route_view(tableName, "save")),
                path(r'{}/add'.format(tableName.lower()),
                     route_view(tableName, "add")),
                path(r'{}/thumbsup/<id_>'.format(tableName.lower()),
                     route_view(tableName, "thumbsup")),
                path(r'{}/info/<id_>'.format(tableName.lower()),
                     route_view(tableName, "info")),
                path(r'{}/detail/<id_>'.format(tableName.lower()),
                     route_view(tableName, "detail")),
                path(r'{}/update'.format(tableName.lower()),
                     route_view(tableName, "update")),
                path(r'{}/delete'.format(tableName.lower()),
                     route_view(tableName, "delete")),
                path(r'{}/vote/<id_>'.format(tableName.lower()),
                     route_view(tableName, "vote")),
                path(r'{}/importExcel'.format(tableName.lower()),
                     route_view(tableName, "importExcel")),
                path(r'{}/autoSort2'.format(tableName.lower()),
                     route_view(tableName, "autoSort2")),

            ]
        )
        #沙箱接口
        if tableName.lower()=="yonghu":
            urlpatterns.extend(
                [
                    path(r'{}/register'.format(tableName.lower()),
                         route_view(tableName, "register")),
                    path(r'{}/accountList'.format(tableName.lower()),
                         route_view(tableName, "accountList")),
                    path(r'{}/login'.format(tableName.lower()),
                         route_view(tableName, "login")),
                    path(r'{}/logout'.format(tableName.lower()),
                         route_view(tableName, "logout")),
                    path(r'{}/resetPass'.format(tableName.lower()),
                         route_view(tableName, "resetPass")),
                    path(r'{}/session'.format(tableName.lower()),
                         route_view(tableName, "session")),
                ]
            )
        if tableName.lower() == "yonghu":
            urlpatterns.extend(
                [
                    path(r'{}/sendemail'.format(tableName.lower()),
                         route_view(tableName, "sendemail")),
                    path(r'{}/sendemail/content'.format(tableName.lower()),
                         route_view(tableName, "sendemail_content")),
                    path(r'{}/sendemail/login'.format(tableName.lower()),
                         route_view(tableName, "sendemail_login")),
                    path(r'{}/email/login'.format(tableName.lower()),
                         route_view(tableName, "email_login")),
                ]
            )
        if tableName.lower()=="dianyuan":
            urlpatterns.extend(
                [
                    path(r'{}/register'.format(tableName.lower()),
                         route_view(tableName, "register")),
                    path(r'{}/accountList'.format(tableName.lower()),
                         route_view(tableName, "accountList")),
                    path(r'{}/login'.format(tableName.lower()),
                         route_view(tableName, "login")),
                    path(r'{}/logout'.format(tableName.lower()),
                         route_view(tableName, "logout")),
                    path(r'{}/resetPass'.format(tableName.lower()),
                         route_view(tableName, "resetPass")),
                    path(r'{}/session'.format(tableName.lower()),
                         route_view(tableName, "session")),
                ]
            )
        if tableName.lower() == "dianyuan":
            urlpatterns.extend(
                [
                    path(r'{}/sendemail'.format(tableName.lower()),
                         route_view(tableName, "sendemail")),
                    path(r'{}/sendemail/content'.format(tableName.lower()),
                         route_view(tableName, "sendemail_content")),
                    path(r'{}/sendemail/login'.format(tableName.lower()),
                         route_view(tableName, "sendemail_login")),
                    path(r'{}/email/login'.format(tableName.lower()),
                         route_view(tableName, "email_login")),
                ]
            )
        if tableName.lower() == "chongwuyongpin":
            urlpatterns.extend(
                [
                    path(r'chongwuyongpin/remind/<columnName>/<type>',route_view(tableName, "remind"))
                ]
            )
        if tableName.lower() == "jifenlipin":
            urlpatterns.extend(
                [
                    path(r'jifenlipin/remind/<columnName>/<type>',route_view(tableName, "remind"))
                ]
            )
        if tableName.lower()=="fuwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/value/<xColumnName>/<yColumnName>/<timeStatType>'.format(tableName.lower()),
                         route_view(tableName, "value")),
                    path(r'{}/value/<xColumnName>/<yColumnName>'.format(tableName.lower()),
                         route_view(tableName, "o_value")),
                    path(r'{}/group/<columnName>'.format(tableName.lower()),
                         route_view(tableName, "group")),
                    path(r'{}/valueMul/<xColumnName>/<timeStatType>'.format(tableName.lower()),
                         route_view(tableName, "valueMul")),
                    path(r'{}/valueMul/<xColumnName>'.format(tableName.lower()),
                         route_view(tableName, "o_valueMul")),
                ]
            )
        if tableName.lower() == "fuwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/count'.format(tableName.lower()),
                         route_view(tableName, "count")),
                ]
            )
        if tableName.lower() == "fuwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         route_view(tableName, "shBatch")),
                ]
            )
        if tableName.lower()=="jiyangdingdan":
            urlpatterns.extend(
                [
                    path(r'{}/value/<xColumnName>/<yColumnName>/<timeStatType>'.format(tableName.lower()),
                         route_view(tableName, "value")),
                    path(r'{}/value/<xColumnName>/<yColumnName>'.format(tableName.lower()),
                         route_view(tableName, "o_value")),
                    path(r'{}/group/<columnName>'.format(tableName.lower()),
                         route_view(tableName, "group")),
                    path(r'{}/valueMul/<xColumnName>/<timeStatType>'.format(tableName.lower()),
                         route_view(tableName, "valueMul")),
                    path(r'{}/valueMul/<xColumnName>'.format(tableName.lower()),
                         route_view(tableName, "o_valueMul")),
                ]
            )
        if tableName.lower() == "jiyangdingdan":
            urlpatterns.extend(
                [
                    path(r'{}/count'.format(tableName.lower()),
                         route_view(tableName, "count")),
                ]
            )
        if tableName.lower() == "jiyangdingdan":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         route_view(tableName, "shBatch")),
                ]
            )
        if tableName.lower()=="chongwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/value/<xColumnName>/<yColumnName>/<timeStatType>'.format(tableName.lower()),
                         route_view(tableName, "value")),
                    path(r'{}/value/<xColumnName>/<yColumnName>'.format(tableName.lower()),
                         route_view(tableName, "o_value")),
                    path(r'{}/group/<columnName>'.format(tableName.lower()),
                         route_view(tableName, "group")),
                    path(r'{}/valueMul/<xColumnName>/<timeStatType>'.format(tableName.lower()),
                         route_view(tableName, "valueMul")),
                    path(r'{}/valueMul/<xColumnName>'.format(tableName.lower()),
                         route_view(tableName, "o_valueMul")),
                ]
            )
        if tableName.lower() == "chongwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/count'.format(tableName.lower()),
                         route_view(tableName, "count")),
                ]
            )
        if tableName.lower() == "chongwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         route_view(tableName, "shBatch")),
                ]
            )
        if tableName.lower() == "lingyangshenqing":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         route_view(tableName, "shBatch")),
                ]
            )
        if tableName.lower() == "duihuandingdan":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         route_view(tableName, "shBatch")),
                ]
            )
        if tableName.lower()=="shangpindingdan":
            urlpatterns.extend(
                [
                    path(r'{}/value/<xColumnName>/<yColumnName>/<timeStatType>'.format(tableName.lower()),
                         route_view(tableName, "value")),
                    path(r'{}/value/<xColumnName>/<yColumnName>'.format(tableName.lower()),
                         route_view(tableName, "o_value")),
                    path(r'{}/group/<columnName>'.format(tableName.lower()),
                         route_view(tableName, "group")),
                    path(r'{}/valueMul/<xColumnName>/<timeStatType>'.format(tableName.lower()),
                         route_view(tableName, "valueMul")),
                    path(r'{}/valueMul/<xColumnName>'.format(tableName.lower()),
                         route_view(tableName, "o_valueMul")),
                ]
            )
        if tableName.lower() == "shangpindingdan":
            urlpatterns.extend(
                [
                    path(r'{}/count'.format(tableName.lower()),
                         route_view(tableName, "count")),
                ]
            )
        if tableName.lower() == "shangpindingdan":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         route_view(tableName, "shBatch")),
                ]
            )
        if tableName.lower() == "tuikuanshenqing":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         route_view(tableName, "shBatch")),
                ]
            )
        if tableName.lower() == "jiankangshuju":
            urlpatterns.extend(
                [
                    path(r'jiankangshuju/remind/<columnName>/<type>',route_view(tableName, "remind"))
                ]
            )
        if tableName.lower() == "chat":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        if tableName.lower() == "storeup":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        if tableName.lower() == "systemintro":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        if tableName.lower() == "emailregistercode":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        if tableName.lower()=="users":
            urlpatterns.extend(
                [
                    path(r'{}/register'.format(tableName.lower()),
                         route_view(tableName, "register")),
                    path(r'{}/accountList'.format(tableName.lower()),
                         route_view(tableName, "accountList")),
                    path(r'{}/login'.format(tableName.lower()),
                         route_view(tableName, "login")),
                    path(r'{}/logout'.format(tableName.lower()),
                         route_view(tableName, "logout")),
                    path(r'{}/resetPass'.format(tableName.lower()),
                         route_view(tableName, "resetPass")),
                    path(r'{}/session'.format(tableName.lower()),
                         route_view(tableName, "session")),
                ]
            )
        if tableName.lower() == "users":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        if tableName.lower() == "discusschongwufuwu":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        if tableName.lower() == "discusschongwuyongpin":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        if tableName.lower() == "discussjiyangfuwu":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        if tableName.lower() == "discusszaishouchongwu":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        if tableName.lower() == "discusslingyangchongwu":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        if tableName.lower() == "discussjifenlipin":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         route_view(tableName, "security")),
                ]
            )
        # examrecord特定接口
        if tableName.lower() == "examrecord":
            urlpatterns.extend(
                [
                    path(r'{}/groupby'.format(tableName.lower()),
                         route_view(tableName, "groupby")),
                    path(r'{}/deleteRecords'.format(tableName.lower()),
                         route_view(tableName, "deleterecords")),
                    path(r'{}/options/num'.format(tableName.lower()),
                                 route_view(tableName, "options_num")),
                ]
            )

# examrecord特定接口
        if tableName.lower() == "orders":
            urlpatterns.extend(
                [
                    path(r'{}/mch/list'.format(tableName.lower()),
                         route_view(tableName, "mch_list")),
                ]
            )

        # forum特定接口
        if tableName.lower() == "forum":
            urlpatterns.extend(
                [
                    path(r'{}/flist'.format(tableName.lower()),
                         route_view(tableName, "flist")),
                    path(r'{}/list/<id_>'.format(tableName.lower()),
                         route_view(tableName, "list_id")),
                    path(r'{}/query'.format(tableName.lower()),
                         route_view(tableName, "query")),
                    path(r'{}/list'.format(tableName.lower()),
                         route_view(tableName, "list")),
                    path(r'{}/lists'.format(tableName.lower()),
                         route_view(tableName, "lists")),
                ]
            )
        else:
            urlpatterns.extend(
                [
                    path(r'{}/list'.format(tableName.lower()),
                         route_view(tableName, "list")),
                    path(r'{}/query'.format(tableName.lower()),
                         route_view(tableName, "query")),
                    path(r'{}/lists'.format(tableName.lower()),
                         route_view(tableName, "lists")),
                ]
            )
urlpatterns.extend(
    [
        path(r'deepseek/askai', schema_v.schemaName_deepseek_askai),
        path(r'cal/<str:tableName>/<str:columnName>', schema_v.schemaName_cal),
        path(r'file/download', schema_v.schemaName_file_download),
        path(r'file/encrypt', schema_v.schemaName_file_encrypt),
        path(r'file/decrypt', schema_v.schemaName_file_decrypt),
        path(r'file/upload', schema_v.schemaName_file_upload),
        path(r'follow/<tableName>/<columnName>/<level>/<parent>', schema_v.schemaName_follow_level),
        path(r'follow/<tableName>/<columnName>', schema_v.schemaName_follow),
        path(r'location', schema_v.schemaName_location),
        path(r'matchFace', schema_v.schemaName_matchface),
        path(r'option/<tableName>/<columnName>', schema_v.schemaName_option),
        path(r'sh/<tableName>', schema_v.schemaName_sh),
        path(r'upload/<fileName>', schema_v.schemaName_upload),
        path(r'upload/<tableName>/<fileName>', schema_v.schemaName_upload_forecast),
        path(r'group/<tableName>/<columnName>', schema_v.schemaName_group_quyu),
        path(r'value/<tableName>/<xColumnName>/<yColumnName>', schema_v.schemaName_value_quyu),
        path(r'value/<tableName>/<xColumnName>/<yColumnName>/<timeStatType>', schema_v.schemaName_value_riqitj),
        path(r'spider/<tableName>', schema_v.schemaName_spider),
        path(r'updateColumn/<tableName>/<type>', schema_v.schemaName_updateColumn),
        path(r'deleteColumn/<tableName>', schema_v.schemaName_deleteColumn),
        path(r'ws', schema_v.websocket_connect),
        path(r'comment/list', schema_v.comment_list),
    ]
)

# print(urlpatterns)
