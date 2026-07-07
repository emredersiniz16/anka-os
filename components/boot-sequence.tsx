"use client"

import { useEffect, useMemo, useRef, useState } from "react"
import { FlyGlyph } from "./fly-glyph"
import { playBuzz, playClick } from "@/lib/audio"

type Stage = "buzz" | "click" | "fragment" | "form" | "done"

const BOOT_LOG = [
  "PURGING LEGACY ECOSYSTEM",
  "[-] Google Play Services -> DELETED",
  "[-] Adware Daemons -> DELETED",
  "[-] Background Trackers -> DELETED",
  "[-] UI Bloatware -> DELETED",
  "INJECTING ANKA AI-CORE KERNEL",
  "[*] Flashing Core Orchestrator...",
  "Felsefe dogrulandi: 'Sifir Uygulama, Saf Irade.'",
]

export function BootSequence({ soundOn, onComplete }: { soundOn: boolean; onComplete: () => void }) {
  const [stage, setStage] = useState<Stage>("buzz")
  const [logIndex, setLogIndex] = useState(0)
  const [flyPos, setFlyPos] = useState({ x: 30, y: 40 })
  const stopBuzzRef = useRef<() => void>(() => {})

  // Data fragments the fly shatters into.
  const fragments = useMemo(
    () =>
      Array.from({ length: 44 }, () => ({
        fx: (Math.random() - 0.5) * 320 + "px",
        fy: (Math.random() - 0.5) * 320 + "px",
        fr: Math.random() * 720 - 360 + "deg",
        delay: Math.random() * 0.15,
        left: 45 + Math.random() * 10,
        top: 38 + Math.random() * 10,
      })),
    [],
  )

  // Buzz stage: fly wanders, buzzing plays.
  useEffect(() => {
    if (stage !== "buzz") return
    if (soundOn) stopBuzzRef.current = playBuzz(3)

    const wander = setInterval(() => {
      setFlyPos({ x: 15 + Math.random() * 70, y: 20 + Math.random() * 55 })
    }, 260)

    const toClick = setTimeout(() => {
      clearInterval(wander)
      setStage("click")
    }, 3000)

    return () => {
      clearInterval(wander)
      clearTimeout(toClick)
      stopBuzzRef.current?.()
    }
  }, [stage, soundOn])

  // Click stage: CLICK sound + move to fragment.
  useEffect(() => {
    if (stage !== "click") return
    if (soundOn) playClick()
    setFlyPos({ x: 50, y: 42 })
    const t = setTimeout(() => setStage("fragment"), 120)
    return () => clearTimeout(t)
  }, [stage, soundOn])

  // Fragment stage: shatter, then boot log.
  useEffect(() => {
    if (stage !== "fragment") return
    const t = setTimeout(() => setStage("form"), 700)
    return () => clearTimeout(t)
  }, [stage])

  // Form stage: stream the boot log then finish.
  useEffect(() => {
    if (stage !== "form") return
    if (logIndex >= BOOT_LOG.length) {
      const t = setTimeout(() => {
        setStage("done")
        onComplete()
      }, 700)
      return () => clearTimeout(t)
    }
    const t = setTimeout(() => setLogIndex((i) => i + 1), 260)
    return () => clearTimeout(t)
  }, [stage, logIndex, onComplete])

  return (
    <div className="relative flex h-full w-full flex-col overflow-hidden bg-obsidian">
      {/* Fly during buzz + click */}
      {(stage === "buzz" || stage === "click") && (
        <div
          className="absolute transition-all duration-200 ease-out"
          style={{ left: `${flyPos.x}%`, top: `${flyPos.y}%`, transform: "translate(-50%, -50%)" }}
        >
          <FlyGlyph size={40} />
        </div>
      )}

      {stage === "buzz" && (
        <div className="absolute inset-x-0 bottom-16 text-center">
          <p className="font-mono text-[11px] tracking-widest text-neon-cyan animate-flicker">Bzzz... Bzzz...</p>
          <p className="mt-1 font-mono text-[10px] text-muted">donanim taraniyor</p>
        </div>
      )}

      {stage === "click" && (
        <div className="absolute inset-0 flex items-center justify-center">
          <span className="font-mono text-2xl font-bold tracking-[0.3em] text-electric-blue">*CLICK*</span>
          <span
            className="absolute h-24 w-24 rounded-full border border-electric-blue"
            style={{ animation: "pulse-ring 0.5s ease-out" }}
          />
        </div>
      )}

      {/* Shatter fragments */}
      {stage === "fragment" &&
        fragments.map((f, i) => (
          <span
            key={i}
            className="absolute h-1.5 w-1.5 bg-electric-blue"
            style={{
              left: `${f.left}%`,
              top: `${f.top}%`,
              // @ts-expect-error custom props consumed by the keyframes
              "--fx": f.fx,
              "--fy": f.fy,
              "--fr": f.fr,
              animation: `fragment-out 0.7s ${f.delay}s ease-out forwards`,
            }}
          />
        ))}

      {/* Boot log forms the core */}
      {stage === "form" && (
        <div className="flex h-full flex-col justify-center px-6">
          <pre className="mb-4 font-mono text-[10px] leading-tight text-neon-cyan">{`   .·.    ▲    .·.
  // \\  //\\  // \\
 //***\\//__\\//***\\
[===== ANKA OS =====]`}</pre>
          <div className="space-y-1">
            {BOOT_LOG.slice(0, logIndex).map((line, i) => (
              <p
                key={i}
                className={`animate-rise font-mono text-[10px] ${
                  line.startsWith("[-]")
                    ? "text-muted"
                    : line.startsWith("[*]")
                      ? "text-electric-blue"
                      : line.startsWith("Felsefe")
                        ? "text-tactical"
                        : "text-neon-cyan"
                }`}
              >
                {line.includes("->") || line.startsWith("[") ? `  ${line}` : `» ${line}`}
              </p>
            ))}
            {logIndex < BOOT_LOG.length && (
              <p className="font-mono text-[10px] text-electric-blue caret" aria-hidden="true" />
            )}
          </div>
        </div>
      )}
    </div>
  )
}
