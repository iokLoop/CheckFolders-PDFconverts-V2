from PIL import Image
import numpy as np
import os
#from apps.front import utils

class alphaOFF():

    def alpha_to_color(self,image, color=(255, 255, 255)):
        """Set all fully transparent pixels of an RGBA image to the specified color.
        This is a very simple solution that might leave over some ugly edges, due
        to semi-transparent areas. You should use alpha_composite_with color instead.

        Source: http://stackoverflow.com/a/9166671/284318

        Keyword Arguments:
        image -- PIL RGBA Image object
        color -- Tuple r, g, b (default 255, 255, 255)

        """ 
        x = np.array(image)
        try:
            r, g, b, a = np.rollaxis(x, axis=-1)
        except ValueError:
            r, g, b = np.rollaxis(x, axis=-1)
        finally:
            pass
        
        r[a == 0] = color[0]
        g[a == 0] = color[1]
        b[a == 0] = color[2] 
        x = np.dstack([r, g, b, a])
        return Image.fromarray(x, 'RGBA')


    def alpha_composite(self,front, back):
        """Alpha composite two RGBA images.

        Source: http://stackoverflow.com/a/9166671/284318

        Keyword Arguments:
        front -- PIL RGBA Image object
        back -- PIL RGBA Image object

        """
        front = np.asarray(front)
        back = np.asarray(back)
        result = np.empty(front.shape, dtype='float')
        alpha = np.index_exp[:, :, 3:]
        rgb = np.index_exp[:, :, :3]
        falpha = front[alpha] / 255.0
        balpha = back[alpha] / 255.0
        result[alpha] = falpha + balpha * (1 - falpha)
        old_setting = np.seterr(invalid='ignore')
        result[rgb] = (front[rgb] * falpha + back[rgb] * balpha * (1 - falpha)) / result[alpha]
        np.seterr(**old_setting)
        result[alpha] *= 255
        np.clip(result, 0, 255)
        # astype('uint8') maps np.nan and np.inf to 0
        result = result.astype('uint8')
        result = Image.fromarray(result, 'RGBA')
        return result


    def alpha_composite_with_color(self,image, color=(255, 255, 255)):
        """Alpha composite an RGBA image with a single color image of the
        specified color and the same size as the original image.

        Keyword Arguments:
        image -- PIL RGBA Image object
        color -- Tuple r, g, b (default 255, 255, 255)

        """
        back = Image.new('RGBA', size=image.size, color=color + (255,))
        return alpha_composite(image, back)


    def pure_pil_alpha_to_color_v1(self,image, color=(255, 255, 255)):
        """Alpha composite an RGBA Image with a specified color.

        NOTE: This version is much slower than the
        alpha_composite_with_color solution. Use it only if
        numpy is not available.

        Source: http://stackoverflow.com/a/9168169/284318

        Keyword Arguments:
        image -- PIL RGBA Image object
        color -- Tuple r, g, b (default 255, 255, 255)

        """ 
        def blend_value(self,back, front, a):
            return (front * a + back * (255 - a)) / 255

        def blend_rgba(self,back, front):
            result = [self.blend_value(back[i], front[i], front[3]) for i in (0, 1, 2)]
            return tuple(result + [255])

        im = image.copy()  # don't edit the reference directly
        p = im.load()  # load pixel array
        for y in range(im.size[1]):
            for x in range(im.size[0]):
                p[x, y] = blend_rgba(color + (255,), p[x, y])

        return im

    def pure_pil_alpha_to_color_v2(self,image, color=(255, 255, 255)):
        """Alpha composite an RGBA Image with a specified color.

        Simpler, faster version than the solutions above.

        Source: http://stackoverflow.com/a/9459208/284318

        Keyword Arguments:
        image -- PIL RGBA Image object
        color -- Tuple r, g, b (default 255, 255, 255)

        """
        image.load()  # needed for split()
        background = Image.new('RGB', image.size, color)
        background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
        return background
    
    def __init__(self,_Metodo,_imagen,_imgEXTENTION,_imgDestino,_quality,_dirOrigin,_dirDestiny):
        """
        => metodo 0) alpha_to_color

        => metodo 1) alpha_composite_with_color

        => metodo 2) pure_pil_alpha_to_color

        => metodo 3) pure_pil_alpha_to_color_v2

        si _dirIMAGEN es igual a None _dirDestiny sera igual a _dirIMAGEN
        """
        print("\nEn Funcion  <<< alphaOFF >>> con PID# ",os.getpid())
        if _dirDestiny==None:
            _dirDestiny=_dirOrigin

        if _imgDestino==None:
            _imgDestino=_imagen

        i = Image.open(os.path.join(_dirOrigin,_imagen))

        if _Metodo==0:
            i2 = self.alpha_to_color(i)
        elif _Metodo==1:
            i2 = self.alpha_composite_with_color(i)
        elif _Metodo==2:
            i2 = self.pure_pil_alpha_to_color_v1(i)
        elif _Metodo==3:
            i2 = self.pure_pil_alpha_to_color_v2(i)
        i2.save(_imgDestino, _imgEXTENTION, quality=_quality)


if __name__=="__main__":
    # => metodo 0) alpha_to_color
    # => metodo 1) alpha_composite_with_color
    # => metodo 2) pure_pil_alpha_to_color
    # => metodo 3) pure_pil_alpha_to_color_v2
    # =>
    _imagenDestino="aaaa.png"
    imgDestino=os.path.join(_dirOrigin,_imagenDestino)
    x=alphaOFF(3,"alpha-channel-unity-clip-art.png","png",imgDestino,80,"C:/Users/yokaa/Desktop/aqui",None)
    
