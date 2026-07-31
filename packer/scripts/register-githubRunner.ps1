$Owner = $args[0]
$Repo = $args[1]
$PAT = $args[2]

if (Test-Path "C:\actions-runner\.runner")
{
    exit 0
}

if ($Owner -like '' -or $Repo -like '' -or $PAT -like ''){
    exit 1
}

$RunnerName = $env:COMPUTERNAME

$Headers = @{
    Authorization = "Bearer $PAT"
    Accept = "application/vnd.github+json"
}

$TokenResponse = Invoke-RestMethod `
    -Method POST `
    -Uri "https://api.github.com/repos/$Owner/$Repo/actions/runners/registration-token" `
    -Headers $Headers

$Token = $TokenResponse.token

Set-Location C:\actions-runner

.\config.cmd `
    --url "https://github.com/$Owner/$Repo" `
    --token $Token `
    --name $RunnerName `
    --unattended `
    --replace `
    --runasservice