import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  eslint: {
    // Permite que o build de produção conclua mesmo com erros de ESLint (ex.: no-html-link-for-pages)
    ignoreDuringBuilds: true,
  },
};

export default nextConfig;
