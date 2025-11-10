import {fileURLToPath, URL} from 'node:url';

import {defineConfig, loadEnv} from 'vite';
import vue from '@vitejs/plugin-vue';
import vueDevTools from 'vite-plugin-vue-devtools';
import tailwindcss from '@tailwindcss/vite';

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
    const env = loadEnv(mode, process.cwd(), '');
    const DEFAULT_VITE_DEV_PORT = 5173;

    return {
        plugins: [vue(), vueDevTools(), tailwindcss()],
        resolve: {
            alias: {
                '@': fileURLToPath(new URL('./src', import.meta.url)),
            },
        },
        server: {
            port: env.VITE_DEV_PORT ? Number(env.VITE_DEV_PORT) : DEFAULT_VITE_DEV_PORT,
        },
    };
});
