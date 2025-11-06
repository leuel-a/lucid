<script setup>
defineProps({
    model: String,
});
</script>

<template>
    <div class="flex items-center justify-between border-b border-white px-4 py-3">
        <div class="flex items-center gap-3">
            <i class="pi pi-comments text-2xl text-white/90"></i>
            <div>
                <div class="text-lg font-semibold">Lucid</div>
                <div class="text-muted text-sm">Ask questions about your uploaded documents</div>
            </div>
        </div>
        <div class="text-muted text-sm">Model: {{ model }}</div>
    </div>
</template>
