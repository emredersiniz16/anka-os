"use client"

import { useEffect, useState } from "react"
import { FlyGlyph } from "./fly-glyph"

// Always-On Display at 1 Hz. The fly drifts to a new coordinate once per second,
// tracing its 24h "industrial blueprint". Clock ticks at 1 Hz too.
export function AmbientFly({ onWake }: { onWake: () => void }) {
  const [pos, setPos] = useState({ x: 50, y: 45 })
  const [now, setNow] = useState<string>("")
  const [coord, setCoord] = useState({ x: 0, y: 0 })

  useEffect(() => {
    const tick = () => {
      const x = 12 + Math.random() * 76
      const y = 20 + Math.random() * 55
      setPos({ x, y })
      setCoord({ x: Math.round(x * 3.6 * 100) / 100, y: Math.round(y * 1.8 * 100) / 100 })
      const d = new Date()
      setNow(
        `${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}:${String(
          d.getSeconds(),
        ).padStart(2, "0")}`,
      )
    }
    tick()
    // 1 Hz refresh — deliberately choppy, anti burn-in.
    const iv = setInterval(tick, 1000)
    return () => clearInterval(iv)
  }, [])

  return (
    <button
      type="button"
      onClick={onWake}
      aria-label="Uyandır"
      className="relative block h-full w-full overflow-hidden bg-black text-left"
    >
      {/* clock */}
      <div className="absolute inset-x-0 top-10 text-center">
        <p className="font-mono text-3xl font-light tracking-widest text-neon-cyan/80">{now}</p>
        <p className="mt-1 font-mono text-[9px] tracking-[0.3em] text-muted">ANKA OS · SLEEP · 1 Hz</p>
      </div>

      {/* the 1 Hz wandering fly (no transition → snaps once per second) */}
      <div
        className="absolute"
        style={{ left: `${pos.x}%`, top: `${pos.y}%`, transform: "translate(-50%, -50%)" }}
      >
        <FlyGlyph size={26} color="var(--neon-cyan)" wingColor="var(--muted)" />
      </div>

      {/* cryptic telemetry */}
      <div className="absolute inset-x-0 bottom-8 text-center">
        <p className="font-mono text-[9px] text-muted/70">
          DRIFT X:{coord.x.toFixed(2)} Y:{coord.y.toFixed(2)}
        </p>
        <p className="mt-2 font-mono text-[9px] text-muted/50">dokun → uyandır</p>
      </div>
    </button>
  )
}
