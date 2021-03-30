# PyReflect
Python Reflection for OSRS and Private Servers.

## About 

This is a port of https://github.com/Brandon-T/Reflection to Python.


## Current Goals

- [ ] Completely implement RemoteInput 
- [ ] Completely port Reflection include

---

## Usage/Setup

Download the correct RemoteInput dll from https://github.com/brandon-t/reflection/releases

The version of RemoteInput <u>must</u>:

* Match your operating system (Windows, Linux, Mac)
* Be the same bit version as python interpreter you will run code on (python 32-bit for 32-bit DLL)
* Match the same version of client you are trying to inject to (Default old school client is 32-bit)

You can than import RemoteInput and set up the connection to client:

```python
import RemoteInput

# Create instance of Remote Input
reflect = RemoteInput.RemoteInput()

# Inject EIOS 
reflect.EIOS_Inject()

# Get number of clients
client_count = reflect.EIOS_GetClients()

# Get first clients PID
client_pid = reflect.EIOS_GetClientPID(0)

# Pair the client and get the target or eiosptr
eiosptr = reflect.EIOS_PairClient(client_pid)
```

---

## PyReflect Status

There are various builds for the remote, so using the correct one you should be able to get it to work, but these are the environments currently tested on:

| OS                                                | Status   |
| ------------------------------------------------- | -------- |
| Windows 10 (32 bit)                               | Untested |
| Windows 10 (64 bit)                               | Working  |
| macOS Big Sur (Apple M1)                          | Working  |
| macOS Big Sur (Intel)                             | Untested |
| Ubuntu or Linux Distro (32-bit, 64-bit, arm, etc) | Untested |

