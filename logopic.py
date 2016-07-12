import os

from PIL import Image


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def resize_image(input_dir, output_dir, width, height, output_name=None, logo=None):
    """
    :param input_dir:
    :param output_dir:
    :param output_name:
    :param width:
    :param height:
    :return:
    """
    for n, file_ in enumerate(os.listdir(input_dir)):
        image = Image.open(os.path.join(BASE_DIR, input_dir, file_))
        out_name = output_name and '{0}_{1}'.format(output_name, n) or '{0}_{1}'.format(file_, n)
        image.thumbnail((width, height), Image.ANTIALIAS)

        if logo:
            logo_img = Image.open(os.path.join(BASE_DIR, 'logo', 'logo.png'))
            logo_img.thumbnail((200, 200), Image.ANTIALIAS)

            # get images size to position a logo
            main_img_box = image.getbbox()
            logo_img_box = logo_img.getbbox()
            box = (main_img_box[2] - logo_img_box[2], main_img_box[3] - logo_img_box[3])

            # paste a logo inside a main_image
            image.paste(logo_img, box, mask=logo_img)

        outfile = os.path.join(output_dir, '{0}.jpg'.format(out_name))
        image.save(outfile, 'JPEG')


def main():
    # AddLogo(os.path.join(BASE_DIR, 'input.jpg'), os.path.join(BASE_DIR, 'logo', 'logo.png'), os.path.join(BASE_DIR, 'output.png'))
    input_dir = os.path.join(BASE_DIR, 'photos')
    output_dir = os.path.join(BASE_DIR, 'output')
    resize_image(input_dir, output_dir, 1024, 768, output_name='result', logo=True)
    print('feito!')
    return


if __name__ == '__main__':
    main()
