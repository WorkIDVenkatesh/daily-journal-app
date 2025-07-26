import datetime as dt


entries = input("What Did you done today ? ").strip()
rating = input("⭐ Rate your productivity today (1-5, optional)").strip()

now = dt.datetime.now()

date_str = now.strftime("%Y-%M-%D - %I:%M %p")

journal_entry = f"\n📅 {date_str}\n{entries}"
if rating:
    journal_entry += f"\n Productivity Rating: {rating}\n"
    # journal_entry += f"\n⭐ {rating}/5"   
journal_entry += "\n" + "-" * 50


with open("learning_journal.txt","a", encoding="utf-8") as f:
    f.write(journal_entry)


print(f"\n your journal entry has been stored  to 'learning_journal.txt'file.")