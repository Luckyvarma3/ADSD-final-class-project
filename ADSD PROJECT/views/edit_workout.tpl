<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Workout</title>
</head>
<body>
    <h1>Edit Workout</h1>
    <form action="/workout/edit/{{ workout[0] }}" method="post">
        <label for="trainee_id">Trainee ID:</label>
        <input type="text" id="trainee_id" name="trainee_id" value="{{ workout[1] }}" required>
        <label for="hours">Hours:</label>
        <input type="text" id="hours" name="hours" value="{{ workout[2] }}" required>
        <input type="submit" value="Update Workout">
    </form>
    <a href="/workouts">Back to Workouts</a>
</body>
</html>
