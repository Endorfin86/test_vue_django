<template>
 Страница-тест vue js<br>
 <button @click="get_products">Запрос</button>
 <br>
 {{ result }}
 <br><br>
 <button @click="get_invoice">Запрос2</button>
 <br>
 {{ result2 }}
</template>

<script>
import axios from 'axios'
import { ref } from 'vue'
 
export default {
  name: "App",
  setup() {
    var result = ref('null')
    var result2 = ref('null')

    async function get_products() {
      var res = await axios.get('http://127.0.0.1:8000/list/')
      this.result = res.data
    }

    async function get_invoice() {
      var res = await axios.get('http://127.0.0.1:8000/get_invoice/')
      this.result2 = res.data
    }

    return {
      result,
      result2,
      get_products,
      get_invoice
    }
  }
}
</script>

<style>

</style>
