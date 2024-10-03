from tkinter import *
from tkinter.ttk import *
#import numpy as np
try:
    from bluepy.btle import Scanner, DefaultDelegate, UUID, Peripheral
except:
    print("No Bluetooth available")
    pass

#MAC = ['Stimulation device', 'f6:2a:82:fb:64:65']
MAC = []
code_p1 = int('11111111',2)
code_p2 = int('00000011',2)
code_p21 = int('11110000',2)
code_p22 = int('00000011',2)
code_p3 = int('00000000',2)
code_p4 = int('00000000',2)
code_p5 = int('00000001',2)
q = Peripheral()

def scanbtle():
    results = []
    scanner = Scanner()
    devices = scanner.scan(10.0)
    for dev in devices:
        data=dev.getScanData()
        appended=0
        for x in range(len(data)):
#            if(data[x][2]=="6e400001-b5a3-f393-e0a9-e50e24dcca9e"):
            if x==0:
                for y in range(len(data)):
                    if(data[y][0]==9):
                        results.append([dev.addr,data[y][2]])
                        appended=1
        if appended == 0:
            results.append([dev.addr,dev.addr])
    return results

#Routine to connect to communication characteristics on "mac"-Address
'''
def connectbtle(mac):
    try:
        led_service_uuid = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
        led_char_uuid = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
        global p
        p = Peripheral(mac, "random")
        LedService=p.getServiceByUUID(led_service_uuid)
        global ch
        ch = LedService.getCharacteristics(led_char_uuid)[0]
        print("connected")
        return 1
    except:
        print("Connection failed")
        return 0
'''   
#Routine to disconnect BTLE Device
def disconnectbtle():
    try:
        p.disconnect()
    except:
        pass
    
def sendBLEActivate():
        try:
            cha.write(b'~')
        except:
            self.label_connect.setText("Connection failed")
            print("disconnected")
        
#Deactivate stimulation device chargepumps
def sendBLEDeactivate():
    try:
        cha.write(b'#')
    except:
        self.label_connect.setText("Connection failed")
        print("disconnected")
    #print("Led toggle")

#Update Hex Command in GUI
'''
def updateHex(self):
    cur1send=self.cur1.value()
    cur2send=self.cur2.value()
    if cur1send<0:
        cur1send=hex(int(cur1send*(-1)*20+128))
    else:
        cur1send=hex(int(cur1send*20))
    if cur2send<0:
        cur2send=hex(int(cur2send*(-1)*20+128))
    else:
        cur2send=hex(int(cur2send*20))
    sendValue="0x70 "+hex(int(self.dur1.value()*100-16))+" "+hex(int(self.dur2.value()*100-16))+" "+hex(int(self.delay1.value()*20-4))+" "+hex(int(self.tonext.value()*20-4))+" "+hex(self.pulsecount.value())+" "+cur1send+" "+cur2send+" "+hex(int(self.freq.value()))+" 0x65"
    self.hexCode.setText(sendValue)
    self.signalPainter.updateValues(self.dur1.value(),self.dur2.value(),self.delay1.value(),self.tonext.value(),self.cur1.value(),self.cur2.value(),self.pulsecount.value())
'''

'''
#Update period to frequency in GUI
def updateHz(self):
    self.label_hz.setText(str(round(1000/self.freq.value(),3))+" kHz")
'''

'''
#gerenerate bytearray for the stimulation command and send over BLE
def sendBLESend(self):
    cur1send=self.cur1.value()*1.25
    cur2send=self.cur2.value()*1.25
    if cur1send<0:
        cur1send=int(cur1send*(-1)*20+128)
    else:
        cur1send=int(cur1send*20)
    if cur2send<0:
        cur2send=int(cur2send*(-1)*20+128)
    else:
        cur2send=int(cur2send*20)
    sendValue=bytearray([112,int(self.dur1.value()*100-16)>>8&0xff,int(self.dur1.value()*100-16)&0xff, int(self.dur2.value()*100-16)>>8&0xff,int(self.dur2.value()*100-16)&0xff, int(self.delay1.value()*20-4)>>8&0xff,int(self.delay1.value()*20-4)&0xff, int(self.tonext.value()*20-4)>>8&0xff, int(self.tonext.value()*20-4)&0xff, self.pulsecount.value(), cur1send, cur2send, int(self.freq.value()), 101])
    try:
        ch.write(sendValue)
    except:
        self.label_connect.setText("Connection failed")
        print("disconnected")
            
    self.label_connect.setText("Connect now")
    self.actionScan_for_Devices.triggered.connect(self.scan)
    self.actionDisconnect.triggered.connect(self.disconnect)
'''

