<template>
    <v-layout justify-center>
      <v-flex>
        <v-container fluid grid-list-md>
          <v-layout row wrap>
            <v-flex v-for="item in items" v-bind="{ [`xs${item.flex}`]: true }" md8 :key="item.id">
              <v-card class="mb-3">
                <v-layout row>
                  <v-flex md2 xs3>
                    <v-img :src="item.src" height="200px" @click.stop="$router.push(item.id)">
                      <v-container fill-height fluid pa-2>
                        <v-layout fill-height>
                          <v-flex xs12 align-end flexbox>
                            <span class="headline white--text" v-text="item.title"></span>
                          </v-flex>
                        </v-layout>
                      </v-container>
                    </v-img>
                  </v-flex>
                  <v-flex md6 xs9>
                    <v-card-title>
                      <div>
                        <span class="grey--text">Number 10</span><br>
                        <span>Whitehaven Beach</span><br>
                        <span>Whitsunday Island, Whitsunday Islands</span>
                      </div>
                    </v-card-title>
                    <v-card-actions>
                      <v-btn flat color="orange">Share</v-btn>
                      <v-btn flat color="orange">Explore</v-btn>
                    </v-card-actions>
                  </v-flex>
                </v-layout>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-flex>
    </v-layout>
</template>

<script>
export default {
  name: 'BlogList',
  data () {
    return {
      items: [ {
        id:1,
        flex:12,
        title: 'Rock & Roll!',
        src: 'https://www.codeproject.com/KB/GDI-plus/ImageProcessing2/img.jpg'
      },
        {
        id:2,
        flex:12,
        title: 'Rock & Roll!',
        src: 'https://www.codeproject.com/KB/GDI-plus/ImageProcessing2/img.jpg'
      },
        {
        id:3,
        flex:12,
        title: 'Rock & Roll!',
        src: 'https://www.codeproject.com/KB/GDI-plus/ImageProcessing2/img.jpg'
      }
      ]
    }
  }
}
</script>

<style scoped>

</style>
