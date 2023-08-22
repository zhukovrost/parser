<?php
include '../../templates/func.php';
include '../../templates/settings.php';
$a = json_decode(file_get_contents( "themes.json"));
foreach ($a as $theme){
  $insert_sql = "INSERT INTO themes (theme) VALUES ('$theme')";
  $conn->query($insert_sql);
}

?>