# Weekly Schedule — Disciplined Trader's Life

A comprehensive weekly lifestyle schedule for a disciplined options trader.
Covers Monday-Sunday in 5-15 minute blocks with trading, coding, workouts,
meal plans, and routines.

## Live Schedule

- **HTML:** https://worth78.github.io/weekly-schedule/weekly_schedule.html
- **ICS:** https://worth78.github.io/weekly-schedule/weekly_schedule.ics

## iPhone Setup

1. Open the **Calendar** app
2. Tap **Calendars** > **Add Calendar** > **Add Subscription Calendar**
3. Paste: `https://worth78.github.io/weekly-schedule/weekly_schedule.ics`
4. Tap **Find** > **Done**

Calendar auto-refreshes when the schedule is updated and pushed.

## Files

| File | Description |
|------|-------------|
| `weekly_schedule.md` | Master schedule (source of truth) |
| `weekly_schedule.html` | Styled HTML view |
| `weekly_schedule.ics` | iCalendar file for Apple Calendar |
| `generate_ics.py` | Regenerates .ics from code |
| `calendar_export.js` | In-browser .ics download |
| `sync_schedule.py` | File watcher: MD changes auto-update HTML |
| `start_sync.bat` | One-click launcher for sync watcher |
| `iphone_integration.md` | Full iPhone integration guide |
| `prompt.md` | Schedule context and preferences |

## Update Workflow

1. Edit `weekly_schedule.md`
2. Run: `python sync_schedule.py --once` (regenerates HTML)
3. Run: `python generate_ics.py` (regenerates ICS)
4. `git add . && git commit -m "Update schedule" && git push`
5. iPhone picks up changes within 24 hours
