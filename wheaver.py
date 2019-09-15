import cv2
import tkinter
from tkinter import filedialog
from math import sin, cos, radians


def black(y_test, x_test, variable):
    color = [image.item(y_test, x_test, 0), image.item(y_test, x_test, 1), image.item(y_test, x_test, 2)]
    if color[0] == 0 and color[1] == 0 and color[2] == 0:
        variable += 1
        return int(variable)
    else:
        return int(variable)


def pixels_analysis(point_1, point_2):
    yd = point_2[0] - point_1[0]
    xd = point_2[1] - point_1[1]
    y_abs = abs(yd)
    x_abs = abs(xd)
    if y_abs > x_abs:
        step = y_abs
    else:
        step = x_abs
    black_pixels = 0
    for pixel in range(1, step):
        y_position = int(round(point_1[0] + (yd * (pixel / step))))
        x_position = int(round(point_1[1] + (xd * (pixel / step))))
        pxp = [x_position, y_position]
        color = [image.item(pxp[0], pxp[1], 0), image.item(pxp[0], pxp[1], 1), image.item(pxp[0], pxp[1], 2)]
        if color[0] == color[1] == color[2] == 0:
            black_pixels += 1
    return [black_pixels, point_1, point_2]


def clean_image():
    for y_axis in range(0, image.shape[0]):
        for x_axis in range(0, image.shape[1]):
            cleaned.itemset(y_axis, x_axis, 0, 255)
            cleaned.itemset(y_axis, x_axis, 1, 255)
            cleaned.itemset(y_axis, x_axis, 2, 255)


root = tkinter.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
image = cv2.imread(file_path)
cleaned = cv2.imread(file_path)
clean_image()
size = image.shape
# (Y,X)
center = [int(size[1] / 2), int(size[0] / 2)]
nail_number = int(input('nails number: '))
angle = 360 / nail_number
nail_positions = []
for i in range(0, nail_number):
    x = int(center[0] + ((center[0] - 1) * sin(-(radians(angle * i)))))
    y = int(center[1] + ((center[0] - 1) * cos(-(radians(angle * i)))))
    positions = [y, x]
    nail_positions.append(positions)
actual_point = nail_positions[0]
segments = [0]
lines = 0
while True:
    bigger = [0, nail_positions[0], nail_positions[0]]
    for i in range(0, nail_number):
        point_analysis = nail_positions[i]
        a = pixels_analysis(actual_point, point_analysis)
        if a[0] > bigger[0]:
            bigger = [a[0], a[1], a[2]]
    actual_point = bigger[2]
    line = [bigger[1], bigger[2]]
    index = nail_positions.index(bigger[2])
    segments.append(index)
    cv2.line(image, (line[1][0], line[1][1]), (line[0][0], line[0][1]), (255, 255, 255), 1)
    cv2.line(cleaned, (line[1][0], line[1][1]), (line[0][0], line[0][1]), (0, 0, 0), 1)
    image_output_1 = cv2.resize(image, (700, 700))
    image_output_2 = cv2.resize(cleaned, (700, 700))
    cv2.imshow('output_1', image_output_1)
    cv2.imshow('output_2', image_output_2)
    cv2.waitKey(10)
    lines += 1
    if bigger[0] == 0 or lines == 1800:
        break
print('Finish')
image_output_2 = cv2.resize(cleaned, (700, 700))
cv2.imshow('output', image_output_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
archive = [f'Finish, {lines} lines\n']
for i in range(1, len(segments)):
    archive.append(f'from {segments[(i - 1)]} to {segments[i]}\n')
cv2.destroyAllWindows()
file_type = [['text file', '*.txt']]
file_path = filedialog.asksaveasfilename(filetypes=file_type, defaultextension=file_type)
archive_txt = open(file_path, 'a')
archive_txt.writelines(archive)
archive_txt.close()
