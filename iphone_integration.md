# iPhone Integration Guide

This guide covers all the ways to integrate your Weekly Schedule with your iPhone.

---

## Quick Answer to Your Update Question:

For auto-updating when you change the schedule:
1. Host the .ics file on GitHub Pages (free)
2. Subscribe to that URL in Apple Calendar
3. When you change the schedule, re-export and upload the new .ics
4. iPhone auto-refreshes within 24 hours

## The Integration Guide Covers:

```
┌───────────────────────┬──────────────────────────────────────────┐
│        Option         │                 Best For                 │
├───────────────────────┼──────────────────────────────────────────┤
│ Calendar Import       │ Quick one-time setup                     │
├───────────────────────┼──────────────────────────────────────────┤
│ Calendar Subscription │ Auto-updates when schedule changes       │
├───────────────────────┼──────────────────────────────────────────┤
│ Home Screen PWA       │ App-like access to full schedule         │
├───────────────────────┼──────────────────────────────────────────┤
│ Shortcuts App         │ Custom automations & notifications       │
├───────────────────────┼──────────────────────────────────────────┤
│ Reminders App         │ Simple recurring reminders               │
├───────────────────────┼──────────────────────────────────────────┤
│ Focus Modes           │ Block distractions during trading/coding │
├───────────────────────┼──────────────────────────────────────────┤
│ Widgets               │ See schedule on home screen              │
├───────────────────────┼──────────────────────────────────────────┤
│ Apple Watch           │ Wrist notifications                      │
└───────────────────────┴──────────────────────────────────────────┘
```

## My Recommendation:
- Calendar Subscription (for events + auto-updates)
- Home Screen PWA (quick access)
- Focus Modes (distraction blocking)

---

## Option 1: Apple Calendar (Recommended)

### One-Time Import
1. Open `weekly_schedule.html` on your computer
2. Click **"Download to Apple Calendar"**
3. Transfer `weekly_schedule.ics` to your iPhone:
   - **AirDrop** (easiest)
   - **iCloud Drive** - save to Files, open on iPhone
   - **Email** - send to yourself, open attachment
4. Tap the file → **Add All Events**
5. Events appear in Apple Calendar with reminders

**Pros:** Simple, works offline, native reminders
**Cons:** Must re-import when schedule changes (creates duplicates)

---

### Auto-Sync via Calendar Subscription (Best for Updates)

This method auto-refreshes your calendar when you update the schedule.

#### Step 1: Host Your Schedule Online

**Option A: GitHub Pages (Free)**
1. Create a GitHub repository
2. Add these files:
   - `weekly_schedule.ics` (download from the HTML page)
   - `index.html` (optional - your schedule page)
3. Go to Settings → Pages → Enable GitHub Pages
4. Your .ics file will be at: `https://yourusername.github.io/repo-name/weekly_schedule.ics`

**Option B: iCloud Drive**
1. Save `weekly_schedule.ics` to iCloud Drive
2. Right-click → Share → Copy Link
3. Use this link for subscription

**Option C: Dropbox**
1. Upload `weekly_schedule.ics` to Dropbox
2. Get shareable link
3. Change `?dl=0` to `?dl=1` at end of URL

#### Step 2: Subscribe on iPhone
1. Open **Settings** → **Calendar** → **Accounts**
2. Tap **Add Account** → **Other**
3. Tap **Add Subscribed Calendar**
4. Enter your .ics URL
5. Tap **Next** → **Save**

#### Step 3: Update Your Calendar
When you change your schedule:
1. Re-download the .ics file from the HTML page
2. Replace the hosted file (GitHub/iCloud/Dropbox)
3. iPhone refreshes automatically (usually within 24 hours)
4. Force refresh: Settings → Calendar → Accounts → [Your subscription] → pull down to refresh

---

## Option 2: Add to Home Screen (PWA)

Make the schedule page work like an app on your iPhone.

### Setup
1. Host `weekly_schedule.html` online (GitHub Pages, etc.)
2. Open the URL in Safari on iPhone
3. Tap the **Share** button (square with arrow)
4. Tap **Add to Home Screen**
5. Name it "Schedule" → **Add**

### What You Get
- App icon on home screen
- Opens in full-screen (no browser UI)
- Works offline (with service worker - see advanced setup)
- Quick access to your schedule

### Add Offline Support (Advanced)
Add this service worker for offline access:

Create `sw.js`:
```javascript
const CACHE_NAME = 'schedule-v1';
const urlsToCache = [
  '/',
  '/weekly_schedule.html',
  '/calendar_export.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
```

Add to your HTML `<head>`:
```html
<link rel="manifest" href="manifest.json">
<meta name="apple-mobile-web-app-capable" content="yes">
<script>
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js');
  }
</script>
```

Create `manifest.json`:
```json
{
  "name": "Weekly Schedule",
  "short_name": "Schedule",
  "start_url": "/weekly_schedule.html",
  "display": "standalone",
  "background_color": "#667eea",
  "theme_color": "#667eea",
  "icons": [
    {
      "src": "icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    }
  ]
}
```

