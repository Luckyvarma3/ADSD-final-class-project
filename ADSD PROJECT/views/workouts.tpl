<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workouts</title>
</head>
<body>
    <h1>Workouts</h1>
    <a href="/workout/new">Add Workout</a>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Trainee ID</th>
            <th>Hours</th>
            <th>Action</th>
        </tr>
        % for workout in workouts:
            <tr>
                <td>{{ workout[0] }}</td>
                <td>{{ workout[1] }}</td>
                <td>{{ workout[2] }}</td>
                <td>
                    <a href="/workout/edit/{{ workout[0] }}">Edit</a>
                    <a href="/workout/delete/{{ workout[0] }}" onclick="return confirm('Are you sure?')">Delete</a>
                </td>
            </tr>
        % end
    </table>
</body>
</html>
