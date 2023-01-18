## 입력 제한 해재, 인덱스가 17이상이면 실수형태('ne+n') 형태로 출력하도록 변경 및 기타 예외처리 추가
## global 변수 static화
## 함수 세분화 진행, 정수파트, 연산자파트, 출력파트, 예외 처리로 분류
## 무한대 예외처리 추가

import tkinter

screen = tkinter.Tk()
screen.title("KIM's CALCULATOR")
screen.geometry('297x342')
screen.resizable(False, False)
screen.rowconfigure(1, weight=1)
for s_col in range(4):
    screen.columnconfigure(s_col, weight=1)


#####           function part             #####
def outputResult(val):
    if val != '': input.calcValue[input.calindex] += str(val)

    if len(input.calcValue[input.calindex]) < 13:
        if input.optFin == 1 and (len(input.calcValue[0]) > 13 or len(input.calcValue[2]) > 13):
            output_current.config(height=2, font=('D2Coding', 17))
        elif input.optFin == 0 and len(input.calcValue[0]) > 13 and input.calcValue[2] == '':
            output_current.config(height=2, font=('D2Coding', 17))
        else:
            output_current.config(height=1, font=('D2Coding', 30))
    elif len(input.calcValue[input.calindex]) > 12:
        output_current.config(height=2, font=('D2Coding', 17))

    if not input.calcValue[2]: output_current.config(text=input.calcValue[0])
    else: output_current.config(text=input.calcValue[input.calindex])

    print(*input.calcValue)

def resetter():
    input.calcValue[0] = '0'
    input.calcValue[1] = ''
    input.calcValue[2] = ''
    input.calindex = 0
    input.optFin = 0
    output_history.config(text='')

def integer(val):
    ##### integer part
    if len(input.calcValue[input.calindex]) > 13:  # automatically changes the font size
        output_current.config(height=2, font=('D2Coding', 17))
        if len(input.calcValue[input.calindex]) > 15:
            val = ''
    else : output_current.config(height=1, font=('D2Coding', 30))

    if input.optFin == 1:
        resetter()
        output_current.config(height=1, font=('D2Coding', 30))
        output_history.config(height=1, font=('D2Coding', 15))

    if val != 0 and val != '' and input.calcValue[input.calindex] == '0':    # prevent 0 in the value's head
        input.calcValue[input.calindex] = input.calcValue[input.calindex].replace('0', '')

    if val == 0 and input.calcValue[input.calindex] == '0':    # prevent multiple 0 when the entire value is 0
        val = ''

    outputResult(val)

def operator(val):
    if not input.calcValue[0]: input.calcValue[0] = '0'
    if val == '.':  ### decimal point part
        if input.optFin == 1:
            resetter()
        else:
            if input.calcValue[input.calindex] == '': input.calcValue[input.calindex] = '0'
            if input.calcValue[input.calindex].find('.') != -1: val = ''  # when user input '.', check if there's already a decimal point
        input.calcValue[input.calindex] += val

    elif val == '+' or val == '-' or val == '*' or val == '/' or val == '%':
        if input.calcValue[0] == 'inf':
            val = ''
        if not input.calcValue[1] or input.calcValue[1] == '=':
            input.calcValue[1] = val
        elif input.calcValue[1] and input.optFin == 1:
            input.calcValue[1] = val
            input.calcValue[input.calindex] = ''
            input.optFin = 0
        elif not input.calcValue[2]:
            input.calcValue[1] = val
        elif input.calcValue[2]:
            total = ''
            for value in input.calcValue:
                total += str(value)

            if len(str(eval(total))) > 16 or total.find('e+') != -1:
                input.calcValue[0] = str(float(eval(total)))
            else:
                input.calcValue[0] = str(eval(total))

            input.calcValue[1] = val
            input.calcValue[2] = ''
        if input.calcValue[0] == 'inf':
            output_history.config(text=input.calcValue[:1])
        else:
            output_history.config(text=input.calcValue[:2])

    elif val == '=' or val == 'Enter':
        total = ''
        if input.calcValue[0] == 'inf':
            val = ''
        if not input.calcValue[1]:
            input.calcValue[1] = '='
            output_history.config(text=input.calcValue[:2])
            if input.calcValue[0] == '0': input.calindex = 0
        elif input.calcValue[1] == '=':
            val = ''
        elif not input.calcValue[2]:
            input.calcValue[input.calindex] = input.calcValue[0]
            input.calindex = 0
            input.calcValue.append('=')
            output_history.config(text=input.calcValue)
            del input.calcValue[len(input.calcValue) - 1]
            for value in input.calcValue:
                total += str(value)

            if total == 'inf':
                pass
            elif len(str(eval(total))) > 16 or total.find('e+') != -1:
                input.calcValue[0] = str(float(eval(total)))
            else:
                input.calcValue[0] = str(eval(total))

            output_current.config(text=input.calcValue[input.calindex])
            input.optFin = 1
        else:
            if input.calcValue[1] == '/' and input.calcValue[2] == '0':
                input.calcValue[0] = '0'
                input.calcValue[1] = ''
                input.calcValue[2] = ''
                val = ''
                input.optFin = 1
                output_current.config(height=2, font=('D2Coding', 17))
                output_history.config(height=1, font=('D2Coding', 15), text='')
                input.calcValue[0] = 'Cannot divide by 0'
                input.calindex = 0
            else:
                input.calcValue.append('=')
                output_history.config(text=(input.calcValue))
                del input.calcValue[len(input.calcValue) - 1]
                for value in input.calcValue:
                    total += str(value)

                if total.find('inf') != -1:
                    input.calcValue[1] = ''
                    input.calcValue[2] = ''
                    output_history.config(text=input.calcValue[0])
                elif len(str(eval(total))) > 16 or total.find('e+') != -1:
                    input.calcValue[0] = str(float(eval(total)))
                else:
                    input.calcValue[0] = str(eval(total))

                input.calindex = 0
                # if len(input.calcValue[0]) + len(input.calcValue[2]) > 25:
                #     output_history.config(height=1, font=('D2Coding', 8))
                output_current.config(text=input.calcValue[input.calindex])
                input.optFin = 1
        if len(input.calcValue[0]) + len(input.calcValue[2]) > 24:
            output_history.config(height=1, font=('D2Coding', 9))

    elif val == 'Back' or val == '\x08':
        if input.calcValue[0].find('inf') != -1:
            input.calcValue[0] = '0'
            input.calcValue[1] = ''
            input.calcValue[2] = ''
            input.optFin = 0
            output_current.config(height=1, font=('D2Coding', 30))
            output_history.config(height=1, font=('D2Coding', 15), text='')
        if input.optFin == 1:
            temp = input.calcValue[0]
            for i in range(len(input.calcValue)):
                input.calcValue[i] = ''
            output_history.config(text='')
            input.calcValue[0] = temp
            input.optFin = 0
            input.calindex = 0
            output_history.config(height=1, font=('D2Coding', 15))
            output_current.config(height=1, font=('D2Coding', 30))
        else:
            valSize = len(input.calcValue[input.calindex]) - 1
            if input.calcValue[input.calindex].find('e+') != -1:
                input.calcValue[input.calindex] = str(float(input.calcValue[input.calindex]) / 10)
            else: input.calcValue[input.calindex] = input.calcValue[input.calindex][:valSize]


        if input.calindex == 0 and input.calcValue[input.calindex] == '':
            input.calcValue[input.calindex] = '0'
        elif input.calindex == 2 and input.calcValue[2] == '':
            input.calcValue[input.calindex] = '0'
        elif input.calcValue[input.calindex] == 'Cannot divide by 0':
            input.calcValue[input.calindex] = '0'

    elif val == 'C':
        input.calcValue[0] = '0'
        input.calcValue[1] = ''
        input.calcValue[2] = ''
        val = ''
        input.optFin = 0
        output_current.config(height=1, font=('D2Coding', 30))
        output_history.config(height=1, font=('D2Coding', 15), text='')

    elif val == 'CE' or val == 'Delete':
        if input.optFin == 1:
            for i in range(len(input.calcValue)):
                input.calcValue[i] = ''
            output_history.config(text='')
            input.calcValue[0] = '0'
            input.optFin = 0
            output_current.config(height=1, font=('D2Coding', 30))
            output_history.config(height=1, font=('D2Coding', 15))
        input.calcValue[input.calindex] = '0'
    val = ''

    outputResult(val)

