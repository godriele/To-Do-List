/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        customGray: '#ede9e9',
        customBeige: '#f5ebe0',
        customLightBeige: '#d6ccc2',
        customMuted: '#e3d5ca',
        customDarkBeige: '#d5bdaf',
    },
  },
},
  plugins: [],
}