def tinh_tien_dien(soluongdien: int):
    if soluongdien < 0:
        return -1
    if soluongdien <= 50:
        return soluongdien * 1806
    elif soluongdien <= 100:
        return 90300 + (soluongdien - 50) * 1866
    elif soluongdien <= 200:
        return 183600 + (soluongdien - 100) * 2167
    elif soluongdien <= 300:
        return 400300 + (soluongdien - 200) * 2729
    elif soluongdien <= 400:
        return 673200 + (soluongdien - 300) * 3050
    else:
        return 978200 + (soluongdien - 400) * 3151