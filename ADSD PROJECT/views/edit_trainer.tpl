<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Trainer</title>
</head>
<body>
    <h1>Edit Trainer</h1>
    <form action="/trainer/edit/{{ trainer[0] }}" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ trainer[1] }}" required>
        <input type="submit" value="Update Trainer">
    </form>
    <a href="/trainers">Back to Trainers</a>
</body>
</html>
