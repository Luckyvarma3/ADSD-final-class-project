<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Trainer</title>
</head>
<body>
    <h1>Add Trainer</h1>
    <form action="/trainer/new" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <input type="submit" value="Add Trainer">
    </form>
    <a href="/trainers">Back to Trainers</a>
</body>
</html>
