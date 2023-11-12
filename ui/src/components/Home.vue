<template>
    <SIS v-if="showPage === 'SIS'"></SIS>
    <FusionPortal v-if="showPage === 'FusionPortal'"></FusionPortal>
</template>

<script setup>
import SIS from './SIS.vue'
import FusionPortal from './FusionPortal.vue'
import { useRoute } from 'vue-router'
const route = useRoute()
const showPage = route.query.page

</script>

<style scoped>

</style>
