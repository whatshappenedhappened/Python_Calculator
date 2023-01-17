import tkinter

screen = tkinter.Tk()
screen.title('CALCULATOR')
screen.geometry('297x342')
screen.resizable(False, False)


#####           function part             #####
def input(val):
    global optFin
    calindex = 0
    if calcValue[1] : calindex = 2

    if type(val) == str:                            ##### operator part
        if not calcValue[0] : calcValue[0] = '0'
        if val == '.':                              ### decimal point part
            if optFin == 1:
                calcValue[0] = '0'
                calcValue[1] = ''
                calcValue[2] = ''
                calindex = 0
                optFin = 0
                output_history.config(text='')
            else :
                for check in calcValue[calindex]:          # when user input '.', check if there's already a decimal point
                    if check == '.':
                        val = ''
            calcValue[calindex] += val
            val = ''

        if val == '+' or val == '-' or val == '*' or val == '/' or val == '%':             ################################## 오퍼레이터가 없으면 추가하고, 있으면 다음 인덱스의 값의 여부를 조회하여 있으면 합산값을 인덱스1에 저장후 오퍼레이터 오버라이딩
            if not calcValue[1] or calcValue[1] == '=':
                calcValue[1] = val
            elif calcValue[1] and optFin == 1:
                calcValue[1] = val
                calcValue[calindex] = ''
                optFin = 0
            elif not calcValue[2]:
                calcValue[1] = val
            elif calcValue[2]:
                total = ''
                for value in calcValue:
                    total += str(value)
                calcValue[0] = eval(total)
                calcValue[1] = val
                calcValue[2] = ''
            output_history.config(text=calcValue[:2])
            val = ''

        elif val == '=':
            total = ''
            if not calcValue[1]:
                calcValue[1] = val
                output_history.config(text=calcValue[:2])
                if calcValue[0] == '0': calindex = 0
            elif calcValue[1] == '=':
                val = ''
            elif not calcValue[2]:
                calcValue[calindex] = calcValue[0]
                calindex = 0
                calcValue.append(val)
                output_history.config(text=calcValue)
                del calcValue[len(calcValue) - 1]
                for value in calcValue:
                    total += str(value)
                calcValue[calindex] = str(eval(total))
                if len(calcValue[0]) > 15 or len(calcValue[2]) > 15:
                    output_history.config(height=1, font=('D2Coding', 8))
                output_current.config(text=calcValue[calindex])
                optFin = 1
            else :
                if calcValue[1] == '/' and calcValue[2] == '0':
                    calcValue[0] = '0'
                    calcValue[1] = ''
                    calcValue[2] = ''
                    val = ''
                    optFin = 1
                    output_current.config(height=2, font=('D2Coding', 15))
                    output_history.config(height=1, font=('D2Coding', 15), text='')
                    calcValue[0] = 'Cannot divide by 0'
                else:
                    calcValue.append(val)
                    output_history.config(text=(calcValue))
                    del calcValue[len(calcValue) - 1]
                    for value in calcValue:
                        total += str(value)
                    calcValue[0] = str(eval(total))
                    calindex = 0
                    if len(calcValue[0]) > 15 or len(calcValue[2]) > 15:
                        output_history.config(height=1, font=('D2Coding', 8))
                    output_current.config(text=calcValue[calindex])
                    optFin = 1
            val = ''

        elif val == 'Back':
            if optFin == 1:
                for i in range(len(calcValue)):
                    calcValue[i] = ''
                output_history.config(text='')
                calcValue[0] = '0'
                optFin = 0
                output_history.config(height=1, font=('D2Coding', 15))
                output_current.config(height=1, font=('D2Coding', 30))
            valSize = len(calcValue[calindex]) - 1
            calcValue[calindex] = calcValue[calindex][:valSize]

            if calcValue[calindex] == '': calcValue[calindex] = '0'
            val = ''

        elif val == 'C':
            calcValue[0] = '0'
            calcValue[1] = ''
            calcValue[2] = ''
            val = ''
            optFin = 0
            output_current.config(height=1, font = ('D2Coding', 30))
            output_history.config(height=1, font=('D2Coding', 15), text='')

        elif val == 'CE':
            if optFin == 1:
                for i in range(len(calcValue)):
                    calcValue[i] = ''
                output_history.config(text='')
                calcValue[0] = '0'
                optFin = 0
                output_current.config(height=1, font=('D2Coding', 30))
                output_history.config(height=1, font=('D2Coding', 15))
            calcValue[calindex] = '0'
            val = ''

    else:                                               ##### integer part
        if len(calcValue[calindex]) > 13:  # automatically changes the font size
            output_current.config(height=2, font=('D2Coding', 17))
            if len(calcValue[calindex]) > 20:
                val = ''
        else : output_current.config(height=1, font=('D2Coding', 30))

        if optFin == 1:
            calcValue[0] = '0'
            calcValue[1] = ''
            calcValue[2] = ''
            calindex = 0
            optFin = 0
            output_history.config(text='')
            output_current.config(height=1, font=('D2Coding', 30))
            output_history.config(height=1, font=('D2Coding', 15))

        if val != 0 and val != '' and calcValue[calindex] == '0':    # prevent 0 in the value's head
            calcValue[calindex] = calcValue[calindex].replace('0', '')

        if val == 0 and calcValue[calindex] == '0':    # prevent multiple 0 when the entire value is 0
            val = ''

    if not val == '': calcValue[calindex] += str(val)

    if not calcValue[2]: output_current.config(text=calcValue[0])
    else: output_current.config(text=calcValue[calindex])

    print(calcValue)


#####           mapping             #####
buttonmap = (('Back', 'C', 'CE', '%'),
          (7, 8, 9, '/'),
          (4, 5, 6, '*'),
          (1, 2, 3, '-'),
          (0, '.', '=', '+'))
mapper_size_row = len(buttonmap)
mapper_size_col = len(buttonmap[0])

btn = None
calcValue = ['', '', '']
calindex = len(calcValue) - 1
optFin = 0
crCount = 0

for row in range(mapper_size_row):
    for col in range(mapper_size_col):
        btn = tkinter.Button(screen, text='{}'.format(buttonmap[row][col]), height=2, width=8, bg='white', font=('D2Coding', '13'), command=lambda i = buttonmap[row][col]:input(i))
        # if buttonmap[row][col] != 'CE' and buttonmap[row][col] != '-' :
        #     screen.bind('<{}>'.format(buttonmap[row][col]), lambda i = buttonmap[row][col]: input(i))
        # print(buttonmap[row][col])
        btn.grid(row=row+2, column=col)


#####           output part             #####
output_history = tkinter.Label(screen, text=calcValue[calindex], font=('D2Coding', 15), anchor='se', fg='sky blue', bg='dark grey', height=1, width=10)
output_history.grid(row=0, column=0, columnspan=4, sticky='e'+'w'+'s'+'n')
output_current = tkinter.Label(screen, text='0', font=('D2Coding', 30), anchor='se', fg='white', bg='dark grey', height=1, width=10)
output_current.grid(row=1, column=0, columnspan=4, sticky='e'+'w'+'s'+'n')

screen.mainloop()