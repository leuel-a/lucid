<script setup>
import {computed, useAttrs} from 'vue';

const emits = defineEmits(['update:modelValue', 'keydown']);

defineProps({
    draft: String,
    modelValue: String,
    onKeyDown: Function,
});

const attrs = computed(() => {
    const {placeholder, class: _, rows, ...rest} = useAttrs();
    return rest;
});

/**
 * Handle InputChange in the textarea
 * @param {InputEvent} event - The InputEvent object
 */
const onInputHandler = (event) => {
    emits('update:modelValue', event.target.value);
}

/**
 * Handle changes in the chat textarea
 * @param {KeyboardEvent} event - The InputEvent object
 */
const onKeyDownHandler = (event) => {
    emits('keydown', event);
}
</script>

<template>
    <textarea
        @input="onInputHandler"
        @keydown="onKeyDownHandler"
        :value="modelValue"
        rows="1"
        placeholder="Type a message..."
        class="placeholder:text-muted flex-1 resize-none rounded bg-white/4 p-3 text-sm"
        v-bind="attrs"
    ></textarea>
</template>
