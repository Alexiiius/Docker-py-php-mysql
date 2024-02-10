<?php

echo "Hola mundo desde php en docker!";

$servername = "db";
$username = "user";
$password = "password"; // Asegúrate de que esto es una cadena de texto
$dbname = "mydb";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "CREATE TABLE IF NOT EXISTS MyTable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(40),
    lastname VARCHAR(40)
)";

if ($conn->query($sql) === TRUE) {
    echo "Table created successfully";
} else {
    echo "Error creating table: " . $conn->error;
}

// Insertar datos aleatorios
$sql = "INSERT INTO MyTable (firstname, lastname) VALUES ('Antonio', 'Recio')";
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Seleccionar y mostrar los datos
$sql = "SELECT id, firstname, lastname FROM MyTable";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // Mostrar los datos de cada fila
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();
?>