# 宠物综合服务平台 API 接口文档

## 概述

- **项目名称**：宠物综合服务平台（djangoq0l722c8）
- **技术栈**：Django 5.2 + MySQL
- **基础路径**：`/{dbName}/`（`dbName` 由 `config.ini` 配置，在 `dj2/settings.py` 中加载）
- **响应格式**：所有接口返回 JSON，格式统一为 `{"code": int, "msg": str, "data": any}`
- **认证方式**：Base64 编码的 Token，通过请求头 `HTTP_TOKEN` 传递，由 `xauth` 中间件和 `util/auth.py` 处理

---

## 目录

1. [通用响应码](#1-通用响应码)
2. [认证与用户接口](#2-认证与用户接口)
3. [标准 CRUD 接口](#3-标准-crud-接口)
4. [业务表一览](#4-业务表一览)
5. [各表字段说明](#5-各表字段说明)
6. [通用跨表接口](#6-通用跨表接口)
7. [文件接口](#7-文件接口)
8. [页面前端路由](#8-页面前端路由)

---

## 1. 通用响应码

| code | 含义 |
|------|------|
| 0    | 成功（normal_code） |
| -1   | 密码错误（password_error_code） |
| -2   | 其他错误（other_code） |
| -3   | CRUD 操作错误（crud_error_code） |
| 500  | 服务器内部错误 |

---

## 2. 认证与用户接口

### 2.1 普通用户（yonghu）

#### `POST/GET /{dbName}/yonghu/register`
用户注册

**请求参数**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| zhanghao | string | 是 | 账号（唯一） |
| mima | string | 是 | 密码 |
| xingming | string | 是 | 姓名 |
| xingbie | string | 否 | 性别 |
| shoujihaoma | string | 否 | 手机号码 |
| shouhuodizhi | string | 是 | 收货地址 |
| touxiang | text | 否 | 头像 URL |
| email | string | 否 | 邮箱 |
| emailcode | string | 否 | 邮箱验证码（若提供则校验） |

#### `POST/GET /{dbName}/yonghu/login`
用户登录

**请求参数**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| username | string | 是 | 账号 |
| mima（或 password） | string | 是 | 密码 |

**响应示例**：
```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "token": "Base64编码的Token",
    "userInfo": { ... }
  }
}
```

#### `POST/GET /{dbName}/yonghu/logout`
用户登出

#### `POST/GET /{dbName}/yonghu/session`
获取当前会话信息

#### `POST/GET /{dbName}/yonghu/resetPass`
重置密码

#### `POST/GET /{dbName}/yonghu/accountList`
账号列表

#### `POST/GET /{dbName}/yonghu/sendemail`
发送邮箱验证码

#### `POST/GET /{dbName}/yonghu/sendemail/content`
发送邮件内容

#### `POST/GET /{dbName}/yonghu/sendemail/login`
发送邮箱登录验证码

#### `POST/GET /{dbName}/yonghu/email/login`
邮箱验证码登录

**请求参数**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| email | string | 是 | 邮箱 |
| emailcode | string | 是 | 验证码 |

---

### 2.2 店员（dianyuan）

#### `POST/GET /{dbName}/dianyuan/register`
店员注册

**请求参数**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| gonghao | string | 是 | 工号（唯一） |
| mima | string | 是 | 密码 |
| yuangongxingming | string | 是 | 员工姓名 |
| xingbie | string | 否 | 性别 |
| lianxifangshi | string | 否 | 联系方式 |
| touxiang | text | 否 | 头像 |
| email | string | 否 | 邮箱 |

#### `POST/GET /{dbName}/dianyuan/login`
店员登录

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| username | string | 是 | 工号 |
| mima | string | 是 | 密码 |

#### `POST/GET /{dbName}/dianyuan/logout`
| `session` | `resetPass` | `accountList` — 同用户接口模式

#### 邮箱相关
- `/dianyuan/sendemail`
- `/dianyuan/sendemail/content`
- `/dianyuan/sendemail/login`
- `/dianyuan/email/login`

---

### 2.3 管理员（users）

#### `POST/GET /{dbName}/users/register`
管理员注册

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| username | string | 是 | 用户名 |
| password | string | 是 | 密码 |
| role | string | 否 | 角色（默认"管理员"） |
| image | text | 否 | 头像 |

#### `POST/GET /{dbName}/users/login`
管理员登录

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| username | string | 是 | 用户名 |
| password | string | 是 | 密码 |

#### `POST/GET /{dbName}/users/logout`
| `session` | `resetPass` | `accountList` — 同用户接口模式

#### `POST/GET /{dbName}/users/security`
安全相关接口

---

## 3. 标准 CRUD 接口

每个业务表（`*_v.py`，排除 `schema_v.py`、`config_v.py`）自动注册以下标准路由。

> 路径格式：`/{dbName}/{tableName}/{action}`

### 3.1 分页查询
#### `POST/GET /{dbName}/{tableName}/page`

**请求参数**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| page | int | 否 | 当前页码，默认 1 |
| limit | int | 否 | 每页条数，默认 99999 |
| sort | string | 否 | 排序字段，默认 `id` |
| order | string | 否 | 排序方向，`asc` 或 `desc` |
| 其他字段 | - | 否 | 按字段名精确过滤 |
| 字段名% | string | 否 | 末尾带 `%` 表示模糊搜索（`LIKE %value%`） |
| 字段名_start | string | 否 | 时间范围过滤-起始 |
| 字段名_end | string | 否 | 时间范围过滤-结束 |

**响应示例**：
```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "currPage": 1,
    "totalPage": 5,
    "total": 50,
    "pageSize": 10,
    "list": [ ... ]
  }
}
```

### 3.2 列表查询
#### `POST/GET /{dbName}/{tableName}/list`
返回全量数据列表（不分页），数据结构同 `page` 响应中的 `list` 字段。

### 3.3 高级列表
#### `POST/GET /{dbName}/{tableName}/lists`
前台使用的列表接口，通常带身份过滤。

### 3.4 查询
#### `POST/GET /{dbName}/{tableName}/query`
条件查询，返回匹配的第一条记录。

### 3.5 新增
#### `POST/GET /{dbName}/{tableName}/save`
#### `POST/GET /{dbName}/{tableName}/add`

**请求参数**：按表字段传入对应数据（参考第 5 节字段说明）。`save` 和 `add` 功能相同。

### 3.6 详情
#### `GET /{dbName}/{tableName}/info/<id>`
根据 ID 获取单条记录详情。

#### `GET /{dbName}/{tableName}/detail/<id>`
详情页接口（会触发点击计数等逻辑）。

### 3.7 更新
#### `POST/GET /{dbName}/{tableName}/update`

**请求参数**：

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | int | 是 | 记录 ID |
| 其他字段 | - | 按需 | 要更新的字段 |

### 3.8 删除
#### `POST/GET /{dbName}/{tableName}/delete`

**请求参数**：`id`（单个或逗号分隔的多个 ID）

### 3.9 默认值
#### `GET /{dbName}/{tableName}/default`
返回标记为"默认"的记录。

### 3.10 智能排序
#### `GET /{dbName}/{tableName}/autoSort`
按点击次数/浏览时长倒序，用于智能推荐。

#### `GET /{dbName}/{tableName}/autoSort2`
辅助排序接口。

### 3.11 赞/踩
#### `POST/GET /{dbName}/{tableName}/thumbsup/<id>`
点赞/踩（需要表 `__thumbsUp__` = '是'）。

### 3.12 投票
#### `POST/GET /{dbName}/{tableName}/vote/<id>`
投票（需要表 `__browseClick__` 中 vote 功能开启）。

### 3.13 Excel 导入
#### `POST/GET /{dbName}/{tableName}/importExcel`
从 Excel 文件导入数据。

---

## 4. 业务表一览

| 序号 | 表名 | 中文学名 | 视图文件 |
|------|------|----------|----------|
| 1 | `yonghu` | 用户 | `Yonghu_v.py` |
| 2 | `dianyuan` | 店员 | `Dianyuan_v.py` |
| 3 | `chongwuxinxi` | 宠物信息 | `Chongwuxinxi_v.py` |
| 4 | `chongwufuwu` | 宠物服务 | `Chongwufuwu_v.py` |
| 5 | `chongwuyongpin` | 宠物用品 | `Chongwuyongpin_v.py` |
| 6 | `chongwuhudong` | 宠物互动 | `Chongwuhudong_v.py` |
| 7 | `fuwudingdan` | 服务订单 | `Fuwudingdan_v.py` |
| 8 | `jiyangfuwu` | 寄养服务 | `Jiyangfuwu_v.py` |
| 9 | `jiyangdingdan` | 寄养订单 | `Jiyangdingdan_v.py` |
| 10 | `chongwudingdan` | 宠物订单 | `Chongwudingdan_v.py` |
| 11 | `zaishouchongwu` | 在售宠物 | `Zaishouchongwu_v.py` |
| 12 | `lingyangchongwu` | 领养宠物 | `Lingyangchongwu_v.py` |
| 13 | `lingyangshenqing` | 领养申请 | `Lingyangshenqing_v.py` |
| 14 | `shangpindingdan` | 商品订单 | `Shangpindingdan_v.py` |
| 15 | `fahuojilu` | 发货记录 | `Fahuojilu_v.py` |
| 16 | `tuikuanshenqing` | 退款申请 | `Tuikuanshenqing_v.py` |
| 17 | `jiankangshuju` | 健康数据 | `Jiankangshuju_v.py` |
| 18 | `jifenlipin` | 积分礼品 | `Jifenlipin_v.py` |
| 19 | `duihuandingdan` | 兑换订单 | `Duihuandingdan_v.py` |
| 20 | `forum` | 宠物论坛 | `Forum_v.py` |
| 21 | `chat` | 在线客服 | `Chat_v.py` |
| 22 | `news` | 公告信息 | `News_v.py` |
| 23 | `storeup` | 收藏表 | `Storeup_v.py` |
| 24 | `systemintro` | 系统简介 | `Systemintro_v.py` |
| 25 | `emailregistercode` | 邮箱验证码 | `Emailregistercode_v.py` |
| 26 | `users` | 管理员 | `Users_v.py` |
| 27 | `config` | 系统配置 | `config_v.py` |

### 评论/讨论子表

| 序号 | 表名 | 关联主体 | 说明 |
|------|------|----------|------|
| 28 | `discusschongwufuwu` | 宠物服务 | 宠物服务评论 |
| 29 | `discusschongwuyongpin` | 宠物用品 | 宠物用品评论 |
| 30 | `discussjiyangfuwu` | 寄养服务 | 寄养服务评论 |
| 31 | `discusszaishouchongwu` | 在售宠物 | 在售宠物评论 |
| 32 | `discusslingyangchongwu` | 领养宠物 | 领养宠物评论 |
| 33 | `discussjifenlipin` | 积分礼品 | 积分礼品评论 |

---

## 5. 各表字段说明

### 5.1 yonghu（用户）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| zhanghao | VARCHAR(255) | 是 | 账号（唯一） |
| mima | VARCHAR(255) | 是 | 密码 |
| xingming | VARCHAR(255) | 是 | 姓名 |
| xingbie | VARCHAR(255) | 否 | 性别 |
| shoujihaoma | VARCHAR(255) | 否 | 手机号码 |
| shouhuodizhi | VARCHAR(255) | 是 | 收货地址 |
| jifen | Float | 否 | 积分 |
| touxiang | Text | 否 | 头像 |
| email | VARCHAR(255) | 否 | 邮箱 |
| status | Integer | 否 | 状态（0:正常, 1:锁定） |

### 5.2 dianyuan（店员）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| gonghao | VARCHAR(255) | 是 | 工号（唯一） |
| mima | VARCHAR(255) | 是 | 密码 |
| yuangongxingming | VARCHAR(255) | 是 | 员工姓名 |
| xingbie | VARCHAR(255) | 否 | 性别 |
| lianxifangshi | VARCHAR(255) | 否 | 联系方式 |
| touxiang | Text | 否 | 头像 |
| email | VARCHAR(255) | 否 | 邮箱 |

### 5.3 chongwuxinxi（宠物信息）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| chongwuxingming | VARCHAR(255) | 否 | 宠物姓名 |
| chongwutupian | Text | 否 | 宠物图片 |
| pinzhong | VARCHAR(255) | 否 | 品种 |
| xingbie | VARCHAR(255) | 否 | 性别 |
| chushengriqi | Date | 否 | 出生日期 |
| zhanghao | VARCHAR(255) | 否 | 关联用户账号 |

### 5.4 chongwufuwu（宠物服务）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| fuwumingcheng | VARCHAR(255) | 是 | 服务名称 |
| fuwufengmian | Text | 否 | 服务封面 |
| fuwuleixing | VARCHAR(255) | 是 | 服务类型 |
| fuwufanwei | VARCHAR(255) | 否 | 服务范围 |
| chongwuleixing | VARCHAR(255) | 否 | 宠物类型 |
| jifen | Float | 否 | 服务价格 |
| fuwushizhang | VARCHAR(255) | 否 | 服务时长 |
| fuwujieshao | Text | 否 | 服务介绍 |
| clicktime | DateTime | - | 最近点击时间（自动） |
| clicknum | Integer | - | 点击次数 |
| discussnum | Integer | - | 评论数 |
| storeupnum | Integer | - | 收藏数 |

### 5.5 chongwuyongpin（宠物用品）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| shangpinmingcheng | VARCHAR(255) | 是 | 商品名称 |
| shangpinfengmian | Text | 否 | 商品封面 |
| shangpinleixing | VARCHAR(255) | 是 | 商品类型 |
| guige | VARCHAR(255) | 否 | 规格 |
| pinpai | VARCHAR(255) | 否 | 品牌 |
| chandi | VARCHAR(255) | 否 | 产地 |
| shangpinjianjie | Text | 否 | 商品简介 |
| jiage | Float | 否 | 价格 |
| kucun | Integer | 否 | 库存 |
| clicktime | DateTime | - | 最近点击时间 |
| clicknum | Integer | - | 点击次数 |
| discussnum | Integer | - | 评论数 |
| storeupnum | Integer | - | 收藏数 |

### 5.6 jiyangfuwu（寄养服务）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| fuwumingcheng | VARCHAR(255) | 是 | 服务名称 |
| fuwufengmian | Text | 否 | 服务封面 |
| fuwuleixing | VARCHAR(255) | 是 | 服务类型 |
| chongwuleixing | VARCHAR(255) | 否 | 宠物类型 |
| baohanxiangmu | Text | 否 | 包含项目 |
| jifen | Float | 否 | 价格 |
| xiangqing | Text | 否 | 详情 |
| discussnum | Integer | - | 评论数 |
| storeupnum | Integer | - | 收藏数 |

### 5.7 fuwudingdan（服务订单）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| dingdanbianhao | VARCHAR(255) | 否 | 订单编号（唯一，自动生成） |
| fuwumingcheng | VARCHAR(255) | 否 | 服务名称 |
| fuwufengmian | Text | 否 | 服务封面 |
| fuwuleixing | VARCHAR(255) | 否 | 服务类型 |
| jifen | Float | 否 | 服务价格 |
| fuwushizhang | VARCHAR(255) | 否 | 服务时长 |
| chongwuxingming | VARCHAR(255) | 是 | 宠物姓名 |
| pinzhong | VARCHAR(255) | 否 | 品种 |
| yuyueriqi | Date | 是 | 预约日期 |
| beizhu | VARCHAR(255) | 否 | 备注 |
| xiadanshijian | Date | 否 | 下单时间 |
| zhanghao | VARCHAR(255) | 否 | 账号（当前用户） |
| xingming | VARCHAR(255) | 否 | 姓名 |
| shoujihaoma | VARCHAR(255) | 否 | 手机号码 |
| sfsh | VARCHAR(255) | 否 | 审核状态（待审核/通过/拒绝） |
| shhf | Text | 否 | 审核回复 |
| ispay | VARCHAR(255) | 否 | 支付状态（未支付/已支付） |

### 5.8 jiyangdingdan（寄养订单）
同 `fuwudingdan` 结构，差异字段：`jiyangriqi`（寄养日期）代替 `yuyueriqi`。

### 5.9 chongwudingdan（宠物订单）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| dingdanbianhao | VARCHAR(255) | 否 | 订单编号（唯一） |
| chongwunicheng | VARCHAR(255) | 否 | 宠物昵称 |
| chongwupinzhong | VARCHAR(255) | 否 | 宠物品种 |
| chongwutupian | Text | 否 | 宠物图片 |
| yanse | VARCHAR(255) | 否 | 颜色 |
| jifen | Float | 否 | 售价 |
| xiadanriqi | Date | 否 | 下单日期 |
| beizhu | VARCHAR(255) | 否 | 备注 |
| zhanghao | VARCHAR(255) | 否 | 账号 |
| xingming | VARCHAR(255) | 否 | 姓名 |
| shoujihaoma | VARCHAR(255) | 否 | 手机号码 |
| sfsh | VARCHAR(255) | 否 | 审核状态 |
| shhf | Text | 否 | 审核回复 |
| ispay | VARCHAR(255) | 否 | 支付状态 |

### 5.10 zaishouchongwu（在售宠物）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| chongwunicheng | VARCHAR(255) | 是 | 宠物昵称 |
| chongwupinzhong | VARCHAR(255) | 是 | 宠物品种 |
| chongwutupian | Text | 否 | 宠物图片 |
| zhonglei | VARCHAR(255) | 是 | 种类 |
| xingbie | VARCHAR(255) | 否 | 性别 |
| chushengriqi | Date | 否 | 出生日期 |
| yanse | VARCHAR(255) | 否 | 颜色 |
| aihao | VARCHAR(255) | 否 | 爱好 |
| jifen | Float | 否 | 售价 |
| yimiaojilu | Text | 否 | 疫苗记录 |
| quchongjilu | Text | 否 | 驱虫记录 |
| chushouzhuangtai | VARCHAR(255) | 否 | 出售状态 |
| discussnum | Integer | - | 评论数 |
| storeupnum | Integer | - | 收藏数 |

### 5.11 lingyangchongwu（领养宠物）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| chongwunicheng | VARCHAR(255) | 是 | 宠物昵称 |
| chongwupinzhong | VARCHAR(255) | 是 | 宠物品种 |
| chongwutupian | Text | 否 | 宠物图片 |
| xingbie | VARCHAR(255) | 否 | 性别 |
| chushengriqi | Date | 否 | 出生日期 |
| xinggetedian | VARCHAR(255) | 否 | 性格特点 |
| yimiaojilu | Text | 否 | 疫苗记录 |
| lingyangzhuangtai | VARCHAR(255) | 否 | 领养状态 |
| discussnum | Integer | - | 评论数 |
| storeupnum | Integer | - | 收藏数 |

### 5.12 lingyangshenqing（领养申请）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| shenqingbianhao | VARCHAR(255) | 否 | 申请编号（唯一） |
| chongwunicheng | VARCHAR(255) | 否 | 宠物昵称 |
| chongwupinzhong | VARCHAR(255) | 否 | 宠物品种 |
| chongwutupian | Text | 否 | 宠物图片 |
| xingbie | VARCHAR(255) | 否 | 性别 |
| xinggetedian | VARCHAR(255) | 否 | 性格特点 |
| shenqingriqi | Date | 否 | 申请日期 |
| lingyangshuoming | Text | 否 | 领养说明 |
| zhanghao | VARCHAR(255) | 否 | 账号 |
| xingming | VARCHAR(255) | 否 | 姓名 |
| shoujihaoma | VARCHAR(255) | 否 | 手机号码 |
| sfsh | VARCHAR(255) | 否 | 审核状态 |
| shhf | Text | 否 | 审核回复 |

### 5.13 shangpindingdan（商品订单）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| dingdanbianhao | VARCHAR(255) | 否 | 订单编号（唯一） |
| shangpinmingcheng | VARCHAR(255) | 否 | 商品名称 |
| shangpinfengmian | Text | 否 | 商品封面 |
| shangpinleixing | VARCHAR(255) | 否 | 商品类型 |
| guige | VARCHAR(255) | 否 | 规格 |
| pinpai | VARCHAR(255) | 否 | 品牌 |
| chandi | VARCHAR(255) | 否 | 产地 |
| jiage | Float | 否 | 价格 |
| kucun | Integer | 是 | 购买数量 |
| jifen | Float | 否 | 应付金额 |
| xiadanriqi | Date | 否 | 下单日期 |
| zhanghao | VARCHAR(255) | 否 | 账号 |
| xingming | VARCHAR(255) | 否 | 姓名 |
| shoujihaoma | VARCHAR(255) | 否 | 手机号码 |
| shouhuodizhi | VARCHAR(255) | 否 | 收货地址 |
| fahuozhuangtai | VARCHAR(255) | 否 | 发货状态 |
| sfsh | VARCHAR(255) | 否 | 审核状态 |
| shhf | Text | 否 | 审核回复 |
| ispay | VARCHAR(255) | 否 | 支付状态 |

### 5.14 fahuojilu（发货记录）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| dingdanbianhao | VARCHAR(255) | 否 | 订单编号 |
| shangpinmingcheng | VARCHAR(255) | 否 | 商品名称 |
| shangpinfengmian | Text | 否 | 商品封面 |
| pinpai | VARCHAR(255) | 否 | 品牌 |
| jiage | Float | 否 | 价格 |
| kucun | Integer | 否 | 购买数量 |
| jifen | Float | 否 | 应付金额 |
| xiadanriqi | Date | 否 | 下单日期 |
| zhanghao | VARCHAR(255) | 否 | 账号 |
| xingming | VARCHAR(255) | 否 | 姓名 |
| shoujihaoma | VARCHAR(255) | 否 | 手机号码 |
| shouhuodizhi | VARCHAR(255) | 否 | 收货地址 |
| fahuoriqi | Date | 否 | 发货日期 |
| duihuanma | VARCHAR(255) | 否 | 兑换码 |

### 5.15 tuikuanshenqing（退款申请）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| dingdanbianhao | VARCHAR(255) | 否 | 订单编号 |
| shangpinmingcheng | VARCHAR(255) | 否 | 商品名称 |
| shangpinfengmian | Text | 否 | 商品封面 |
| pinpai | VARCHAR(255) | 否 | 品牌 |
| jiage | Float | 否 | 价格 |
| kucun | Integer | 否 | 购买数量 |
| jifen | Float | 否 | 退款金额 |
| xiadanriqi | Date | 否 | 下单日期 |
| zhanghao | VARCHAR(255) | 否 | 账号 |
| xingming | VARCHAR(255) | 否 | 姓名 |
| shoujihaoma | VARCHAR(255) | 否 | 手机号码 |
| shouhuodizhi | VARCHAR(255) | 否 | 收货地址 |
| shenqingriqi | Date | 否 | 申请日期 |
| tuikuanyuanyin | Text | 否 | 退款原因 |
| sfsh | VARCHAR(255) | 否 | 审核状态 |
| shhf | Text | 否 | 审核回复 |
| ispay | VARCHAR(255) | 否 | 支付状态 |

### 5.16 jiankangshuju（健康数据）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| jilubianhao | VARCHAR(255) | 否 | 记录编号（唯一） |
| chongwuxingming | VARCHAR(255) | 否 | 宠物姓名 |
| chongwutupian | Text | 否 | 宠物图片 |
| pinzhong | VARCHAR(255) | 否 | 品种 |
| xingbie | VARCHAR(255) | 否 | 性别 |
| zhanghao | VARCHAR(255) | 否 | 账号 |
| shengao | VARCHAR(255) | 否 | 身高(cm) |
| tizhong | VARCHAR(255) | 否 | 体重(kg) |
| tiwen | VARCHAR(255) | 否 | 体温(℃) |
| shenghuoxiguan | VARCHAR(255) | 否 | 生活习惯 |
| yinshipianhao | VARCHAR(255) | 否 | 饮食偏好 |
| jiankangyuce | Text | 否 | 健康预测 |

### 5.17 chongwuhudong（宠物互动）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| dingdanbianhao | VARCHAR(255) | 否 | 订单编号 |
| fuwumingcheng | VARCHAR(255) | 否 | 服务名称 |
| jifen | Float | 否 | 价格 |
| jiyangriqi | Date | 否 | 寄养日期 |
| chongwuxingming | VARCHAR(255) | 否 | 宠物姓名 |
| pinzhong | VARCHAR(255) | 否 | 品种 |
| gengxinriqi | Date | 否 | 更新日期 |
| zhanghao | VARCHAR(255) | 否 | 账号 |
| chongwuzhaopian | Text | 否 | 宠物照片 |
| chongwushipin | Text | 否 | 宠物视频 |
| chongwudongtai | Text | 否 | 宠物动态 |

### 5.18 jifenlipin（积分礼品）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| lipinmingcheng | VARCHAR(255) | 是 | 礼品名称 |
| lipinfengmian | Text | 否 | 礼品封面 |
| lipinleixing | VARCHAR(255) | 否 | 礼品类型 |
| guige | VARCHAR(255) | 否 | 规格 |
| lipinjianjie | Text | 否 | 礼品简介 |
| duihuanjifen | Float | 否 | 兑换积分 |
| kucun | Integer | 否 | 库存 |
| discussnum | Integer | - | 评论数 |
| storeupnum | Integer | - | 收藏数 |

### 5.19 duihuandingdan（兑换订单）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| duihuanbianhao | VARCHAR(255) | 否 | 兑换编号（唯一） |
| lipinmingcheng | VARCHAR(255) | 否 | 礼品名称 |
| lipinfengmian | Text | 否 | 礼品封面 |
| lipinleixing | VARCHAR(255) | 否 | 礼品类型 |
| guige | VARCHAR(255) | 否 | 规格 |
| duihuanjifen | Float | 否 | 兑换积分 |
| kucun | Integer | 是 | 兑换数量 |
| jifen | Float | 否 | 应付积分 |
| duihuanriqi | Date | 否 | 兑换日期 |
| duihuanbeizhu | VARCHAR(255) | 否 | 兑换备注 |
| zhanghao | VARCHAR(255) | 否 | 账号 |
| xingming | VARCHAR(255) | 否 | 姓名 |
| shoujihaoma | VARCHAR(255) | 否 | 手机号码 |
| sfsh | VARCHAR(255) | 否 | 审核状态 |
| shhf | Text | 否 | 审核回复 |

### 5.20 forum（宠物论坛）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | VARCHAR(255) | 否 | 帖子标题 |
| content | Text | 是 | 帖子内容 |
| parentid | BigInteger | 否 | 父节点 ID（支持楼层回复） |
| username | VARCHAR(255) | 否 | 用户名 |
| avatarurl | Text | 否 | 头像 |
| isdone | VARCHAR(255) | 否 | 状态 |
| istop | Integer | 否 | 是否置顶（0:否,1:是） |
| toptime | DateTime | 否 | 置顶时间 |
| cover | Text | 否 | 封面 |
| isanon | Integer | 否 | 是否匿名（0:否,1:是） |
| delflag | Integer | 否 | 是否删除（0:否,1:是） |
| userid | BigInteger | 否 | 用户 ID |
| storeupnum | Integer | - | 收藏数 |

> **论坛特有接口**：
> - `POST/GET /{dbName}/forum/flist` — 前台帖子列表
> - `POST/GET /{dbName}/forum/list/<id>` — 按父节点 ID 获取回复列表
> - `POST/GET /{dbName}/forum/query` — 查询帖子
> - `POST/GET /{dbName}/forum/list` — 帖子列表
> - `POST/GET /{dbName}/forum/lists` — 帖子列表（前台）

### 5.21 chat（在线客服）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| userid | BigInteger | 是 | 用户 ID |
| adminid | BigInteger | 否 | 管理员 ID |
| ask | Text | 否 | 提问内容 |
| reply | Text | 否 | 回复内容 |
| isreply | Integer | 否 | 是否回复 |
| isread | Integer | 否 | 已读/未读（1:已读, 0:未读） |
| uname | VARCHAR(255) | 否 | 用户名 |
| uimage | Text | 否 | 用户头像 |
| type | Integer | 否 | 内容类型（1:文本,2:图片,3:视频,4:文件,5:表情） |

### 5.22 news（公告信息）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | VARCHAR(255) | 是 | 标题 |
| introduction | Text | 否 | 简介 |
| picture | Text | 是 | 图片 |
| content | Text | 是 | 内容 |
| name | VARCHAR(255) | 否 | 发布人 |
| headportrait | Text | 否 | 头像 |
| storeupnum | Integer | - | 收藏数 |

### 5.23 storeup（收藏表）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| userid | BigInteger | 是 | 用户 ID |
| refid | BigInteger | 否 | 关联记录 ID |
| tablename | VARCHAR(255) | 否 | 关联表名 |
| name | VARCHAR(255) | 是 | 收藏名称 |
| picture | Text | 否 | 图片 |
| type | VARCHAR(255) | 否 | 类型（默认"1"） |
| inteltype | VARCHAR(255) | 否 | 推荐类型 |
| remark | VARCHAR(255) | 否 | 备注 |

### 5.24 systemintro（系统简介）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| title | VARCHAR(255) | 是 | 标题 |
| subtitle | VARCHAR(255) | 否 | 副标题 |
| content | Text | 是 | 内容 |
| picture1~3 | Text | 否 | 图片 1~3 |

### 5.25 emailregistercode（邮箱验证码）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| email | VARCHAR(255) | 是 | 邮箱 |
| role | VARCHAR(255) | 是 | 角色 |
| code | VARCHAR(255) | 是 | 验证码 |

### 5.26 users（管理员）

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| username | VARCHAR(255) | 是 | 用户名 |
| password | VARCHAR(255) | 是 | 密码 |
| role | VARCHAR(255) | 否 | 角色（默认"管理员"） |
| image | Text | 否 | 头像 |

### 5.27 评论子表通用字段

所有 `discuss*` 表共用以下字段：

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| refid | BigInteger | 是 | 关联主体记录的 ID |
| userid | BigInteger | 是 | 评论用户 ID |
| avatarurl | Text | 否 | 头像 |
| nickname | VARCHAR(255) | 否 | 用户名 |
| content | Text | 是 | 评论内容 |
| reply | Text | 否 | 管理员回复内容 |
| thumbsupnum | Integer | - | 点赞数 |
| crazilynum | Integer | - | 点踩数 |
| istop | Integer | 否 | 置顶（0:否,1:是） |
| tuserids | Text | 否 | 赞用户 ID 列表 |
| cuserids | Text | 否 | 踩用户 ID 列表 |

---

## 6. 通用跨表接口

以下接口定义在 `main/schema_v.py` 中，可作用于任意表。

### 6.1 图表聚合接口

#### `POST/GET /{dbName}/group/<tableName>/<columnName>`
按指定字段分组统计数量。

#### `POST/GET /{dbName}/value/<tableName>/<xColumnName>/<yColumnName>`
按值统计（X轴/Y轴）。

#### `POST/GET /{dbName}/value/<tableName>/<xColumnName>/<yColumnName>/<timeStatType>`
按时间维度统计（日/周/月/年）。

#### `POST/GET /{dbName}/cal/<tableName>/<columnName>`
计算聚合值（sum、max、min、avg）。

### 6.2 选项/跟进接口

#### `POST/GET /{dbName}/option/<tableName>/<columnName>`
获取某表某字段的去重值列表。

#### `POST/GET /{dbName}/follow/<tableName>/<columnName>`
#### `POST/GET /{dbName}/follow/<tableName>/<columnName>/<level>/<parent>`
级联筛选/跟进功能。

### 6.3 审核接口

#### `POST/GET /{dbName}/sh/<tableName>`
通用审核接口，修改 `sfsh` 和 `shhf` 字段。

### 6.4 批量审核

以下表具有 `shBatch` 批量审核接口：
- `fuwudingdan` — 服务订单
- `jiyangdingdan` — 寄养订单
- `chongwudingdan` — 宠物订单
- `lingyangshenqing` — 领养申请
- `duihuandingdan` — 兑换订单
- `shangpindingdan` — 商品订单
- `tuikuanshenqing` — 退款申请

#### `POST/GET /{dbName}/{tableName}/shBatch`

### 6.5 提醒接口

#### `POST/GET /{dbName}/chongwuyongpin/remind/<columnName>/<type>`
宠物用品库存提醒。

#### `POST/GET /{dbName}/jifenlipin/remind/<columnName>/<type>`
积分礼品库存提醒。

#### `POST/GET /{dbName}/jiankangshuju/remind/<columnName>/<type>`
健康数据提醒。

### 6.6 统计图表接口（各订单表）

以下表具有 `value` / `group` / `valueMul` 统计接口：
- `fuwudingdan`（服务订单）
- `jiyangdingdan`（寄养订单）
- `chongwudingdan`（宠物订单）
- `shangpindingdan`（商品订单）

#### `POST/GET /{dbName}/{tableName}/value/<xColumnName>/<yColumnName>/<timeStatType>`
#### `POST/GET /{dbName}/{tableName}/value/<xColumnName>/<yColumnName>`
#### `POST/GET /{dbName}/{tableName}/group/<columnName>`
#### `POST/GET /{dbName}/{tableName}/valueMul/<xColumnName>/<timeStatType>`
#### `POST/GET /{dbName}/{tableName}/valueMul/<xColumnName>`

### 6.7 计数接口

以下表具有 `count` 接口：
- `fuwudingdan`、`jiyangdingdan`、`chongwudingdan`、`shangpindingdan`

#### `POST/GET /{dbName}/{tableName}/count`

### 6.8 DeepSeek AI 接口

#### `POST/GET /{dbName}/deepseek/askai`
调用 DeepSeek AI 问答。

### 6.9 位置服务

#### `POST/GET /{dbName}/location`
获取位置信息（调用百度地图 API）。

### 6.10 人脸匹配

#### `POST/GET /{dbName}/matchFace`
人脸匹配（调用百度 AI API）。

### 6.11 爬虫接口

#### `POST/GET /{dbName}/spider/<tableName>`
爬虫数据采集。

### 6.12 列管理

#### `POST/GET /{dbName}/updateColumn/<tableName>/<type>`
更新列。

#### `POST/GET /{dbName}/deleteColumn/<tableName>`
删除列。

### 6.13 评论列表

#### `POST/GET /{dbName}/comment/list`
评论列表接口。

### 6.14 安全接口

以下表具有 `security` 接口：
- `chat`、`storeup`、`systemintro`、`emailregistercode`、`users`
- 所有 `discuss*` 评论子表

#### `POST/GET /{dbName}/{tableName}/security`

### 6.15 WebSocket

#### `WS /{dbName}/ws`
WebSocket 实时通信端点，用于在线客服/即时通讯。

---

## 7. 文件接口

### 7.1 上传

#### `POST/GET /{dbName}/upload/<fileName>`
通用文件上传。

#### `POST/GET /{dbName}/upload/<tableName>/<fileName>`
为指定表上传文件（如预测/关联上传）。

### 7.2 下载

#### `POST/GET /{dbName}/file/download`
文件下载。

### 7.3 加密/解密

#### `POST/GET /{dbName}/file/encrypt`
文件加密。

#### `POST/GET /{dbName}/file/decrypt`
文件解密。

---

## 8. 页面前端路由

### 8.1 管理后台（Admin）

| 路由规则 | 说明 |
|----------|------|
| `/{dbName}/admin/` | 管理后台首页（Vue 3 SPA） |
| `/{dbName}/admin/dist/index.html` | 管理后台入口 |
| `/admin/` | 管理后台（别名） |
| `/xadmin/` | Django 原生 admin |

### 8.2 前台页面

| 路由规则 | 说明 |
|----------|------|
| `/` | 前台首页 |
| `/index.html` | 前台首页 |
| `/{dbName}/index.html` | 前台首页 |
| `/{dbName}/front/index.html` | 前台首页 |
| `/{dbName}/front/...` | 前台其他页面 |
| `/{dbName}/front-pc/...` | PC 端前台页面 |
| `/index/` | index 视图 |

### 8.3 静态资源

| 路由规则 | 说明 |
|----------|------|
| `/admin/lib/...` | Admin 静态库 |
| `/admin/page/...` | Admin 页面 |
| `/admin/pages/...` | Admin 多页 |
| `/admin/(p1)/(p2)...` | Admin 文件资源 |
| `/layui/...` | LayUI 资源 |
| `/pages/...` | 前台页面资源 |
| `/modules/...` | 模块资源 |
| `/css/...` | 样式文件 |
| `/js/...` | 脚本文件 |
| `/img/...` | 图片资源 |

---

> **文档版本**：v1.0  
> **生成日期**：2026-06-13  
> **说明**：本文档基于项目 `main/*_v.py`、`main/urls.py`、`main/models.py` 自动分析生成。
