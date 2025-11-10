<script setup>
import {ref} from 'vue';
import ChatPanelHeader from './ChatPanelHeader.vue';
import ChatPanelSendButton from './ChatPanelSendButton.vue';
import ChatPanelTextInput from '@/components/ChatPanelTextInput.vue';

defineProps({
    messages: {type: Array, default: () => []},
    sending: {type: Boolean},
});

const draft = ref('');

const model = ref('gemini-2.5-flash');

const emit = defineEmits(['send']);

/**
 * Submits the current Message to the websocket
 */
function submitHandler() {
    emit('send', draft.value);
    draft.value = '';
}

/**
 * Handles KeyDown events on the input
 * Submits the form when Enter is pressed without Shift
 *
 * @param {KeyboardEvent} event - The keydown event object.
 */
function onKeyDownHandler(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        submitHandler();
    }
}
</script>

<template>
    <div class="flex h-full w-full flex-col">
        <ChatPanelHeader :model="model" />

        <div
            class="flex-1 space-y-4 overflow-auto p-4"
            id="chat-history"
        >
            <transition-group
                name="msg"
                tag="div"
            >
                <div
                    class="flex"
                    v-for="(message, idx) in messages"
                    :key="message.id || idx"
                    :class="message.role === 'user' ? 'justify-end' : 'justify-start'"
                >
                    <div
                        v-if="message.role === 'assistant'"
                        class="max-w-9/12 rounded bg-white/6 p-3 shadow"
                    >
                        <div
                            class="text-sm"
                            v-html="message.content"
                        ></div>
                        <div class="text-muted mt-2 text-xs">{{ message.time }}</div>
                    </div>
                    <div
                        v-else
                        class="max-w-9/12 rounded bg-linear-to-r from-blue-gray-700 to-blue-gray-900 p-3 text-right shadow"
                    >
                        <div
                            class="text-sm"
                            v-html="message.content"
                        ></div>
                        <div
                            class="text-muted mt-2 text-xs"
                            v-html="message.time"
                        ></div>
                    </div>
                </div>
            </transition-group>
        </div>

        <div class="border-t border-white/6 px-4 py-3">
            <div class="flex items-center gap-3">
                <ChatPanelTextInput
                    v-model="draft"
                    @keydown="onKeyDownHandler"
                />
                <ChatPanelSendButton
                    :draft="draft"
                    :sending="sending"
                    :onsubmit="submitHandler"
                />
            </div>
        </div>
    </div>
</template>
