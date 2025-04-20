import subprocess
from ollama import chat

ollama_process = None  # Global variable to track the Ollama process

def start_ollama():
    """
    Starts the Ollama model in a subprocess.
    """
    global ollama_process
    try:
        print("[Checkpoint] Starting Ollama...")
        ollama_process = subprocess.Popen(["ollama", "run", "llama3.2"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[Checkpoint] Ollama started successfully.")
    except Exception as e:
        print(f"[Error] Failed to start Ollama: {e}")

def stop_ollama():
    """
    Stops the Ollama model by terminating the subprocess.
    """
    global ollama_process
    if ollama_process:
        try:
            print("[Checkpoint] Stopping Ollama...")
            ollama_process.terminate()  # Terminate the process
            ollama_process.wait()  # Wait for the process to exit
            print("[Checkpoint] Ollama stopped successfully.")
        except Exception as e:
            print(f"[Error] Failed to stop Ollama: {e}")

def generate_speech(topic):
    """
    Generates a speech-like explanation for the given topic.
    """
    print("[Checkpoint] Generating speech for the topic...")
    prompt = (
        f"Create a detailed explanation about '{topic}' in a speech format. "
        "Ensure the text includes appropriate pauses, such as commas, periods, and ellipses, "
        "to make it suitable for text-to-speech conversion. The tone should be clear and engaging."
    )

    try:
        # Call the locally installed Llama 3.2 model
        response = chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}])
        explanation = response['message']['content'].strip()
        print("[Checkpoint] Speech generated successfully.")
        return explanation
    except Exception as e:
        print(f"[Error] Failed to generate speech: {e}")
        return None

if __name__ == "__main__":
    print("[Checkpoint] Script started.")
    start_ollama()  # Start Ollama before generating speech

    topic = input("[Checkpoint] Enter the topic for the speech: ")
    speech_text = generate_speech(topic)

    if speech_text:
        # Save the speech to a file
        output_file = "generated_speech.txt"
        try:
            print("[Checkpoint] Saving speech to file...")
            with open(output_file, "w") as file:
                file.write(speech_text)
            print(f"[Checkpoint] Speech saved to {output_file}")
        except Exception as e:
            print(f"[Error] Failed to save speech to file: {e}")
    else:
        print("[Error] No speech generated.")

    stop_ollama()  # Stop Ollama after the task is completed
    print("[Checkpoint] Script completed.")
