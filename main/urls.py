# coding:utf-8

import os
from django.urls import path
from main import config_v, schema_v
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

# 循环当前目录下的py文件

view_tuple = set()
for i in os.listdir(mainDir):
    if i not in excludeList and i[-5:] == "_v.py":
        viewName = i[:-3]  # 去掉.py后缀字符串
        view_tuple.add("from main import {}".format(viewName))

# 组合成import字符串
import_str = '\n'.join(view_tuple)
# print(import_str)
exec(import_str)

for i in os.listdir(mainDir):
    if i not in excludeList and i[-5:] == "_v.py":
        tableName = i[:-5]
        tableName = tableName.replace(" ", "").strip()
        print("tableName============>", tableName, len(tableName))

        urlpatterns.extend(
            [
                path(r'{}/default'.format(tableName.lower()),
                     eval("{}_v.{}_default".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/page'.format(tableName.lower()),
                     eval("{}_v.{}_page".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/autoSort'.format(tableName.lower()),
                     eval("{}_v.{}_autoSort".format(tableName.capitalize(), tableName.lower()))),

                path(r'{}/save'.format(tableName.lower()),
                     eval("{}_v.{}_save".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/add'.format(tableName.lower()),
                     eval("{}_v.{}_add".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/thumbsup/<id_>'.format(tableName.lower()),
                     eval("{}_v.{}_thumbsup".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/info/<id_>'.format(tableName.lower()),
                     eval("{}_v.{}_info".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/detail/<id_>'.format(tableName.lower()),
                     eval("{}_v.{}_detail".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/update'.format(tableName.lower()),
                     eval("{}_v.{}_update".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/delete'.format(tableName.lower()),
                     eval("{}_v.{}_delete".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/vote/<id_>'.format(tableName.lower()),
                     eval("{}_v.{}_vote".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/importExcel'.format(tableName.lower()),
                     eval("{}_v.{}_importExcel".format(tableName.capitalize(), tableName.lower()))),
                path(r'{}/autoSort2'.format(tableName.lower()),
                     eval("{}_v.{}_autoSort2".format(tableName.capitalize(), tableName.lower()))),

            ]
        )
        #沙箱接口
        if tableName.lower()=="yonghu":
            urlpatterns.extend(
                [
                    path(r'{}/register'.format(tableName.lower()),
                         eval("{}_v.{}_register".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/accountList'.format(tableName.lower()),
                         eval("{}_v.{}_accountList".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/login'.format(tableName.lower()),
                         eval("{}_v.{}_login".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/logout'.format(tableName.lower()),
                         eval("{}_v.{}_logout".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/resetPass'.format(tableName.lower()),
                         eval("{}_v.{}_resetPass".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/session'.format(tableName.lower()),
                         eval("{}_v.{}_session".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "yonghu":
            urlpatterns.extend(
                [
                    path(r'{}/sendemail'.format(tableName.lower()),
                         eval("{}_v.{}_sendemail".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/sendemail/content'.format(tableName.lower()),
                         eval("{}_v.{}_sendemail_content".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/sendemail/login'.format(tableName.lower()),
                         eval("{}_v.{}_sendemail_login".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/email/login'.format(tableName.lower()),
                         eval("{}_v.{}_email_login".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower()=="dianyuan":
            urlpatterns.extend(
                [
                    path(r'{}/register'.format(tableName.lower()),
                         eval("{}_v.{}_register".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/accountList'.format(tableName.lower()),
                         eval("{}_v.{}_accountList".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/login'.format(tableName.lower()),
                         eval("{}_v.{}_login".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/logout'.format(tableName.lower()),
                         eval("{}_v.{}_logout".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/resetPass'.format(tableName.lower()),
                         eval("{}_v.{}_resetPass".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/session'.format(tableName.lower()),
                         eval("{}_v.{}_session".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "dianyuan":
            urlpatterns.extend(
                [
                    path(r'{}/sendemail'.format(tableName.lower()),
                         eval("{}_v.{}_sendemail".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/sendemail/content'.format(tableName.lower()),
                         eval("{}_v.{}_sendemail_content".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/sendemail/login'.format(tableName.lower()),
                         eval("{}_v.{}_sendemail_login".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/email/login'.format(tableName.lower()),
                         eval("{}_v.{}_email_login".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "chongwuyongpin":
            urlpatterns.extend(
                [
                    path(r'chongwuyongpin/remind/<columnName>/<type>',eval("{}_v.{}_remind".format(tableName.capitalize(), tableName.lower())))
                ]
            )
        if tableName.lower() == "jifenlipin":
            urlpatterns.extend(
                [
                    path(r'jifenlipin/remind/<columnName>/<type>',eval("{}_v.{}_remind".format(tableName.capitalize(), tableName.lower())))
                ]
            )
        if tableName.lower()=="fuwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/value/<xColumnName>/<yColumnName>/<timeStatType>'.format(tableName.lower()),
                         eval("{}_v.{}_value".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/value/<xColumnName>/<yColumnName>'.format(tableName.lower()),
                         eval("{}_v.{}_o_value".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/group/<columnName>'.format(tableName.lower()),
                         eval("{}_v.{}_group".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/valueMul/<xColumnName>/<timeStatType>'.format(tableName.lower()),
                         eval("{}_v.{}_valueMul".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/valueMul/<xColumnName>'.format(tableName.lower()),
                         eval("{}_v.{}_o_valueMul".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "fuwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/count'.format(tableName.lower()),
                         eval("{}_v.{}_count".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "fuwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         eval("{}_v.{}_shBatch".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower()=="jiyangdingdan":
            urlpatterns.extend(
                [
                    path(r'{}/value/<xColumnName>/<yColumnName>/<timeStatType>'.format(tableName.lower()),
                         eval("{}_v.{}_value".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/value/<xColumnName>/<yColumnName>'.format(tableName.lower()),
                         eval("{}_v.{}_o_value".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/group/<columnName>'.format(tableName.lower()),
                         eval("{}_v.{}_group".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/valueMul/<xColumnName>/<timeStatType>'.format(tableName.lower()),
                         eval("{}_v.{}_valueMul".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/valueMul/<xColumnName>'.format(tableName.lower()),
                         eval("{}_v.{}_o_valueMul".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "jiyangdingdan":
            urlpatterns.extend(
                [
                    path(r'{}/count'.format(tableName.lower()),
                         eval("{}_v.{}_count".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "jiyangdingdan":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         eval("{}_v.{}_shBatch".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower()=="chongwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/value/<xColumnName>/<yColumnName>/<timeStatType>'.format(tableName.lower()),
                         eval("{}_v.{}_value".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/value/<xColumnName>/<yColumnName>'.format(tableName.lower()),
                         eval("{}_v.{}_o_value".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/group/<columnName>'.format(tableName.lower()),
                         eval("{}_v.{}_group".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/valueMul/<xColumnName>/<timeStatType>'.format(tableName.lower()),
                         eval("{}_v.{}_valueMul".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/valueMul/<xColumnName>'.format(tableName.lower()),
                         eval("{}_v.{}_o_valueMul".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "chongwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/count'.format(tableName.lower()),
                         eval("{}_v.{}_count".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "chongwudingdan":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         eval("{}_v.{}_shBatch".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "lingyangshenqing":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         eval("{}_v.{}_shBatch".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "duihuandingdan":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         eval("{}_v.{}_shBatch".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower()=="shangpindingdan":
            urlpatterns.extend(
                [
                    path(r'{}/value/<xColumnName>/<yColumnName>/<timeStatType>'.format(tableName.lower()),
                         eval("{}_v.{}_value".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/value/<xColumnName>/<yColumnName>'.format(tableName.lower()),
                         eval("{}_v.{}_o_value".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/group/<columnName>'.format(tableName.lower()),
                         eval("{}_v.{}_group".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/valueMul/<xColumnName>/<timeStatType>'.format(tableName.lower()),
                         eval("{}_v.{}_valueMul".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/valueMul/<xColumnName>'.format(tableName.lower()),
                         eval("{}_v.{}_o_valueMul".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "shangpindingdan":
            urlpatterns.extend(
                [
                    path(r'{}/count'.format(tableName.lower()),
                         eval("{}_v.{}_count".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "shangpindingdan":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         eval("{}_v.{}_shBatch".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "tuikuanshenqing":
            urlpatterns.extend(
                [
                    path(r'{}/shBatch'.format(tableName.lower()),
                         eval("{}_v.{}_shBatch".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "jiankangshuju":
            urlpatterns.extend(
                [
                    path(r'jiankangshuju/remind/<columnName>/<type>',eval("{}_v.{}_remind".format(tableName.capitalize(), tableName.lower())))
                ]
            )
        if tableName.lower() == "chat":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "storeup":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "systemintro":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "emailregistercode":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower()=="users":
            urlpatterns.extend(
                [
                    path(r'{}/register'.format(tableName.lower()),
                         eval("{}_v.{}_register".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/accountList'.format(tableName.lower()),
                         eval("{}_v.{}_accountList".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/login'.format(tableName.lower()),
                         eval("{}_v.{}_login".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/logout'.format(tableName.lower()),
                         eval("{}_v.{}_logout".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/resetPass'.format(tableName.lower()),
                         eval("{}_v.{}_resetPass".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/session'.format(tableName.lower()),
                         eval("{}_v.{}_session".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "users":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "discusschongwufuwu":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "discusschongwuyongpin":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "discussjiyangfuwu":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "discusszaishouchongwu":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "discusslingyangchongwu":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        if tableName.lower() == "discussjifenlipin":
            urlpatterns.extend(
                [
                    path(r'{}/security'.format(tableName.lower()),
                         eval("{}_v.{}_security".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        # examrecord特定接口
        if tableName.lower() == "examrecord":
            urlpatterns.extend(
                [
                    path(r'{}/groupby'.format(tableName.lower()),
                         eval("{}_v.{}_groupby".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/deleteRecords'.format(tableName.lower()),
                         eval("{}_v.{}_deleterecords".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/options/num'.format(tableName.lower()),
                                 eval("{}_v.{}_options_num".format(tableName.capitalize(), tableName.lower()))),
                ]
            )

# examrecord特定接口
        if tableName.lower() == "orders":
            urlpatterns.extend(
                [
                    path(r'{}/mch/list'.format(tableName.lower()),
                         eval("{}_v.{}_mch_list".format(tableName.capitalize(), tableName.lower()))),
                ]
            )

        # forum特定接口
        if tableName.lower() == "forum":
            urlpatterns.extend(
                [
                    path(r'{}/flist'.format(tableName.lower()),
                         eval("{}_v.{}_flist".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/list/<id_>'.format(tableName.lower()),
                         eval("{}_v.{}_list_id".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/query'.format(tableName.lower()),
                         eval("{}_v.{}_query".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/list'.format(tableName.lower()),
                         eval("{}_v.{}_list".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/lists'.format(tableName.lower()),
                         eval("{}_v.{}_lists".format(tableName.capitalize(), tableName.lower()))),
                ]
            )
        else:
            urlpatterns.extend(
                [
                    path(r'{}/list'.format(tableName.lower()),
                         eval("{}_v.{}_list".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/query'.format(tableName.lower()),
                         eval("{}_v.{}_query".format(tableName.capitalize(), tableName.lower()))),
                    path(r'{}/lists'.format(tableName.lower()),
                         eval("{}_v.{}_lists".format(tableName.capitalize(), tableName.lower()))),
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
