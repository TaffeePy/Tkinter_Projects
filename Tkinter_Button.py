from tkinter import Tk,     Frame,Label,Button,     TOP,LEFT,RIGHT,BOTTOM,      GROOVE
window= Tk()
window.geometry('450x600')
#Title
window.title('Note Pad')

#Frame 1 && Button 1 to 7 
frame_top=Frame(window, bg="deep sky blue", borderwidth=3,relief=GROOVE).pack(side=LEFT,anchor='n')
b1_file=Button(frame_top,text='File',fg='black',bg='deep sky blue').pack(side=LEFT, anchor='n')
b2_edit_=Button(frame_top,text='Edit',fg='black',bg='deep sky blue').pack(side=LEFT,anchor='n')
b3_document_=Button(frame_top,text='Document',fg='black',bg='deep sky blue').pack(side=LEFT,anchor='n')
b4_view_=Button(frame_top,text='View',fg='black',bg='deep sky blue').pack(side=LEFT,anchor='n')
b5_search_=Button(frame_top,text='Search',fg='black',bg='deep sky blue').pack(side=LEFT,anchor='n')
b6_tool_=Button(frame_top,text='Tool',fg='black',bg='deep sky blue').pack(side=LEFT,anchor='n')
b7_help_=Button(frame_top,text='Help',fg='black',bg='deep sky blue').pack(side=LEFT,anchor='n')


frame_2_top=Frame(window, bg="deep sky blue", borderwidth=3,relief=GROOVE).pack(side=LEFT,anchor='w')
b8_open=Button(frame_2_top,text='Open',fg='black',bg='sky blue').pack(side=LEFT, anchor='w')








window.mainloop()