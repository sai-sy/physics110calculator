import math

def inputLoop(prompt):
    '''This is the custom input command which lets us always process a quit'''
    response: str = input(prompt)
    if response == 'q' or response  == 'quit':
        quit()
    else:
        return response

def vectorMagnitude():
    x = float(inputLoop('Enter your x value: '))
    y = float(inputLoop('Enter your y value: '))
    z = float(inputLoop('Enter your z value: '))
    vm = math.sqrt((x**2)+(y**2)+(z**2))
    print('Unit Vector is: ' + str(vm))
    return {'x': x, 'y': y,'z': z, 'vm': vm}

def unitVector():
    choice = inputLoop('By mag or angle: ')
    if choice == 'mag':
        vm = vectorMagnitude()
        x = vm['x']/vm['vm']
        y = vm['y']/vm['vm']
        z = vm['z']/vm['vm']
        uv = [x,y,z]
        print('Unit Vector is: ')
        print(uv)
        return uv
    elif choice == 'angle':
        x = float(inputLoop('Enter the angle off the x-axis: '))
        y = float(inputLoop('Enter the angle off the y-axis: '))
        z = float(inputLoop('Enter the angle off the z-axis: '))

        uv = [math.cos(math.radians(x)), math.cos(math.radians(y)), math.cos(math.radians(z))]
        print('Unit Vector is [cos(' + str(x)  + '), cos(' + str(y) +  '), cos(' +str(z) + '),]')
        print(uv)
        return uv

def vectorBuildUV():
    uv = unitVector()
    arr = []
    ret = float(inputLoop('What is the new vector magnitude: '))
    for i in uv:
        arr.append(i*ret)
    print('New Vector is: ')
    print(arr)
    return arr


if __name__ == "__main__":
    print('Welcome to the PCS 110 CLI Calulator. This helps me get through my homework a bit faster while making sure I understand the steps I need to take.')
    print('At any point enter "q" or "quit" to exit')
    print('Problem Codes:')
    print('vmag -- vectorMagnitude\nuv -- unitVector\nvbuv -- Build a new vector with a magnitude and a Unit Vector')
    while(True):
        ret = inputLoop('What problem: ')
        if ret == 'vmag':
            vectorMagnitude()
        elif ret == 'uv':
            unitVector()
        elif ret == 'vbuv':
            vectorBuildUV()