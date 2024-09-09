# Ollama-installation-without-root-priviledge

### Step1. Download pre-built binaries 
https://github.com/ollama/ollama/issues/2111 <br>
https://github.com/ollama/ollama/releases <br>
<br>
chmod +x ollama-linux-amd64<br>

### Step2. Start the server
cd /ollama_binary<br>
ollama serve &<br>
or ollama-linux-amd64 serve & (depends on binary names)<br>

### Step3. Run a local model or run a Python script using API
ollama-linux-amd64 pull llama3 (pull model only)<br>
ollama-linux-amd64 run llama3<br>
<br>
test.py<br>

### Change model dirs (if needed)
https://www.reddit.com/r/ollama/comments/1c4zg15/does_anyone_know_how_to_change_where_your_models/<br>
<br>
export OLLAMA_MODELS=/export/data/yanglab/ollama_models<br>

### Offline model installation (if an error occurs using ollama pull)
https://github.com/ollama/ollama/issues/696 <br>

### Check Status
(ollama) [user@ssh-server] $ ollama-linux-amd64 ps <br>
NAME               	ID          	SIZE 	PROCESSOR	UNTIL              <br>
llama3:70b-instruct	786f3184aec0	44 GB	100% GPU 	4 minutes from now <br>

### How to kill the server
(ollama) [user@ssh-server] $ ps aux | grep ollama <br>
user     3702943 48.5  0.0 22327612 921660 pts/1 Sl   18:09   4:23 ./ollama serve <br>
user     3703746  0.0  0.0   9364  1992 pts/4    S+   18:18   0:00 grep ollama <br>

### or
(ollama) [user@ssh-server] $ lsof -i :11434 <br>
COMMAND     PID  USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME <br>
ollama  3702943 user   3u  IPv4 63450143      0t0  TCP localhost:11434 (LISTEN) <br>

### Kill:
(ollama) [user@ssh-server] $ kill 3702943 <br>
