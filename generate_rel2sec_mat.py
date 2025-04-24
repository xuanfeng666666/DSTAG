# import json
# import os
# import numpy as np
# from utils import read_dict

# with open('./dataset/ICEWS14/auxiliary/rel2sec.json', encoding='utf-8') as f:
#     rel2sec_14 = json.load(f)

# ent2id_14, _ = read_dict('./dataset/ICEWS14/relation2id.txt')

# total_sec_l = set()
# for k, v in rel2sec_14.items():
#     total_sec_l.update(v)
#     rel2sec_14[k] = list(set(v))
# sec2id = dict(zip(sorted(total_sec_l), np.arange(len(total_sec_l))))

# rel2sec_mat = np.zeros([len(ent2id_14), len(sec2id)])
# for k, v_l in rel2sec_14.items():
#     for v in v_l:
#         rel2sec_mat[ent2id_14[k], sec2id[v]] = 1

# save_path = './dataset/ICEWS14/auxiliary/'
# os.makedirs(save_path, exist_ok=True)

# np.save(save_path + 'rel2sec_matrix_v1.npy', rel2sec_mat)
# print(f'save entity_to_sector matrix in {save_path}/rel2sec_matrix_v1.npy')


import json
import os
import numpy as np
from utils import read_dict

with open('./dataset/ICEWS18/auxiliary/rel2sec.json', encoding='utf-8') as f:
    ent2sec_14 = json.load(f)

ent2id_14, _ = read_dict('./dataset/ICEWS18/relation2id.txt')

total_sec_l = set()
for k, v in ent2sec_14.items():
    total_sec_l.update(v)
    ent2sec_14[k] = list(set(v))
sec2id = dict(zip(sorted(total_sec_l), np.arange(len(total_sec_l))))

ent2sec_mat = np.zeros([len(ent2id_14), len(sec2id)])
for k, v_l in ent2sec_14.items():
    for v in v_l:
        ent2sec_mat[ent2id_14[k], sec2id[v]] = 1

save_path = './dataset/ICEWS18/auxiliary/'
os.makedirs(save_path, exist_ok=True)

np.save(save_path + 'rel2sec_matrix_v1.npy', ent2sec_mat)
print(f'save rel_to_sector matrix in {save_path}/rel2sec_matrix_v1.npy')
