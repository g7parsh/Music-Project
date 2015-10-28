
for  %%A in (*.webm)  do ffmpeg -i "%%A" -f mp3 "%%~NA".mp3
pause