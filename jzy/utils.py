import os
import json
import cv2


def mkdirs(*dirs_path):
    for dir in dirs_path:
        if not os.path.exists(dir):
            os.makedirs(dir)


def label_split(label_dir, Labels_split_dir):
    labels_list = os.listdir(label_dir)

    for label in labels_list:
        label_path = os.path.join(label_dir, label)
        print(label_path)

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
            print(label_split_name)
            ROI = [roi for roi in ROIs if roi['roiID'] == RoiID]
            cells = [cell for cell in Cells if cell['RoiID'] == RoiID]
            label_split = {
                "FileInfo": FileInfo,
                "ROI": ROI,
                "CellRect": cells}
            label_split = json.dumps(label_split)
            with open(label_split_name, "w") as f:
                f.write(label_split)


if __name__ == '__main__':
    label_dir = './testdir/label'
    label_split_dir = './testdir/label_split_dir'

    mkdirs(label_split_dir)
    label_split(label_dir, label_split_dir)
