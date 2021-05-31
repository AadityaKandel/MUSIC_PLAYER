echo off
cls

echo Checking Music_Player.py [ file ]
echo.
timeout /T 3

if EXIST "Music_Player.py" ( goto ch_su ) else ( goto ch_unsu )

:ch_su

cls
echo Music_Player.py File Found........
echo.
timeout /T 3
cls
echo Installing EYED3 Via Python........
echo.
pip install eyed3
cls

if %ERRORLEVEL% EQU 0 ( cls & echo EYED3 Is Installed Succesfully & echo. & timeout /T 2 & goto step2 ) else ( goto quit )

:ch_unsu

cls
echo Installization Of Python Packages Failed
echo.
echo Reason [ Music_Player.py cannot be found ]
echo.
pause
exit

:quit
cls
echo Installization Of This Package Is Unsuccessful
echo If one package is not available, application cannot be run
echo.
echo EXITTING........
echo.
pause
exit

:step2
cls
echo Installing Pygame Via Python..........
echo.
pip install pygame
if %ERRORLEVEL% EQU 0 ( cls & echo Pygame Is Installed Succesfully & echo. & timeout /T 2 & goto step3 ) else ( goto quit )

:step3
cls
echo Installing Mutagen Via Python..........
echo.
pip install mutagen
if %ERRORLEVEL% EQU 0 ( cls & echo Mutagen Is Installed Succesfully & echo. & timeout /T 2 & goto at_last ) else ( goto quit )

:at_last
cls
echo All Installization Succeed.....
echo.
echo Opening Music_Player.py In 4 Seconds
timeout /T 4
cls
start Music_Player.py
cls
exit
