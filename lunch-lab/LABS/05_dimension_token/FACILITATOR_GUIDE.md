# Facilitator Guide: Dimension Token

## Lab purpose

Participants rapidly make a small dimension-controlled 3D file, export it as an STL, and see at least one design move from CAD into a live print queue.

This lab keeps the magic visible: digital dimensions become machine instructions; machine instructions become plastic; plastic reveals design decisions.

## Core challenge

Make a **30 mm × 18 mm × 3 mm** token with one raised mark, initials, icon, or short word. Optional: add a **4 mm** hole so the object can become a tag.

## 45-minute run

| Time | Segment | Action |
|---:|---|---|
| 0:00–0:04 | Show the object | Hold up a finished token and a failed token. Name the exact dimensions. |
| 0:04–0:08 | Explain the constraint | “Your job is not to make anything; your job is to make a tiny object that obeys measurements.” |
| 0:08–0:20 | Rapid CAD sprint | Participants open the prepared Tinkercad template or OpenSCAD template and personalize within limits. |
| 0:20–0:26 | Export + collect | Participants export STL files or submit to the facilitator queue. |
| 0:26–0:30 | Start live print | Slice one selected STL or a pre-vetted participant file; begin the print. |
| 0:30–0:40 | Print conversation | Use `DISCUSSION_DURING_PRINT.md`: first layer, tolerances, speed vs. quality, file-to-object pipeline. |
| 0:40–0:44 | Dimension Card | Participants record exact dimensions, one decision, and one predicted risk. |
| 0:44–0:45 | Bridge | Connect to createMPLS youth pathways and queued-print follow-up. |

## 60-minute run

| Time | Segment | Action |
|---:|---|---|
| 0:00–0:05 | Show artifacts | Finished token, failed token, slicer preview, and a “too big / too small” example. |
| 0:05–0:10 | Tool orientation | Tinkercad workplane, dimensions, grouping, text/icon, export. |
| 0:10–0:25 | CAD sprint | Participants make and personalize tokens. |
| 0:25–0:32 | Export + queue | Collect STLs; sort into “print now,” “print later,” and “needs repair.” |
| 0:32–0:38 | Slice live | Show nozzle, layer height, infill, supports, time estimate, and first layer preview. |
| 0:38–0:50 | Print + discuss | Start print and lead the constraint conversation. |
| 0:50–0:56 | Dimension Card + gallery | Participants complete cards; photograph cards/tokens. |
| 0:56–1:00 | Share + bridge | Ask: “What did the slicer reveal that CAD hid?” |

## Opening script

> Welcome to Dimension Token. In this Lunch Lab, you are going to make a small 3D file with real measurements: 30 by 18 by 3 millimeters. Then we will send one or more designs to the printer while we talk about what happens between idea, file, machine, and finished object.

## Key vocabulary

- Dimension
- Constraint
- STL
- Slicer
- Layer height
- Nozzle
- First layer
- Tolerance
- Support
- Iteration

## Facilitator decisions before the event

Choose one workflow:

1. **Tinkercad path** — easiest for mixed adults and classroom analogy.
2. **OpenSCAD / BlocksCAD path** — strongest exact-dimension and “code as object” framing.
3. **Hybrid path** — Tinkercad for participants; OpenSCAD on projector for parameter drama.

Choose one live-print model:

- **One selected participant design** if the file is clean.
- **One pre-vetted demo token** if time or software misbehaves.
- **Four-up batch plate** if multiple printers are ready and the room is small.

## Print-while-talking prompts

Use the running print as a visible clock. Do not fill the print time with filler. Keep returning to the object:

- What did the model promise?
- What did the slicer reveal?
- What does the first layer tell us?
- What would fail if the token were twice as thin?
- What changes when this becomes 100 copies instead of one?

## Closing prompt

> The file is not the finish line. The printed part is not the finish line either. The real skill is learning how to move between intention, measurement, machine behavior, and revision.
