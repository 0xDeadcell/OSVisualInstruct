$totalFrames = 0
Get-ChildItem -Path 'C:\Users\Matt3\git\OSVisualInstruct\recordings' -Recurse -Filter *.mp4 | ForEach-Object {
    $frameCount = ffprobe -v 0 -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of compact=p=0:nk=1 $_.FullName
    $totalFrames += $frameCount
}
$totalFrames
