import type { Metadata, Viewport } from "next"
import { Geist, Geist_Mono } from "next/font/google"
import "./globals.css"

const geistSans = Geist({ subsets: ["latin"], variable: "--font-geist-sans" })
const geistMono = Geist_Mono({ subsets: ["latin"], variable: "--font-geist-mono" })

export const metadata: Metadata = {
  title: "Anka OS — Simülatör / Simulator",
  description:
    "Eski cihazlar için uygulamasız yapay zeka çekirdeği. Anka OS'un boot sekansını, Nöral Dalga'yı, 1 Hz sineği ve sohbet arayüzünü telefona yüklemeden tarayıcıda deneyin.",
  generator: "v0.app",
}

export const viewport: Viewport = {
  themeColor: "#0b0c10",
  userScalable: false,
  width: "device-width",
  initialScale: 1,
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="tr" className={`bg-background ${geistSans.variable} ${geistMono.variable}`}>
      <body className="font-sans">{children}</body>
    </html>
  )
}
