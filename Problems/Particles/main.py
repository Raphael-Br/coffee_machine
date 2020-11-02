a = input()
b = input()

if a == "1" and b == "0":
    print('Photon Boson')
elif a == "1/2":
    if b == "-1/3":
        print('Strange Quark')
    if b == "2/3":
        print('Charm Quark')
    if b == "-1":
        print('Electron Lepton')
    if b == "0":
        print('Neutrino Lepton')
