<template>
  <v-content>
    <v-container fill-height>
      <v-layout justify-center align-center>
        <v-flex>
          <slot></slot>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
export default {
    name: 'Content',
}
</script>

<style scoped>

</style>
