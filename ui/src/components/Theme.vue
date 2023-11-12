<template>
    <div></div>
</template>
  
<script>
export default {
    created() {
        // 使用matchMedia监听系统主题变化
        const darkModeQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        const changeTheme = () => {
        if (darkModeQuery.matches) {
            // 切换到暗色主题
            this.$ELEMENT.theme = 'dark';
        } else {
            // 切换到亮色主题
            this.$ELEMENT.theme = 'light';
        }
        };

        // 初始化主题
        changeTheme();

        // 监听系统主题变化
        darkModeQuery.addListener(changeTheme);
    },
};
</script>
  