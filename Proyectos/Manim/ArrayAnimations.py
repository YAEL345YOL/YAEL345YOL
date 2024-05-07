from manim import *

class Array:

    def __init__(self,elements_,scale_=1):
        self.elements = elements_
        self.size = len(self.elements)
        self.scale = scale_
        self.max_element = max(self.elements)
        self.min_element = min(self.elements)
        self.table = Table([[str(number) for number in self.elements]],include_outer_lines=True).scale(scale_)
        self.downPoints = []
        self.upPoints = []

    def getUpPoints(self,delta):
        upPoints = []
        for column in self.table.get_columns():
            final_column = column.get_top();
            final_column[1]+=self.scale*delta
            upPoints.append(final_column)
        return upPoints

    def getDownPoints(self,delta):
        downPoints = []
        for column in self.table.get_columns():
            final_column = column.get_bottom();
            final_column[1]-=self.scale*delta
            downPoints.append(final_column)
        return downPoints

    def putIndex(self,scene,index=[]):
        points = self.getUpPoints(1)
        for pos in range(0,self.size):
            text = Text(f"{pos} ").scale(self.scale).move_to(points[pos])
            index.append(text)
            scene.play(Write(index[pos]),run_time=0.2)
    
    def denoteArray(self,scene,name):
        name.next_to(self.table,LEFT).scale(self.scale)
        scene.play(Write(name),run_time=2)

    def linearSearch(self,scene,target,waitOnElement=2):
        points = self.getDownPoints(1.4)
        arrow = Arrow().scale(self.scale).rotate(PI/2).move_to(points[0])
        scene.play(Write(arrow),run_time=1.5)
        for pos in range(0,len(points)):
            scene.play(arrow.animate.move_to(points[pos]),runt_time=1.5)
            scene.wait(waitOnElement)
            if(self.elements[pos]==target):
                break
        scene.play(FadeOut(arrow),run_time=1.5)
    


class Introduction(Scene):
    def construct(self):
        # Code here
        self.wait(5)
