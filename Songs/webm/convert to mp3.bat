set usr_out = n

for  %%A in (*.webm)  do ffmpeg -i "%%A" -f mp3 "%%~NA".mp3 -nostdin
for %%A in (*.webm) do del "%%A"
pause