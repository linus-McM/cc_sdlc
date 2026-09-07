
# Start a Gemini session in YOLO approval mode
g_session:
    @agy --model top --dangerously-skip-permissions

opus:
    @claude --permission-mode auto --model opus "/caveman"


fable:
    @claude --permission-mode auto --model fable "/caveman"