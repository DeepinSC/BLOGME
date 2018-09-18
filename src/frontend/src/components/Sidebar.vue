<template>
  <v-navigation-drawer
    dark
    app
    clipped
    v-model="visible"
    >
    <v-container grid-list-sm>
      <v-layout row justify-center align-center>
        <v-flex xs12>
          <v-card flat>
            <v-card-title flat>
              <v-container grid-list-sm>
                <v-layout row wrap>
                  <v-flex xs12
                    align-center justify-center text-xs-center
                  >
                    <v-avatar
                      tile="tile"
                    >
                      <img src="../assets/logo.png" alt="avatar">
                    </v-avatar>
                  </v-flex>
                  <v-flex xs12
                    align-center justify-center text-xs-center
                    headline
                  >
                      <div @click.stop="toRoute('home')">
                        BLOGME
                      </div>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-title>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <v-list>
    <template>
      <v-list-tile v-for="(item, i) in items" :key="i"  >
        <v-list-tile-action @click.stop="toRoute(item.link)">
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-tile-action>
        <v-list-tile-content @click.stop="toRoute(item.link)">
          <v-list-tile-title>
            {{ item.text }}
          </v-list-tile-title>
        </v-list-tile-content>
        <v-list-tile-action v-if="item.add">
            <v-tooltip right>
              <v-icon dark color="primary" @click.stop="toRoute(item.add)" slot="activator">add</v-icon>
               <span>{{item.ttip}}</span>
            </v-tooltip>
        </v-list-tile-action>
      </v-list-tile>
    </template>
    <v-spacer></v-spacer>
    <v-list-tile >
      <v-list-tile-action>
        <v-icon>copyright</v-icon>
      </v-list-tile-action>
      <v-list-tile-content>
        <v-list-tile-title>
          Copyright {{ year }}
        </v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'Sidebar',
  props: ['visible'],
  methods: {
    toRoute (rname, rparams = {}, query = {}) {
      this.dialog = true
      this.$router.push({name: rname, params: rparams, query: query})
    }
  },
  computed: {
    year () {
      return new Date().getFullYear()
    }
  }
}
</script>

<style scoped>

</style>
