import os
from functools import wraps
from typing import Any

from flask import Flask, jsonify, redirect, render_template, request, session, url_for


app = Flask(__name__, template_folder="app/templates", static_folder="static")
app.secret_key = os.getenv("APP_SECRET_KEY", "placement-drive-demo-secret")

DEMO_USERS = {
    "demo@stratfuse.ai": {
        "password": "Demo@123",
        "name": "Demo Analyst",
        "role": "Intelligence Engineer",
    },
    "admin@stratfuse.ai": {
        "password": "Admin@123",
        "name": "System Admin",
        "role": "Platform Owner",
    },
}


def login_required(fn):
    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any):
        if "user_email" not in session:
            return redirect(url_for("login"))
        return fn(*args, **kwargs)

    return wrapper


@app.get("/")
def index():
    if "user_email" in session:
        return redirect(url_for("home"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if "user_email" in session:
            return redirect(url_for("home"))
        return render_template("login.html", error=None)

    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    user = DEMO_USERS.get(email)
    if not user or user["password"] != password:
        return render_template("login.html", error="Invalid credentials. Use demo login details."), 401

    session["user_email"] = email
    session["user_name"] = user["name"]
    session["user_role"] = user["role"]
    return redirect(url_for("home"))


@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.get("/home")
@login_required
def home():
    return render_template(
        "home.html",
        user_name=session.get("user_name"),
        user_email=session.get("user_email"),
        user_role=session.get("user_role"),
    )


@app.get("/ps1")
@login_required
def page_ps1():
    return render_template("ps1_intelligence_dashboard.html")


@app.get("/ps3")
@login_required
def page_ps3():
    return render_template("ps3_urban_growth.html")


@app.get("/ps4")
@login_required
def page_ps4():
    return render_template("ps4_traffic_intelligence_1.html")


@app.get("/api/me")
@login_required
def me():
    return jsonify(
        {
            "email": session.get("user_email"),
            "name": session.get("user_name"),
            "role": session.get("user_role"),
        }
    )


@app.get("/api/ps1/intel-nodes")
@login_required
def ps1_nodes():
    return jsonify(
        [
            {"id": 1, "type": "OSINT", "title": "Port Activity Spike", "lat": 28.5621, "lon": 77.2923},
            {"id": 2, "type": "HUMINT", "title": "Field Contact Alert", "lat": 28.6138, "lon": 77.2090},
            {"id": 3, "type": "IMINT", "title": "Thermal Trace", "lat": 28.6529, "lon": 77.2418},
        ]
    )


@app.get("/api/ps3/growth-zones")
@login_required
def ps3_zones():
    return jsonify(
        [
            {"zone": "Dwarka Sector 21", "gvs": 84, "horizon_months": 36},
            {"zone": "Noida Extension", "gvs": 78, "horizon_months": 30},
            {"zone": "Sohna Corridor", "gvs": 71, "horizon_months": 48},
        ]
    )


@app.get("/api/ps4/predicted-hotspots")
@login_required
def ps4_hotspots():
    return jsonify(
        [
            {"location": "AIIMS Flyover", "risk_level": "HIGH", "eta_to_standstill_min": 22},
            {"location": "ITO Junction", "risk_level": "MEDIUM", "eta_to_standstill_min": 31},
            {"location": "Dhaula Kuan", "risk_level": "HIGH", "eta_to_standstill_min": 18},
        ]
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
