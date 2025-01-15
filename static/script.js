const allEvents = []

async function fetchEvents() {
    try {
        const res = await fetch('/api/events')
        if (!res.ok)
            throw new Error('Network response was not ok ' + res.statusText);

        const { events } = await res.json()
        events.forEach(event => {
            console.log(event)
            if (!allEvents.some(e => e._id === event._id)) {
                allEvents.push(event);
            }
        });
        populateEvents()
    }
    catch (error) {
        console.error('Error fetching events:', error);
        document.getElementById('events').innerHTML = `<p style="color: red;">Failed to load events: ${error.message}</p>`;
    }
}

function populateEvents() {
    const eventsDiv = document.getElementById('events');

    if (allEvents.length > 0) {
        eventsDiv.innerHTML = ''; // Clear the previous content

        allEvents.forEach(event => {
            const eventDiv = document.createElement('div');
            eventDiv.classList.add('event');

            // Create formatted message for different event types
            let message = '';
            if (event.action === 'PUSH') {
                message = `${event.action} ${event.author}`;
            } else if (event.action === 'PULL_REQUEST') {
                message = `${event.action} ${event.author}`;
            } else if (event.action === 'MERGE') {
                message = `${event.action} ${event.author}`;
            }

            eventDiv.textContent = message;
            eventsDiv.appendChild(eventDiv);
        });
    } else {
        eventsDiv.textContent = 'No recent events found.';
    }

}

// Fetch events every 15 seconds
setInterval(fetchEvents, 15000);

// Fetch events on page load
fetchEvents();