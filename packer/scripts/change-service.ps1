$ServiceName = (Get-Service "actions.runner*").Name

Stop-Service $ServiceName -ErrorAction SilentlyContinue

sc.exe config $ServiceName obj= LocalSystem

Start-Service $ServiceName