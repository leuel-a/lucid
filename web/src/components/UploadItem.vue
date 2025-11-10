<script setup>
import Button from './ui/Button.vue';

const props = defineProps({
    file: {
        type: Object,
        required: true,
    },
});

const emit = defineEmits(['remove']);

function handleRemove() {
    emit('remove', props.file.id);
}
</script>

<template>
    <div class="shadow flex items-center justify-between gap-3 rounded bg-white/4 p-3">
        <div class="flex items-center gap-3">
            <i class="pi pi-file text-2xl"></i>
            <div>
                <div class="font-medium">{{ file.name }}</div>
                <div class="text-muted text-xs">
                    {{ file.sizeKB }} KB • {{ file.type || 'unknown' }}
                </div>
            </div>
        </div>
        <div>
            <Button
                @click="handleRemove"
                :custom-class="'rounded hover:border hover:border-white bg-white/6 px-2 py-2 text-sm'"
            >
                <i class="pi pi-times"></i>
            </Button>
        </div>
    </div>
</template>
