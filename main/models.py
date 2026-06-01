#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    zhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    shouhuodizhi=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收货地址' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='积分' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    email=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    status=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='状态' )
    '''
    zhanghao=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    shoujihaoma=VARCHAR
    shouhuodizhi=VARCHAR
    jifen=Float
    touxiang=Text
    email=VARCHAR
    status=Integer
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class dianyuan(BaseModel):
    __doc__ = u'''dianyuan'''
    __tablename__ = 'dianyuan'

    __loginUser__='gonghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='gonghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='是'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    gonghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='工号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yuangongxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='员工姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    lianxifangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系方式' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    email=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    '''
    gonghao=VARCHAR
    mima=VARCHAR
    yuangongxingming=VARCHAR
    xingbie=VARCHAR
    lianxifangshi=VARCHAR
    touxiang=Text
    email=VARCHAR
    '''
    class Meta:
        db_table = 'dianyuan'
        verbose_name = verbose_name_plural = '店员'
class chongwufuwu(BaseModel):
    __doc__ = u'''chongwufuwu'''
    __tablename__ = 'chongwufuwu'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='用协'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    fuwumingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='服务名称' )
    fuwufengmian=models.TextField   (  null=True, unique=False, verbose_name='服务封面' )
    fuwuleixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='服务类型' )
    fuwufanwei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务范围' )
    chongwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物类型' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='服务价格' )
    fuwushizhang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务时长' )
    fuwujieshao=models.TextField   (  null=True, unique=False, verbose_name='服务介绍' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    fuwumingcheng=VARCHAR
    fuwufengmian=Text
    fuwuleixing=VARCHAR
    fuwufanwei=VARCHAR
    chongwuleixing=VARCHAR
    jifen=Float
    fuwushizhang=VARCHAR
    fuwujieshao=Text
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'chongwufuwu'
        verbose_name = verbose_name_plural = '宠物服务'
class chongwuyongpin(BaseModel):
    __doc__ = u'''chongwuyongpin'''
    __tablename__ = 'chongwuyongpin'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='用协'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    shangpinmingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品名称' )
    shangpinfengmian=models.TextField   (  null=True, unique=False, verbose_name='商品封面' )
    shangpinleixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='商品类型' )
    guige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='规格' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    chandi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='产地' )
    shangpinjianjie=models.TextField   (  null=True, unique=False, verbose_name='商品简介' )
    jiage=models.FloatField   (  null=True, unique=False, verbose_name='价格' )
    kucun=models.IntegerField  (  null=True, unique=False, verbose_name='库存' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    shangpinmingcheng=VARCHAR
    shangpinfengmian=Text
    shangpinleixing=VARCHAR
    guige=VARCHAR
    pinpai=VARCHAR
    chandi=VARCHAR
    shangpinjianjie=Text
    jiage=Float
    kucun=Integer
    clicktime=DateTime
    clicknum=Integer
    discussnum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'chongwuyongpin'
        verbose_name = verbose_name_plural = '宠物用品'
class jiyangfuwu(BaseModel):
    __doc__ = u'''jiyangfuwu'''
    __tablename__ = 'jiyangfuwu'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    fuwumingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='服务名称' )
    fuwufengmian=models.TextField   (  null=True, unique=False, verbose_name='服务封面' )
    fuwuleixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='服务类型' )
    chongwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物类型' )
    baohanxiangmu=models.TextField   (  null=True, unique=False, verbose_name='包含项目' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='价格' )
    xiangqing=models.TextField   (  null=True, unique=False, verbose_name='详情' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    fuwumingcheng=VARCHAR
    fuwufengmian=Text
    fuwuleixing=VARCHAR
    chongwuleixing=VARCHAR
    baohanxiangmu=Text
    jifen=Float
    xiangqing=Text
    discussnum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'jiyangfuwu'
        verbose_name = verbose_name_plural = '寄养服务'
class zaishouchongwu(BaseModel):
    __doc__ = u'''zaishouchongwu'''
    __tablename__ = 'zaishouchongwu'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    chongwunicheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='宠物昵称' )
    chongwupinzhong=models.CharField ( max_length=255,null=False, unique=False, verbose_name='宠物品种' )
    chongwutupian=models.TextField   (  null=True, unique=False, verbose_name='宠物图片' )
    zhonglei=models.CharField ( max_length=255,null=False, unique=False, verbose_name='种类' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    chushengriqi=models.DateField   (  null=True, unique=False, verbose_name='出生日期' )
    yanse=models.CharField ( max_length=255, null=True, unique=False, verbose_name='颜色' )
    aihao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='爱好' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='售价' )
    yimiaojilu=models.TextField   (  null=True, unique=False, verbose_name='疫苗记录' )
    quchongjilu=models.TextField   (  null=True, unique=False, verbose_name='驱虫记录' )
    chushouzhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='出售状态' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    chongwunicheng=VARCHAR
    chongwupinzhong=VARCHAR
    chongwutupian=Text
    zhonglei=VARCHAR
    xingbie=VARCHAR
    chushengriqi=Date
    yanse=VARCHAR
    aihao=VARCHAR
    jifen=Float
    yimiaojilu=Text
    quchongjilu=Text
    chushouzhuangtai=VARCHAR
    discussnum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'zaishouchongwu'
        verbose_name = verbose_name_plural = '在售宠物'
class lingyangchongwu(BaseModel):
    __doc__ = u'''lingyangchongwu'''
    __tablename__ = 'lingyangchongwu'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    chongwunicheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='宠物昵称' )
    chongwupinzhong=models.CharField ( max_length=255,null=False, unique=False, verbose_name='宠物品种' )
    chongwutupian=models.TextField   (  null=True, unique=False, verbose_name='宠物图片' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    chushengriqi=models.DateField   (  null=True, unique=False, verbose_name='出生日期' )
    xinggetedian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性格特点' )
    yimiaojilu=models.TextField   (  null=True, unique=False, verbose_name='疫苗记录' )
    lingyangzhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='领养状态' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    chongwunicheng=VARCHAR
    chongwupinzhong=VARCHAR
    chongwutupian=Text
    xingbie=VARCHAR
    chushengriqi=Date
    xinggetedian=VARCHAR
    yimiaojilu=Text
    lingyangzhuangtai=VARCHAR
    discussnum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'lingyangchongwu'
        verbose_name = verbose_name_plural = '领养宠物'
class jifenlipin(BaseModel):
    __doc__ = u'''jifenlipin'''
    __tablename__ = 'jifenlipin'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    lipinmingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='礼品名称' )
    lipinfengmian=models.TextField   (  null=True, unique=False, verbose_name='礼品封面' )
    lipinleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='礼品类型' )
    guige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='规格' )
    lipinjianjie=models.TextField   (  null=True, unique=False, verbose_name='礼品简介' )
    duihuanjifen=models.FloatField   (  null=True, unique=False, verbose_name='兑换积分' )
    kucun=models.IntegerField  (  null=True, unique=False, verbose_name='库存' )
    discussnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='评论数' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    lipinmingcheng=VARCHAR
    lipinfengmian=Text
    lipinleixing=VARCHAR
    guige=VARCHAR
    lipinjianjie=Text
    duihuanjifen=Float
    kucun=Integer
    discussnum=Integer
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'jifenlipin'
        verbose_name = verbose_name_plural = '积分礼品'
class chongwuxinxi(BaseModel):
    __doc__ = u'''chongwuxinxi'''
    __tablename__ = 'chongwuxinxi'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    chongwuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物姓名' )
    chongwutupian=models.TextField   (  null=True, unique=False, verbose_name='宠物图片' )
    pinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品种' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    chushengriqi=models.DateField   (  null=True, unique=False, verbose_name='出生日期' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    '''
    chongwuxingming=VARCHAR
    chongwutupian=Text
    pinzhong=VARCHAR
    xingbie=VARCHAR
    chushengriqi=Date
    zhanghao=VARCHAR
    '''
    class Meta:
        db_table = 'chongwuxinxi'
        verbose_name = verbose_name_plural = '宠物信息'
class fuwudingdan(BaseModel):
    __doc__ = u'''fuwudingdan'''
    __tablename__ = 'fuwudingdan'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='订单编号' )
    fuwumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务名称' )
    fuwufengmian=models.TextField   (  null=True, unique=False, verbose_name='服务封面' )
    fuwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务类型' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='服务价格' )
    fuwushizhang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务时长' )
    chongwuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='宠物姓名' )
    pinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品种' )
    yuyueriqi=models.DateField   ( null=False, unique=False, verbose_name='预约日期' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    xiadanshijian=models.DateField   (  null=True, unique=False, verbose_name='下单时间' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    dingdanbianhao=VARCHAR
    fuwumingcheng=VARCHAR
    fuwufengmian=Text
    fuwuleixing=VARCHAR
    jifen=Float
    fuwushizhang=VARCHAR
    chongwuxingming=VARCHAR
    pinzhong=VARCHAR
    yuyueriqi=Date
    beizhu=VARCHAR
    xiadanshijian=Date
    zhanghao=VARCHAR
    xingming=VARCHAR
    shoujihaoma=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'fuwudingdan'
        verbose_name = verbose_name_plural = '服务订单'
class jiyangdingdan(BaseModel):
    __doc__ = u'''jiyangdingdan'''
    __tablename__ = 'jiyangdingdan'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='订单编号' )
    fuwumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务名称' )
    fuwufengmian=models.TextField   (  null=True, unique=False, verbose_name='服务封面' )
    fuwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务类型' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='价格' )
    jiyangriqi=models.DateField   ( null=False, unique=False, verbose_name='寄养日期' )
    chongwuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='宠物姓名' )
    pinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品种' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    xiadanshijian=models.DateField   (  null=True, unique=False, verbose_name='下单时间' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    dingdanbianhao=VARCHAR
    fuwumingcheng=VARCHAR
    fuwufengmian=Text
    fuwuleixing=VARCHAR
    jifen=Float
    jiyangriqi=Date
    chongwuxingming=VARCHAR
    pinzhong=VARCHAR
    beizhu=VARCHAR
    xiadanshijian=Date
    zhanghao=VARCHAR
    xingming=VARCHAR
    shoujihaoma=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'jiyangdingdan'
        verbose_name = verbose_name_plural = '寄养订单'
class chongwudingdan(BaseModel):
    __doc__ = u'''chongwudingdan'''
    __tablename__ = 'chongwudingdan'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='订单编号' )
    chongwunicheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物昵称' )
    chongwupinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物品种' )
    chongwutupian=models.TextField   (  null=True, unique=False, verbose_name='宠物图片' )
    yanse=models.CharField ( max_length=255, null=True, unique=False, verbose_name='颜色' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='售价' )
    xiadanriqi=models.DateField   (  null=True, unique=False, verbose_name='下单日期' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    dingdanbianhao=VARCHAR
    chongwunicheng=VARCHAR
    chongwupinzhong=VARCHAR
    chongwutupian=Text
    yanse=VARCHAR
    jifen=Float
    xiadanriqi=Date
    beizhu=VARCHAR
    zhanghao=VARCHAR
    xingming=VARCHAR
    shoujihaoma=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'chongwudingdan'
        verbose_name = verbose_name_plural = '宠物订单'
class lingyangshenqing(BaseModel):
    __doc__ = u'''lingyangshenqing'''
    __tablename__ = 'lingyangshenqing'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    shenqingbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='申请编号' )
    chongwunicheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物昵称' )
    chongwupinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物品种' )
    chongwutupian=models.TextField   (  null=True, unique=False, verbose_name='宠物图片' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    xinggetedian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性格特点' )
    shenqingriqi=models.DateField   (  null=True, unique=False, verbose_name='申请日期' )
    lingyangshuoming=models.TextField   (  null=True, unique=False, verbose_name='领养说明' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    shenqingbianhao=VARCHAR
    chongwunicheng=VARCHAR
    chongwupinzhong=VARCHAR
    chongwutupian=Text
    xingbie=VARCHAR
    xinggetedian=VARCHAR
    shenqingriqi=Date
    lingyangshuoming=Text
    zhanghao=VARCHAR
    xingming=VARCHAR
    shoujihaoma=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'lingyangshenqing'
        verbose_name = verbose_name_plural = '领养申请'
class duihuandingdan(BaseModel):
    __doc__ = u'''duihuandingdan'''
    __tablename__ = 'duihuandingdan'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    duihuanbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='兑换编号' )
    lipinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='礼品名称' )
    lipinfengmian=models.TextField   (  null=True, unique=False, verbose_name='礼品封面' )
    lipinleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='礼品类型' )
    guige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='规格' )
    duihuanjifen=models.FloatField   (  null=True, unique=False, verbose_name='兑换积分' )
    kucun=models.IntegerField  ( null=False, unique=False, verbose_name='兑换数量' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='应付积分' )
    duihuanriqi=models.DateField   (  null=True, unique=False, verbose_name='兑换日期' )
    duihuanbeizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='兑换备注' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    duihuanbianhao=VARCHAR
    lipinmingcheng=VARCHAR
    lipinfengmian=Text
    lipinleixing=VARCHAR
    guige=VARCHAR
    duihuanjifen=Float
    kucun=Integer
    jifen=Float
    duihuanriqi=Date
    duihuanbeizhu=VARCHAR
    zhanghao=VARCHAR
    xingming=VARCHAR
    shoujihaoma=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'duihuandingdan'
        verbose_name = verbose_name_plural = '兑换订单'
class shangpindingdan(BaseModel):
    __doc__ = u'''shangpindingdan'''
    __tablename__ = 'shangpindingdan'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='订单编号' )
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    shangpinfengmian=models.TextField   (  null=True, unique=False, verbose_name='商品封面' )
    shangpinleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品类型' )
    guige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='规格' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    chandi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='产地' )
    jiage=models.FloatField   (  null=True, unique=False, verbose_name='价格' )
    kucun=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='应付金额' )
    xiadanriqi=models.DateField   (  null=True, unique=False, verbose_name='下单日期' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    shouhuodizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收货地址' )
    fahuozhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发货状态' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    dingdanbianhao=VARCHAR
    shangpinmingcheng=VARCHAR
    shangpinfengmian=Text
    shangpinleixing=VARCHAR
    guige=VARCHAR
    pinpai=VARCHAR
    chandi=VARCHAR
    jiage=Float
    kucun=Integer
    jifen=Float
    xiadanriqi=Date
    zhanghao=VARCHAR
    xingming=VARCHAR
    shoujihaoma=VARCHAR
    shouhuodizhi=VARCHAR
    fahuozhuangtai=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'shangpindingdan'
        verbose_name = verbose_name_plural = '商品订单'
class fahuojilu(BaseModel):
    __doc__ = u'''fahuojilu'''
    __tablename__ = 'fahuojilu'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='订单编号' )
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    shangpinfengmian=models.TextField   (  null=True, unique=False, verbose_name='商品封面' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    jiage=models.FloatField   (  null=True, unique=False, verbose_name='价格' )
    kucun=models.IntegerField  (  null=True, unique=False, verbose_name='购买数量' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='应付金额' )
    xiadanriqi=models.DateField   (  null=True, unique=False, verbose_name='下单日期' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    shouhuodizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收货地址' )
    fahuoriqi=models.DateField   (  null=True, unique=False, verbose_name='发货日期' )
    duihuanma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='兑换码' )
    '''
    dingdanbianhao=VARCHAR
    shangpinmingcheng=VARCHAR
    shangpinfengmian=Text
    pinpai=VARCHAR
    jiage=Float
    kucun=Integer
    jifen=Float
    xiadanriqi=Date
    zhanghao=VARCHAR
    xingming=VARCHAR
    shoujihaoma=VARCHAR
    shouhuodizhi=VARCHAR
    fahuoriqi=Date
    duihuanma=VARCHAR
    '''
    class Meta:
        db_table = 'fahuojilu'
        verbose_name = verbose_name_plural = '发货记录'
class tuikuanshenqing(BaseModel):
    __doc__ = u'''tuikuanshenqing'''
    __tablename__ = 'tuikuanshenqing'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='订单编号' )
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    shangpinfengmian=models.TextField   (  null=True, unique=False, verbose_name='商品封面' )
    pinpai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    jiage=models.FloatField   (  null=True, unique=False, verbose_name='价格' )
    kucun=models.IntegerField  (  null=True, unique=False, verbose_name='购买数量' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='退款金额' )
    xiadanriqi=models.DateField   (  null=True, unique=False, verbose_name='下单日期' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    shouhuodizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收货地址' )
    shenqingriqi=models.DateField   (  null=True, unique=False, verbose_name='申请日期' )
    tuikuanyuanyin=models.TextField   (  null=True, unique=False, verbose_name='退款原因' )
    crossuserid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表用户id' )
    crossrefid=models.BigIntegerField  (  null=True, unique=False, verbose_name='跨表主键id' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    dingdanbianhao=VARCHAR
    shangpinmingcheng=VARCHAR
    shangpinfengmian=Text
    pinpai=VARCHAR
    jiage=Float
    kucun=Integer
    jifen=Float
    xiadanriqi=Date
    zhanghao=VARCHAR
    xingming=VARCHAR
    shoujihaoma=VARCHAR
    shouhuodizhi=VARCHAR
    shenqingriqi=Date
    tuikuanyuanyin=Text
    crossuserid=BigInteger
    crossrefid=BigInteger
    sfsh=VARCHAR
    shhf=Text
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'tuikuanshenqing'
        verbose_name = verbose_name_plural = '退款申请'
class jiankangshuju(BaseModel):
    __doc__ = u'''jiankangshuju'''
    __tablename__ = 'jiankangshuju'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    jilubianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='记录编号' )
    chongwuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物姓名' )
    chongwutupian=models.TextField   (  null=True, unique=False, verbose_name='宠物图片' )
    pinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品种' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    shengao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='身高cm' )
    tizhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='体重kg' )
    tiwen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='体温℃' )
    shenghuoxiguan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='生活习惯' )
    yinshipianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='饮食偏好' )
    jiankangyuce=models.TextField   (  null=True, unique=False, verbose_name='健康预测' )
    '''
    jilubianhao=VARCHAR
    chongwuxingming=VARCHAR
    chongwutupian=Text
    pinzhong=VARCHAR
    xingbie=VARCHAR
    zhanghao=VARCHAR
    shengao=VARCHAR
    tizhong=VARCHAR
    tiwen=VARCHAR
    shenghuoxiguan=VARCHAR
    yinshipianhao=VARCHAR
    jiankangyuce=Text
    '''
    class Meta:
        db_table = 'jiankangshuju'
        verbose_name = verbose_name_plural = '健康数据'
class chongwuhudong(BaseModel):
    __doc__ = u'''chongwuhudong'''
    __tablename__ = 'chongwuhudong'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='订单编号' )
    fuwumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='服务名称' )
    jifen=models.FloatField   (  null=True, unique=False, verbose_name='价格' )
    jiyangriqi=models.DateField   (  null=True, unique=False, verbose_name='寄养日期' )
    chongwuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物姓名' )
    pinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品种' )
    gengxinriqi=models.DateField   (  null=True, unique=False, verbose_name='更新日期' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    chongwuzhaopian=models.TextField   (  null=True, unique=False, verbose_name='宠物照片' )
    chongwushipin=models.TextField   (  null=True, unique=False, verbose_name='宠物视频' )
    chongwudongtai=models.TextField   (  null=True, unique=False, verbose_name='宠物动态' )
    '''
    dingdanbianhao=VARCHAR
    fuwumingcheng=VARCHAR
    jifen=Float
    jiyangriqi=Date
    chongwuxingming=VARCHAR
    pinzhong=VARCHAR
    gengxinriqi=Date
    zhanghao=VARCHAR
    chongwuzhaopian=Text
    chongwushipin=Text
    chongwudongtai=Text
    '''
    class Meta:
        db_table = 'chongwuhudong'
        verbose_name = verbose_name_plural = '宠物互动'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    name=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    headportrait=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    title=VARCHAR
    introduction=Text
    picture=Text
    content=Text
    name=VARCHAR
    headportrait=Text
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '公告信息'
class forum(BaseModel):
    __doc__ = u'''forum'''
    __tablename__ = 'forum'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='是'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255, null=True, unique=False, verbose_name='帖子标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='帖子内容' )
    parentid=models.BigIntegerField  (  null=True, unique=False, verbose_name='父节点id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    isdone=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='是否置顶' )
    toptime=models.DateTimeField  (  null=True, unique=False, verbose_name='置顶时间' )
    cover=models.TextField   (  null=True, unique=False, verbose_name='封面' )
    isanon=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='是否匿名(1:是,0:否)' )
    delflag=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='是否删除(1:是,0:否)' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    '''
    title=VARCHAR
    content=Text
    parentid=BigInteger
    username=VARCHAR
    avatarurl=Text
    isdone=VARCHAR
    istop=Integer
    toptime=DateTime
    cover=Text
    isanon=Integer
    delflag=Integer
    userid=BigInteger
    storeupnum=Integer
    '''
    class Meta:
        db_table = 'forum'
        verbose_name = verbose_name_plural = '宠物论坛'
class chat(BaseModel):
    __doc__ = u'''chat'''
    __tablename__ = 'chat'



    __authTables__={}
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    adminid=models.BigIntegerField  (  null=True, unique=False, verbose_name='管理员id' )
    ask=models.TextField   (  null=True, unique=False, verbose_name='提问' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复' )
    isreply=models.IntegerField  (  null=True, unique=False, verbose_name='是否回复' )
    isread=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='已读/未读(1:已读,0:未读)' )
    uname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    uimage=models.TextField   (  null=True, unique=False, verbose_name='用户头像' )
    type=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='内容类型(1:文本,2:图片,3:视频,4:文件,5:表情)' )
    '''
    userid=BigInteger
    adminid=BigInteger
    ask=Text
    reply=Text
    isreply=Integer
    isread=Integer
    uname=VARCHAR
    uimage=Text
    type=Integer
    '''
    class Meta:
        db_table = 'chat'
        verbose_name = verbose_name_plural = '在线客服'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class systemintro(BaseModel):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'systemintro'
        verbose_name = verbose_name_plural = '系统简介'
class emailregistercode(BaseModel):
    __doc__ = u'''emailregistercode'''
    __tablename__ = 'emailregistercode'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    email=models.CharField ( max_length=255,null=False, unique=False, verbose_name='邮箱' )
    role=models.CharField ( max_length=255,null=False, unique=False, verbose_name='角色' )
    code=models.CharField ( max_length=255,null=False, unique=False, verbose_name='验证码' )
    '''
    email=VARCHAR
    role=VARCHAR
    code=VARCHAR
    '''
    class Meta:
        db_table = 'emailregistercode'
        verbose_name = verbose_name_plural = '邮箱验证码'
class users(BaseModel):
    __doc__ = u'''users'''
    __tablename__ = 'users'



    __authTables__={}
    __authPeople__ = '是'
    __isAdmin__ = '是'
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    username=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户名' )
    password=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    role=models.CharField ( max_length=255, null=True, unique=False,default='管理员', verbose_name='角色' )
    image=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    username=VARCHAR
    password=VARCHAR
    role=VARCHAR
    image=Text
    '''
    class Meta:
        db_table = 'users'
        verbose_name = verbose_name_plural = '管理员'
