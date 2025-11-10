<script setup>
import {ref, onMounted, onUnmounted} from 'vue';
import Button from './components/ui/Button.vue';
import ChatPanel from './components/ChatPanel.vue';
import DocumentPanel from './components/DocumentPanel.vue';

/** @type {WebSocket} **/
let socket;

onMounted(() => {
    socket = new WebSocket(import.meta.env.VITE_WEBSOCKET_URL);

    socket.onmessage = (event) => {
        recieveMessage(event);
        sendingMessage.value = false;
    };
});

onUnmounted(() => socket.close());

const sendingMessage = ref(false);

const HUMAN_MESSAGE_ROLE = "user";
const ASSISTANT_MESSAGE_ROLE = "assistant";
const messages = ref([
    {
        id: 1,
        role: ASSISTANT_MESSAGE_ROLE,
        content: 'Welcome! Upload documents on the right and ask me about them.',
        time: new Date().toLocaleTimeString(),
    },
]);

const mobileView = ref('both');

/**
 * Sends the current text to the LLM
 * @param {String} message
 */
function sendMessage(message) {
    sendingMessage.value = true;

    messages.value.push({
        id: messages.value[messages.value.length - 1].id + 1,
        role: HUMAN_MESSAGE_ROLE,
        content: message,
        time: new Date().toLocaleTimeString(),
    });

    socket.send(`chat${JSON.stringify({message})}`);
}

/**
 * Recieves a message from the WebSocket
 * @param {MessageEvent} event
 */
function recieveMessage(event) {
    /** @type {import('./types.js').SocketResponse} */
    const data = JSON.parse(event.data);

    messages.value.push({
        id: messages.value[messages.value.length - 1].id + 1,
        role: ASSISTANT_MESSAGE_ROLE,
        content: data.content,
        time: new Date().toLocaleTimeString(),
    });
}
</script>

<template>
    <div class="flex h-screen w-screen flex-col">
        <div class="flex items-center justify-between bg-white/5 px-3 py-2 md:hidden">
            <div class="flex items-center gap-3">
                <Button
                    @click="mobileView = mobileView === 'chat' ? 'both' : 'chat'"
                    custom-class="rounded bg-white/6 p-2"
                >
                    <i class="pi pi-comments"></i>
                </Button>
                <div class="font-semibold">Lucid — Documents RAG</div>
            </div>
            <div>
                <Button
                    @click="mobileView = mobileView === 'docs' ? 'both' : 'docs'"
                    :custom-class="'rounded bg - white / 6 p - 2'"
                >
                    <i class="pi pi-folder-open"></i>
                </Button>
            </div>
        </div>

        <div class="flex flex-1 gap-4 overflow-hidden px-4 py-4">
            <div
                v-show="mobileView === 'both' || mobileView === 'chat'"
                class="flex-1 md:w-7/10"
            >
                <div class="flex flex-column rounded card-shadow h-full overflow-hidden bg-white/6">
                    <ChatPanel
                        :messages="messages"
                        :sending="sendingMessage"
                        v-on:send="sendMessage"
                    />
                </div>
            </div>

            <div
                v-show="mobileView === 'both' || mobileView === 'docs'"
                class="hidden md:block md:w-3/10"
            >
                <div class="rounded card-shadow h-full overflow-hidden bg-white/6">
                    <DocumentPanel />
                </div>
            </div>

            <div
                v-show="mobileView === 'docs'"
                class="mt-4 w-full md:hidden"
            >
                <div class="rounded card-shadow overflow-hidden bg-white/6">
                    <DocumentPanel />
                </div>
            </div>
        </div>
    </div>
</template>
