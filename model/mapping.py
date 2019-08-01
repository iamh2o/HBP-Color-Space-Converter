from typing import Dict, List
PixelMap = Dict[int, List[int]]

# This cell -> pixels mapping is created from an old version, but it should produce something.                             
def demo_triangle_mapping() -> PixelMap:
    return {
0: [1051,1052,1053,1054,1055,1056,1057,1058],
1: [1018,1019,1020,1021,1022,1023,1024,1025],
2: [1050,1051,1052,1053,1054,1055,1056,1057],
3: [1026,1027,1028,1029,1030,1031,1032,1033],
4: [969,970,971,972,973,974,975,976],
5: [1017,1018,1019,1020,1021,1022,1023,1024],
6: [977,978,979,980,981,982,983,984],
7: [1025,1026,1027,1028,1029,1030,1031,1032],
8: [985,986,987,988,989,990,991,992],
9: [904,905,906,907,908,909,910,911],
10: [968,969,970,971,972,973,974,975],
11: [912,913,914,915,916,917,918,919],
12: [976,977,978,979,980,981,982,983],
13: [920,921,922,923,924,925,926,927],
14: [984,985,986,987,988,989,990,991],
15: [928,929,930,931,932,933,934,935],
16: [823,824,825,826,827,828,829,830],
17: [903,904,905,906,907,908,909,910],
18: [831,832,833,834,835,836,837,838],
19: [911,912,913,914,915,916,917,918],
20: [839,840,841,842,843,844,845,846],
21: [919,920,921,922,923,924,925,926],
22: [847,848,849,850,851,852,853,854],
23: [927,928,929,930,931,932,933,934],
24: [855,856,857,858,859,860,861,862],
25: [726,727,728,729,730,731,732,733],
26: [822,823,824,825,826,827,828,829],
27: [734,735,736,737,738,739,740,741],
28: [830,831,832,833,834,835,836,837],
29: [742,743,744,745,746,747,748,749],
30: [838,839,840,841,842,843,844,845],
31: [750,751,752,753,754,755,756,757],
32: [846,847,848,849,850,851,852,853],
33: [758,759,760,761,762,763,764,765],
34: [854,855,856,857,858,859,860,861],
35: [766,767,768,769,770,771,772,773],
36: [613,614,615,616,617,618,619,620],
37: [725,726,727,728,729,730,731,732],
38: [621,622,623,624,625,626,627,628],
39: [733,734,735,736,737,738,739,740],
40: [629,630,631,632,633,634,635,636],
41: [741,742,743,744,745,746,747,748],
42: [637,638,639,640,641,642,643,644],
43: [749,750,751,752,753,754,755,756],
44: [645,646,647,648,649,650,651,652],
45: [757,758,759,760,761,762,763,764],
46: [653,654,655,656,657,658,659,660],
47: [765,766,767,768,769,770,771,772],
48: [661,662,663,664,665,666,667,668],
49: [484,485,486,487,488,489,490,491],
50: [612,613,614,615,616,617,618,619],
51: [492,493,494,495,496,497,498,499],
52: [620,621,622,623,624,625,626,627],
53: [500,501,502,503,504,505,506,507],
54: [628,629,630,631,632,633,634,635],
55: [508,509,510,511,512,513,514,515],
56: [636,637,638,639,640,641,642,643],
57: [516,517,518,519,520,521,522,523],
58: [644,645,646,647,648,649,650,651],
59: [524,525,526,527,528,529,530,531],
60: [652,653,654,655,656,657,658,659],
61: [532,533,534,535,536,537,538,539],
62: [660,661,662,663,664,665,666,667],
63: [540,541,542,543,544,545,546,547],
64: [339,340,341,342,343,344,345,346],
65: [483,484,485,486,487,488,489,490],
66: [347,348,349,350,351,352,353,354],
67: [491,492,493,494,495,496,497,498],
68: [355,356,357,358,359,360,361,362],
69: [499,500,501,502,503,504,505,506],
70: [363,364,365,366,367,368,369,370],
71: [507,508,509,510,511,512,513,514],
72: [371,372,373,374,375,376,377,378],
73: [515,516,517,518,519,520,521,522],
74: [379,380,381,382,383,384,385,386],
75: [523,524,525,526,527,528,529,530],
76: [387,388,389,390,391,392,393,394],
77: [531,532,533,534,535,536,537,538],
78: [395,396,397,398,399,400,401,402],
79: [539,540,541,542,543,544,545,546],
80: [403,404,405,406,407,408,409,410],
81: [178,179,180,181,182,183,184,185],
82: [338,339,340,341,342,343,344,345],
83: [186,187,188,189,190,191,192,193],
84: [346,347,348,349,350,351,352,353],
85: [194,195,196,197,198,199,200,201],
86: [354,355,356,357,358,359,360,361],
87: [202,203,204,205,206,207,208,209],
88: [362,363,364,365,366,367,368,369],
89: [210,211,212,213,214,215,216,217],
90: [370,371,372,373,374,375,376,377],
91: [218,219,220,221,222,223,224,225],
92: [378,379,380,381,382,383,384,385],
93: [226,227,228,229,230,231,232,233],
94: [386,387,388,389,390,391,392,393],
95: [234,235,236,237,238,239,240,241],
96: [394,395,396,397,398,399,400,401],
97: [242,243,244,245,246,247,248,249],
98: [402,403,404,405,406,407,408,409],
99: [250,251,252,253,254,255,256,257],
100: [1,2,3,4,5,6,7,8],
101: [177,178,179,180,181,182,183,184],
102: [9,10,11,12,13,14,15,16],
103: [185,186,187,188,189,190,191,192],
104: [17,18,19,20,21,22,23,24],
105: [193,194,195,196,197,198,199,200],
106: [25,26,27,28,29,30,31,32],
107: [201,202,203,204,205,206,207,208],
108: [33,34,35,36,37,38,39,40],
109: [209,210,211,212,213,214,215,216],
110: [41,42,43,44,45,46,47,48],
111: [217,218,219,220,221,222,223,224],
112: [49,50,51,52,53,54,55,56],
113: [225,226,227,228,229,230,231,232],
114: [57,58,59,60,61,62,63,64],
115: [233,234,235,236,237,238,239,240],
116: [65,66,67,68,69,70,71,72],
117: [241,242,243,244,245,246,247,248],
118: [73,74,75,76,77,78,79,80],
119: [249,250,251,252,253,254,255,256],
120: [81,82,83,84,85,86,87,88]
}
