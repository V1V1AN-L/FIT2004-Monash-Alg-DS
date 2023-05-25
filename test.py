from assignment2 import *
import unittest

__author__ = "Angus Corr"


class Q1Test(unittest.TestCase):

    def test_provided(self):
        """
        Using test provided by problem sheet.
        """
        connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000),
                       (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]
        maxIn = [5000, 3000, 3000, 3000, 2000]
        maxOut = [5000, 3000, 3000, 2500, 1500]
        origin = 0
        targets = [4, 2]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 4500)

    def test_0(self):
        connections = [(0, 1, 10), (0, 2, 100), (1, 3, 50),
                       (2, 3, 50)]
        maxIn = [1, 60, 50, 7]
        maxOut = [1, 60, 50, 7]
        origin = 0
        targets = [3]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 1)

    def test_1(self):
        connections = [(0, 1, 10), (0, 2, 100), (1, 3, 50),
                       (2, 3, 50)]
        maxIn = [20, 60, 50, 7]
        maxOut = [20, 60, 50, 7]
        origin = 0
        targets = [3]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 7)

    def test_2(self):
        connections = [(0, 1, 10), (0, 2, 100), (1, 3, 50),
                       (2, 3, 50)]
        maxIn = [1, 60, 50, 7]
        maxOut = [20, 60, 50, 7]
        origin = 0
        targets = [3]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 7)

    def test_3(self):
        connections = [(0, 1, 20), (1, 2, 20)]
        maxIn = [20, 5, 20]
        maxOut = [20, 100, 20]
        origin = 0
        targets = [1]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 5)

    def test_4(self):
        connections = [(0, 1, 50), (1, 2, 20), (1, 3, 35)]
        maxIn = [60, 60, 10, 30]
        maxOut = [60, 50, 30, 2]
        origin = 0
        targets = [2, 3]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 40)

    def test_canada_roads_from_notes(self):
        connections = [(0, 1, 16), (1, 2, 12), (2, 3, 20), (4, 1, 4), (5, 2, 7), (0, 4, 13), (4, 5, 14), (5, 3, 4),
                       (5, 1, 9)]
        maxIn = [100] * len(connections)
        maxOut = [100] * len(connections)
        origin = 0
        targets = [3]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 23)

    def test_420_databases(self):
        connections = [(155, 393, 70), (19, 192, 51), (89, 116, 18), (79, 151, 65), (181, 393, 13), (146, 59, 36),
                       (127, 376, 78), (398, 271, 68), (222, 197, 77), (138, 47, 63), (209, 261, 60),
                       (106, 227, 100), (76, 146, 15), (387, 216, 91), (247, 375, 75), (66, 143, 21), (50, 123, 43),
                       (157, 3, 34), (321, 414, 91), (109, 416, 95), (196, 407, 65), (221, 372, 98), (247, 336, 83),
                       (97, 227, 16), (256, 143, 59), (389, 229, 86), (406, 86, 49), (292, 231, 43), (134, 218, 73),
                       (95, 106, 70), (204, 412, 58), (393, 155, 50), (212, 51, 89), (340, 232, 28), (363, 61, 41),
                       (264, 346, 28),
                       (385, 362, 96), (160, 149, 74), (263, 54, 14), (101, 114, 21), (100, 388, 70), (273, 78, 46),
                       (329, 145, 37), (211, 115, 25), (368, 152, 65), (45, 38, 44), (347, 205, 27), (159, 361, 4),
                       (50, 409, 99), (168, 70, 74), (374, 59, 99), (177, 229, 43), (60, 30, 42), (159, 352, 49),
                       (323, 363, 64), (344, 171, 14), (325, 367, 36), (147, 254, 97), (176, 66, 86), (76, 177, 96),
                       (123, 145, 95), (201, 129, 100), (396, 145, 2), (314, 222, 24), (85, 254, 14),
                       (119, 112, 22), (264, 27, 37), (98, 404, 25), (86, 54, 55), (295, 115, 14), (282, 111, 50),
                       (104, 33, 34), (77, 36, 70), (338, 263, 66),
                       (355, 77, 33), (6, 179, 81), (389, 370, 20), (392, 16, 86), (94, 162, 99), (243, 233, 19),
                       (36, 126, 95), (383, 381, 35), (394, 56, 43), (37, 233, 93), (297, 73, 79), (349, 175, 32),
                       (110, 24, 90), (39, 1, 69), (113, 34, 50), (213, 269, 84), (31, 236, 38), (288, 21, 50),
                       (269, 264, 54), (317, 153, 30), (368, 86, 100), (400, 361, 51), (52, 331, 81), (51, 145, 46),
                       (268, 352, 2), (73, 347, 69), (215, 134, 27), (13, 149, 82), (249, 45, 65), (412, 86, 35),
                       (158, 225, 97), (271, 119, 17), (403, 245, 21), (371, 418, 82), (180, 28, 89),
                       (243, 109, 64), (233, 122, 25), (21, 73, 45), (327, 113, 49),
                       (158, 201, 23), (7, 29, 27), (278, 353, 14), (383, 342, 65), (64, 263, 18), (151, 2, 23),
                       (15, 333, 88), (172, 348, 84), (43, 218, 88), (65, 386, 84), (192, 283, 55), (17, 220, 51),
                       (53, 415, 34),
                       (206, 0, 91), (39, 165, 37), (277, 86, 79), (127, 274, 5), (333, 72, 72), (67, 170, 71),
                       (0, 38, 48), (142, 261, 42), (143, 404, 58), (312, 284, 36), (82, 391, 79), (379, 168, 3),
                       (219, 383, 71),
                       (60, 359, 58), (59, 403, 97), (227, 137, 14), (193, 252, 48), (46, 7, 23), (283, 33, 57),
                       (130, 6, 44), (289, 370, 35), (183, 11, 33), (92, 335, 55), (390, 237, 75), (17, 75, 46),
                       (55, 14, 24), (249, 75, 65), (135, 374, 39), (190, 201, 94), (262, 42, 7), (148, 28, 75),
                       (270, 332, 39), (182, 402, 98), (241, 249, 36), (279, 376, 3), (96, 321, 32), (409, 112, 77),
                       (222, 316, 89), (366, 35, 90), (330, 124, 15), (357, 294, 67), (419, 413, 88),
                       (407, 309, 40), (166, 338, 37), (306, 188, 3), (220, 378, 8), (168, 229, 51), (74, 372, 88),
                       (38, 62, 29), (198, 403, 16), (145, 276, 36),
                       (254, 330, 47), (55, 195, 31), (407, 173, 44), (39, 169, 6), (258, 221, 81), (413, 240, 83),
                       (263, 219, 21), (90, 191, 57), (374, 7, 4), (187, 231, 75), (339, 380, 73), (358, 289, 77),
                       (345, 374, 76), (251, 310, 80), (216, 297, 6), (275, 320, 36), (272, 293, 31), (380, 92, 78),
                       (53, 239, 23), (141, 277, 64), (29, 160, 71), (122, 256, 7), (185, 145, 5), (24, 122, 73),
                       (405, 305, 18), (14, 96, 88), (106, 374, 43), (285, 366, 95), (286, 315, 74), (78, 215, 59),
                       (60, 158, 8), (33, 63, 70), (193, 361, 84), (293, 101, 15), (414, 25, 25), (214, 377, 72),
                       (337, 175, 16), (16, 392, 17), (27, 362, 68),
                       (2, 1, 44), (47, 112, 99), (63, 215, 25), (167, 153, 75), (342, 316, 26), (25, 340, 41),
                       (214, 244, 73), (68, 155, 59), (139, 123, 64), (188, 33, 59), (30, 259, 15), (307, 184, 11),
                       (160, 179, 97), (373, 96, 6), (302, 415, 5), (85, 339, 18), (69, 335, 12), (198, 286, 24),
                       (356, 348, 97), (8, 72, 76), (115, 154, 87), (224, 306, 17), (383, 350, 17), (179, 296, 23),
                       (133, 210, 98), (353, 222, 95), (415, 362, 96), (174, 72, 29), (54, 58, 26), (314, 394, 83),
                       (26, 147, 35), (170, 324, 10), (79, 189, 100), (104, 386, 68), (32, 374, 32), (417, 183, 68),
                       (101, 373, 15), (412, 272, 34), (384, 63, 31),
                       (170, 83, 78), (261, 38, 63), (165, 42, 5), (75, 393, 13), (116, 278, 89), (364, 240, 85),
                       (179, 68, 20), (28, 344, 25), (9, 141, 60), (305, 367, 98), (41, 315, 70), (71, 188, 89),
                       (208, 279, 18), (187, 48, 69), (103, 219, 32), (396, 202, 14), (3, 47, 100), (112, 206, 66),
                       (372, 320, 2), (22, 40, 84), (250, 46, 10), (125, 402, 69), (371, 19, 51), (362, 222, 16),
                       (108, 386, 22), (347, 160, 19), (255, 261, 55), (354, 401, 19), (140, 189, 70),
                       (388, 49, 41), (132, 172, 93), (353, 317, 66), (5, 204, 89), (49, 391, 5), (185, 316, 97),
                       (110, 259, 11), (403, 29, 38), (1, 171, 7), (305, 296, 42),
                       (375, 227, 32), (300, 170, 11), (234, 343, 95), (280, 51, 12), (281, 90, 54), (365, 336, 21),
                       (139, 306, 3), (133, 322, 23), (81, 323, 72), (83, 332, 43), (235, 56, 14),
                       (378, 272, 12), (16, 137, 80), (11, 21, 32), (100, 248, 48), (145, 327, 80), (397, 184, 39),
                       (124, 33, 65), (238, 259, 74), (325, 22, 37), (386, 86, 29), (4, 109, 63), (236, 168, 1),
                       (274, 38, 28), (228, 338, 68), (40, 147, 99), (313, 172, 21), (226, 231, 39), (283, 228, 81),
                       (246, 69, 43), (282, 233, 57), (253, 130, 76), (282, 256, 31), (257, 333, 46), (70, 312, 15),
                       (359, 411, 35), (339, 140, 62), (53, 237, 55), (301, 388, 71), (42, 383, 66), (285, 127, 35),
                       (276, 361, 7), (112, 301, 46), (35, 200, 84), (194, 83, 67), (231, 46, 50), (152, 317, 57),
                       (271, 100, 44), (87, 248, 74),
                       (382, 166, 93), (385, 338, 11), (141, 96, 66), (157, 128, 58), (357, 60, 94), (102, 71, 16),
                       (370, 317, 51), (329, 182, 47), (328, 286, 3), (205, 308, 15), (248, 13, 45), (163, 419, 42),
                       (402, 375, 9), (297, 177, 54), (319, 347, 62), (48, 229, 47), (386, 58, 91), (156, 326, 51),
                       (162, 386, 96), (290, 17, 64), (331, 47, 44), (26, 12, 15), (81, 160, 67), (232, 217, 82),
                       (280, 413, 66), (244, 65, 61), (175, 82, 69), (315, 32, 10), (322, 207, 57), (223, 173, 35),
                       (57, 371, 39), (60, 376, 16), (63, 278, 65), (126, 418, 24), (171, 21, 19), (295, 149, 41),
                       (410, 399, 29), (262, 384, 71),
                       (105, 304, 85), (299, 391, 79), (136, 228, 64), (268, 225, 85), (107, 220, 12),
                       (230, 298, 1), (185, 324, 90), (308, 184, 79), (172, 389, 92), (317, 27, 50), (371, 188, 82),
                       (88, 164, 93), (242, 20, 78), (10, 183, 4), (361, 78, 75), (384, 91, 63), (408, 298, 48),
                       (154, 226, 15), (320, 397, 21), (114, 300, 54), (360, 361, 13), (304, 293, 31),
                       (93, 120, 52), (332, 224, 26), (37, 18, 18), (399, 310, 100), (291, 238, 65), (296, 199, 99),
                       (247, 54, 3), (120, 290, 50), (355, 9, 21), (218, 74, 48), (84, 37, 42), (156, 381, 98),
                       (311, 348, 71), (54, 135, 30), (225, 68, 1), (90, 417, 27),
                       (265, 201, 49), (260, 382, 89), (153, 39, 72), (410, 150, 56), (202, 112, 25),
                       (267, 401, 14), (331, 138, 31), (41, 312, 74), (409, 200, 53), (58, 333, 6), (286, 61, 63),
                       (298, 97, 4), (61, 364, 34), (22, 302, 4), (178, 257, 70), (322, 181, 17), (169, 236, 61),
                       (121, 176, 37), (44, 22, 60), (12, 44, 85), (358, 207, 24), (309, 126, 65), (346, 87, 22),
                       (411, 92, 60), (67, 245, 67), (137, 291, 32), (387, 382, 82), (351, 238, 46), (367, 246, 59),
                       (217, 339, 13), (36, 140, 80), (274, 286, 91), (343, 337, 2), (418, 214, 77), (350, 282, 31),
                       (303, 319, 56), (266, 314, 74), (27, 135, 43), (38, 145, 35),
                       (164, 76, 27), (416, 200, 89), (195, 338, 3), (401, 180, 76), (35, 55, 45), (318, 137, 9),
                       (71, 186, 70), (118, 268, 1), (409, 217, 69), (220, 167, 96), (404, 286, 57), (111, 361, 7),
                       (34, 199, 78), (186, 418, 36), (376, 112, 10), (74, 224, 98), (209, 120, 16), (417, 106, 18),
                       (20, 332, 92), (148, 386, 14), (139, 28, 86), (203, 77, 23), (76, 128, 60), (255, 222, 37),
                       (312, 202, 94), (128, 90, 29), (138, 339, 13), (395, 408, 93), (259, 228, 45), (284, 37, 54),
                       (117, 340, 41), (56, 143, 16), (287, 356, 87), (348, 256, 92), (394, 12, 95), (336, 331, 55),
                       (126, 283, 39),
                       (140, 106, 85), (160, 176, 85), (147, 351, 74), (91, 346, 41), (324, 268, 44), (279, 315, 8),
                       (334, 205, 3), (210, 43, 61), (150, 21, 80), (99, 325, 93), (254, 148, 49), (156, 8, 52),
                       (326, 10, 34), (279, 212, 28), (150, 408, 44), (381, 75, 47), (391, 395, 73), (370, 49, 39),
                       (409, 71, 14), (208, 107, 35), (311, 96, 19), (18, 302, 38), (245, 372, 100), (239, 258, 84),
                       (297, 325, 30), (131, 67, 45), (144, 177, 27), (32, 301, 86), (252, 357, 31), (29, 163, 92),
                       (313, 317, 16), (316, 70, 19), (80, 58, 92), (369, 326, 82), (191, 111, 88), (131, 270, 1),
                       (189, 334, 85), (121, 108, 75),
                       (67, 205, 100), (377, 394, 7), (149, 140, 36), (237, 340, 85), (64, 115, 92), (314, 201, 49),
                       (352, 117, 80), (22, 333, 93), (110, 123, 23), (104, 274, 41), (266, 344, 41),
                       (220, 380, 18), (129, 165, 8), (98, 145, 78), (62, 293, 52), (162, 128, 88), (55, 354, 43),
                       (31, 387, 45), (132, 152, 47), (62, 244, 43), (161, 47, 60), (173, 244, 7), (168, 39, 21),
                       (41, 87, 61), (204, 282, 89), (215, 322, 41), (286, 87, 41), (23, 85, 38), (341, 352, 71),
                       (397, 416, 11), (161, 245, 44), (39, 387, 45), (22, 241, 90), (110, 199, 22), (45, 28, 19),
                       (311, 207, 25), (275, 334, 65), (270, 218, 93), (311, 4, 47),
                       (94, 114, 98), (199, 320, 94), (45, 85, 9), (175, 386, 93), (257, 279, 87), (72, 345, 60),
                       (160, 210, 95), (207, 288, 53), (417, 171, 63), (184, 222, 65), (294, 191, 8),
                       (335, 191, 71), (240, 49, 35), (229, 2, 20), (183, 171, 56), (339, 48, 94), (158, 263, 14),
                       (218, 225, 86), (418, 28, 15), (200, 160, 51), (101, 321, 95), (354, 329, 29),
                       (310, 126, 72), (197, 104, 36)]
        maxIn = [190, 588, 161, 80, 65, 517, 235, 369, 553, 413, 574, 548, 451, 472, 78, 509, 367, 78, 346, 425,
                 580, 279, 189, 418, 590, 471, 479, 314, 56, 584, 145, 68, 12, 38, 591, 233, 534, 70, 486, 249, 471,
                 564, 48, 386, 335, 498, 146, 496, 66, 296, 267, 173, 269, 328, 388, 81, 399, 110, 546, 244, 23,
                 338, 287, 77, 434, 548, 501, 207, 375, 14, 542, 319, 123, 573, 64, 247, 428, 386, 455, 118, 162,
                 254, 325, 231, 401, 497, 478, 305, 42, 305, 417, 54, 569, 151, 269, 383, 345, 397, 456, 559, 6,
                 200, 167, 266, 402, 66, 38, 125, 350, 392, 414, 465, 88, 240, 169, 153, 179, 107, 242, 407, 544,
                 108, 434, 534, 418, 488, 159, 255, 441, 305, 581, 576, 211, 308, 5, 63, 384, 99, 116, 360, 450, 86,
                 62, 437, 21, 25, 437, 535, 168, 168, 67, 575, 594, 344, 144, 222, 284, 82, 439, 55, 581, 307, 183,
                 135, 143, 334, 54, 342, 380, 447, 433, 476, 594, 106, 392, 472, 197, 365, 86, 239, 258, 357, 12,
                 333, 385, 526, 7, 402, 262, 63, 176, 42, 527, 410, 340, 256, 360, 25, 493, 126, 443, 433, 417, 344,
                 543, 330, 199, 377, 374, 574, 218, 234, 291, 277, 577, 134, 487, 358, 264, 440, 207, 315, 371, 88,
                 143, 343, 99, 44, 371, 32, 539, 356, 418, 55, 289, 276, 461, 426, 584, 81, 335, 526, 84, 133, 30,
                 143, 182, 70, 153, 219, 163, 363, 551, 574, 141, 224, 65, 87, 227, 86, 484, 572, 248, 444, 444,
                 520, 406, 234, 113, 537, 297, 442, 239, 526, 81, 327, 483, 532, 523, 162, 273, 391, 283, 273, 214,
                 350, 375, 193, 115, 539, 552, 379, 143, 95, 398, 487, 6, 465, 394, 304, 50, 501, 294, 215, 434,
                 426, 459, 204, 42, 272, 261, 20, 370, 247, 55, 186, 211, 159, 246, 485, 94, 293, 261, 544, 279,
                 103, 116, 206, 128, 493, 21, 250, 441, 115, 470, 129, 320, 10, 531, 268, 44, 459, 120, 41, 537, 59,
                 339, 599, 368, 445, 568, 282, 51, 167, 600, 153, 101, 320, 115, 519, 154, 26, 388, 357, 238,
                 488, 171, 90, 195, 391, 75, 165, 542, 559, 442, 467, 235, 325, 306, 258, 210, 342, 176, 397, 450,
                 190, 529, 384, 133, 440, 359, 462, 38, 297, 64, 231, 160, 484, 466, 304, 323, 188, 232, 331, 119,
                 357, 336, 330, 557, 395, 178, 443, 251, 506, 191, 329, 286, 596, 419, 6]
        maxOut = [365, 152, 415, 32, 358, 465, 134, 67, 20, 39, 101, 167, 597, 286, 225, 115, 569, 177, 390, 38, 76,
                  582, 33, 23, 267, 163, 540, 424, 405, 274, 153, 563, 263, 591, 334, 420, 47, 540, 505,
                  334, 379, 392, 310, 60, 186, 334, 214, 47, 572, 216, 462, 208, 103, 585, 288, 594, 433, 207, 328,
                  430, 274, 312, 370, 257, 442, 258, 394, 56, 239, 181, 98, 591, 426, 185, 180, 497, 291, 470, 385,
                  232, 209, 78, 134, 230, 232, 430, 167, 288, 525, 85, 216, 568, 352, 17, 585, 375, 308, 541, 435,
                  75, 166, 179, 520, 455, 122, 264, 528, 96, 219, 494, 204, 534, 353, 557, 553, 400, 193, 318, 579,
                  563, 401, 236, 85, 578, 223, 552, 119, 217, 193, 585, 202, 523, 304, 415, 498, 462, 494, 162, 416,
                  271, 548, 433, 60, 98, 135, 481, 440, 517, 393, 145, 531, 122, 490, 52, 427, 330, 549, 435, 182,
                  77, 381, 66, 202, 54, 336, 190, 34, 368, 476, 413, 388, 256, 19, 505, 292, 542, 221, 171, 176,
                  557, 124, 174, 111, 85, 27, 85, 270, 88, 579, 428, 504, 318, 53, 366, 527, 398, 128, 587, 58, 303,
                  521, 546, 503, 148, 364, 353, 546, 17, 57, 133, 202, 471, 90, 552, 148, 179, 566, 9, 235, 409,
                  134, 578, 579, 74, 277, 67, 289, 206, 133, 550, 526, 217, 418, 380, 180, 362, 288, 432, 400, 410,
                  79, 10, 114, 374, 189, 96, 198, 84, 211, 581, 401, 166, 88, 181, 407, 479, 537, 194, 234, 263,
                  406, 15, 331, 90, 107, 326, 417, 102, 370, 188, 92, 113, 5, 123, 526, 199, 176, 272, 482, 178,
                  560, 508, 171, 25, 282, 526, 465, 580, 598, 528, 433, 369, 559, 95, 476, 544, 247, 440, 276, 525,
                  26, 113, 296, 186, 517, 109, 217, 360, 468, 530, 161, 526, 173, 59, 233, 304, 88, 175, 315, 503,
                  497, 14, 186, 191, 568, 385, 579, 520, 474, 422, 86, 299, 477, 69, 175, 229, 148, 389, 65, 236,
                  79, 68, 137, 266, 171, 555, 381, 268, 532, 52, 67, 430, 58, 75, 240, 159, 397, 281, 156, 234, 391,
                  159, 393, 69,
                  173, 77, 457, 56, 366, 587, 65, 543, 596, 240, 579, 574, 33, 253, 130, 517, 8, 255, 360, 349, 391,
                  149, 475, 23, 575, 466, 480, 358, 471, 200, 214, 257, 578, 166, 414, 247, 563, 97, 312, 7, 305,
                  275, 202, 98, 20, 341, 234, 515, 444, 8, 41, 466, 158, 56, 117, 248]
        origin = 143
        targets = [277, 294, 249, 347, 400, 406, 202, 151, 148, 373, 408, 271, 378, 39, 62, 167, 119, 310, 100, 309,
                   272, 160, 399, 257, 49, 71, 15, 231, 368, 64, 210, 365, 193, 356, 108, 304, 50, 258, 223, 168,
                   37, 134, 254, 158, 247, 232, 411, 183, 184, 121, 120, 289, 263, 192, 351, 412, 128, 334, 314, 77,
                   205, 93, 70, 403, 198, 383, 330, 129, 146, 161, 269, 369, 335, 360, 152, 390, 221, 248, 109, 230,
                   336, 233, 362, 191, 91, 349, 395, 150, 33, 244, 87, 270, 118, 407, 388, 350, 224, 220, 371, 110,
                   380, 242, 419, 107, 136, 363, 355, 332, 86, 42, 417, 130, 354, 153, 96, 122, 280, 43, 245,
                   327, 10, 32, 173, 172, 53, 262, 126, 311, 213, 0, 16, 397, 26, 115, 387, 203, 361, 357, 305, 344,
                   66, 237, 75, 404, 51, 35, 296, 246, 13, 94, 170, 14, 79, 329, 104, 18, 401, 331, 315, 98, 392,
                   275, 80, 381, 320]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 58)
    def test_731623(self):
        connections = [(15, 18, 559), (13, 8, 920), (19, 14, 341), (25, 5, 425), (10, 15, 348), (18, 17, 597), (21, 1, 562), (20, 14, 959), (5, 4, 740), (2, 7, 300), (7, 4, 617), (6, 7, 509), (24, 21, 415), (5, 12, 338), (15, 12, 890), (3, 8, 895), (16, 7, 357), (16, 13, 818), (16, 23, 478), (7, 5, 627), (17, 9, 740), (1, 18, 452), (22, 10, 967), (23, 8, 881), (17, 0, 301), (25, 12, 326), (3,
    22, 262), (13, 7, 554), (8, 12, 472), (17, 15, 786), (13, 26, 576), (12, 6, 980), (7, 27, 736), (24, 1, 578), (22, 12, 677), (11, 13, 959), (24, 5, 585), (11, 10, 762), (15, 0, 786), (0, 19, 458), (9, 14, 347), (14, 6, 660), (25, 16, 530), (10, 23, 472), (12, 4, 607), (7, 6, 322), (4, 15, 371), (4, 24, 618), (14, 25, 807), (26, 19, 370), (16, 5, 797), (19, 10, 713), (27, 18, 578), (10, 4,
    937), (0, 20, 828)]
        maxIn = [752, 988, 406, 975, 344, 109, 382, 156, 774, 511, 266, 961, 450, 929, 45, 646, 436, 742, 877, 870, 149, 751, 296, 647, 684, 779, 830, 174]
        maxOut = [29, 975, 742, 90, 476, 382, 156, 150, 907, 394, 143, 473, 552, 644, 423, 223, 881, 76, 267, 703, 592, 221, 758, 534, 450, 973, 868, 842]
        origin = 22
        targets = [16, 24, 4]
        # myres = 593
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 389)

    def test_846955(self):
        connections = [(10, 6, 989), (0, 3, 268), (7, 6, 351), (3, 11, 973), (11, 7, 538), (10, 11, 310), (10, 5, 757), (11, 0, 587), (9, 2, 282), (0, 9, 900), (7, 10, 485), (6, 2, 435), (2, 8, 538),
    (7, 5, 928), (5, 1, 788), (2, 4, 745), (1, 0, 680), (8, 0, 677), (5, 8, 265), (4, 9, 520), (8, 10, 251), (2, 11, 652), (3, 1, 936)]
        maxIn = [259, 684, 841, 892, 929, 370, 884, 471, 154, 884, 688, 901]
        maxOut = [471, 208, 614, 898, 582, 69, 760, 239, 153, 338, 180, 433]
        origin = 2
        targets = [8, 7, 5]
        # myres = 614
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 587)

if __name__ == "__main__":
    unittest.main()