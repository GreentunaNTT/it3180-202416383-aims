"""Các hàm tìm kiếm đĩa DVD trong danh sách."""


def search_by_category(items, category):
    """Trả về các đĩa thuộc thể loại category (không phân biệt hoa thường).

    items: danh sách DigitalVideoDisc; category: tên thể loại cần tìm.
    """
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]


def search_by_title(items, keyword):
    """Trả về các đĩa có tiêu đề chứa keyword.

    items: danh sách DigitalVideoDisc; keyword: chuỗi cần tìm.
    """
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]