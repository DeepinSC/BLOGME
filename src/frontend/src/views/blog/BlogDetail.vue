<template>
  <v-layout justify-center>
    <v-container>
      <v-flex>
        <v-breadcrumbs>
          <v-icon slot="divider">chevron_right</v-icon>

          <v-breadcrumbs-item
            v-for="crumb in crumbs"
            :disabled="crumb.disabled"
            :key="crumb.text"
            :to="crumb.to"
          >
            {{ crumb.text }}
          </v-breadcrumbs-item>
        </v-breadcrumbs>
      </v-flex>
    </v-container>
  </v-layout>
</template>

<script>
export default {
  name: 'BlogDetail',
  data () {
    return {
      crumbs: [
        {
          text: 'Home',
          disabled: false,
          to: '/'
        },
        {
          text: 'Blog list',
          disabled: false,
          to: '/blog/list'
        },
        {
          text: 'Link 2',
          disabled: true
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
