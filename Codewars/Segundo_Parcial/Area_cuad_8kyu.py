def get_size(w,h,d):
    """
    Función que calcula el area y volumen de una figura.
    @param w:
    @param h:
    @param d:
    @return:
    """
    ls = []
    a = 2 * (w * h + h * d + w * d)
    ls.append(a)
    b = w*h*d
    ls.append(b)
    return ls