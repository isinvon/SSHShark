@echo off
rem SSHShark - Windows �����ű�

rem ���� Python ��������������⻷�����滻·����
set PYTHON_PATH=python

rem ����Ƿ񴫵��˲���
if "%~1"=="" (
    echo �봫��������� SSHShark
    echo ����: sshsk.bat --login
    goto end
)

rem ִ�� Python ���ű�
%PYTHON_PATH% sshsk.py %*

:end
pause
