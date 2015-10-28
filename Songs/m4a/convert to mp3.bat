
for  %%A in (*.m4a)  do ffmpeg -i "%%A" -f mp3 "%%~NA".mp3
for %%A in (*.m4a) do del "%%A"
pause