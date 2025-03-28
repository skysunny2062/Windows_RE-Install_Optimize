# Zack Ver.250328

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f
clip=video_in

H_Pre=2160 #4K處理
Model=23 #目前使用的模型 我有放23 70
T_Tta=False #禁用 ensemble（高品質版模型 我也沒放），減少計算量，適合 RX 9070 XT
Fps_Num=60 #目標fps Fps_Num/Fps_Den 的值即帧率倍数
Fps_Den=24 #原始fps
Sc_Mode=1 #標準場景檢測，平衡效果與性能
Skip=True #跳過靜止幀
Stat_Th=60.0 #靜止幀閾值設為最大值，優化效率
Gpu=0 #第一張顯卡
Gpu_T=2 #雙執行緒適合中高端 GPU
Lk_Fmt=False #不鎖定格式，保留10bit


ret=k7f.FPS_CTRL(clip,fps_in=container_fps,fps_ret=True)
clip=k7f.FMT_CTRL(clip,h_max=H_Pre,fmt_pix=1 if Lk_Fmt else 0)
clip=k7f.RIFE_STD(clip,model=Model,t_tta=T_Tta,fps_num=Fps_Num,fps_den=Fps_Den,sc_mode=Sc_Mode,skip=Skip,stat_th=Stat_Th,gpu=Gpu,gpu_t=Gpu_T)

clip.set_output()