import Vue from 'vue'
import Router from 'vue-router'
import Vuetify from 'vuetify'
import MainContainer from '../components/MainContainer'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainContainer',
      component: MainContainer
    }
  ]
})
