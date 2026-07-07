"use client"

import { useEffect, useRef, useState } from "react"
import { NeuralWave } from "./neural-wave"
import { FlyGlyph } from "./fly-glyph"
import { generateResponse, type CoreLine } from "@/lib/anka-core"
import { playClick, playBlip } from "@/lib/audio"

type Msg =
  | { id: number; role: "user"; text: string }
  | { id: number; role: "core"; lines: CoreLine[] }

const toneColor: Record<CoreLine["tone"], string> = {
  core: "text-electric-blue",
  agent: "text-neon-cyan",
  ok: "text-foreground",
  warn: "text-tactical",
  sys: "text-muted",
}

let idc = 0

export function ChatInterface({ soundOn }: { soundOn: boolean }) {
  const [messages, setMessages] = useState<Msg[]>([])
  const [input, setInput] = useState("")
  const [thinking, setThinking] = useState(false)
  const [blink, setBlink] = useState(false)
  const scrollRef = useRef<HTMLDivElement>(null)

  const energy = thinking ? 0 : messages.length > 0 ? 0.55 : 0.32

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" })
  }, [messages, thinking])

  // 1 Hz eye-rubbing rhythm for the thinking fly.
  useEffect(() => {
    if (!thinking) return
    const iv = setInterval(() => setBlink((b) => !b), 500)
    return () => clearInterval(iv)
  }, [thinking])

  const send = () => {
    const value = input.trim()
    if (!value || thinking) return
    if (soundOn) playClick()

    const userMsg: Msg = { id: idc++, role: "user", text: value }
    setMessages((m) => [...m, userMsg])
    setInput("")
    setThinking(true)

    const lines = generateResponse(value)
    // Simulate the fly "orchestrating" a background operation.
    window.setTimeout(() => {
      setThinking(false)
      if (soundOn) playBlip()
      setMessages((m) => [...m, { id: idc++, role: "core", lines }])
    }, 1600 + Math.random() * 900)
  }

  const onKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.nativeEvent.isComposing || e.keyCode === 229) return
    if (e.key === "Enter") {
      e.preventDefault()
      send()
    }
  }

  return (
    <div className="flex h-full flex-col bg-obsidian">
      {/* Neural Wave / Thinking Fly header */}
      <div className="relative h-28 shrink-0 border-b border-border-soft">
        {thinking ? (
          <div className="flex h-full flex-col items-center justify-center gap-1">
            <FlyGlyph size={46} blink={blink} />
            <span className="font-mono text-[10px] tracking-widest text-neon-cyan">düşünüyor · 1 Hz</span>
          </div>
        ) : (
          <NeuralWave energy={energy} />
        )}
        <div className="pointer-events-none absolute left-3 top-7 flex items-center gap-1.5">
          <span className="h-1.5 w-1.5 rounded-full bg-electric-blue" />
          <span className="font-mono text-[9px] tracking-widest text-muted">CORE: ACTIVE</span>
        </div>
      </div>

      {/* Message stream */}
      <div ref={scrollRef} className="flex-1 space-y-3 overflow-y-auto px-3 py-4">
        {messages.length === 0 && (
          <div className="mt-6 text-center">
            <p className="font-mono text-[11px] leading-relaxed text-muted text-balance">
              Dinliyorum... Paris&apos;e bilet mi keselim, dünyayı mı değiştirelim?
            </p>
            <p className="mt-3 font-mono text-[9px] text-muted/70">
              dene: &quot;Paris&apos;e bilet bak ve araç ayarla&quot; · &quot;ekrandaki sinek ne?&quot;
            </p>
          </div>
        )}

        {messages.map((m) =>
          m.role === "user" ? (
            <div key={m.id} className="flex justify-end">
              <div className="max-w-[80%] rounded-lg rounded-br-sm border border-border-soft bg-panel px-3 py-2">
                <p className="font-mono text-[11px] leading-relaxed text-foreground">{m.text}</p>
              </div>
            </div>
          ) : (
            <div key={m.id} className="flex justify-start">
              <div className="max-w-[88%] rounded-lg rounded-bl-sm border border-neon-cyan/30 bg-panel px-3 py-2">
                {m.lines.map((line, i) => (
                  <p
                    key={i}
                    className={`animate-rise font-mono text-[11px] leading-relaxed ${toneColor[line.tone]}`}
                    style={{ animationDelay: `${i * 90}ms` }}
                  >
                    {line.tone === "core" && <span className="text-muted">🪰 </span>}
                    {line.text}
                  </p>
                ))}
              </div>
            </div>
          ),
        )}
      </div>

      {/* Input with Fly Glyph send button */}
      <div className="flex shrink-0 items-center gap-2 border-t border-border-soft bg-panel px-3 py-3">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={onKeyDown}
          placeholder="çekirdeğe seslen..."
          aria-label="Anka çekirdeğine mesaj"
          className="min-w-0 flex-1 rounded-md border border-border-soft bg-obsidian px-3 py-2 font-mono text-[12px] text-foreground outline-none placeholder:text-muted focus:border-neon-cyan"
        />
        <button
          type="button"
          onClick={send}
          disabled={!input.trim() || thinking}
          aria-label="Gönder (CLICK)"
          className="flex h-9 w-9 shrink-0 items-center justify-center rounded-md border border-neon-cyan/40 bg-obsidian transition-transform active:scale-90 disabled:opacity-40"
        >
          <FlyGlyph size={22} />
        </button>
      </div>
    </div>
  )
}
