from django.urls import path, include
from .views import (
    UAVListCreateView, UAVDetailView,
    FlightLogListCreateView, FlightLogDetailView, FlightGPSDataUploadView,
    MaintenanceLogListCreateView, MaintenanceLogDetailView,
    MaintenanceReminderListCreateView, MaintenanceReminderDetailView,
    FileListCreateView, FileDetailView,
    UserListCreateView, UserDetailView,
    UserSettingsListCreateView, UserSettingsDetailView,
    AdminUserListView, AdminUserDetailView, AdminUAVListView, AdminUAVDetailView,
    UAVImportView, FlightLogImportView, UserDataExportView, UserDataImportView,
    UAVConfigListCreateView, UAVConfigDetailView,
    FlightLogMetaView, UAVMetaView
)

urlpatterns = [
    # Endpunkte für UAVs
    path('uavs/', UAVListCreateView.as_view(), name='uav-list'),
    path('uavs/<int:pk>/', UAVDetailView.as_view(), name='uav-detail'),

    # New endpoint for UAV meta
    path('uavs/meta/', UAVMetaView.as_view(), name='uav-meta'),

    # Endpunkte für Flightlogs
    path('flightlogs/', FlightLogListCreateView.as_view(), name='flightlog-list'),
    path('flightlogs/<int:pk>/', FlightLogDetailView.as_view(), name='flightlog-detail'),
    
    # New endpoint for GPS data
    path('flightlogs/<int:flightlog_id>/gps/', FlightGPSDataUploadView.as_view(), name='flightlog-gps'),

    # New endpoint for FlightLog meta
    path('flightlogs/meta/', FlightLogMetaView.as_view(), name='flightlog-meta'),

    # Endpunkte für Wartungsprotokolle
    path('maintenance/', MaintenanceLogListCreateView.as_view(), name='maintenance-list'),
    path('maintenance/<int:pk>/', MaintenanceLogDetailView.as_view(), name='maintenance-detail'),

    # Endpunkte für Wartungserinnerungen
    path('maintenance-reminders/', MaintenanceReminderListCreateView.as_view(), name='maintenance-reminder-list'),
    path('maintenance-reminders/<int:pk>/', MaintenanceReminderDetailView.as_view(), name='maintenance-reminder-detail'),

    # Endpunkte für Dateien
    path('files/', FileListCreateView.as_view(), name='file-list'),
    path('files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),

    # Optional: Endpunkte für Benutzer
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Optional: Endpunkte für Benutzereinstellungen
    path('user-settings/', UserSettingsListCreateView.as_view(), name='user-settings-list'),
    path('user-settings/<int:pk>/', UserSettingsDetailView.as_view(), name='user-settings-detail'),

    # Admin routes
    path('admin/users/', AdminUserListView.as_view(), name='admin-user-list'),
    path('admin/users/<int:pk>/', AdminUserDetailView.as_view(), name='admin-user-detail'),
    path('admin/uavs/', AdminUAVListView.as_view(), name='admin-uavs-list'),
    path('admin/uavs/<int:pk>/', AdminUAVDetailView.as_view(), name='admin-uav-detail'),

    # Import endpoints
    path('import/uav/', UAVImportView.as_view(), name='uav-import'),
    path('import/flightlog/', FlightLogImportView.as_view(), name='flightlog-import'),

    # Export and Import endpoints
    path('export-user-data/', UserDataExportView.as_view(), name='export-user-data'),
    path('import-user-data/', UserDataImportView.as_view(), name='import-user-data'),

    # Endpoints for UAV Configurations
    path('uav-configs/', UAVConfigListCreateView.as_view(), name='uav-config-list'),
    path('uav-configs/<int:pk>/', UAVConfigDetailView.as_view(), name='uav-config-detail'),
]
