from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import subprocess

def get_master_volume():
    # Lấy ra tất cả các thiết bị audio
    devices = AudioUtilities.GetSpeakers()
    # Lấy ra endpoint volume interface
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    # Chuyển đổi interface sang IAudioEndpointVolume
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
    # Lấy giá trị âm lượng
    volume = volume_interface.GetMasterVolumeLevelScalar() * 100
    return volume

def set_master_volume(volume):
    # Lấy ra tất cả các thiết bị audio
    devices = AudioUtilities.GetSpeakers()
    # Lấy ra endpoint volume interface
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    # Chuyển đổi interface sang IAudioEndpointVolume
    volume_interface = cast(interface, POINTER(IAudioEndpointVolume))
    # Set âm lượng
    volume_interface.SetMasterVolumeLevelScalar(volume / 100, None)

# Đặt âm lượng ban đầu là 50%
set_master_volume(50)
