<script setup>
import Button from './ui/Button.vue';

defineProps({
    draft: String,
    sending: Boolean,
    onsubmit: Function,
});
</script>

<template>
    <Button
        :disabled="!draft.trim() || sending"
        :custom-class="'from-accent to-accent-secondary flex items-center gap-2 rounded bg-linear-to-b p-3 text-white'"
        v-on:click="onsubmit"
    >
        <i class="pi pi-send"></i>
        <span class="hidden sm:inline">Send</span>
    </Button>
</template>
