"use client"

import { useCallback, useState } from "react"
import { BootSequence } from "./boot-sequence"
import { ChatInterface } from "./chat-interface"
import { AmbientFly } from "./ambient-fly"
import { FlyGlyph } from "./fly-glyph"

type Power = "off" | "booting" | "on" | "sleep"

export function AnkaDevice() {
  const [power, setPower] = useState<Power>("off")
  const [day, setDay] = useState(false)
  const [soundOn, setSoundOn] = useState(true)

  const onBootComplete = useCallback(() => setPower("on"), [])

  const pressPower = () => {
    if (power === "off") setPower("booting")
    else if (power === "on") setPower("sleep")
    else if (power === "sleep") setPower("on")
  }

  return (
    <div className="flex flex-col items-center gap-6">
      {/* Device */}
      <div className="relative">
        {/* Side power button */}
        <button
          type="button"
          onClick={pressPower}
          aria-label={power === "off" ? "Cihazı aç" : power === "sleep" ? "Uyandır" : "Uyut"}
          className="absolute -right-1.5 top-28 z-30 h-14 w-1.5 rounded-r-md bg-neutral-700 transition-colors hover:bg-neutral-500"
        />
        {/* Volume buttons (decorative) */}
        <div className="absolute -left-1.5 top-24 z-30 h-10 w-1.5 rounded-l-md bg-neutral-800" />
        <div className="absolute -left-1.5 top-36 z-30 h-10 w-1.5 rounded-l-md bg-neutral-800" />

        {/* Bezel */}
        <div className="relative rounded-[2.6rem] border border-neutral-700 bg-neutral-900 p-2.5 shadow-2xl">
          {/* Screen */}
          <div
            className={`scanlines relative h-[600px] w-[300px] overflow-hidden rounded-[2rem] ${day ? "theme-day" : ""}`}
          >
            {/* Notch */}
            <div className="absolute left-1/2 top-0 z-30 h-6 w-28 -translate-x-1/2 rounded-b-2xl bg-black">
              <div className="absolute right-6 top-2.5 h-1.5 w-1.5 rounded-full bg-neutral-700" />
            </div>

            {/* Status bar */}
            {power !== "off" && (
              <div className="absolute inset-x-0 top-0 z-20 flex items-center justify-between px-5 pt-1.5">
                <span className="font-mono text-[9px] text-foreground/70">ANKA</span>
                <span className="font-mono text-[9px] text-foreground/70">
                  {power === "sleep" ? "1 Hz" : "◍ 100%"}
                </span>
              </div>
            )}

            {/* Screen content */}
            <div className="absolute inset-0">
              {power === "off" && (
                <button
                  type="button"
                  onClick={pressPower}
                  className="flex h-full w-full flex-col items-center justify-center gap-4 bg-black"
                  aria-label="Cihazı aç"
                >
                  <FlyGlyph size={44} color="#1f2833" wingColor="#12141a" />
                  <span className="font-mono text-[10px] tracking-[0.3em] text-neutral-600">GÜÇ TUŞUNA BAS</span>
                </button>
              )}
              {power === "booting" && <BootSequence soundOn={soundOn} onComplete={onBootComplete} />}
              {power === "on" && <ChatInterface soundOn={soundOn} />}
              {power === "sleep" && <AmbientFly onWake={() => setPower("on")} />}
            </div>
          </div>
        </div>
      </div>

      {/* Controls */}
      <div className="flex flex-wrap items-center justify-center gap-2">
        <ControlButton onClick={pressPower}>
          {power === "off" ? "Aç" : power === "sleep" ? "Uyandır" : power === "on" ? "Uyut" : "Boot..."}
        </ControlButton>
        <ControlButton onClick={() => setDay((d) => !d)} disabled={power === "off"}>
          {day ? "Gündüz ☀" : "Gece ◑"}
        </ControlButton>
        <ControlButton onClick={() => setSoundOn((s) => !s)}>{soundOn ? "Ses açık" : "Ses kapalı"}</ControlButton>
        <ControlButton onClick={() => setPower("off")} disabled={power === "off"}>
          Kapat
        </ControlButton>
      </div>
    </div>
  )
}

function ControlButton({
  children,
  onClick,
  disabled,
}: {
  children: React.ReactNode
  onClick: () => void
  disabled?: boolean
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className="rounded-md border border-[#1f2833] bg-[#12141a] px-3 py-1.5 font-mono text-[11px] text-[#66fcf1] transition-colors hover:border-[#45a29e] hover:text-white disabled:cursor-not-allowed disabled:opacity-40"
    >
      {children}
    </button>
  )
}
