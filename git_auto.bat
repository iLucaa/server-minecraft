@echo off
git add .
git commit -m "Commit auto: %date% %time%"
git push origin main
