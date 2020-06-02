import platform
from ctypes import *

class RemoteInput:
    """
    This class allows for python to access RemoteInput
    """

    def __init__(self):
        if platform.system() == 'Windows':
            self.ri = WinDLL('./libremoteinput.dll')
        elif platform.system() == 'Dawrin':
            self.ri = CDLL('./libremoteinput.dylib')
        else:
            self.ri = CDLL('.libremoteinput.so')

    ## EIOS

    def EIOS_RequestTarget(self, initstr):
        """ 
        EIOS* EIOS_RequestTarget(const char* initargs) noexcept;

        :param initstr: TODO 
        :type initstr: String

        :return: EIOS Target 
        :rtype: EIOS
        """
        self.ri.EIOS_RequestTarget.argtypes = [c_char_p]
        self.ri.EIOS_RequestTarget.rtype = EIOS

        return self.EIOS_RequestTarget(bytes(initstr, encoding='utf8'))


    def EIOS_ReleaseTarget(self, target):
        """
        void EIOS_ReleaseTarget(EIOS* eios) noexcept;

        :param target: The EIOS target
        :type target: EIOS

        :return: None
        """
        pass

    def EIOS_GetTargetDimensions(self, target):
        pass

    def EIOS_GetImageBuffer(self, target):
        pass

    def EIOS_GetDebugImageBuffer(self, target):
        pass

    def EIOS_SetGraphicsDebugging(self, target, enabled):
        pass

    def EIOS_UpdateImageBuffer(self, target):
        pass

    def EIOS_HasFocus(self, target):
        pass

    def EIOS_GainFocus(self, target):
        pass

    def EIOS_LoseFocus(self, target):
        pass

    def EIOS_IsInputEnabled(self, target):
        pass

    def EIOS_SetInputEnabled(self, target, enabled):
        pass

    def EIOS_GetMousePosition(self, target):
        pass

    def EIOS_GetRealMousePosition(self, target):
        pass

    def EIOS_MoveMouse(self, target, x, y):
        pass

    def EIOS_HoldMouse(self, target, x, y, button):
        pass

    def EIOS_ReleaseMouse(self, target, x, y, button):
        pass

    def EIOS_ScrollMouse(self, target, x, y, lines):
        pass

    def EIOS_IsMouseButtonHeld(self, target, button):
        pass

    def EIOS_SendString(self, target, text, keywait, keymodwait):
        pass

    def EIOS_HoldKey(self, target, key):
        pass

    def EIOS_ReleaseKey(self, target, key):
        pass

    def EIOS_IsKeyHeld(self, target, key):
        pass

    def EIOS_GetKeyboardSpeed(self, target):
        pass

    def EIOS_SetKeyboardSpeed(self, target, speed):
        pass

    def EIOS_GetKeyboardRepeatDelay(self, target):
        pass

    def EIOS_SetKeyboardRepeatDelay(self, target, delay):
        pass

    def EIOS_PairClient(self, pid):
        pass

    def EIOS_KillClientPID(self, pid):
        pass

    def EIOS_KillClient(self, target):
        pass

    def EIOS_KillZombieClients(self):
        pass

    def EIOS_GetClients(self, unpaired_only):
        pass

    def EIOS_GetClientPID(self, index):
        pass


    ## Reflection

    def EIOS_Inject(self, process_name: str='JagexLauncher.exe'):
        """
        void EIOS_Inject(const char* process_name) noexcept;

        :return: None
        """
        self.ri.EIOS_Inject.argtypes = [c_char_p]
        self.ri.EIOS_Inject.rtype = None
        self.ri.EIOS_Inject(bytes(process_name, encoding='utf8'))

    def EIOS_Inject_PID(self, pid):
        pass

    def Reflect_GetEIOS(self, pid):
        pass

    # TODO Implement below methods
    #def Reflect_Object(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_IsSame_Object(self, EIOS* eios, jobject first, jobject second):
    #    pass

    #def Reflect_InstanceOf(self, EIOS* eios, jobject object, const char* cls):
    #    pass

    #def Reflect_Release_Object(self, EIOS* eios, jobject object):
    #    pass

    #def Reflect_Release_Objects(self, EIOS* eios, jobject* objects, std::size_t amount):
    #    pass

    #def Reflect_Bool(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_Char(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_Byte(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_Short(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_Int(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_Long(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_Float(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_Double(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_String(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc, char* output, std::size_t output_size):
    #    pass

    #def Reflect_Array(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_Array_With_Size(self, EIOS* eios, jobject object, std::size_t* output_size, const char* cls, const char* field, const char* desc):
    #    pass

    #def Reflect_Array_Size(self, EIOS* eios, jarray array):
    #    pass

    #def Reflect_Array_Index(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t index, std::size_t length):
    #    pass

    #def Reflect_Array_Index2D(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y):
    #    pass

    #def Reflect_Array_Index3D(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z):
    #    pass

    #def Reflect_Array_Index4D(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z, std::int32_t w):
    #    pass

    #def Reflect_Array_Indices(self, EIOS* eios, jarray array, ReflectionArrayType type, std::int32_t* indices, std::size_t length):
    #    pass


