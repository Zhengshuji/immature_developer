from function_used import *
import output
import cv2

dir = "Data//"
inner_output = "inner"
outer_output = "outer"
origin_file_dir = "origin_file//"
file_name = "1.jpg"

if __name__ == '__main__':
    #img = graph_progress.preprocess_image(origin_file)
    #cv2.imshow('img', img)
    #x_axis,y_axis = OCR.detect_axis(img)
    #OCR.ocr(inner_output+'//inner_box.jpg')


    ######  1.选取文件
    origin_file = dir + origin_file_dir + file_name             #输入图片路径
    inner_output = dir + inner_output                           #输入图像分解路径
    outer_output = dir + outer_output                           #输出结果路径

    #####   2.手动分解图片
    manu_select(origin_file,outer_output)

    ####    3.图像数据识别及与预处理
    x_info = ocr_axis(outer_output,'x_axis')
    #print(x_info)
    cv2.waitKey(0.1)
    y_info = ocr_axis(outer_output,'y_axis')
    #print(y_info)

    ####    4.图像处理
    print('Processing the figure')
    processed_img = img_process(f'{outer_output}','figure.jpg')
    print('Complete the figure process')

    ####    5.图像数据获取
    print('Data collecting')
    '''x_info = {'start_string': '2023.04.11', 'end_string': '2025.03.05', 'start': 45025, 'end': 45719, 'range': 694, 'unit': 'days'}
    y_info = {'start_string': '0.00%', 'end_string': '4.42%', 'start': 0.0, 'end': 4.42, 'range': 4.42, 'unit': '%'}'''
    img_data_extract(f'{outer_output}',f'processed_figure.jpg',[x_info,y_info])
    print('Data collected successfully')

    ####    6.时序预测
    print('Predicting')
    Time_Predicting(f'{outer_output}//origin_datas.csv',topath=outer_output+r'/output.csv')
    print('Already predicted')

    ####    7.输出结果
    print('Output the virtualized results')
    output.outputs_draw(f"{outer_output}//origin_datas.csv",f"{outer_output}//output.csv","timestamp","value")
    print('Completed')