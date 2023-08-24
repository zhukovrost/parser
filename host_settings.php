<?php
# Host settings

define("HOSTNAME", "localhost");
define("HOSTUSER", "root");
define("HOSTPASSWORD", "");
define("HOSTDB", "english");


date_default_timezone_set("Europe/Moscow");

$conn = new mysqli(HOSTNAME, HOSTUSER, HOSTPASSWORD, HOSTDB);
