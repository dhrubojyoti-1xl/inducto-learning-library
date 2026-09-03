Add-Type -AssemblyName System.IO.Compression.FileSystem
$root = (Get-Location).Path
$out = @()
Get-ChildItem -LiteralPath $root -Recurse -File | Where-Object Extension -eq '.pptx' | Sort-Object FullName | ForEach-Object {
  $file = $_
  $zip = [System.IO.Compression.ZipFile]::OpenRead($file.FullName)
  try {
    $slides = @()
    $entries = $zip.Entries | Where-Object { $_.FullName -match '^ppt/slides/slide(\d+)\.xml$' } | Sort-Object { [int]([regex]::Match($_.FullName,'slide(\d+)').Groups[1].Value) }
    foreach ($entry in $entries) {
      $reader = [IO.StreamReader]::new($entry.Open())
      try { $xmlText = $reader.ReadToEnd() } finally { $reader.Dispose() }
      [xml]$xml = $xmlText
      $texts = @($xml.SelectNodes("//*[local-name()='t']") | ForEach-Object { $_.'#text' })
      $slideNum = [int]([regex]::Match($entry.FullName,'slide(\d+)').Groups[1].Value)
      $relName = "ppt/slides/_rels/slide$slideNum.xml.rels"
      $rel = $zip.GetEntry($relName)
      $links = @()
      if ($rel) {
        $rr = [IO.StreamReader]::new($rel.Open())
        try { [xml]$rx = $rr.ReadToEnd() } finally { $rr.Dispose() }
        $links = @($rx.SelectNodes("//*[local-name()='Relationship']") | Where-Object { $_.TargetMode -eq 'External' } | ForEach-Object { $_.Target })
      }
      $notes = @()
      $notesEntry = $zip.GetEntry("ppt/notesSlides/notesSlide$slideNum.xml")
      if ($notesEntry) {
        $nr = [IO.StreamReader]::new($notesEntry.Open())
        try { [xml]$nx = $nr.ReadToEnd() } finally { $nr.Dispose() }
        $notes = @($nx.SelectNodes("//*[local-name()='t']") | ForEach-Object { $_.'#text' })
      }
      $slides += [pscustomobject]@{ slide=$slideNum; text=($texts -join ' | '); links=$links; notes=($notes -join ' | ') }
    }
    $relative = $file.FullName.Substring($root.TrimEnd('\').Length + 1)
    $out += [pscustomobject]@{ filename=$file.Name; relative_path=$relative; slide_count=$slides.Count; slides=$slides }
  } finally { $zip.Dispose() }
}
$out | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $root 'pptx_extract.json') -Encoding utf8
Write-Output ("Extracted {0} decks and {1} slides" -f $out.Count, (($out | ForEach-Object slide_count | Measure-Object -Sum).Sum))
