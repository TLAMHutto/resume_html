# import os
# import sys
# import time

# def watch_files(file_paths):
#     last_modified_times = {file_path: os.path.getmtime(file_path) for file_path in file_paths}
#     print("Watching files:", file_paths)  # Debugging line
#     while True:
#         time.sleep(1)
#         for file_path in file_paths:
#             current_modified = os.path.getmtime(file_path)
#             if current_modified != last_modified_times[file_path]:
#                 print(f"Change detected in {file_path}. Restarting...")  # Debugging line
#                 last_modified_times[file_path] = current_modified
#                 os.execv(sys.executable, ['python'] + sys.argv)  # Ensure this is correct
def watch_files(file_patha):
    print('Reload inst enabled')