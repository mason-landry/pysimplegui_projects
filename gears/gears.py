import PySimpleGUI as sg
import matplotlib.pyplot as plt

class Setup:
    def __init__(self,fronts,rears,name):
        self.fronts = fronts
        self.rears = rears
        self.name = name
        self.GRs = []
        for f in fronts:
            self.GRs.append([f/r for r in rears])


def draw_plot(setups, name):
    plt.figure(figsize=(6,6))
    for s in setups:
        
        for i,g in enumerate(s.GRs):
            plt.scatter(s.rears,g,marker='*')
            for a,b in enumerate(s.rears):
                xy=(b,g[a])
                plt.annotate('GR: %.2f' % xy[1], xy=xy, xytext=(xy[0]+0.5, xy[1]) )
            plt.plot(s.rears,g, label=s.name + ' Front Gear: ' + str(s.fronts[i]))
    plt.xlabel('Num Teeth per Rear gear')
    plt.ylabel('Gear Ratio')
    plt.grid()
    plt.legend()
    plt.show(block=False)

def draw_plot_ordered(setups, name):
    for s in setups:
        GRs_sorted = [gr for gs in s.GRs for gr in gs]
        num_gears = len(s.fronts)*len(s.rears)
        Gs = range(num_gears+1,1,-1)
        GRs_sorted.sort()
        print(GRs_sorted)
        plt.scatter(Gs,GRs_sorted,marker='*')
        plt.plot(Gs,GRs_sorted, label=s.name + ' Front Gear(s): ' + str(s.fronts))
    plt.xlabel('Gear (largest to smallest)')   
    plt.ylabel('Gear Ratio')
    plt.grid()
    plt.legend()
    plt.show(block=False)

sg.theme("SystemDefault")
# Pre-defined gear setups:
SramEagle = [[32],[10,12,14,16,18,21,24,28,32,36,42,50]]
Sram111 = [[32],[10,12,14,16,18,21,24,28,32,36,42]]
Shimano111 = [[32],[11,13,15,17,19,21,24,28,32,37,46]]
Shimano210 = [[22,36],[11,13,15,17,19,21,24,28,32,36]]
Option2 = [[32], [11,13,15,18,21,24,28,32,37,42]]
Option3 = [[32], [11,13,15,19,21,24,28,32,36,42]]

front_labels = ['-F1-','-F2-','-F3-']
rear_labels = ['-R1-','-R2-','-R3-','-R4-','-R5-','-R6-','-R7-','-R8-','-R9-','-R10-','-R11-','-R12-']
predefined = ['Custom','Sram Eagle', 'Sram 1x11', 'Option 1: New 11-46 Groupset', 'Current Setup 11-36','Option 2: New 11-42 Cassette', 'Option 3: Add 42T Cog']
predefinedGears = [[],SramEagle, Sram111, Shimano111, Shimano210, Option2, Option3]

layout = [[sg.Text('Choose pre-defined setup:'), sg.Combo(predefined, default_value=predefined[1]), sg.Button('Update')],
          [sg.Text('Setup Name:'), sg.Input(key='-Name-')],
          [sg.Text('Front Gear Options:'),
           sg.Input(size=(5,1), key='-F1-'),
           sg.Input(do_not_clear=False, size=(5,1),key='-F2-'),
           sg.Input(do_not_clear=False, size=(5,1),key='-F3-'),
           sg.Text('Teeth')],
          [sg.Text('Rear Gear Options: '),
           sg.Input(size=(5,1),key='-R1-'),
           sg.Input(size=(5,1),key='-R2-'),
           sg.Input(size=(5,1),key='-R3-'),
           sg.Input(size=(5,1),key='-R4-'),
           sg.Input(size=(5,1),key='-R5-'),
           sg.Input(size=(5,1),key='-R6-'),
           sg.Input(size=(5,1),key='-R7-'),
           sg.Input(size=(5,1),key='-R8-'),
           sg.Input(size=(5,1),key='-R9-'),
           sg.Input(size=(5,1),key='-R10-'),
           sg.Input(do_not_clear=False, size=(5,1),key='-R11-'),
           sg.Input(do_not_clear=False, size=(5,1),key='-R12-'),
           sg.Text('Teeth')],
          [sg.Button('Plot'), sg.Cancel()]]

window = sg.Window('Mountainbike', layout)
setups = []
while True:
    event, values = window.read()
    print(values)
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'Update':
        idx = predefined.index(values[0])
        window['-Name-'].update(values[0])
        if predefinedGears[idx] == []:
            pass
        else:
            fr = predefinedGears[idx][0]    # Front gears
            r = predefinedGears[idx][1]    # Rear gears
            for c, val in enumerate(fr):
                window[front_labels[c]].update(val)
            for c, val in enumerate(r):
                window[rear_labels[c]].update(val)
        
    elif event == 'Plot':
        plt.close()
        fronts = []
        rears = []
        name = values['-Name-']
        print(name)
        for f in front_labels:
            if values[f] != '':
                fronts.append(int(values[f]))
        for r in rear_labels:
            if values[r] != '':
                rears.append(int(values[r]))
        # for c,val in enumerate(values):
        setups.append(Setup(fronts,rears, name))
        # draw_plot(setups, name)
        draw_plot(setups, name)

        
window.close()
plt.close()
