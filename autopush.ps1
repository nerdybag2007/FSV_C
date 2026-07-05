while ($true) {
    git add .

    $changes = git status --porcelain

    if ($changes) {
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

        git commit -m "Auto commit $timestamp"
        git push origin $(git branch --show-current)
    }

    Start-Sleep -Seconds 60
}