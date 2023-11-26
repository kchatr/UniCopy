/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,css}", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {colors: {
      ...require('tailwindcss/defaultTheme').colors,
      dark_bg: '#1B262C', // Your custom color
    },},
  },
  plugins: [],
}

