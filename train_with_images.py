def data_gen(img_names, batch_size, colorspace):
    c = 0
    n = img_names  # List of training images
    random.shuffle(n)

    while (True):
        img = np.zeros((batch_size, 150, 150, 3)).astype('float')
        labels = []

        # initially from 0 to 16, c = 0.

        for i in range(c, c + batch_size):
            # print(i)
            train_img = cv2.imread(n[i])
            train_img = cv2.resize(train_img, (150, 150))  # Read an image from folder and resize

            if colorspace == 'hsv':
                train_img = cv2.cvtColor(train_img, cv2.COLOR_BGR2HSV)
                train_img[0, :, :] = train_img[0, :, :] / 180.
                train_img[1:3, :, :] = train_img[1:3, :, :] / 255.
            elif colorspace == 'lab':
                train_img = cv2.cvtColor(train_img, cv2.COLOR_BGR2Lab)
            elif colorspace == 'ycrcb':
                train_img = cv2.cvtColor(train_img, cv2.COLOR_BGR2YCrCb)
            elif colorspace == 'luv':
                train_img = cv2.cvtColor(train_img, cv2.COLOR_BGR2LUV)
            elif colorspace == 'xyz':
                train_img = cv2.cvtColor(train_img, cv2.COLOR_BGR2XYZ)

            if colorspace != 'hsv':
                train_img = train_img / 255.

            img[i - c] = train_img  # add to array - img[0], img[1], and so on.
            if len(re.findall('dog', n[i])) == 3:
                labels.append(0)
            else:
                labels.append(1)
        labels = np.array(labels)
        c += batch_size
        if (c + batch_size >= len(img_names)):
            c = 0
            random.shuffle(n)
            # print "randomizing again"
        yield img, labels
