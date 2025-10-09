document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: []
    });

    calendar.render();

    // Request permission for notifications
    if (Notification.permission !== 'granted') {
        Notification.requestPermission();
    }

    document.getElementById('event-form').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const eventName = document.getElementById('event-name').value;
        const eventTime = new Date(document.getElementById('event-time').value);
        
        calendar.addEvent({
            title: eventName,
            start: eventTime
        });

        const now = new Date();
        const timeDifference = eventTime - now;
        
        if (timeDifference > 0) {
            setTimeout(() => {
                if (Notification.permission === 'granted') {
                    new Notification(`Reminder: ${eventName} is starting soon!`);
                } else {
                    alert(`Event "${eventName}" is starting soon!`);
                }
            }, timeDifference);
        }
        
        document.getElementById('event-form').reset();
    });
});