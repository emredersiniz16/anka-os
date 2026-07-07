import { AnkaDevice } from "@/components/anka-device"

export default function Page() {
  return (
    <main className="min-h-screen bg-[#05060a] text-[#c5c6c7]">
      <div className="mx-auto flex max-w-6xl flex-col items-center px-4 py-10 lg:py-16">
        {/* Header */}
        <header className="mb-10 text-center">
          <p className="mb-3 font-mono text-[11px] tracking-[0.35em] text-[#45a29e]">PROJECT PHOENIX</p>
          <h1 className="text-balance font-mono text-3xl font-bold tracking-tight text-[#66fcf1] sm:text-4xl">
            🪰 ANKA OS
          </h1>
          <p className="mx-auto mt-4 max-w-xl text-pretty font-mono text-[13px] leading-relaxed text-[#8a9099]">
            Eski cihazlar için uygulamasız yapay zeka çekirdeği. Telefona yüklemeden önce nasıl göründüğünü ve
            çalıştığını burada, tarayıcıda dene. Gerçek bir kurulum yapılmaz — bu güvenli bir simülasyondur.
          </p>
        </header>

        {/* Device + guide side by side on desktop */}
        <div className="grid w-full gap-10 lg:grid-cols-[auto_1fr] lg:items-start lg:gap-14">
          <div className="flex justify-center">
            <AnkaDevice />
          </div>

          {/* Guide */}
          <section className="mx-auto max-w-md space-y-6 lg:mt-6">
            <div>
              <h2 className="mb-3 font-mono text-sm font-semibold tracking-widest text-[#66fcf1]">NASIL DENENİR</h2>
              <ol className="space-y-3">
                {[
                  "Sağ taraftaki güç tuşuna (veya “Aç” butonuna) bas. 3 saniyelik sinek vızıltısı ve mekanik CLICK ile boot sekansı başlar.",
                  "Android kalıntıları silinir, Anka çekirdeği yüklenir ve Nöral Dalga belirir.",
                  "Çekirdeğe yaz: örn. “Paris’e bilet bak ve araç ayarla”. Ajanlar çalışırken dalga “düşünen sinek”e dönüşür.",
                  "“Uyut” de — ekran 1 Hz’e düşer ve ortam sineği ekranda gezinmeye başlar (OLED yanma önleme).",
                ].map((step, i) => (
                  <li key={i} className="flex gap-3">
                    <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full border border-[#45a29e] font-mono text-[11px] text-[#66fcf1]">
                      {i + 1}
                    </span>
                    <span className="font-mono text-[12px] leading-relaxed text-[#8a9099]">{step}</span>
                  </li>
                ))}
              </ol>
            </div>

            <div className="rounded-lg border border-[#1f2833] bg-[#0b0c10] p-4">
              <h3 className="mb-2 font-mono text-[11px] tracking-widest text-[#ff6b1a]">CLICK EVRENİ</h3>
              <ul className="space-y-1.5 font-mono text-[11px] leading-relaxed text-[#8a9099]">
                <li>» Boot: vızıltı + mekanik CLICK, sinek veri parçacıklarına bölünür</li>
                <li>» 1 Hz Canlı Sinek: uyku modunda gezinen anti-burn-in silüet</li>
                <li>» Düşünen Sinek: işlem sırasında gözlerini ovan 1 Hz animasyon</li>
                <li>» Gönder tuşu klasik ok yerine sinek glifidir</li>
              </ul>
            </div>

            <p className="font-mono text-[10px] leading-relaxed text-[#4a4e54]">
              Not: Gerçek çekirdek (core/*.c) root erişimli bir Android cihazda framebuffer üzerinde çalışır. Bu web
              simülatörü, o deneyimi güvenli biçimde önizlemek içindir.
            </p>
          </section>
        </div>
      </div>
    </main>
  )
}
