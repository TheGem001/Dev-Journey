#!/data/data/com.termux/files/usr/bin/python
import yt_dlp
import os
import subprocess
import threading
import time

# --- CONFIGURATION ---
SAVE_FOLDER = '/sdcard/downloaded'

def scan_file(path):
    """Refreshes Gallery so video appears immediately"""
    try:
        subprocess.run(['termux-media-scan', path], check=False)
    except:
        pass

def download_task(url):
    """This runs in the background for each video"""
    
    # 1. Create folder if needed
    if not os.path.exists(SAVE_FOLDER):
        try:
            os.makedirs(SAVE_FOLDER)
        except:
            print(f"\n[ERROR] Permission Denied. Run 'termux-setup-storage'")
            return

    print(f"\n[>>>] Started downloading: {url[:30]}...")

    # 2. Configure - QUIET MODE IS ESSENTIAL HERE
    # We must hide the progress bar so you can type the next link!
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{SAVE_FOLDER}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'quiet': True,        # Hides the scrolling text
        'no_warnings': True,
        'ignoreerrors': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            
            # Find filename
            if 'requested_downloads' in info:
                final_file = info['requested_downloads'][0]['filepath']
            else:
                final_file = ydl.prepare_filename(info)
                base, _ = os.path.splitext(final_file)
                final_file = base + ".mp4"

            # Get title for the success message
            title = info.get('title', 'Video')
            
            # Fix Gallery
            scan_file(final_file)
            
            print(f"\n\n[DONE] Finished: {title}\n(Enter next link below)")
            
    except Exception as e:
        print(f"\n[FAIL] Error downloading {url}: {e}")

if __name__ == "__main__":
    print("\n" + "="*35)
    print("   MULTI-DOWNLOADER (Background)")
    print("="*35)
    print("Paste links one by one.")
    print("Downloads happen silently in background.")
    print("Type 'q' to quit.")
    print("-" * 35)
    
    while True:
        # This input stays active even while others download!
        url = input("\nPaste Link: ").strip()
        
        if url.lower() == 'q':
            print("Exiting (Active downloads will finish)...")
            break
            
        if url:
            # Create a new "worker" thread for this download
            # This allows the code to loop back immediately
            t = threading.Thread(target=download_task, args=(url,))
            t.start()
