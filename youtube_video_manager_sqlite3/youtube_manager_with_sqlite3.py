import sqlite3

DB_NAME = 'youtube_videos.db'

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                time TEXT NOT NULL
            )
        ''')

def list_videos():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT * FROM videos")
        videos = cursor.fetchall()
        if videos:
            for video in videos:
                print(f"ID: {video[0]} | Name: {video[1]} | Time: {video[2]}")
        else:
            print("No videos found.")

def add_video(name, time):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
        print("Video added successfully.")

def update_video(video_id, new_name, new_time):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
        if cursor.rowcount:
            print("Video updated successfully.")
        else:
            print("No video found with that ID.")

def delete_video(video_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        if cursor.rowcount:
            print("Video deleted successfully.")
        else:
            print("No video found with that ID.")

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    create_table()

    while True:
        print("\nYouTube Video Manager")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ").strip()
            time = input("Enter the video time (e.g., 10:05): ").strip()
            add_video(name, time)
        elif choice == '3':
            video_id = get_valid_integer("Enter video ID to update: ")
            new_name = input("Enter the new video name: ").strip()
            new_time = input("Enter the new video time: ").strip()
            update_video(video_id, new_name, new_time)
        elif choice == '4':
            video_id = get_valid_integer("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
