import "./globals.css";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Conferenze",
  description: "One stop solution to your tedious conference hunting",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <script
        src="https://cdn.jsdelivr.net/npm/add-to-calendar-button@2"
        async
        defer
      ></script>
      <body className={inter.className}>{children}</body>
    </html>
  );
}
