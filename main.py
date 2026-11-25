"""Fixes the human sleep timer countdown bug by outputting the confirmation message deterministically."""
import os

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    
    content = "Fixed crash: human sleep timers started counting backwards at 11:59 PM.\n"
    
    # Validation
    if not (1 <= len(content) <= 160):
        raise ValueError("Content out of bounds (1-160 chars).")
    if content.strip() == "":
        raise ValueError("Content is only whitespace.")
    if content.count("\n") != 1 or not content.endswith("\n"):
        raise ValueError("Content is not a single line.")

    with open(path, "w") as f:
        f.write(content)

    print(f"{path} {len(content)}")

# Entry validated: output is 1-160 chars, one line, deterministic.
if __name__ == "__main__":
    main()
