import cv2

FHD = (1920, 1080)

if __name__ == '__main__':
	video_path = "output.mp4"

	cap = cv2.VideoCapture(video_path)
	out = cv2.VideoWriter(f'temp_test_5.mp4', 0, 0, FHD)
	
	while (cap.isOpened):
		success, frame = cap.read()
		if not success:
			break

		cv2.putText(frame, "Text will show quanlity: 1231", org=(100, 500), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=3, color=(0,0,255), thickness=3)
		out.write(frame)

	# Destroy all the windows
	cap.release()
	out.release()
	cv2.destroyAllWindows()


# dsds A
#                                 1983148141	mp4
# >>> cv2.cv.FOURCC( *"XVID" )    1145656920	avi
# >>> cv2.cv.FOURCC( *"MJPG" )    1196444237	avi


# # Connect a GitHub connection into VSCode
# $ git config --list --show-origin
# $ git config --global user.name "Im-Watching-You"
# $ git config --global user.email "maksym.labs@gmail.com"
# $ git config --global core.editor "subl -n -w"

# $ git config --global init.defaultBranch main



# git init
# git add .
# git status
# git commit -m "First commit"
# 	git reset HEAD~1
# git remote add origin git@github.com/Im-Watching-You/GitHub-test.git
# git remote -v
# git push -u origin master
# git diff
# git checkout .

# git clone git@github.com/Im-Watching-You/GitHub.git
# git add .
# git status
# git commit -m "First commit"
# git push

# git pull