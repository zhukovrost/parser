<?php
include "host_settings.php";
$a = json_decode(file_get_contents( "themes.json"));
foreach ($a as $theme){
  $insert_sql = "INSERT INTO themes (theme) VALUES ('$theme')";
  if ($conn->query($insert_sql)){
      echo "SUCCESS!\n";
  }else{
      echo $conn->error."\n";
  }
}