class discusschongwufuwu(BaseModel):
    __doc__ = u'''discusschongwufuwu'''
    __tablename__ = 'discusschongwufuwu'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discusschongwufuwu'
        verbose_name = verbose_name_plural = '宠物服务评论'
class discusschongwuyongpin(BaseModel):
    __doc__ = u'''discusschongwuyongpin'''
    __tablename__ = 'discusschongwuyongpin'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discusschongwuyongpin'
        verbose_name = verbose_name_plural = '宠物用品评论'
class discussjiyangfuwu(BaseModel):
    __doc__ = u'''discussjiyangfuwu'''
    __tablename__ = 'discussjiyangfuwu'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discussjiyangfuwu'
        verbose_name = verbose_name_plural = '寄养服务评论'
class discusszaishouchongwu(BaseModel):
    __doc__ = u'''discusszaishouchongwu'''
    __tablename__ = 'discusszaishouchongwu'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discusszaishouchongwu'
        verbose_name = verbose_name_plural = '在售宠物评论'
class discusslingyangchongwu(BaseModel):
    __doc__ = u'''discusslingyangchongwu'''
    __tablename__ = 'discusslingyangchongwu'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discusslingyangchongwu'
        verbose_name = verbose_name_plural = '领养宠物评论'
class discussjifenlipin(BaseModel):
    __doc__ = u'''discussjifenlipin'''
    __tablename__ = 'discussjifenlipin'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='关联表id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='评论内容' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    istop=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='置顶' )
    tuserids=models.TextField   (  null=True, unique=False, verbose_name='赞用户ids' )
    cuserids=models.TextField   (  null=True, unique=False, verbose_name='踩用户ids' )
    '''
    refid=BigInteger
    userid=BigInteger
    avatarurl=Text
    nickname=VARCHAR
    content=Text
    reply=Text
    thumbsupnum=Integer
    crazilynum=Integer
    istop=Integer
    tuserids=Text
    cuserids=Text
    '''
    class Meta:
        db_table = 'discussjifenlipin'
        verbose_name = verbose_name_plural = '积分礼品评论'
