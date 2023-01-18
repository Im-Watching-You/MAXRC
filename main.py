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


# >>> cv2.cv.FOURCC( *"XVID" )    1145656920	avi
# >>> cv2.cv.FOURCC( *"MJPG" )    1196444237	avi


# Connect a GitHub connection into VSCode
	# $ git config --list --show-origin
	# $ git config --global user.name "Im-Watching-You"
	# $ git config --global user.email "maksym.labs@gmail.com"
	# $ git config --global core.editor "subl -n -w"

	# $ git config --global init.defaultBranch main


# MAIN push code:
	# git clone git@github.com/Im-Watching-You/GitHub.git
	# git add .
	# git status
	# git commit -m "First commit"
	# git push

# MAIN pull code:
	# git pull

# MAIN create branch code:
	# git checkout -b feature_A
	# max-height-integration

# git branch -d <local-branch>
# git push origin --delete <remote-branch-name>

# $ git branch <branch_name>   # create
# $ git checkout <branch_name> # switch to <branch_name>
# $ git branch -a # show all



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


# github@branch/c/remote/push  (new-branch)
# git clone https://github.com/learn-git-fast/git-branch-examples.git
# cd git*
# git checkout -b new-branch

# github@branch/c/remote/push (new-branch)
# git branch -a
# touch devolution.jpg
# git add .
# git commit -m "Are we not gender neutral people? We are Devo?"
# git push --set-upstream origin feature_A

# github@branch/c/remote/push (new-branch)
# touch eden.html
# git add .
# git commit -m "Eden added"
# git push origin