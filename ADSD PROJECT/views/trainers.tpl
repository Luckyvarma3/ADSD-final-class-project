<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trainers</title>
</head>
<body>
    <h1>Trainers</h1>
    <a href="/trainer/new">Add Trainer</a>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Action</th>
        </tr>
        % for trainer in trainers:
            <tr>
                <td>{{ trainer[0] }}</td>
                <td>{{ trainer[1] }}</td>
                <td>
                    <a href="/trainer/edit/{{ trainer[0] }}">Edit</a>
                    <a href="/trainer/delete/{{ trainer[0] }}" onclick="return confirm('Are you sure?')">Delete</a>
                </td>
            </tr>
        % end
    </table>
</body>
</html>
