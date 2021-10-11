I ran out of time, so I did not have time to finish the entire assignment and make things run the way they are supposed to before the deadline.
I have not implemented the tests from 4.3 or 4.5. I did however implement 4.6 for the bonus points.
Also, I have not created an environment and it is not possible to run the instapy-file from anywhere (or from the bin folder for that matter).
I will instead explain what has to be done to run the program.

- The user first has to make sure that opencv is installed.
  If it is not it can be installed by typing 'pip install opencv-python' in the terminal.
- The user might have to install numba by typing 'pip install numba' in the terminal.
- Then the user has to be inside the assignment4 folder and install the package by typing 'pip install . --user' in the terminal.
- The program can then be run from the same folder by typing 'python instapy.py [FLAGS]' in the terminal.
  Type 'python instapy.py -h' or 'python instapy.py --help' in the terminal to get a view of all possible flags.

  The reason why the user has to do it this way is because I didn't get the PATH to work and also for some reason the script can't be run from
  the bin folder. So I had to make a copy and place that copy inside the instapy folder. I know it's not supposed to be like that, and that this
  kind of ruins the whole points of using packages with a setup-file with a script inside. But I didn't get it to work by the deadline and I
  figured it would be better to actually deliver something that is able to run, even though it doesn't run the in the way it is supposed to.


The image that is to be converted has to be inside the folder named originals (instapy/photos/originals). The converted photos will be saved inside the folder named grayscale or sepia, depending on which filter was used. If the user scales down the original photo the scaled down photo will be saved in the scaled folder and then be used to convert the colors. The photo 'rain.jpg' is already inside the originals folder and the user can use that
filename to run the program. If the user wants to try another photo, the user has to add it to the originals folder themselves first.

The reports are found inside the filters folder.
