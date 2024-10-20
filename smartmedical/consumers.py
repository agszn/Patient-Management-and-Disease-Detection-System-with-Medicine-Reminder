# yourapp/consumers.py

import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from .models import Prescription

class PrescriptionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'prescription_notifications'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Call the function to check for matching prescriptions
        await self.send_alerts()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_alerts(self):
        while True:
            current_time = timezone.now().time()
            matching_prescriptions = Prescription.objects.filter(time_to_be_taken=current_time)
            if matching_prescriptions.exists():
                alert_message = "Time to take medicine."
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'prescription_alert',
                        'message': alert_message
                    }
                )
            await asyncio.sleep(60)  # Check every minute
