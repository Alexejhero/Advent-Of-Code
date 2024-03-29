import copy
import re

data = """position=<-30052,  -9918> velocity=< 3,  1>
position=< 20349, -50260> velocity=<-2,  5>
position=< 40505, -40169> velocity=<-4,  4>
position=< 30444,  50599> velocity=<-3, -5>
position=< 40549, -50259> velocity=<-4,  5>
position=< 30454, -30087> velocity=<-3,  3>
position=< 50623,  20347> velocity=<-5, -2>
position=< 30439, -50262> velocity=<-3,  5>
position=< 50623,  40516> velocity=<-5, -4>
position=<-40143, -30090> velocity=< 4,  3>
position=< 50594,  50602> velocity=<-5, -5>
position=< -9884, -30087> velocity=< 1,  3>
position=<-19958, -40168> velocity=< 2,  4>
position=< 20357,  40513> velocity=<-2, -4>
position=<-50240,  30431> velocity=< 5, -3>
position=< 20351,  40516> velocity=<-2, -4>
position=<-50257, -20005> velocity=< 5,  2>
position=<-30073,  10253> velocity=< 3, -1>
position=<-50265,  50597> velocity=< 5, -5>
position=<-40154,  50601> velocity=< 4, -5>
position=<-19987, -40168> velocity=< 2,  4>
position=<-19987, -30087> velocity=< 2,  3>
position=<-50257,  30425> velocity=< 5, -3>
position=< 40558,  30425> velocity=<-4, -3>
position=<-19990,  10256> velocity=< 2, -1>
position=<-19979,  30425> velocity=< 2, -3>
position=<-19976, -50254> velocity=< 2,  5>
position=< 30446, -40172> velocity=<-3,  4>
position=<-40157,  40515> velocity=< 4, -4>
position=<-40143,  20342> velocity=< 4, -2>
position=< 30467, -50255> velocity=<-3,  5>
position=<-30040,  50606> velocity=< 3, -5>
position=<-30037,  50605> velocity=< 3, -5>
position=< 20382, -30086> velocity=<-2,  3>
position=< 50594,  10262> velocity=<-5, -1>
position=< 20342,  40515> velocity=<-2, -4>
position=<-19963, -50258> velocity=< 2,  5>
position=<-40135,  50599> velocity=< 4, -5>
position=< 40558,  10262> velocity=<-4, -1>
position=< 20366, -40177> velocity=<-2,  4>
position=< -9888,  -9919> velocity=< 1,  1>
position=<-19998,  40511> velocity=< 2, -4>
position=< 50608,  40516> velocity=<-5, -4>
position=< 10263,  40520> velocity=<-1, -4>
position=< 40521, -40171> velocity=<-4,  4>
position=< 30427, -20005> velocity=<-3,  2>
position=< 20333,  -9916> velocity=<-2,  1>
position=< -9909,  -9913> velocity=< 1,  1>
position=< 50628,  40511> velocity=<-5, -4>
position=< 50610,  30430> velocity=<-5, -3>
position=<-50248,  30433> velocity=< 5, -3>
position=< 50612,  50599> velocity=<-5, -5>
position=<-50253, -40170> velocity=< 5,  4>
position=< -9880,  40513> velocity=< 1, -4>
position=< 20362,  10256> velocity=<-2, -1>
position=< -9877, -30087> velocity=< 1,  3>
position=<-40182, -30082> velocity=< 4,  3>
position=<-50240, -20003> velocity=< 5,  2>
position=<-40138,  10255> velocity=< 4, -1>
position=<-50221,  20348> velocity=< 5, -2>
position=< -9896,  -9917> velocity=< 1,  1>
position=<-50209,  40516> velocity=< 5, -4>
position=< 20352,  50602> velocity=<-2, -5>
position=< 50607, -19998> velocity=<-5,  2>
position=<-19995, -30087> velocity=< 2,  3>
position=<-20003,  40517> velocity=< 2, -4>
position=<-50219,  30431> velocity=< 5, -3>
position=< 40521, -20001> velocity=<-4,  2>
position=<-30036,  20339> velocity=< 3, -2>
position=< 50624,  10257> velocity=<-5, -1>
position=<-50224,  40517> velocity=< 5, -4>
position=< -9907,  20344> velocity=< 1, -2>
position=< 40534, -40169> velocity=<-4,  4>
position=<-30065, -20003> velocity=< 3,  2>
position=< -9922,  20339> velocity=< 1, -2>
position=<-30052,  50602> velocity=< 3, -5>
position=< 10276, -50263> velocity=<-1,  5>
position=< 50594,  10258> velocity=<-5, -1>
position=< -9876,  10258> velocity=< 1, -1>
position=<-20001, -30091> velocity=< 2,  3>
position=<-50253,  50602> velocity=< 5, -5>
position=<-40159, -20002> velocity=< 4,  2>
position=<-50224, -30091> velocity=< 5,  3>
position=<-20001,  40511> velocity=< 2, -4>
position=< 20357, -40173> velocity=<-2,  4>
position=< 50615,  10255> velocity=<-5, -1>
position=< -9877, -50254> velocity=< 1,  5>
position=< 30440,  40516> velocity=<-3, -4>
position=< 30427,  50605> velocity=<-3, -5>
position=< 30419, -30090> velocity=<-3,  3>
position=< 20376, -20001> velocity=<-2,  2>
position=< 10255,  20344> velocity=<-1, -2>
position=< 30419,  20344> velocity=<-3, -2>
position=< 50595, -40169> velocity=<-5,  4>
position=<-30081,  40513> velocity=< 3, -4>
position=<-40143, -30090> velocity=< 4,  3>
position=< 40553,  20344> velocity=<-4, -2>
position=< 40529, -40170> velocity=<-4,  4>
position=< 30427, -50262> velocity=<-3,  5>
position=<-50240, -19996> velocity=< 5,  2>
position=<-50245, -30090> velocity=< 5,  3>
position=< 30448, -30087> velocity=<-3,  3>
position=< -9875, -40171> velocity=< 1,  4>
position=< -9900,  50599> velocity=< 1, -5>
position=<-19954, -40168> velocity=< 2,  4>
position=< 40526,  40518> velocity=<-4, -4>
position=<-20011,  30428> velocity=< 2, -3>
position=< 10283,  10257> velocity=<-1, -1>
position=<-40175,  40520> velocity=< 4, -4>
position=< 50636,  -9915> velocity=<-5,  1>
position=< -9904,  10255> velocity=< 1, -1>
position=< 30435,  40520> velocity=<-3, -4>
position=< 30424, -50254> velocity=<-3,  5>
position=< 20393,  50602> velocity=<-2, -5>
position=<-50261, -30083> velocity=< 5,  3>
position=<-30065,  10254> velocity=< 3, -1>
position=<-30052, -40177> velocity=< 3,  4>
position=< 50625, -50263> velocity=<-5,  5>
position=<-40142, -20001> velocity=< 4,  2>
position=< 20338, -19996> velocity=<-2,  2>
position=< 50599,  50604> velocity=<-5, -5>
position=< 40534, -40176> velocity=<-4,  4>
position=<-50235,  20339> velocity=< 5, -2>
position=<-30068,  -9918> velocity=< 3,  1>
position=<-40173,  20339> velocity=< 4, -2>
position=<-30054,  -9915> velocity=< 3,  1>
position=< 10255,  20348> velocity=<-1, -2>
position=<-40162,  40520> velocity=< 4, -4>
position=<-40158,  -9918> velocity=< 4,  1>
position=< 40508,  20348> velocity=<-4, -2>
position=< 10307, -40177> velocity=<-1,  4>
position=< 40545, -50261> velocity=<-4,  5>
position=<-30073, -40172> velocity=< 3,  4>
position=<-50209,  -9918> velocity=< 5,  1>
position=< -9913,  40515> velocity=< 1, -4>
position=< -9873, -50262> velocity=< 1,  5>
position=< -9877,  10261> velocity=< 1, -1>
position=<-50245, -30084> velocity=< 5,  3>
position=< 30440,  50606> velocity=<-3, -5>
position=<-40167,  40514> velocity=< 4, -4>
position=<-30076, -50255> velocity=< 3,  5>
position=< -9891, -19996> velocity=< 1,  2>
position=< -9877,  20340> velocity=< 1, -2>
position=< 20365,  -9911> velocity=<-2,  1>
position=<-50256,  10253> velocity=< 5, -1>
position=< -9909, -19996> velocity=< 1,  2>
position=< 30479,  -9919> velocity=<-3,  1>
position=<-30065,  10257> velocity=< 3, -1>
position=< 50652,  -9919> velocity=<-5,  1>
position=< 20338,  -9914> velocity=<-2,  1>
position=<-30062,  20339> velocity=< 3, -2>
position=< 20360,  10259> velocity=<-2, -1>
position=< 40537,  50604> velocity=<-4, -5>
position=<-50221,  50603> velocity=< 5, -5>
position=< 40505, -30090> velocity=<-4,  3>
position=< -9890,  20339> velocity=< 1, -2>
position=<-30097, -50261> velocity=< 3,  5>
position=<-19995, -30086> velocity=< 2,  3>
position=< 20341,  10255> velocity=<-2, -1>
position=<-19977, -20005> velocity=< 2,  2>
position=<-30053, -50259> velocity=< 3,  5>
position=<-30065, -40173> velocity=< 3,  4>
position=< 50617,  50601> velocity=<-5, -5>
position=< 50631, -40171> velocity=<-5,  4>
position=< -9925,  -9915> velocity=< 1,  1>
position=<-40150,  10262> velocity=< 4, -1>
position=< 40526,  40516> velocity=<-4, -4>
position=<-30055,  -9915> velocity=< 3,  1>
position=<-50264,  30432> velocity=< 5, -3>
position=< 10287, -20003> velocity=<-1,  2>
position=< 40534,  20348> velocity=<-4, -2>
position=<-19960, -19998> velocity=< 2,  2>
position=< 30464, -40173> velocity=<-3,  4>
position=<-50220, -50259> velocity=< 5,  5>
position=< 40537,  -9919> velocity=<-4,  1>
position=< 20357,  20346> velocity=<-2, -2>
position=< 40510,  50598> velocity=<-4, -5>
position=< 50607, -40172> velocity=<-5,  4>
position=< 40537, -19996> velocity=<-4,  2>
position=< 50636,  10261> velocity=<-5, -1>
position=< -9896,  30425> velocity=< 1, -3>
position=< -9917,  10255> velocity=< 1, -1>
position=<-50248,  50606> velocity=< 5, -5>
position=<-50237,  -9919> velocity=< 5,  1>
position=<-30073, -20005> velocity=< 3,  2>
position=< 40529,  50606> velocity=<-4, -5>
position=< 50650, -30082> velocity=<-5,  3>
position=<-30093,  10258> velocity=< 3, -1>
position=< 30456, -40177> velocity=<-3,  4>
position=< 40521, -40170> velocity=<-4,  4>
position=< 30468,  10257> velocity=<-3, -1>
position=< 10276, -50261> velocity=<-1,  5>
position=< 30421,  -9919> velocity=<-3,  1>
position=< -9877,  20346> velocity=< 1, -2>
position=< 10258, -40177> velocity=<-1,  4>
position=<-50264,  40516> velocity=< 5, -4>
position=< -9883, -40173> velocity=< 1,  4>
position=<-40127, -50256> velocity=< 4,  5>
position=< -9885,  20343> velocity=< 1, -2>
position=< 20382,  -9914> velocity=<-2,  1>
position=<-30076, -19998> velocity=< 3,  2>
position=<-30073,  50601> velocity=< 3, -5>
position=< -9893,  20345> velocity=< 1, -2>
position=< -9904,  10258> velocity=< 1, -1>
position=< 20393, -40171> velocity=<-2,  4>
position=<-19984,  50603> velocity=< 2, -5>
position=< -9889,  20343> velocity=< 1, -2>
position=<-19982,  40512> velocity=< 2, -4>
position=<-20009, -40168> velocity=< 2,  4>
position=<-30069, -19997> velocity=< 3,  2>
position=<-19987, -30085> velocity=< 2,  3>
position=< 10252,  10259> velocity=<-1, -1>
position=< -9917,  30428> velocity=< 1, -3>
position=< 10287,  20342> velocity=<-1, -2>
position=<-50245, -20000> velocity=< 5,  2>
position=<-40165, -40177> velocity=< 4,  4>
position=<-40135, -50262> velocity=< 4,  5>
position=<-19984, -30085> velocity=< 2,  3>
position=< 30428, -30091> velocity=<-3,  3>
position=<-30089,  30431> velocity=< 3, -3>
position=< 30467,  20344> velocity=<-3, -2>
position=<-19987,  40520> velocity=< 2, -4>
position=<-30037,  40512> velocity=< 3, -4>
position=< 40557, -50255> velocity=<-4,  5>
position=< 40550,  10254> velocity=<-4, -1>
position=<-40159,  10258> velocity=< 4, -1>
position=< 40539,  20343> velocity=<-4, -2>
position=< 30440,  50605> velocity=<-3, -5>
position=< 30453,  30434> velocity=<-3, -3>
position=< 40550, -30088> velocity=<-4,  3>
position=<-40151,  10256> velocity=< 4, -1>
position=< 10276,  40514> velocity=<-1, -4>
position=< 10280,  20348> velocity=<-1, -2>
position=<-20009, -30091> velocity=< 2,  3>
position=< 30467,  50601> velocity=<-3, -5>
position=< 30439, -20000> velocity=<-3,  2>
position=< 10276, -20005> velocity=<-1,  2>
position=< 40562, -30082> velocity=<-4,  3>
position=<-19986, -20004> velocity=< 2,  2>
position=< 20333,  10259> velocity=<-2, -1>
position=<-50224,  -9911> velocity=< 5,  1>
position=< -9872,  -9919> velocity=< 1,  1>
position=< 10295, -30085> velocity=<-1,  3>
position=<-19990,  30429> velocity=< 2, -3>
position=< 10295, -30084> velocity=<-1,  3>
position=< 30429,  40515> velocity=<-3, -4>
position=< 20365, -30086> velocity=<-2,  3>
position=< 50618,  10258> velocity=<-5, -1>
position=<-20010,  -9910> velocity=< 2,  1>
position=< 20373, -40169> velocity=<-2,  4>
position=< 10307, -50261> velocity=<-1,  5>
position=< 20381,  10256> velocity=<-2, -1>
position=< 40513,  40517> velocity=<-4, -4>
position=< -9865,  20345> velocity=< 1, -2>
position=< -9909,  20347> velocity=< 1, -2>
position=< 10284,  20348> velocity=<-1, -2>
position=<-30073,  20342> velocity=< 3, -2>
position=<-30078,  30425> velocity=< 3, -3>
position=< -9899,  20342> velocity=< 1, -2>
position=< 20333,  30429> velocity=<-2, -3>
position=< 10306,  10253> velocity=<-1, -1>
position=<-50261,  10260> velocity=< 5, -1>
position=< 30459,  -9912> velocity=<-3,  1>
position=< 10292, -40176> velocity=<-1,  4>
position=< 20389, -30083> velocity=<-2,  3>
position=<-40166,  20340> velocity=< 4, -2>
position=< -9901,  20345> velocity=< 1, -2>
position=< 40557, -20004> velocity=<-4,  2>
position=<-40158, -30090> velocity=< 4,  3>
position=<-50209,  10255> velocity=< 5, -1>
position=<-50265, -40172> velocity=< 5,  4>
position=<-50245,  50605> velocity=< 5, -5>
position=< 30443, -40177> velocity=<-3,  4>
position=< -9916,  20339> velocity=< 1, -2>
position=< 50640,  50601> velocity=<-5, -5>
position=<-19971, -20005> velocity=< 2,  2>
position=< 40522,  -9914> velocity=<-4,  1>
position=< 50607, -19999> velocity=<-5,  2>
position=<-50243,  40515> velocity=< 5, -4>
position=<-50240,  10260> velocity=< 5, -1>
position=< 40561, -19998> velocity=<-4,  2>
position=<-50211, -50254> velocity=< 5,  5>
position=<-40143,  30431> velocity=< 4, -3>
position=< 30430, -50259> velocity=<-3,  5>
position=< 30479, -20002> velocity=<-3,  2>
position=<-30092,  20344> velocity=< 3, -2>
position=<-30092, -40168> velocity=< 3,  4>
position=< 50601,  10257> velocity=<-5, -1>
position=< 20373,  40515> velocity=<-2, -4>
position=< 30479, -19997> velocity=<-3,  2>
position=<-40175,  50605> velocity=< 4, -5>
position=< -9880, -40173> velocity=< 1,  4>
position=< 20349, -50255> velocity=<-2,  5>
position=< 20362,  -9914> velocity=<-2,  1>
position=<-30089,  50601> velocity=< 3, -5>
position=< 30467,  10253> velocity=<-3, -1>
position=< 40565,  30429> velocity=<-4, -3>
position=<-40142,  10257> velocity=< 4, -1>
position=< 50609, -50263> velocity=<-5,  5>
position=< -9881, -40173> velocity=< 1,  4>
position=< 50639,  40515> velocity=<-5, -4>
position=<-50269, -40170> velocity=< 5,  4>
position=< 40553,  -9910> velocity=<-4,  1>
position=< 30455,  30434> velocity=<-3, -3>
position=< 20362,  10258> velocity=<-2, -1>
position=< 40505,  50603> velocity=<-4, -5>
position=<-19990,  10260> velocity=< 2, -1>
position=< 30447, -19998> velocity=<-3,  2>
position=<-40150, -30087> velocity=< 4,  3>
position=< -9907, -40172> velocity=< 1,  4>
position=<-30044,  20348> velocity=< 3, -2>
position=<-40178,  -9913> velocity=< 4,  1>
position=<-50261,  30428> velocity=< 5, -3>
position=<-40151,  20348> velocity=< 4, -2>
position=<-50224,  30432> velocity=< 5, -3>
position=< 50652, -50263> velocity=<-5,  5>
position=<-19952,  50606> velocity=< 2, -5>
position=< 30431,  40511> velocity=<-3, -4>
position=< 30459, -30088> velocity=<-3,  3>
position=< 50651,  20347> velocity=<-5, -2>
position=< 10292, -30082> velocity=<-1,  3>
position=< 20366,  10257> velocity=<-2, -1>
position=<-19987,  -9913> velocity=< 2,  1>
position=< -9865, -40170> velocity=< 1,  4>
position=< -9889,  50597> velocity=< 1, -5>
position=<-30065, -50262> velocity=< 3,  5>
position=< -9921,  20347> velocity=< 1, -2>
position=<-30084,  10253> velocity=< 3, -1>
position=< 10248, -20005> velocity=<-1,  2>
position=< 20345,  -9915> velocity=<-2,  1>
position=< -9882,  -9915> velocity=< 1,  1>
position=<-30065,  50602> velocity=< 3, -5>
position=< 40565,  50599> velocity=<-4, -5>
position=< 20349, -50261> velocity=<-2,  5>
position=<-19960, -19998> velocity=< 2,  2>
position=< 10255, -50258> velocity=<-1,  5>
position=< -9901, -50255> velocity=< 1,  5>
position=<-50219,  -9916> velocity=< 5,  1>
position=< 40524, -30086> velocity=<-4,  3>
position=< 40550,  50600> velocity=<-4, -5>
position=<-50233, -30091> velocity=< 5,  3>
position=< 30440, -50257> velocity=<-3,  5>
position=< -9920,  50605> velocity=< 1, -5>
position=< 40507,  20339> velocity=<-4, -2>
position=< 10264,  30426> velocity=<-1, -3>
position=< 40556,  20341> velocity=<-4, -2>
position=< -9875,  -9913> velocity=< 1,  1>
position=<-30068, -50254> velocity=< 3,  5>
position=< -9889,  30425> velocity=< 1, -3>
position=<-20011, -40172> velocity=< 2,  4>
position=<-50269,  10259> velocity=< 5, -1>
position=<-40132,  30432> velocity=< 4, -3>
position=< 40553,  -9913> velocity=<-4,  1>
position=<-30073,  10256> velocity=< 3, -1>
position=<-30092,  20340> velocity=< 3, -2>
position=< 40542,  50606> velocity=<-4, -5>
position=<-50224,  20347> velocity=< 5, -2>
position=<-40143,  50606> velocity=< 4, -5>
position=<-19971, -20000> velocity=< 2,  2>
position=< 40553,  20340> velocity=<-4, -2>
position=<-30081, -20001> velocity=< 3,  2>
position=<-30037, -40172> velocity=< 3,  4>
position=< -9865,  30428> velocity=< 1, -3>
position=< 30479,  20340> velocity=<-3, -2>
position=< 30429,  20343> velocity=<-3, -2>
position=<-19971, -40172> velocity=< 2,  4>
position=< 30431,  50601> velocity=<-3, -5>
position=<-19982,  10256> velocity=< 2, -1>
position=< 20344,  20343> velocity=<-2, -2>""".splitlines()


