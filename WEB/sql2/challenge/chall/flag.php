<?php

session_start();
if (isset($_SESSION['login']) && $_SESSION['login'] != '') {
	echo '<p>Parabéns pelo ótimo trabalho.</p><p>Sua flag é DC5551{Sql_1nj3ct10n_c0nclu1d0_947}</p>';
	die;
}
header('location: http://' . $_SERVER['HTTP_HOST'] . '/index.php');

?>
