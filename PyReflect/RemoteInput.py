import platform
from ctypes import *

class ImageData:
    """
    typedef struct ImageData
    {
        std::int32_t parent_process_id;
        std::int32_t parent_thread_id;
        std::int32_t width;
        std::int32_t height;
        bool debug_graphics;
        EIOSCommand command;
        std::uint8_t args[4096 * 8];
    } ImageData;
    """
    pass

class EIOS:
    """
    typedef struct EIOS
    {
        std::int32_t pid;
        std::int32_t width;
        std::int32_t height;
        std::intptr_t local_storage;
        std::unique_ptr<ControlCenter> control_center;
    } EIOS;
    """
    pass

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
        pass

    def EIOS_ReleaseTarget(self, target):
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

    def EIOS_GetMousePosition(self, EIOS* eios, std::int32_t* x, std::int32_t* y):
        pass

    def EIOS_GetRealMousePosition(self, EIOS* eios, std::int32_t* x, std::int32_t* y):
        pass

    def EIOS_MoveMouse(self, EIOS* eios, std::int32_t x, std::int32_t y):
        pass

    def EIOS_HoldMouse(self, EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t button):
        pass

    def EIOS_ReleaseMouse(self, EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t button):
        pass

    def EIOS_ScrollMouse(self, EIOS* eios, std::int32_t x, std::int32_t y, std::int32_t lines):
        pass

    def EIOS_IsMouseButtonHeld(self, EIOS* eios, std::int32_t button):
        pass

    def EIOS_SendString(self, EIOS* eios, const char* string, std::int32_t keywait, std::int32_t keymodwait):
        pass

    def EIOS_HoldKey(self, EIOS* eios, std::int32_t key):
        pass

    def EIOS_ReleaseKey(self, EIOS* eios, std::int32_t key):
        pass

    def EIOS_IsKeyHeld(self, EIOS* eios, std::int32_t key):
        pass

    def EIOS_GetKeyboardSpeed(self, EIOS* eios):
        pass

    def EIOS_SetKeyboardSpeed(self, EIOS* eios, std::int32_t speed):
        pass

    def EIOS_GetKeyboardRepeatDelay(self, EIOS* eios):
        pass

    def EIOS_SetKeyboardRepeatDelay(self, EIOS* eios, std::int32_t delay):
        pass

    def EIOS_PairClient(self, pid_t pid):
        pass

    def EIOS_KillClientPID(self, pid_t pid):
        pass

    def EIOS_KillClient(self, EIOS* eios):
        pass

    def EIOS_KillZombieClients(self, ):
        pass

    def EIOS_GetClients(self, bool unpaired_only):
        pass

    def EIOS_GetClientPID(self, std::size_t index):
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

    def EIOS_Inject_PID(self, std::int32_t pid):
        pass

    def Reflect_GetEIOS(self, std::int32_t pid):
        pass

    def Reflect_Object(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_IsSame_Object(self, EIOS* eios, jobject first, jobject second):
        pass

    def Reflect_InstanceOf(self, EIOS* eios, jobject object, const char* cls):
        pass

    def Reflect_Release_Object(self, EIOS* eios, jobject object):
        pass

    def Reflect_Release_Objects(self, EIOS* eios, jobject* objects, std::size_t amount):
        pass

    def Reflect_Bool(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_Char(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_Byte(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_Short(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_Int(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_Long(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_Float(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_Double(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_String(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc, char* output, std::size_t output_size):
        pass

    def Reflect_Array(self, EIOS* eios, jobject object, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_Array_With_Size(self, EIOS* eios, jobject object, std::size_t* output_size, const char* cls, const char* field, const char* desc):
        pass

    def Reflect_Array_Size(self, EIOS* eios, jarray array):
        pass

    def Reflect_Array_Index(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t index, std::size_t length):
        pass

    def Reflect_Array_Index2D(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y):
        pass

    def Reflect_Array_Index3D(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z):
        pass

    def Reflect_Array_Index4D(self, EIOS* eios, jarray array, ReflectionArrayType type, std::size_t length, std::int32_t x, std::int32_t y, std::int32_t z, std::int32_t w):
        pass

    def Reflect_Array_Indices(self, EIOS* eios, jarray array, ReflectionArrayType type, std::int32_t* indices, std::size_t length):
        pass


