/**
 * Calendar Export for Weekly Schedule
 * Generates .ics file for Apple Calendar with reminders
 */

// Generate ICS content
function generateICSContent() {
    const today = new Date();
    const dayOfWeek = today.getDay();
    const daysUntilMonday = (8 - dayOfWeek) % 7 || 7;
    const nextMonday = new Date(today);
    nextMonday.setDate(today.getDate() + daysUntilMonday);

    const formatDateTime = (date, hours, minutes) => {
        const d = new Date(date);
        d.setHours(hours, minutes, 0, 0);
        const year = d.getFullYear();
        const month = String(d.getMonth() + 1).padStart(2, '0');
        const day = String(d.getDate()).padStart(2, '0');
        const h = String(hours).padStart(2, '0');
        const m = String(minutes).padStart(2, '0');
        return `${year}${month}${day}T${h}${m}00`;
    };

    const uid = () => `${Date.now()}-${Math.random().toString(36).substr(2, 9)}@schedule`;

    const createEvent = (date, startHour, startMin, endHour, endMin, title, description, alarmMinutes = 5) => {
        const dtstart = formatDateTime(date, startHour, startMin);
        const dtend = formatDateTime(date, endHour, endMin);
        return `BEGIN:VEVENT
UID:${uid()}
DTSTAMP:${formatDateTime(new Date(), new Date().getHours(), new Date().getMinutes())}
DTSTART:${dtstart}
DTEND:${dtend}
SUMMARY:${title}
DESCRIPTION:${description}
BEGIN:VALARM
TRIGGER:-PT${alarmMinutes}M
ACTION:DISPLAY
DESCRIPTION:${title} in ${alarmMinutes} minutes
END:VALARM
BEGIN:VALARM
TRIGGER:PT0M
ACTION:AUDIO
END:VALARM
END:VEVENT
`;
    };

    let events = '';

    // Monday through Friday
    for (let i = 0; i < 5; i++) {
        const date = new Date(nextMonday);
        date.setDate(nextMonday.getDate() + i);

        events += createEvent(date, 7, 0, 7, 15, 'Wake Up', 'Alarm off. Feet on floor. Make bed.', 0);
        events += createEvent(date, 7, 15, 7, 25, 'Prayer', '10 minutes. Quiet, focused, no phone.', 0);
        events += createEvent(date, 7, 35, 7, 50, 'Morning Yoga', '15-minute flow', 0);
        events += createEvent(date, 7, 55, 8, 10, 'Breakfast', 'Quick breakfast', 0);
        events += createEvent(date, 8, 15, 8, 30, 'Pre-Market Prep', 'Review watchlist, overnight news, set alerts', 5);
        events += createEvent(date, 8, 30, 12, 0, 'TRADING SESSION', 'Full focus. Execute the plan. Log all trades.', 5);
        events += createEvent(date, 10, 30, 10, 35, 'Water Break', 'Stand up. Stretch. Refill water.', 0);
        events += createEvent(date, 12, 5, 12, 30, 'Lunch', 'Eat and recharge', 5);
        events += createEvent(date, 12, 45, 16, 15, 'CODING SESSION', 'SuperTradeBros development', 5);
        events += createEvent(date, 14, 0, 14, 10, 'Coding Break', 'Water. Walk around. Rest eyes.', 0);

        if (i === 1) { // Tuesday
            events += createEvent(date, 15, 15, 15, 30, 'Pre-Workout', 'Snack + change clothes', 5);
            events += createEvent(date, 15, 30, 16, 20, 'WORKOUT', 'Light-Moderate Legs (Home)', 5);
            events += createEvent(date, 16, 50, 17, 10, 'Dinner (Early)', 'Quick meal before class', 5);
            events += createEvent(date, 17, 50, 18, 0, 'Travel to Algo Class', 'Leave for class', 10);
            events += createEvent(date, 18, 0, 22, 0, 'ALGO CLASS', 'Full focus. Take good notes.', 5);
            events += createEvent(date, 22, 10, 22, 30, 'Wind Down', 'Quick yoga + bed prep', 0);
            events += createEvent(date, 22, 30, 22, 31, 'LIGHTS OUT', 'Sleep!', 5);
        } else {
            events += createEvent(date, 16, 15, 16, 30, 'Pre-Workout', 'Snack + change clothes', 5);
            if (i === 2 || i === 4) {
                events += createEvent(date, 16, 30, 17, 30, 'WORKOUT (Gym)', i === 2 ? 'Moderate Upper' : 'Heavy Lower + Pulls', 5);
            } else {
                events += createEvent(date, 16, 30, 17, 15, 'WORKOUT (Home)', i === 0 ? 'Light Upper + Pull-ups' : 'Moderate-Heavy Full Body', 5);
            }
            events += createEvent(date, 18, 15, 18, 35, 'Dinner', 'Sit down. No screens. Enjoy the food.', 5);
            events += createEvent(date, 18, 55, 19, 25, 'Market Analysis', 'Review market. Prep watchlist.', 5);
            events += createEvent(date, 21, 0, 21, 10, 'SCREEN CURFEW', 'All screens off. Evening yoga.', 5);
            events += createEvent(date, 21, 35, 21, 45, 'Bed Prep', 'Brush teeth. Set alarm.', 0);
            events += createEvent(date, 21, 45, 21, 46, 'LIGHTS OUT', '9+ hours of sleep.', 5);
        }
    }

    // Saturday
    const saturday = new Date(nextMonday);
    saturday.setDate(nextMonday.getDate() + 5);
    events += createEvent(saturday, 7, 0, 7, 15, 'Wake Up', 'Make bed.', 0);
    events += createEvent(saturday, 7, 15, 7, 25, 'Prayer', '10 minutes', 0);
    events += createEvent(saturday, 7, 35, 7, 50, 'Morning Yoga', '15-minute flow', 0);
    events += createEvent(saturday, 7, 50, 8, 15, 'Breakfast', 'Peak day needs fuel', 0);
    events += createEvent(saturday, 8, 55, 10, 15, 'Coding / Projects', 'Deep focus coding', 5);
    events += createEvent(saturday, 11, 0, 12, 5, 'PEAK WORKOUT (Gym)', 'Power cleans, heavy squats, bench', 15);
    events += createEvent(saturday, 12, 45, 13, 10, 'Lunch', '', 5);
    events += createEvent(saturday, 13, 20, 16, 30, 'Coding / Projects', '', 5);
    events += createEvent(saturday, 19, 0, 19, 30, 'Weekly Review', 'Trading, coding, fitness review', 5);
    events += createEvent(saturday, 21, 0, 21, 10, 'SCREEN CURFEW', 'Evening yoga', 5);
    events += createEvent(saturday, 21, 45, 21, 46, 'LIGHTS OUT', '9+ hours sleep', 5);

    // Sunday
    const sunday = new Date(nextMonday);
    sunday.setDate(nextMonday.getDate() + 6);
    events += createEvent(sunday, 6, 30, 6, 45, 'Wake Up', 'Early for church.', 0);
    events += createEvent(sunday, 6, 45, 7, 0, 'Prayer', '15 min. Reflect on the week.', 0);
    events += createEvent(sunday, 7, 5, 7, 20, 'Morning Yoga', '15-minute flow', 0);
    events += createEvent(sunday, 7, 20, 7, 50, 'Get Ready for Church', 'Shower, dress', 0);
    events += createEvent(sunday, 8, 0, 8, 30, 'Travel to Church', 'Leave for church', 10);
    events += createEvent(sunday, 8, 30, 9, 30, 'CHURCH', '', 0);
    events += createEvent(sunday, 9, 45, 10, 15, 'Brunch', 'Cook something you enjoy', 5);
    events += createEvent(sunday, 11, 30, 12, 15, 'Grocery Run', 'Get items for meal prep', 10);
    events += createEvent(sunday, 12, 30, 15, 0, 'MEAL PREP', 'Batch cook for the week', 10);
    events += createEvent(sunday, 15, 0, 15, 30, 'Light Walk', 'Active recovery. No phone.', 0);
    events += createEvent(sunday, 18, 35, 19, 20, 'Weekly Planning', 'Set Monday plan, coding goals', 5);
    events += createEvent(sunday, 21, 0, 21, 10, 'SCREEN CURFEW', 'Monday starts NOW.', 5);
    events += createEvent(sunday, 21, 45, 21, 46, 'LIGHTS OUT', '9+ hours to 7:00 AM', 5);

    return `BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Disciplined Trader Schedule//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Weekly Schedule
X-WR-TIMEZONE:America/New_York
${events}END:VCALENDAR`;
}

function downloadCalendar() {
    const icsContent = generateICSContent();
    const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'weekly_schedule.ics';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    alert('Calendar downloaded!\\n\\nOpen the .ics file on your iPhone to import into Apple Calendar.');
}

// Add buttons to page
document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('header');
    if (header) {
        const btnContainer = document.createElement('div');
        btnContainer.style.cssText = 'display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; margin-top: 20px;';

        const downloadBtn = document.createElement('button');
        downloadBtn.textContent = 'Download to Apple Calendar';
        downloadBtn.onclick = downloadCalendar;
        downloadBtn.style.cssText = `
            background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 30px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        `;

        const infoBtn = document.createElement('button');
        infoBtn.textContent = 'Setup Auto-Sync';
        infoBtn.onclick = () => alert('To auto-sync your calendar:\\n\\n1. Host this on GitHub Pages\\n2. Subscribe to the .ics URL in Apple Calendar\\n3. Changes refresh automatically\\n\\nSee iphone_integration.md for details!');
        infoBtn.style.cssText = `
            background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 30px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        `;

        btnContainer.appendChild(downloadBtn);
        btnContainer.appendChild(infoBtn);
        header.appendChild(btnContainer);
    }
});
