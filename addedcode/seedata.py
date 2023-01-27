# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:21:00 2023

@author: shuyu
"""

#@title Loading the annotations and converting them to a Pandas DataFrame for easier handling and visualisation. { vertical-output: true, display-mode: "form" }


#@markdown **Note**: In the ground truth data, the classes are called **not mitotic figure** and **mitotic figure**. In the following, we will use the labels **hard negative** and **mitotic figure** to make the notebook clearer.  


annotation_file = "C:\\Users\\shuyu\\OneDrive - Imperial College London\\MitosisDetection\\training\\MIDOG2022_training.json"
rows = []
with open(annotation_file) as f:
    data = json.load(f)

    #categories = {cat["id"]: cat["name"] for cat in data["categories"]}
    categories = {1: 'mitotic figure', 2: 'hard negative'}

    for row in data["images"]:
        file_name = row["file_name"]
        image_id = row["id"]
        width = row["width"]
        height = row["height"]

        tumortype = id_to_tumortype[image_id]
         
        for annotation in [anno for anno in data['annotations'] if anno["image_id"] == image_id]:
            box = annotation["bbox"]
            cat = categories[annotation["category_id"]]

            rows.append([file_name, image_id, width, height, box, cat, tumortype])

df = pd.DataFrame(rows, columns=["file_name", "image_id", "width", "height", "box", "cat", "tumortype"])
df.head()