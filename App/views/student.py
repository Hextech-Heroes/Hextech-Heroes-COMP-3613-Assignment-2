from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import Student
from App.controllers import (
    create_student,
    get_student,
    get_all_students
)

student = Blueprint("student",__name__)

@student.route("/student/<id>", methods=["GET"])
@jwt_required()
def search_student(id: str) -> tuple[Response, int]:
    student: Student | None = get_student(id)
    if student is None:
        return jsonify(error="Student not found"), 404
    return jsonify(student.get_json()), 200

@student.route("/students", methods=["GET"])
@jwt_required()
def search_students() -> tuple[Response, int]:
    students: list[Student] = get_all_students()
    return jsonify([s.get_json() for s in students]), 200

