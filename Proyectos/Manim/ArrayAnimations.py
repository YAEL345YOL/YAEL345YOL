from manim import *

class Array:

    def __init__(self,elements_,scale_=1):
        self.elements = elements_
        self.name = "A"
        self.size = len(self.elements)
        self.scale = scale_
        self.max_element = max(self.elements)
        self.min_element = min(self.elements)
        self.table = Table([[str(number) for number in self.elements]],include_outer_lines=True).scale(scale_)

    def getUpPoints(self,delta=1.25):
        upPoints = []
        for column in self.table.get_columns():
            final_column = column.get_top();
            final_column[1]+=self.scale*delta
            upPoints.append(final_column)
        return upPoints

    def getDownPoints(self,delta=1.25):
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
        self.name = name
        text = Text(name+" =")
        text.next_to(self.table,LEFT).scale(self.scale)
        scene.play(Write(text),run_time=2)

    def linearSearch(self,scene,target,**kwargs):
        waitOnElement = kwargs.get("waitOnElement",1)
        code = kwargs.get("code")
        iterator = kwargs.get("iterator")
        points = self.getDownPoints(1.4)
        arrow = Arrow().scale(self.scale).rotate(PI/2).move_to(points[0])
        if iterator:
            iterator_copy = iterator.copy()
        if code:
            new_code = Code(code=f'''
            int linearSearch(int target,vector<int>{self.name}){{
                for(int i=0;i<{self.name}.size();i++){{
                    if({self.name}[i]==target){{
                        return target;
                    }}
                }}
                return -1;
            }}
            ''',).match_style(code).move_to(code)
            scene.play(Transform(code,new_code),run_time=1.5)
        scene.play(Write(arrow),run_time=1.5)
        for pos in range(0,len(points)):
            if iterator:
                new_text = Text(f"i = {pos}").move_to(iterator).match_style(iterator_copy)
                scene.play(arrow.animate.move_to(points[pos]), Transform(iterator, new_text),run_time=1.5)
            else:
                scene.play(arrow.animate.move_to(points[pos]),run_time=1.5)
            scene.wait(waitOnElement)
            if(self.elements[pos]==target):
                break
        scene.play(FadeOut(arrow),run_time=1.5)
    


class Introduction(Scene):
    def construct(self):

        # Code here

        # arreglo1 = Array([1,2,4,6,7,3,2,1],0.70)

        # self.play(Write(arreglo1.table))
        # self.play(arreglo1.table.animate.move_to([0,2,0]))
        # arreglo1.putIndex(self)
        # arreglo1.denoteArray(self,"B")
        # arreglo1.linearSearch(self,-1)

        self.wait(5)