'''    
def scan(self):
    self.scanWidget = ScanDialog(self)
    self.scanWidget.exec()
    if(self.scanWidget.returntomain() != 0):
        print(self.scanWidget.returntomain())
        if connectbtle(self.scanWidget.returntomain()[0])==1:
            self.label_connect.setText("Connected to: "+ self.scanWidget.returntomain()[1])
        else:
            self.label_connect.setText("Connected to: Not connected")

def disconnect(self):
    disconnectbtle()
    self.label_connect.setText("Connect now")
'''  
def updtcblist():
    lista = list(GNDCombo['values'])
    lista.remove(outputCombo.get())
    GNDCombo['values'] = lista
    
def resetList(*args):
    GNDCombo['values']= (1, 2, 3, 4)
    
def startTransfer():
    led_service_uuid = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
    led_char_uuid = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
    #select_device()
    #print(results)
    global q
    #q = Peripheral('f6:2a:82:fb:64:65', "random")
    q = Peripheral(MAC[0], "random")
    LedService=q.getServiceByUUID(led_service_uuid)
    global cha
    cha = LedService.getCharacteristics(led_char_uuid)[0]
    #sendBLEActivate()
    #msg = bytearray([int('11110111',2), int('11111111',2)])
    
    outputChannel(outputCombo)
    GNDChannel(GNDCombo)
    outputPeriod(PeriodCombo)
    outputDutyCycle(DutyCycleCombo)
    outputAmplitude(AmpEntry)
    numberOfPulses(PulsesEntry)

    code = [code_p1, code_p2, code_p21, code_p22, code_p3, code_p4, code_p5]
    print(code)
    
    msg = bytearray(code)
    try:
        cha.write(msg)
    except:
        pass
    try:
        q.disconnect()
    except:
        print("Failed to disconnect")


def stopTransfer():
    #global q
    #sendBLEDeactivate()
    try:
        code = ['11110000', '00000000', '11110000', '00000000', code_p3, code_p4, code_p5]
        msg = bytearray(code)
        cha.write(msg)
        q.disconnect()
    except:
        print("Failed to disconnect")
    


def select_device():
    popup = Toplevel(window)
    results = scanbtle()
    DeviceCombo = Combobox(popup)  
    print(results)  

    def CloseAndGet():
        global MAC
        MAC = results[DeviceCombo.current()]
        print(MAC[1])								#debug
        popup.destroy()

    listin = []
    PopupCloseBtn = Button(popup, text="Select", command=CloseAndGet)
    for index in results:
        print(index[1])
        listin += (index[1],)
    DeviceCombo['values'] = listin							#debug
    DeviceCombo.grid(column=0,row=0)
    PopupCloseBtn.grid(column=0,row=1)


    	

 

window = Tk()
 
window.title("Stimulation Device NeoGUI")
 
window.geometry('400x200')

outputlbl = Label(window, text="DAC Output port") 
outputCombo = Combobox(window)

GNDlbl = Label(window, text="DAC Ground port") 
GNDCombo = Combobox(window, postcommand = updtcblist)

Signallbl = Label(window, text="Signal type") 
SignalCombo = Combobox(window)

Amplbl = Label(window, text="Max Signal Amplitude") 
Amplbl2 = Label(window, text="%") 
AmpEntry = Entry(window)

Periodlbl = Label(window, text="Time ON: 30 + ") 
Periodlbl2 = Label(window, text="us") 
PeriodCombo = Combobox(window)

DutyCyclelbl = Label(window, text="Time OFF: 30 + ") 
DutyCyclelbl2 = Label(window, text="us") 
DutyCycleCombo = Combobox(window)

Pulseslbl = Label(window, text="No. of pulses") 
Pulseslbl2 = Label(window, text="us (0-255)") 
PulsesEntry = Entry(window)

SearchBtn = Button(window, text="Search device", command=select_device)
#SearchBtn = Button(window, text="Search device (out of order)") 

