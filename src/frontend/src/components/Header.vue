<template>
  <v-toolbar app dense fixed dark clipped-left class="info darken-2">
    <v-btn dark flat @click.stop="onToggle" class="info">
      <v-icon>menu</v-icon>
    </v-btn>
    <v-toolbar-title class="mr-5 align-center">
      <span @click.stop="toRoute('index')"> BLOGME </span>
    </v-toolbar-title>
    <v-layout row justify-center>
      <v-flex xs12 sm10 style="max-width: 750px">
        <v-text-field
          placeholder="Search..."
          single-line
          append-icon="search"
          :append-icon-cb="() => {}"
          dark
        ></v-text-field>
      </v-flex>
    </v-layout>
    <v-btn dark icon v-if="isList" @click.stop="listView()">
      <v-icon>apps</v-icon>
    </v-btn>
    <v-btn dark icon v-else @click.stop="listView()">
      <v-icon>view_list</v-icon>
    </v-btn>
</v-toolbar>
</template>

<script>
export default {
  name: 'Header',
  props: ['toggle'],
  data () {
    return {
      isList: true
    }
  },
  methods: {
    onToggle () {
      this.toggle()
    }
  }
}
</script>

<style scoped>

</style>