---

## Option 3: Shortcuts App (Automation)

Use Apple Shortcuts for custom reminders and automation.

### Morning Routine Shortcut
1. Open **Shortcuts** app
2. Tap **+** → **Add Action**
3. Build a sequence:
   - Show notification: "Time for prayer"
   - Wait 10 minutes
   - Show notification: "Morning yoga"
   - Wait 15 minutes
   - Show notification: "Breakfast time"
4. Set automation: Run at 7:00 AM on weekdays

### Trading Session Reminder
1. Create shortcut with actions:
   - Show notification: "Pre-market prep in 15 min"
   - Set Focus mode to "Trading" (optional)
2. Automate to run at 8:00 AM weekdays

### Bedtime Reminder
1. Create shortcut:
   - Show notification: "Screen curfew! Put away devices."
   - Set Focus mode to "Sleep"
   - Lower screen brightness
2. Automate to run at 9:00 PM daily

---

## Option 4: Reminders App

Create recurring reminders manually.

### Quick Setup
1. Open **Reminders** app
2. Create a list called "Daily Schedule"
3. Add reminders with times:
   - 7:00 AM - Wake up (repeat: weekdays)
   - 8:15 AM - Pre-market prep (repeat: weekdays)
   - 8:30 AM - Trading session (repeat: weekdays)
   - 12:00 PM - Lunch (repeat: weekdays)
   - 4:15 PM - Pre-workout (repeat: weekdays)
   - 9:00 PM - Screen curfew (repeat: daily)
   - 9:45 PM - Lights out (repeat: daily)

### Sunday-Specific
- 6:30 AM - Wake up for church (repeat: Sundays)
- 8:00 AM - Leave for church (repeat: Sundays)
- 12:30 PM - Start meal prep (repeat: Sundays)

---

## Option 5: Focus Modes

Use Focus modes to minimize distractions during key blocks.

### Trading Focus
1. Settings → Focus → **+** (add new)
2. Name: "Trading"
3. Allowed notifications: Only critical apps
4. Schedule: 8:30 AM - 12:00 PM weekdays
5. Lock Screen: Show only trading-related widgets

### Coding Focus
1. Create "Coding" focus
2. Block social media notifications
3. Schedule: 12:45 PM - 4:15 PM weekdays

### Sleep Focus
1. Use built-in Sleep focus
2. Schedule: 9:45 PM - 7:00 AM
3. Dim lock screen, silence calls

---

## Option 6: Widgets

Add schedule info to your Home Screen.

### Calendar Widget
1. Long press Home Screen → **+**
2. Search "Calendar"
3. Add "Up Next" widget (shows upcoming events)
4. Place at top of Home Screen

### Reminders Widget
1. Add Reminders widget
2. Select your "Daily Schedule" list
3. See today's tasks at a glance

---

## Option 7: Apple Watch

If you have an Apple Watch:

### Calendar Complications
- Add Calendar complication to watch face
- See next event at a glance
- Get haptic reminders

### Reminders on Watch
- Reminders sync automatically
- Check off tasks from wrist

### Focus Mode Sync
- Focus modes sync between iPhone and Watch
- Watch taps you for reminders during focus

---

## Comparison Table

| Method | Auto-Update | Offline | Reminders | Setup Time |
|--------|-------------|---------|-----------|------------|
| Calendar Import | No | Yes | Yes | 5 min |
| Calendar Subscription | Yes | Yes | Yes | 15 min |
| Home Screen PWA | Manual | With SW | In-app | 10 min |
| Shortcuts | N/A | Yes | Custom | 30 min |
| Reminders App | N/A | Yes | Yes | 20 min |
| Focus Modes | N/A | N/A | Indirect | 15 min |

---

## Recommended Setup

For the best experience, combine these:

1. **Calendar Subscription** - Core schedule with auto-updates
2. **Home Screen PWA** - Quick access to full schedule
3. **Focus Modes** - Minimize distractions during trading/coding
4. **Shortcuts** - Custom automations (optional power-user feature)

---

## Troubleshooting

### Calendar not updating?
- Check subscription URL is correct
- Force refresh: Settings → Calendar → Accounts → your subscription
- Subscriptions refresh every 1-24 hours

### Reminders not firing?
- Check notification settings for Calendar/Reminders
- Ensure Do Not Disturb / Focus isn't blocking
- Check alert settings on individual events

### PWA not working offline?
- Service worker must be registered
- Visit the page while online first
- Check browser console for errors

---

## Quick Start Checklist

- [ ] Download .ics from schedule page
- [ ] Import to Apple Calendar (or set up subscription)
- [ ] Add schedule page to Home Screen
- [ ] Set up Trading and Coding Focus modes
- [ ] Configure Sleep Focus for 9:45 PM
- [ ] Add Calendar widget to Home Screen