class Point:
    def __init__(self, line):
        matches = re.match(r"position=< *?(-?\d+), *?(-?\d+)> velocity=< *?(-?\d+), *?(-?\d+)>", line)

        self.xpos = int(matches.group(1))
        self.ypos = int(matches.group(2))
        self.xvel = int(matches.group(3))
        self.yvel = int(matches.group(4))

    def tick(self):
        self.xpos += self.xvel
        self.ypos += self.yvel


points = [Point(line) for line in data]

min_area = 99999999999999999
min_list = None
min_pos = None
min_time = 0
time = 0
for _ in range(0, 100000):
    min_x = min(points, key=lambda p: p.xpos).xpos
    max_x = max(points, key=lambda p: p.xpos).xpos
    min_y = min(points, key=lambda p: p.ypos).ypos
    max_y = max(points, key=lambda p: p.ypos).ypos
    area = (max_x - min_x) * (max_y - min_y)
    if area < min_area:
        min_area = area
        min_list = copy.deepcopy(points)
        min_pos = min_x, min_y, max_x, max_y
        min_time = time

    time += 1
    for point in points:
        point.tick()

print(min_area)
print(min_pos)

for y in range(min_pos[1], min_pos[3] + 1):
    for x in range(min_pos[0], min_pos[2] + 1):
        if any(p.xpos == x and p.ypos == y for p in min_list):
            print("#", end="")
        else:
            print(".", end="")
    print()

print("Time:", min_time)
