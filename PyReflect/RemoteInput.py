import platform
from ctypes import *
import cppyy
#from prompt_toolkit.data_structures import Size


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

    def EIOS_RequestTarget(self, initstr) -> c_void_p:
        """
        EIOS* EIOS_RequestTarget(const char* initargs) noexcept;

        :param initstr: TODO
        :type initstr: String

        :return: EIOS Target
        :rtype: EIOS
        """
        self.ri.EIOS_RequestTarget.argtypes = [c_char_p]
        self.ri.EIOS_RequestTarget.rtype = c_void_p

        return self.EIOS_RequestTarget(bytes(initstr, encoding='utf8'))

    def EIOS_ReleaseTarget(self, target: c_void_p) -> None:
        """
        void EIOS_ReleaseTarget(EIOS* eios) noexcept;

        :param target: The EIOS target
        :type target: EIOS

        :return: None
        """
        self.ri.EIOS_ReleaseTarget.argtypes = [c_void_p]
        self.ri.EIOS_ReleaseTarget(target)

    def EIOS_GetTargetDimensions(self, target: c_void_p):
        """
        void EIOS_GetTargetDimensions(EIOS* eios, std::int32_t* width, std::int32_t* height) noexcept;

        :param target: The EIOS target
        type target: EIOS

        :return: width, height
        """

        width = c_int32()
        height = c_int32()

        self.ri.EIOS_GetTargetDimensions.argtypes = [c_void_p, POINTER(c_int32), POINTER(c_int32)]
        self.ri.EIOS_GetTargetDimensions.restype = None
        self.ri.EIOS_GetTargetDimensions(target, byref(width), byref(width))

        return [width, height]

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
        """
        EIOS* EIOS_PairClient(pid_t pid) noexcept;
        """

        self.ri.EIOS_PairClient.argtypes = [c_int32]
        self.ri.EIOS_PairClient.restype = c_void_p
        return self.ri.EIOS_PairClient(pid)

    def EIOS_KillClientPID(self, pid):
        pass

    def EIOS_KillClient(self, target):
        pass

    def EIOS_KillZombieClients(self):
        pass

    def EIOS_GetClients(self, unpaired_only=False):
        """
        std::size_t EIOS_GetClients(bool unpaired_only) noexcept;

        :param unpaired_only: Should return only unparied clients or all clients
        :type unpaired_only: bool

        :return: injectedtargets
        :rtype: Int
        """

        self.ri.EIOS_GetClients.argtypes = [c_bool]
        self.ri.EIOS_GetClients.rtype = int
        return self.ri.EIOS_GetClients(unpaired_only)

    def EIOS_GetClientPID(self, index):

        self.ri.EIOS_GetClientPID.argtypes = [c_int]
        self.ri.EIOS_GetClientPID.rtype = int

        return self.ri.EIOS_GetClientPID(index)

    ## Reflection

    def EIOS_Inject(self, process_name: str = 'JagexLauncher.exe'):
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
    # def Reflect_Object(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_IsSame_Object(self, EIOS* eios, jobject first, jobject second):
    #    pass

    # def Reflect_InstanceOf(self, EIOS* eios, jobject object, const char* cls):
    #    pass

    # def Reflect_Release_Object(self, EIOS* eios, jobject object):
    #    pass

    # def Reflect_Release_Objects(self, EIOS* eios, jobject* objects, std::size_t amount):
    #    pass

    # def Reflect_Bool(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_Char(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_Byte(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_Short(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_Int(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_Long(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_Float(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_Double(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_String(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc, char* output, std::size_t output_size):
    #    pass

    # def Reflect_Array(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_Array_With_Size(self, EIOS* eios, jobject object, std::size_t* output_size, const char* cls, const char* field, const char* desc):
    #    pass

    # def Reflect_Array_Size(self, EIOS* eios, jarray array):
    #    pass

    # def Reflect_Array_Index(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t index, std::size_t length):
    #    pass

    # def Reflect_Array_Index2D(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y):
    #    pass

    # def Reflect_Array_Index3D(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z):
    #    pass

    # def Reflect_Array_Index4D(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z, std::int32_t w):
    #    pass

    # def Reflect_Array_Indices(self, EIOS* eios, jarray array, ReflectionArrayType type, std::int32_t* indices, std::size_t length):
    #    pass
