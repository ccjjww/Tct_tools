import os
import json
import cv2


def mkdirs(*dirs_path):
    for dir in dirs_path:
        if not os.path.exists(dir):
            os.makedirs(dir)


def load_label(label_path):
    with open(label_path, "r", encoding="utf-8") as load_f:
        data = json.load(load_f)
        # print(json.dumps(data, indent=4))
    ROI = data["ROI"]
    Cells = data["CellRect"]
    FileInfo = data["FileInfo"]
    return ROI, Cells, FileInfo


def label_split(label_dir, Labels_split_dir):
    labels_list = os.listdir(label_dir)

    for label in labels_list:
        label_path = os.path.join(label_dir, label)

        with open(label_path, 'r',encoding='utf-8') as load_f:
            data = json.load(load_f)
        ROIs = data['ROI']
        Cells = data['CellRect']
        FileInfo = data['FileInfo']
        try:
            FileInfo.pop('Path')
        except:
            pass
        file_name = FileInfo['Name'].split('.')[0]
        RoiIDs = set([cell['RoiID'] for cell in Cells])

        for RoiID in RoiIDs:
            label_split_name = os.path.join(Labels_split_dir, str(file_name +
                                                                  '_' + str(RoiID) + '.json'))
            ROI = [roi for roi in ROIs if roi['roiID'] == RoiID]
            cells = [cell for cell in Cells if cell['RoiID'] == RoiID]
            label_split = {
                "FileInfo": FileInfo,
                "ROI": ROI,
                "CellRect": cells}
            label_split = json.dumps(label_split)
            with open(label_split_name, "w") as f:
                f.write(label_split)


def coordinate_relative(ROI, Cells):
    
    roi_x = ROI['x']
    roi_y = ROI['y']
    for cell in Cells:
        # TODO：此处是在原处更新，原始值copy之后的新对象也更新，可能引起BUG
        cell['x'] = int(cell['x'] - roi_x)
        cell['y'] = int(cell['y'] - roi_y)
    return Cells



def cells_cut(img, cells_list, ifsave=False):
    '''
    读取img 和label
    '''
    
    cells_cut={}
    for cell in cells_list:
        cell_x = int(cell['x'] )
        cell_y = int(cell['y'] )
        cell_w = int(cell['w'])
        cell_h = int(cell['h'])


        cell_img=img[cell_y:cell_y+cell_h,cell_x:cell_x+cell_w]
        cells_cut[cell['ID']]=cell_img

        if ifsave:
            cell_img_name = os.path.join('./cells', str(cell['ID']) + '.jpg')
            mkdirs(cell_img_name)
            cv2.imwrite(cell_img_name, cell_img)
    
    return cells_cut







if __name__ == '__main__':
    os.chdir(r'C:\Users\jzy\Documents\GitHub\Tct_tools\jzy')
    label_dir = r'./testdir/label'
    label_split_dir = r'./testdir/label_split_dir'

    # 1 按照ROI拆分json
    mkdirs(label_split_dir)
    label_split(label_dir, label_split_dir)

    # 2 计算相对位置
    img_path =r'./testdir/ROI_Image/04619.tiffROI_1.Tiff'
    labe_pathl=r'./testdir/label_split_dir/04619_1.json'

    img=cv2.cvtColor(cv2.imread(img_path),cv2.COLOR_BGR2RGB)
    ROI, Cells, _=load_label(labe_pathl)
    Cells_coor_relative=coordinate_relative(ROI[0], Cells)

    # 3 切出cell 

    cells=cells_cut(img,Cells_coor_relative)

    
