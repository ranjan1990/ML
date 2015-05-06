# Select the training set for the satellite image
# This will generate input file for the estimated case of the program

import sys
import Tkinter, tkMessageBox
import Image		#,ImageTk
from PIL import ImageTk


class window:
    def __init__(self, parent, filename, outfile, numsamples, priorProbability):
        self.Points = []
        self.ptsInClass = []
        self.numClick = 0
        self.currentClass = -1

        self.parent = parent
        self.inImage = filename
        self.numSamples = numsamples
        self.numClass = len(numsamples)
        self.outfile = open(outfile, 'w')
        self.image = Image.open(self.inImage)
        self.priorProbability = priorProbability

        self.parent.bind("<Button-1>", self.clicked_pos)
        self.parent.bind("<Key>", button_click_exit_main_loop)


    def do(self):
        self.parent.title("Satellite Image")

        tkpi = ImageTk.PhotoImage(self.image)
        self.canvas = Tkinter.Canvas(self.parent, width= self.image.size[0], height= self.image.size[1])
        self.canvas.create_image(0, 0, anchor=Tkinter.NW, image= tkpi)
        #canvas.pack(fill=Tkinter.BOTH, expand=1)
        self.canvas.pack()
        self.canvas.mainloop()

        #label_image = Tkinter.Label(self.parent, image = tkpi)
        #label_image.pack()
        #label_image.mainloop()


    def clicked_pos(self, event):
        if self.currentClass == -1 or self.numClick == self.numSamples[self.currentClass]:
            if self.currentClass == self.numClass-1:
                # The last added points are not added
                self.Points.append(self.ptsInClass)
                #we are done
                self.write_remaining()
                tkMessageBox.showinfo("Exit", "Got all the points exiting")
                button_click_exit_main_loop(event)
                return

            self.currentClass = self.currentClass + 1
            txt = "For Class "+str(self.currentClass+1)+" select "+str(self.numSamples[self.currentClass])+" points"

            self.numClick = 0
            #if currentClass is 0 and control reaches here, then it must be the first time
            #so self.ptsInClass must be empty
            if self.currentClass != 0:
                self.Points.append(self.ptsInClass) #do if not empty
            self.ptsInClass = []

            tkMessageBox.showinfo("Input details", txt)
            return

        print "Click pos:", event.x, event.y
        self.ptsInClass.append( (event.x,event.y) )
        self.canvas.create_rectangle(event.x, event.y, event.x, event.y, outline="red")
        self.numClick = self.numClick + 1

    def write_remaining(self):
        '''write things to self.outfile
        format
        numclass
        for each class
         prior probability
         number of samples
         point1x
		 point1y
         point2x
		 point2y
         ...
        '''
        self.outfile.write(str(self.numClass)+"\n")
        for i in range(self.numClass):
            #self.outfile.write(str(self.priorProbability[i])+"\n")
            self.outfile.write(str(self.numSamples[i])+"\n")
            for j in range(len(self.Points[i])):
                (x, y) = self.Points[i][j]
                self.outfile.write(str(x)+","+str(y)+","+str(i)+"\n")
        

    def __del__(self):
        self.Image.close()
        self.outfile.close()


def button_click_exit_main_loop(event):
    event.widget.quit()



in_img_id = 1
out_file_id = 2

def print_usage():
    print "Usage: python get_points.py <input_image> <output_file>"

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)



    #Input
    numclass = int(raw_input("Number of classes:"))
    numSamples = []
    P = []

    for i in range(numclass):
        print "For Class",i+1

        #p = float(raw_input("Prior Probability:"))
        #P.append(p)

        numpt = int(raw_input("Number of samples:"))
        numSamples.append(numpt)

        #Write this info to output_file
        #numpt \n pts...\n p


    root = Tkinter.Tk()

    f = sys.argv[in_img_id]
    outfile = sys.argv[out_file_id]

    win = window(root, f, outfile, numSamples, P)
    win.do()
