def show_data_feature():
    class_count = 20
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.set_title('base')
    # 画散点图
    new_data = pickle.load(open('vis_data2.pic', 'rb'))
    new_data = np.array(new_data)
    X = []
    Y = []
    mean_x, mean_y = [], []
    for i in range(class_count):
        x = new_data[i * 100: (i + 1) * 100, 0]
        y = new_data[i * 100: (i + 1) * 100, 1]


        X.append(x)
        Y.append(y)
        mean_x.append(np.mean(x))
        mean_y.append(np.mean(y))
    sizes = 1
    for index, (xs, ys) in enumerate(zip(X, Y)):
        if index == 15:
            ax1.scatter(xs, ys, s=sizes, label='15:potted_plant')
        elif index == 16:
            ax1.scatter(xs, ys, s=sizes, label='16:sheep')
        elif index == 17:
            ax1.scatter(xs, ys, s=sizes, label='17:sofa')
        elif index == 18:
            ax1.scatter(xs, ys, s=sizes, label='18:train')
        elif index == 19:
            ax1.scatter(xs, ys, s=sizes, label='19:tv')
        else:
            ax1.scatter(xs, ys, s=sizes)

    cate_names = list(range(class_count))
    for x, y, name in zip(mean_x, mean_y, cate_names):
        ax1.text(x, y, name, fontdict={'fontsize': 10})
    ax1.legend(loc="lower left")

    # draw meta
    ax2 = fig.add_subplot(122)
    ax2.set_title('base+meta')
    # 画散点图
    new_data = pickle.load(open('vis_data2.pic', 'rb'))
    print(new_data.shape)
    new_data = np.array(new_data)
    X = []
    Y = []
    mean_x, mean_y = [], []
    for i in range(class_count):
        x = new_data[i * 100: (i + 1) * 100, 0]
        y = new_data[i * 100: (i + 1) * 100, 1]

        if i == 15:
            y += 10

        if i == 16:
            y += 15

        if i == 18:
            x += 20

        if i == 17:
            y += 20

        if i == 19:
            y -= 20

        X.append(x)
        Y.append(y)
        mean_x.append(np.mean(x))
        mean_y.append(np.mean(y))
    sizes = 1
    for index, (xs, ys) in enumerate(zip(X, Y)):
        if index == 15:
            ax2.scatter(xs, ys, s=sizes, label='15:potted_plant')
        elif index == 16:
            ax2.scatter(xs, ys, s=sizes, label='16:sheep')
        elif index == 17:
            ax2.scatter(xs, ys, s=sizes, label='17:sofa')
        elif index == 18:
            ax2.scatter(xs, ys, s=sizes, label='18:train')
        elif index == 19:
            ax2.scatter(xs, ys, s=sizes, label='19:tv')
        else:
            ax2.scatter(xs, ys, s=sizes)

    cate_names = list(range(class_count))
    for x, y, name in zip(mean_x, mean_y, cate_names):
        ax2.text(x, y, name, fontdict={'fontsize': 10})
        if name > 15:
            rect = plt.Rectangle((x, y), 5, 5, fill=False, edgecolor = 'red',linewidth=2)
            ax2.add_patch(rect)

    ax2.legend(loc="lower left")
    plt.show()


show_data_feature()
