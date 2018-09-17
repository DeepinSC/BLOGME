<template lang="html">
  <vbloglist></vbloglist>
</template>

<script>
export default {
  name: 'index',
   components: {
     'vbloglist': () => import('./BlogList.vue'),
   }
}
</script>

<style scoped>

</style>