outputCombo['values']= (1, 2, 3, 4)
GNDCombo['values']= (1, 2, 3, 4)
SignalCombo['values']= ("{Pulse train}")
AmpEntry.insert(0, '100')
PeriodCombo['values']= (50, 100, 150, 200)
DutyCycleCombo['values']= (50, 100, 150, 200)
PulsesEntry.insert(0, '10')
 
outputlbl.grid(column=0, row=0)
outputCombo.current(0) #set the selected item

GNDlbl.grid(column=0, row=1)
GNDCombo.current(1) #set the selected item

Signallbl.grid(column=0, row=2)
SignalCombo.current(0) #set the selected item

Amplbl.grid(column=0, row=3)
Amplbl2.grid(column=2, row=3)
#AmpCombo.current(0) #set the selected item

Periodlbl.grid(column=0, row=4)
Periodlbl2.grid(column=2, row=4)
PeriodCombo.current(3) #set the selected item

DutyCyclelbl.grid(column=0, row=5)
DutyCycleCombo.current(1) #set the selected item

Pulseslbl.grid(column=0, row=6)
Pulseslbl2.grid(column=2, row=6)

 
outputCombo.grid(column=1, row=0)
GNDCombo.grid(column=1, row=1)
SignalCombo.grid(column=1, row=2)
AmpEntry.grid(column=1, row=3)
PeriodCombo.grid(column=1, row=4)
DutyCycleCombo.grid(column=1, row=5)
PulsesEntry.grid(column=1, row=6)

outputCombo.bind("<<ComboboxSelected>>", resetList)

StartBtn = Button(window, text="Start", command=startTransfer)
 
StartBtn.grid(column=0, row=8)

StopBtn = Button(window, text="Stop", command=stopTransfer)
 
StopBtn.grid(column=1, row=8)

SearchBtn.grid(column=1, row=7)

'''
Code generation part
'''


def outputChannel(outputCombo):
    global code_p1, code_p2
    switcher = {
    '1': int('00011111',2),
    '2': int('00101111',2),
    '3': int('00111111',2),
    '4': int('01001111',2)
    }
    
    print(bin(code_p1))
    print(switcher.get(outputCombo.get()))
    code_p1 = code_p1 & switcher.get(outputCombo.get())
    print(bin(code_p1), bin(code_p2))

def GNDChannel(GNDCombo):
    global code_p21, code_p22
    switcher = {
    '1': int('00011111',2),
    '2': int('00101111',2),
    '3': int('00111111',2),
    '4': int('01001111',2)
    }
    code_p21 = code_p21 & switcher.get(GNDCombo.get())
    print(bin(code_p21), bin(code_p22))

def outputPeriod(PeriodCombo):
    global code_p3
    switcher = {
    '50':  int('00000000',2),
    '100': int('00000001',2),
    '150': int('00000010',2),
    '200': int('00000011',2)
    }
    code_p3 = switcher.get(PeriodCombo.get())
    print(bin(code_p3))

def outputDutyCycle(DutyCycleCombo):
    global code_p4
    switcher = {
    '50':  int('00000000',2),
    '100': int('00000001',2),
    '150': int('00000010',2),
    '200': int('00000011',2)
    }
    code_p4 = switcher.get(DutyCycleCombo.get())
    print(bin(code_p4))

def outputAmplitude(AmpEntry):
    global code_p1, code_p2
    number = bin(int(int(AmpEntry.get()) * 1023 / 100))
    print("flag")
    print(AmpEntry.get())
    print(number)
    binnum = bin(int(number,2) << 2)  # so as to give it 2 zeros to the left, could also be ones
    print(binnum)
    binnumMSB = bin(int(int(binnum,2) / 256))
    print(binnumMSB)
    binnumLSB = bin(int(int(binnum,2) % 256))
    print(binnumLSB)
    print(type(binnumLSB))
    code_p1 = (code_p1 & int(0xF0)) | int(binnumMSB,2)
    print(code_p1)
    code_p2 = int(binnumLSB,2)
    print(code_p2)

def numberOfPulses(PulsesEntry):
    global code_p5

    code_p5 = int(PulsesEntry.get())
    print(code_p5)
 
window.mainloop()
