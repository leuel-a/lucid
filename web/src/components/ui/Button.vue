<script setup>
import {useAttrs, computed} from 'vue';

defineOptions({inheritAttrs: false});
defineProps({
    customClass: String,
});

const attrs = computed(() => {
    const {class: _, ...rest} = useAttrs();
    return rest;
});
</script>

<template>
    <button
        :class="`cursor-pointer ${customClass}`"
        v-bind="attrs"
    >
        <slot></slot>
    </button>
</template>
