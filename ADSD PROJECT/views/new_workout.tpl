<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Workout</title>
</head>
<body>
    <h1>Add Workout</h1>
    <form action="/workout/new" method="post">
        <label for="trainee_id">Trainee ID:</label>
        <input type="text" id="trainee_id" name="trainee_id" required>
        <label for="hours">Hours:</label>
        <input type="text" id="hours" name="hours" required>
        <input type="submit" value="Add Workout">
    </form>
    <a href="/workouts">Back to Workouts</a>
</body>
</html>
