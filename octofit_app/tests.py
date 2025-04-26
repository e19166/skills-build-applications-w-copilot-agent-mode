from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def test_create_user(self):
        data = {"email": "test@example.com", "name": "Test User", "age": 25, "gender": "Male"}
        response = self.client.post("/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def test_create_team(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25, gender="Male")
        data = {"name": "Team A", "members": [user.id]}
        response = self.client.post("/teams/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25, gender="Male")
        data = {"user": user.id, "activity_type": "Running", "duration": 30, "calories_burned": 300, "date": "2025-04-26"}
        response = self.client.post("/activities/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25, gender="Male")
        data = {"user": user.id, "points": 100}
        response = self.client.post("/leaderboard/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        data = {"name": "Morning Run", "description": "A quick morning run.", "duration": 30, "calories_burned": 300}
        response = self.client.post("/workouts/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
