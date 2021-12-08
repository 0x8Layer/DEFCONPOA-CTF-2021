<?php

ini_set('display_errors', 0);
error_reporting(0);

if (isset($_GET['debug'])) {
  die(highlight_string(file_get_contents("index.php")));
}


if (isset($_POST['username']) && $_POST['username'] != '' && isset($_POST['password']) && $_POST['password'] != '') {
  
  $username = $_POST['username'];
  $password = md5($_POST['password']);

  $msg_erro = '';
  if(1 === preg_match('~[0-9]~', $username) || stripos(strtolower($username), 'select') !== false || stripos(strtolower($username), 'union') !== false || stripos(strtolower($username), 'order') !== false || stripos(strtolower($username), 'where') !== false || stripos(strtolower($username), 'join') !== false) {
    $msg_erro = 'Tentativa de ataque bloqueada. Tente novamente';
  }
  else {
    $chars = ['%', ' ', '+', '=', ',', ';', "' ", " '", '"', '\\', '`', '&', 'or', 'Or', 'OR', 'oR', '<', '>'];
    foreach ($chars as $char) {
      if (strpos($username, $char) !== false) {
        $msg_erro = 'Tentativa de ataque bloqueada. Tente novamente';
      }
    }
  }

  if ($msg_erro == '') {
    require 'config.php';
    $conn = new mysqli($db['host'], $db['username'], $db['pass'], $db['database']);

    if ($conn->connect_error) {
      die('Falha ao conectar com o banco de dados');
    }

    $sql = "SELECT login FROM user WHERE login = '{$username}' AND pass = '{$password}' LIMIT 1;";
    $result = @$conn->query($sql);

    if (@$result->num_rows > 0) {
      while($row = $result->fetch_assoc()) {
        session_start();
        $_SESSION['login'] = $row['login'];

        header('location: http://' . $_SERVER['HTTP_HOST'] . '/flag.php');
        die;
      }
    }
    else {
      $msg_erro = 'Usuário e/ou senha inválidos. Tente novamente';
    }
    $conn->close();
  }
}

?>

<!DOCTYPE html>
<html>
  <head>
    <title>SQL 2</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet">
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <form method="POST" action="http://<?= $_SERVER['HTTP_HOST'] ?>/index.php">
      <h1>Login - SQL 2</h1>
      <h5>Entre com o usuário admin para capturar a flag</h5>
      <div class="formcontainer">
      <hr/>
      <?= (isset($msg_erro) ? '<p style="color:red;">'. $msg_erro . '</p>' : ''); ?>
      <div class="container">
        <label for="uname"><strong>Username</strong></label>
        <input type="text" placeholder="Enter Username" name="username" required>
        <label for="password"><strong>Password</strong></label>
        <input type="password" placeholder="Enter Password" name="password" required>
      </div>
      <button type="submit">Login</button>
      <div class="container" style="background-color: #eee">
        <label style="padding-left: 15px">
        <input type="checkbox" checked="checked" name="remember"> Remember me
        </label>
        <span class="psw"><a href="#"> Forgot password?</a></span>
      </div>
    </form>
    <!-- ?debug -->
  </body>
</html>
