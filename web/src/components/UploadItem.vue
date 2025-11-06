<script setup>
import {ref, watch} from 'vue';

const props = defineProps({file: Object});
const emits = defineEmits(['remove']);
const progress = ref(props.file.progress ?? 0);

watch(
    () => props.file.progress,
    (v) => {
        if (typeof v === 'number') progress.value = v;
    },
);
</script>

<template>
    <div class="shadow flex items-center justify-between gap-3 rounded bg-white/4 p-3">
        <div class="flex items-center gap-3">
            <i class="pi pi-file text-2xl"></i>
            <div>
                <div class="font-medium">{{ file.name }}</div>
                <div class="text-muted text-xs">
                    {{ Math.round(file.size / 1024) }} KB • {{ file.type || 'unknown' }}
                </div>
            </div>
        </div>
        <div class="flex w-36 flex-col items-end">
            <div class="h-1.5 bg-white/6 rounded-full overflow-hidden w-full mb-2">
                <div
                    class="h-full bg-linear-to-r from-[#ff7e33] to-[#ff9a5c] transition-all duration-400 ease-[cubic-bezier(0.2,0.8,0.2,1)]"
                    :style="{width: (file.progress ?? progress) + '%'}"
                ></div>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-muted text-xs">{{ Math.round(file.progress ?? progress) }}%</span>
                <button
                    @click="$emit('remove', file.id)"
                    class="rounded bg-white/6 p-1 text-sm"
                >
                    <i class="pi pi-times"></i>
                </button>
            </div>
        </div>
    </div>
</template>
