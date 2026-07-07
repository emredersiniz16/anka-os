"use client"

import { useEffect, useRef } from "react"

// The fluid Neural Wave — the physical manifestation of the AI core.
// `energy` 0..1 scales amplitude (idle vs. speaking).
export function NeuralWave({
  energy = 0.35,
  primary = "var(--electric-blue)",
  secondary = "var(--neon-cyan)",
}: {
  energy?: number
  primary?: string
  secondary?: string
}) {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const energyRef = useRef(energy)
  energyRef.current = energy

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext("2d")
    if (!ctx) return

    let raf = 0
    let t = 0
    const dpr = Math.min(window.devicePixelRatio || 1, 2)

    const resolveColor = (v: string) => {
      if (v.startsWith("var(")) {
        const name = v.slice(4, -1).trim()
        return getComputedStyle(canvas).getPropertyValue(name).trim() || "#66fcf1"
      }
      return v
    }

    const resize = () => {
      const rect = canvas.getBoundingClientRect()
      canvas.width = rect.width * dpr
      canvas.height = rect.height * dpr
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
    }
    resize()
    const ro = new ResizeObserver(resize)
    ro.observe(canvas)

    const draw = () => {
      const rect = canvas.getBoundingClientRect()
      const w = rect.width
      const h = rect.height
      const mid = h / 2
      ctx.clearRect(0, 0, w, h)

      const e = energyRef.current
      const col1 = resolveColor(primary)
      const col2 = resolveColor(secondary)

      // Draw several stacked sine layers for a rich waveform.
      const layers = 3
      for (let l = 0; l < layers; l++) {
        ctx.beginPath()
        const amp = (h * 0.16) * e * (1 - l * 0.25) + 3
        const freq = 0.012 + l * 0.006
        const speed = 0.05 + l * 0.02
        for (let x = 0; x <= w; x += 2) {
          const envelope = Math.sin((x / w) * Math.PI) // taper at edges
          const y =
            mid +
            Math.sin(x * freq + t * speed) * amp * envelope +
            Math.sin(x * freq * 2.3 + t * speed * 1.7) * amp * 0.4 * envelope
          if (x === 0) ctx.moveTo(x, y)
          else ctx.lineTo(x, y)
        }
        ctx.strokeStyle = l === 0 ? col2 : col1
        ctx.globalAlpha = l === 0 ? 0.9 : 0.35 - l * 0.08
        ctx.lineWidth = l === 0 ? 2.2 : 1.2
        ctx.shadowBlur = l === 0 ? 12 : 0
        ctx.shadowColor = col2
        ctx.stroke()
      }
      ctx.globalAlpha = 1
      ctx.shadowBlur = 0

      t += 1
      raf = requestAnimationFrame(draw)
    }
    raf = requestAnimationFrame(draw)

    return () => {
      cancelAnimationFrame(raf)
      ro.disconnect()
    }
  }, [primary, secondary])

  return <canvas ref={canvasRef} className="h-full w-full" aria-hidden="true" />
}
