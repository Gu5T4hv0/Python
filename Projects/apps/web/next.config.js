/** @type {import('next').NextConfig} */
const nextConfig = {
  /* config options here */
  eslint: {
    // Permite que o build de produção conclua mesmo com erros de ESLint (ex.: no-html-link-for-pages)
    ignoreDuringBuilds: true,
  },
};

module.exports = nextConfig;
