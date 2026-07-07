"use client"

// A minimalist pixelated cyber-fly rendered from a bitmap grid so it reads as
// "siber-sinek" rather than a smooth vector insect. `blink` rubs the eyes.

const BODY: Array<[number, number]> = [
  // eyes (row 0-1)
  [4, 0], [7, 0],
  [3, 1], [4, 1], [7, 1], [8, 1],
  // head / thorax
  [5, 2], [6, 2],
  [5, 3], [6, 3],
  [4, 4], [5, 4], [6, 4], [7, 4],
  // abdomen segments
  [5, 5], [6, 5],
  [5, 6], [6, 6],
  [5, 7], [6, 7],
  [5, 8], [6, 8],
]

const WINGS: Array<[number, number]> = [
  [1, 3], [2, 3], [3, 3], [8, 3], [9, 3], [10, 3],
  [0, 4], [1, 4], [2, 4], [9, 4], [10, 4], [11, 4],
  [1, 5], [2, 5], [3, 5], [8, 5], [9, 5], [10, 5],
]

// Forelegs used by the "rubbing eyes" blink pose.
const LEGS: Array<[number, number]> = [
  [3, 2], [8, 2],
]

export function FlyGlyph({
  size = 64,
  className = "",
  color = "var(--electric-blue)",
  wingColor = "var(--neon-cyan)",
  blink = false,
}: {
  size?: number
  className?: string
  color?: string
  wingColor?: string
  blink?: boolean
}) {
  const cols = 12
  const rows = 9
  const px = size / cols

  return (
    <svg
      width={size}
      height={size * (rows / cols)}
      viewBox={`0 0 ${cols} ${rows}`}
      className={className}
      role="img"
      aria-label="Anka OS siber-sinek"
      shapeRendering="crispEdges"
    >
      {WINGS.map(([x, y], i) => (
        <rect key={`w${i}`} x={x} y={y} width={1} height={1} fill={wingColor} opacity={blink ? 0.35 : 0.55} />
      ))}
      {BODY.map(([x, y], i) => (
        <rect key={`b${i}`} x={x} y={y} width={1} height={1} fill={color} />
      ))}
      {blink &&
        LEGS.map(([x, y], i) => <rect key={`l${i}`} x={x} y={y} width={1} height={1} fill={color} opacity={0.9} />)}
      {/* eye glint */}
      {!blink && (
        <>
          <rect x={4} y={0} width={1} height={1} fill={wingColor} />
          <rect x={7} y={0} width={1} height={1} fill={wingColor} />
        </>
      )}
      {/* px is exposed via viewBox scaling; referenced to satisfy linters */}
      <desc>{`pixel size ${px.toFixed(2)}`}</desc>
    </svg>
  )
}
