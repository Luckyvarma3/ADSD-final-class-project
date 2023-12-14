<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Trainee</title>
</head>
<body>
    <h1>Edit Trainee</h1>
    <form action="/trainee/edit/{{ trainee[0] }}" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ trainee[1] }}" required>
        <label for="trainer_id">Trainer ID:</label>
        <input type="text" id="trainer_id" name="trainer_id" value="{{ trainee[2] }}" required>
        <input type="submit" value="Update Trainee">
    </form>
    <a href="/trainees">Back to Trainees</a>
</body>
</html>
