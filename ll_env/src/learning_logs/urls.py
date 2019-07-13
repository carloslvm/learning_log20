""" Defines urls for learning_logs """

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
	# Home Page
	path('', views.index, name='index'),

	# Show all the topics
	path('topics/', views.topics, name='topics'),

	# Detail page for a single topic.
	path('topics/<int:topic_id>/', views.topic, name='topic'),

	# Page for adding new topics.
	path('new_topic/', views.new_topic, name='new_topic'),

	# Page for adding new entry.
	path('newEntry/<int:topic_id>/', views.newEntry, name='newEntry'),
	
	# Page for editing an entry
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

	]
