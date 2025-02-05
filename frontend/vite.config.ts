import {defineConfig} from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'
import tailwindcss from "@tailwindcss/vite";


// https://vite.dev/config/
export default defineConfig({
    plugins: [react(), tailwindcss()],
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src'), // Configura el alias @ a src
        },
    },
    server: {
        proxy: {
            '/api': {
                target: 'http://localhost:8000',
                changeOrigin: true
            }
        },
    }
});