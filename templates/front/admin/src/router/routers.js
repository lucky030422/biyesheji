/**
 * @description: 路由页面列表
 */

const ListPage = () => import("@/views/list/list.vue");

const routes = [
  {
    path: '/',
    component: () => import('@/views/layout/layout.vue'),
    redirect: '/login',
    children: [
      {
        path: '/home',
        component: () => import('@/views/home/home.vue'),
        meta: {
          title: '首页'
        },        
      },
      {
        path: '/center',
        component: () => import('@/views/center.vue'),
        meta: {
          title: '个人信息'
        },
      },
      {
        path: '/updatePassword',
        component: () => import('@/views/updatePassword.vue'),
        meta: {
          title: '修改密码',
        },
      },
      {
        path: '/config/:type',
        component: ListPage,
      },
      {
        path: '/yonghu',
        component: ListPage,
        meta: {
          title: "用户",
        },        
      },  
      {
        path: '/dianyuan',
        component: ListPage,
        meta: {
          title: "店员",
        },        
      },  
      {
        path: '/chongwufuwu',
        component: ListPage,
        meta: {
          title: "宠物服务",
        },        
      },  
      {
        path: '/chongwuyongpin',
        component: ListPage,
        meta: {
          title: "宠物用品",
        },        
      },  
      {
        path: '/jiyangfuwu',
        component: ListPage,
        meta: {
          title: "寄养服务",
        },        
      },  
      {
        path: '/zaishouchongwu',
        component: ListPage,
        meta: {
          title: "在售宠物",
        },        
      },  
      {
        path: '/lingyangchongwu',
        component: ListPage,
        meta: {
          title: "领养宠物",
        },        
      },  
      {
        path: '/jifenlipin',
        component: ListPage,
        meta: {
          title: "积分礼品",
        },        
      },  
      {
        path: '/chongwuxinxi',
        component: ListPage,
        meta: {
          title: "宠物信息",
        },        
      },  
      {
        path: '/fuwudingdan',
        component: ListPage,
        meta: {
          title: "服务订单",
        },        
      },  
      {
        path: '/jiyangdingdan',
        component: ListPage,
        meta: {
          title: "寄养订单",
        },        
      },  
      {
        path: '/chongwudingdan',
        component: ListPage,
        meta: {
          title: "宠物订单",
        },        
      },  
      {
        path: '/lingyangshenqing',
        component: ListPage,
        meta: {
          title: "领养申请",
        },        
      },  
      {
        path: '/duihuandingdan',
        component: ListPage,
        meta: {
          title: "兑换订单",
        },        
      },  
      {
        path: '/shangpindingdan',
        component: ListPage,
        meta: {
          title: "商品订单",
        },        
      },  
      {
        path: '/fahuojilu',
        component: ListPage,
        meta: {
          title: "发货记录",
        },        
      },  
      {
        path: '/tuikuanshenqing',
        component: ListPage,
        meta: {
          title: "退款申请",
        },        
      },  
      {
        path: '/jiankangshuju',
        component: ListPage,
        meta: {
          title: "健康数据",
        },        
      },  
      {
        path: '/chongwuhudong',
        component: ListPage,
        meta: {
          title: "宠物互动",
        },        
      },  
      {
        path: '/news',
        component: ListPage,
        meta: {
          title: "公告信息",
        },        
      },  
      {
        path: '/forum',
        component: ListPage,
        meta: {
          title: "宠物论坛",
        },        
      },  
      {
        path: '/chat',
        component: ListPage,
        meta: {
          title: "在线客服",
        },        
      },  
      {
        path: '/storeup',
        component: ListPage,
        meta: {
          title: "收藏表",
        },        
      },  
      {
        path: '/systemintro',
        component: ListPage,
        meta: {
          title: "系统简介",
        },        
      },  
      {
        path: '/emailregistercode',
        component: ListPage,
        meta: {
          title: "邮箱验证码",
        },        
      },  
      {
        path: '/users',
        component: ListPage,
        meta: {
          title: "管理员",
        },        
      },  
      {
        path: '/discusschongwufuwu',
        component: ListPage,
        meta: {
          title: "宠物服务评论",
        },        
      },  
      {
        path: '/discusschongwuyongpin',
        component: ListPage,
        meta: {
          title: "宠物用品评论",
        },        
      },  
      {
        path: '/discussjiyangfuwu',
        component: ListPage,
        meta: {
          title: "寄养服务评论",
        },        
      },  
      {
        path: '/discusszaishouchongwu',
        component: ListPage,
        meta: {
          title: "在售宠物评论",
        },        
      },  
      {
        path: '/discusslingyangchongwu',
        component: ListPage,
        meta: {
          title: "领养宠物评论",
        },        
      },  
      {
        path: '/discussjifenlipin',
        component: ListPage,
        meta: {
          title: "积分礼品评论",
        },        
      },  
    ],
  },
  {
    path: '/login',
    component: () => import('@/views/login/login.vue'),
    meta: {
      title: "登录",
    },
  },
  {
    path: '/register',
    component: () => import('@/views/register/register.vue'),
    meta: {
      title: "注册",
    },
  },
  {
    path: '/forgetPassword',
    component: () => import('@/views/forgetPassword.vue'),
    meta: {
      title: '忘记密码',
    },
  },
]


export default routes