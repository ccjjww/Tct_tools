'''
Positive cell will be stick randomly on a ROI whit smooth edges





'''

import cv2
import os
from utils import load_label,mkdirs,coordinate_relative

def is_overlaped(coordinate_pasted,*coordinate_bk):
    '''
    判别方法
        bk_img=zero(h,w)
        bk_img=1
        cell_img=1

        if sum(bk_img)=sum(bk_img|cell_img)
            not overlapped
        if sum(bk_img)>sum(bk_img|cell_img)
            overlapped_size=sum(bk_img)-sum(bk_img|cell_img)



    '''

    pass






class Img_Transform():

    def __init__(self, cell_img, bakgground_img, cell_label,bakgground_label,pasted_img,paste_num=None):
        '''
        
        paste_num 默认cell 

        流程：  
            1. 输入 图片,json; 返回img对象和ROI, Cells, FileInfo
            2. cell_img切出cells(img对象)
            3. background_img 提供 img对象,和背景原来cell的相对坐标
            4. 给切出的cells生成随机坐标, 并判断是否与原来cell有交叠,如有则重新生成




        '''
        self.cell_img =cv2.cvtColor( cv2.imread(cell_img),cv2.COLOR_BGR2RGB)
        self.bakgground_img = cv2.cvtColor( cv2.imread(bakgground_img),cv2.COLOR_BGR2RGB)

     


    def paste(self):








        
        pass


if __name__ == '__main__':
    
    os.chdir(r'C:\Users\jzy\Documents\GitHub\Tct_tools\jzy')

    original_img =r'./testdir/ROI_Image/04619.tiffROI_1.Tiff'
    bakgground_img=r'./testdir/ROI_Image/04891.tiffROI_1.Tiff'
    
    cell_label=r'./testdir/label_split_dir/04619_1.json'
    bakgground_label=r'./testdir/label_split_dir/04891_1.json'

    pasted_img=r'./paste_dir/pasted_img.jpg'
    mkdirs(pasted_img)


    img_trans=Img_Transform(original_img,bakgground_img,cell_label,bakgground_label,pasted_img)
