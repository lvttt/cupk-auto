@echo off
cd /d "%~dp0"

set exe1=app.exe
set exe2=httpServe.exe

start "" "%exe1%"
start "" "%exe2%"
