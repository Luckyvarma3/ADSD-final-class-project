<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Trainee</title>
</head>
<body>
    <h1>Add Trainee</h1>
    <form action="/trainee/new" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="trainer_id">Trainer ID:</label>
        <input type="text" id="trainer_id" name="trainer_id" required>
        <input type="submit" value="Add Trainee">
    </form>
    <a href="/trainees">Back to Trainees</a>
</body>
</html>
