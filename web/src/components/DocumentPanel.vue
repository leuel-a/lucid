<script setup>
import {ref} from 'vue';
import UploadItem from './UploadItem.vue';

/**
 * @typedef {import('../types.js').UploadFileItem} UploadFileItem
 */

/** @type {import('vue').Ref<Array<UploadFileItem>>} */
const files = ref([]);

/** @param {DragEvent} event */
function onDrop(event) {
    event.preventDefault();
    const dropped = Array.from(event.dataTransfer?.files || []);
    handleFiles(dropped);
}

/** @param {Event} event */
function onInput(event) {
    const selected = Array.from(event.target.files || []);
    handleFiles(selected);
    event.target.value = '';
}

/** @param {File[]} filesList */
function handleFiles(filesList) {
    const allowedFileTypes = [
        'application/pdf',
        'text/plain',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    ];

    for (const file of filesList) {
        const isAllowed =
            allowedFileTypes.includes(file.type) || file.name.match(/\.(pdf|txt|doc|docx)$/i);

        const nextId = files.value.length > 0 ? files.value[files.value.length - 1].id + 1 : 1;

        files.value.unshift({
            id: nextId,
            name: file.name,
            size: file.size,
            type: file.type,
            progress: 0,
            status: isAllowed ? 'uploading' : 'error',
        });
    }
}

/** @param {number} id */
function removeFile(id) {
    const index = files.value.findIndex((f) => f.id === id);
    if (index !== -1) files.value.splice(index, 1);
}
</script>

<template>
    <div class="flex h-full flex-col">
        <header class="flex items-center justify-between border-b border-white px-4 py-3">
            <div class="flex items-center gap-3">
                <i class="pi pi-folder-open text-2xl"></i>
                <div>
                    <div class="font-semibold">Documents</div>
                    <div class="text-muted text-sm">Upload PDFs, DOCX, and text files</div>
                </div>
            </div>
            <div class="text-muted text-sm">Storage: local</div>
        </header>

        <div class="p-4 space-y-4">
            <!-- Show this large banner only if there are NO files -->
            <div
                v-if="files.length === 0"
                @dragover.prevent
                @drop="onDrop"
                class="shadow rounded bg-white/6 p-6 text-center border-2 border-dashed border-white"
            >
                <i class="pi pi-cloud-upload mb-2 text-3xl"></i>
                <div class="text-sm">Drag & drop files here</div>
                <div class="text-muted mt-2 text-xs">Supported: PDF, DOC, DOCX, TXT</div>
                <div class="mt-4 flex justify-center">
                    <label class="cursor-pointer rounded bg-white/10 px-4 py-2">
                        <input
                            type="file"
                            multiple
                            class="hidden"
                            @change="onInput"
                        />
                        <i class="pi pi-upload mr-2"></i> Browse files
                    </label>
                </div>
            </div>

            <div class="space-y-3">
                <UploadItem
                    v-for="file in files"
                    :key="file.id"
                    :file="file"
                    @remove="removeFile"
                />
            </div>

            <div
                v-if="files.length > 0"
                @dragover.prevent
                @drop="onDrop"
                class="rounded-md border-2 border-dashed border-white/40 p-3 flex items-center justify-center text-sm text-muted gap-8"
            >
                <span>Browser or Drop more files to upload</span>
                <label class="cursor-pointer rounded">
                    <input
                        type="file"
                        multiple
                        class="hidden"
                        @change="onInput"
                    />
                    <i class="pi pi-cloud-upload text-lg"></i>
                </label>
            </div>
        </div>
    </div>
</template>
