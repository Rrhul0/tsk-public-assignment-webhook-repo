async function fetchEvents() {
    try {
        const res = await fetch('/api/events')
        if (!res.ok)
            throw new Error('Network response was not ok ' + res.statusText);

        const { events } = await res.json()

        populateEvents(events)
    }
    catch (error) {
        console.error('Error fetching events:', error);
        document.getElementById('events').innerHTML = `<p style="color: red;">Failed to load events: ${error.message}</p>`;
    }
}

function populateEvents(events) {
    const eventsDiv = document.getElementById('events');

    if (events.length > 0) {
        eventsDiv.innerHTML = ''; // Clear the previous content

        events.forEach(event => {
            const eventDiv = document.createElement('div');
            eventDiv.classList.add('event');

            // Create formatted message for different event types
            let message = '';

            if (event.action === 'PUSH') {
                message = `"${event.author}" pushed to "${event.to_branch}" on ${event.timestamp}`;
            } else if (event.action === 'PULL_REQUEST') {
                message = `"${event.author}" submitted a pull request from "${event.from_branch}" to "${event.to_branch}" on ${event.timestamp}`;
            } else if (event.action === 'MERGE') {
                message = `${event.author} merged branch "${event.from_branch}" to "${event.to_branch}" on ${event.timestamp}`;
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