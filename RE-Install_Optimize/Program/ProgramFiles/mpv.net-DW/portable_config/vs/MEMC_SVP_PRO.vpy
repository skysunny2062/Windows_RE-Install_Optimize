# Zack Ver.250328

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f
clip=video_in

H_Pre=2160 #4K處理
Fps_Num=144 #目標fps
Fps_Den=1
Abs=True #絕對幀率
Nvof=False #禁用光流（RX9070XT不支持）
Gpu=0 #第一張顯卡
Lk_Fmt=False #不鎖定格式，保留10bit

ret=k7f.FPS_CTRL(clip,fps_in=container_fps,fps_ret=True)
clip=k7f.FMT_CTRL(clip,h_max=H_Pre,fmt_pix=1 if Lk_Fmt else 0)
clip=k7f.SVP_PRO(clip,fps_in=container_fps,fps_num=Fps_Num,fps_den=Fps_Den,abs=Abs,nvof=Nvof,gpu=Gpu)
clip.set_output()