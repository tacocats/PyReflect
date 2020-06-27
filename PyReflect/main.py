import RemoteInput
import struct
from ctypes import string_at
from sys import getsizeof
from binascii import hexlify

if __name__ == "__main__":

    print("Creating instance of Remote Input")
    reflect = RemoteInput.RemoteInput()

    print("Injecting EIOS")
    reflect.EIOS_Inject()


    print("Getting clients")
    print(reflect.EIOS_GetClients())
    client_count = reflect.EIOS_GetClients()


    print("Getting clients PID")
    print(reflect.EIOS_GetClientPID(0))
    client_pid = reflect.EIOS_GetClientPID(0)

    print("Pairing with client")
    # eiosptr or target
    eiosptr = reflect.EIOS_PairClient(client_pid)
    print(type(eiosptr))

    print ("Releasing target")
    reflect.EIOS_ReleaseTarget(target=eiosptr)
