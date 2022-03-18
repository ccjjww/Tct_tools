'''
Positive cell will be stick randomly on a ROI whit smooth edges



'''

import cv2
import os
from utils import load_label,mkdirs

def is_overlaped(coordinate_pasted,*coordinate_bk):

    pass






class Img_Transform():

    def __init__(self, cell_img, bakgground_img, cell_label,bakgground_label,pasted_img,paste_num=None):
        '''
        
        paste_num 默认cell 
        '''
        self.cell_img =cv2.cvtColor( cv2.imread(cell_img),cv2.COLOR_BGR2RGB)
        self.bakgground_img = cv2.cvtColor( cv2.imread(bakgground_img),cv2.COLOR_BGR2RGB)

        self.c_Cells=coordinate_trans(cell_label)
        self.b_Cells=coordinate_trans(bakgground_label)

     


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

    pass
