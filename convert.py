import os
import pandas

import config as CONFIG


def convert_txt_to_csv(name):
    from_node = []
    end_node = []
    df = pandas.DataFrame()
    with open(os.path.join(CONFIG.NETWORKS_DIR, name + '.txt'), 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            split = line.split()

            from_node.append(split[0])
            end_node.append((split[1]))

            # break
        df['From Node'] = from_node
        df['End Node'] = end_node

        df.to_csv(CONFIG.NETWORKS_DIR + '\\' + name + '.csv')