def input(val):
    input.calindex = 0
    if input.calcValue[1] : input.calindex = 2

    if type(val) == str:                            ##### operator part
        operator(val)

    else:                                               ##### integer part
        integer(val)

def ballocStr(strinput):
    if strinput.keycode == 46:
        input('Delete')
    if strinput.keycode == 13:
        input('Enter')
    else: input(strinput.char)

def ballocInt(intinput):
    input(int(intinput.char))


#####           mapping             #####
buttonmap = (('Back', 'C', 'CE', '%'),
          (7, 8, 9, '/'),
          (4, 5, 6, '*'),
          (1, 2, 3, '-'),
          (0, '.', '=', '+'))
mapper_size_row = len(buttonmap)
mapper_size_col = len(buttonmap[0])

input_button = None
input.calcValue = ['', '', '']
input.calindex = len(input.calcValue) - 1
input.optFin = 0

for row in range(mapper_size_row):
    for col in range(mapper_size_col):
        if buttonmap[row][col] == '=':
            input_button = tkinter.Button(screen, text='{}'.format(buttonmap[row][col]),
                                 height=2, width=8, bg='sky blue', font=('D2Coding', '13'), command=lambda i=buttonmap[row][col]: input(i))
        else: input_button = tkinter.Button(screen, text='{}'.format(buttonmap[row][col]),
                             height=2, width=8, bg='white', font=('D2Coding', '13'), command=lambda i = buttonmap[row][col]:input(i))
        if buttonmap[row][col] == 'CE':
            screen.bind('<Delete>', ballocStr)
        elif buttonmap[row][col] == '=':
            screen.bind('<Return>', ballocStr)
            screen.bind(str(buttonmap[row][col]), ballocStr)
        elif buttonmap[row][col] == 'Back':
            screen.bind('<BackSpace>', ballocStr)
        elif buttonmap[row][col] == '-':
            screen.bind('<minus>', ballocStr)
        elif type(buttonmap[row][col]) == int:
            screen.bind(str(buttonmap[row][col]), ballocInt)
        elif type(buttonmap[row][col])== str:
            screen.bind(str(buttonmap[row][col]), ballocStr)
        input_button.grid(row=row+3, column=col, sticky="EWSN")


#####           output part             #####
output_history = tkinter.Label(screen, text=input.calcValue[input.calindex], font=('D2Coding', 15), anchor='se', fg='sky blue', bg='grey', height=1, width=10)
output_history.grid(row=0, column=0, columnspan=4, sticky="EWSN")
output_current = tkinter.Label(screen, text='0', font=('D2Coding', 30), anchor='se', fg='white', bg='grey', height=1, width=10)
output_current.grid(row=1, column=0, columnspan=4, sticky="EWSN")
output_padding = tkinter.Label(screen, text='', font=('D2Coding', 2), anchor='se', fg='white', bg='grey', height=1, width=10)
output_padding.grid(row=2, column=0, columnspan=4, sticky="EWSN")

screen.mainloop()