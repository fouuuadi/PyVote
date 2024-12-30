/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}", "./static/**/*.{html,js}"],
  theme: {
    extend: {
      spacing: {
        'custom-gap': '50px', 
        '10': '2.5rem',
      }
    },
  },
  plugins: [],
}

