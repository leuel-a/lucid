<script setup>
import {ref} from 'vue';
import UploadItem from './UploadItem.vue';

const files = ref([]);
let idCounter = 1;

function onDrop(e) {
    e.preventDefault();
    const dropped = Array.from(e.dataTransfer.files || []);
    handleFiles(dropped);
}

function onInput(e) {
    const selected = Array.from(e.target.files || []);
    handleFiles(selected);
    e.target.value = '';
}

function handleFiles(list) {
    const allowed = [
        'application/pdf',
        'text/plain',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    ];
    for (const f of list) {
        if (!allowed.includes(f.type) && !f.name.match(/\.(pdf|txt|doc|docx)$/i)) {
            files.value.push({
                id: idCounter++,
                name: f.name,
                size: f.size,
                type: f.type,
                progress: 0,
                status: 'error',
            });
            continue;
        }

        const fileObj = {
            id: idCounter++,
            name: f.name,
            size: f.size,
            type: f.type,
            progress: 0,
            status: 'uploading',
        };

        files.value.unshift(fileObj);
        fakeUpload(fileObj);
    }
}

function fakeUpload(file) {
    const step = () => {
        if (file.progress >= 100) {
            file.status = 'processed';
            return;
        }
        file.progress += Math.floor(Math.random() * 18) + 6;
        if (file.progress > 100) file.progress = 100;
        setTimeout(step, 300 + Math.random() * 400);
    };
    setTimeout(step, 200);
}

function removeFile(id) {
    const idx = files.value.findIndex((f) => f.id === id);
    if (idx !== -1) files.value.splice(idx, 1);
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

        <div class="p-4">
            <div class="shadow rounded bg-white/6 p-4">
                <div
                    @dragover.prevent
                    @drop="onDrop"
                    class="rounded-md border-2 border-dashed border-white p-6 text-center"
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
            </div>

            <div class="mt-4 space-y-3">
                <div
                    v-if="files.length === 0"
                    class="text-muted text-sm"
                >
                    No documents uploaded yet.
                </div>
                <UploadItem
                    v-for="f in files"
                    :key="f.id"
                    :file="f"
                    @remove="removeFile"
                />
            </div>
        </div>
    </div>
</template>
