from abc import ABC, abstractmethod

class SinhVienPoly(ABC):
    def __init__(self, ho_ten, nganh=None):
        self.ho_ten = ho_ten
        self.nganh = nganh

    @abstractmethod
    def get_diem(self):
        raise NotImplementedError

    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif diem < 7:
            return "Trung bình"
        elif diem < 8:
            return "Khá"
        elif diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def xuat(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Ngành học: {self.nganh}")
        print(f"Điểm: {self.get_diem()}")
        print(f"Học lực: {self.get_hoc_luc()}")
        print("-" * 30)


class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, nganh=None, *scores, **kwargs):
        super().__init__(ho_ten, nganh)
        if scores and len(scores) >= 3:
            self.diem_java, self.diem_html, self.diem_css = scores[:3]
        else:
            self.diem_java = float(kwargs.get('java', kwargs.get('diem_java', 0)))
            self.diem_html = float(kwargs.get('html', kwargs.get('diem_html', 0)))
            self.diem_css = float(kwargs.get('css', kwargs.get('diem_css', 0)))

    def get_diem(self):
        return round((self.diem_java * 2 + self.diem_html + self.diem_css) / 4, 2)


class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, nganh=None, *scores, **kwargs):
        super().__init__(ho_ten, nganh)
        if scores and len(scores) >= 2:
            self.diem_marketing, self.diem_sales = scores[:2]
        else:
            self.diem_marketing = float(kwargs.get('marketing', kwargs.get('diem_marketing', 0)))
            self.diem_sales = float(kwargs.get('sales', kwargs.get('diem_sales', 0)))

    def get_diem(self):
        return round((self.diem_marketing * 2 + self.diem_sales) / 3, 2)


class SinhVien:
    def __init__(self, ho_ten, diem):
        self.ho_ten = ho_ten
        self.diem = float(diem)

    def xep_loai(self):
        if self.diem >= 8:
            return "Giỏi"
        elif self.diem >= 6.5:
            return "Khá"
        elif self.diem >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def xuat_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}, Điểm: {self.diem}, Học lực: {self.xep_loai()}")