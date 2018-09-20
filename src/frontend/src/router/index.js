import Vue from 'vue'
import Router from 'vue-router'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component:  (resolve) => {
        require(['@/views/index/Index'], resolve)
      }
    },
    {
      path: '/blog_list',
      name: 'blog_list',
      component: (resolve) =>  {
        require(['@/views/blog/BlogList'], resolve)
      }
    },
    { path: '/home',
      name: 'home',
      redirect: '/' }
  ]
})
