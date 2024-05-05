from manim import *

def putIndex(self,table,index=[],table_scale=1):
    columns = table.get_columns()
    for i in range(0,len(columns)):
        pos = columns[i].get_top()
        pos[1]+=table_scale*0.9
        act = Text(f'{i} ').move_to(pos).scale(table_scale*0.80);
        index.append(act);
        self.play(Write(index[i]),run_time=0.25)

def iterateArrayAnimation(self,table,start,end,ite,table_scale=1,waitOnElement=1.5):
    ite_copy = ite.copy()
    positions = []
    for element in table.get_columns():
        pos = element.get_bottom()
        pos[1]-=table_scale*1.15
        positions.append(pos)
    arrow = Arrow().scale(table_scale*0.75).rotate(PI/2).move_to(positions[start])
    self.play(Write(arrow),Write(ite),run_time=1.5)
    self.play(Transform(ite,Text(f"i = {start}").match_style(ite_copy).move_to(ite.get_center())),run_time=1.5)
    self.wait(waitOnElement)
    for i in range(start+1,min(len(positions),end+1)):
        self.play(arrow.animate.move_to(positions[i]),Transform(ite,Text(f"i = {i}").match_style(ite_copy).move_to(ite.get_center())),run_time=1.5)
        self.wait(waitOnElement)
    self.play(FadeOut(arrow),run_time=1.5)
    
