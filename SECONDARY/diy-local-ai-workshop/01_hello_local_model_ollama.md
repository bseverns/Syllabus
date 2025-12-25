# Hello Local Model – Ollama Path

> **Goal:** By the end of this guide, you will have:
> - Installed Ollama
> - Downloaded a small language model
> - Had a short “conversation” with it on your own machine

This is the “most gentle” path into local models. We’ll use a tool called **Ollama**, which combines:

- A **model manager** (download/update)
- A **runtime** (how to run the model)
- A simple **interface** (terminal commands)

---

## 1. Check your system

### 1.1. Operating system

You’ll need:

- Windows 10 / 11  
- macOS (Intel or Apple Silicon)  
- or Linux (recent distribution)

If you’re not sure what you’re on, ask the instructor or a neighbor.

### 1.2. Hardware expectations

Rough guide:

- 8 GB RAM → small models, slower responses  
- 16 GB RAM → more comfortable, faster

We’ll start with a **small model** so most machines can participate.

---

## 2. Install Ollama

### 2.1. Download

1. Open your browser.
2. Go to the Ollama website (your instructor will project or share the URL).
3. Download the installer for your operating system.

### 2.2. Run the installer

- On **Windows**:
  - Double-click the `.exe` file
  - Follow the prompts (“Next”, “Install”, etc.)
- On **macOS**:
  - Open the `.dmg`
  - Drag the Ollama app to `Applications` if asked
- On **Linux**:
  - Use the instructions shown on the site (usually a couple of terminal commands)

When the installer finishes, Ollama will likely start a background service.

---

## 3. Confirm the installation

Open a terminal or command prompt:

- On **Windows**:
  - Press `Win + R`, type `cmd`, press Enter
- On **macOS**:
  - Open Spotlight (`Cmd + Space`), type `Terminal`, press Enter
- On **Linux**:
  - Open your usual terminal

Type:

```bash
ollama --version
```

You should see a version number such as:

```text
0.x.y
```

If you see “command not found” or similar, flag down the instructor.

---

## 4. Download a small model

We’re going to **pull** a small-ish model.

Your instructor will tell you the exact model name to use.  
It will look something like:

```bash
ollama pull <model-name>
```

Example pattern (do *not* run this literally unless instructed):

```bash
ollama pull my-small-model
```

This will:

- Connect to Ollama’s online registry
- Download the model weights (a big file that *is* the trained network)
- Store them on your machine

You’ll see progress as it downloads.

> **Instructor note:**  
> If the whole room is on the same Wi-Fi and your bandwidth is limited, consider:
> - Having participants *share* a few machines in small groups, or  
> - Pre-pulling the model on your machine and demonstrating there while slower downloads catch up.

---

## 5. Talk to your local model

Once the download finishes, run (with the model name your instructor specified):

```bash
ollama run <model-name>
```

You should see a prompt similar to:

```text
>>> 
```

Now type:

```text
Write a short, kind greeting from a local AI model running on my laptop.
```

Press Enter. Wait. The model should respond with text.

Try a few more:

```text
Explain what a language model is in two sentences, as if I were 12 years old.
```

```text
Give me three ideas for how a local AI model could help me in my daily life.
```

You can exit the session by typing:

```text
/exit
```

or pressing `Ctrl + C`.

---

## 6. Adjusting the model’s “mood” (temperature)

Inside an Ollama session, you can adjust **temperature**, which influences creativity.

Run again:

```bash
ollama run <model-name>
```

At the prompt:

```text
/temperature 0.2
Explain the difference between local AI and cloud AI in two bullet points.
```

Then:

```text
/temperature 0.8
Now rewrite that explanation as a brief, playful poem.
```

Notice the difference.

> **Instructor note:**  
> Pause here and ask participants:
> - Which setting feels more useful for their own work?
> - Do they see any risks with high creativity for tasks that require accuracy?

---

## 7. Save a transcript (optional)

If you’d like to keep a record of the conversation:

1. Copy/paste from the terminal into a text document, **or**
2. Use your terminal’s “copy whole buffer” feature if it has one.

You can save it as `my-first-local-model.txt` in a folder of your choosing.

---

## 8. Reflection prompts

Take two minutes to jot down:

- One thing that felt **surprisingly easy**
- One thing that felt **intimidating or fragile**
- One real task you’d like to try with this model

You’ll use these in later exercises and pair-work.

---

You’ve now run a language model locally.  
The next step is to see a different path—using Python and Hugging Face—and then we’ll turn these capabilities into small, opinionated tools.
