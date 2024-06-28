const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true
})

module.exports = {
    devServer: {
        port: 5000 // Укажите нужный порт, например, 8081
    }
}