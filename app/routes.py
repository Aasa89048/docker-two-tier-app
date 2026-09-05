from flask import Blueprint, jsonify, request

from .db import get_db_connection, init_db
init_db()


api = Blueprint("api", __name__)


@api.get("/health")
def health():

    return jsonify({
        "status": "healthyy"
    }), 200


@api.get("/tasks")
def get_tasks():
    init_db()  
    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(

        "SELECT id, title, completed FROM tasks ORDER BY id"
    )


    tasks = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(tasks), 200


@api.get("/tasks/<int:task_id>")
def get_task(task_id):
    init_db()  
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, title, completed FROM tasks WHERE id = %s",
        (task_id,)
    )

    task = cursor.fetchone()

    cursor.close()
    connection.close()

    if task is None:
        return jsonify({
            "error": "Task not found"
        }), 404

    return jsonify(task), 200


@api.post("/tasks")
def create_task():
    init_db()  
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({
            "error": "title is required"
        }), 400

    title = data["title"]

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s)",
        (title,)
    )

    connection.commit()

    task_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({
        "id": task_id,
        "title": title,
        "completed": False
    }), 201


@api.put("/tasks/<int:task_id>")
def update_task(task_id):
    init_db()  
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "request body is required"
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET title = COALESCE(%s, title),
            completed = COALESCE(%s, completed)
        WHERE id = %s
        """,
        (
            data.get("title"),
            data.get("completed"),
            task_id
        )
    )

    connection.commit()

    if cursor.rowcount == 0:
        cursor.close()
        connection.close()

        return jsonify({
            "error": "Task not found"
        }), 404

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Task updated successfully"
    }), 200


@api.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    init_db()  
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
    )

    connection.commit()

    deleted = cursor.rowcount

    cursor.close()
    connection.close()

    if deleted == 0:
        return jsonify({
            "error": "Task not found"
        }), 404

    return jsonify({
        "message": "Task deleted successfully"
    }), 200