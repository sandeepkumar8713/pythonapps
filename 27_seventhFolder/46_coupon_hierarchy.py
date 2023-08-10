#  https://leetcode.com/discuss/interview-experience/3527108/Wayfair-or-Software-Engineer-(L2)-or-Bangalore-or-April-2023
#  https://leetcode.com/discuss/interview-question/3788608/WAYFAIR-DSA-Round-1-or-SDE-II
#  We're given categories that are organized hierarchically and a list of coupons where each coupon can be
#  applied to certain categories. Coupons are valid for child categories of categories it can be applied to.
#  First question: Given a category, return list of coupons applicable to that category.
#  Second question: Each coupon now has a validity period, return list of coupons application to given
#  category on a particular date.
#
# I stored coupons in map<category, set<coupon>> and categories in map<child category, parent category>.
# As we need to find coupons that are only applicable to input category, we can ignore its children and
# traverse upwards. I did in a bfs sorta way.
# Like category = input category initially. For subsequent iterations, category = map.get(category),
# it will be set to its parent until we encounter a null parent value.
# As we're traversing, we can lookup in the coupons map if the category has any coupons and store
# them in a result coupons set and return it.
#
# Question Type : Asked
# Used : Make 2 maps: one of coupons and other for category and its parents
#        couponsMap = CategoryName : CouponName
#        categoriesMap = CategoryName : CategoryParentName
# Logic: def find_coupons(self, category_name):
#        if category_name is None:
#           return None
#        if category_name in self.couponsMap:
#           return self.couponsMap.get(category_name)
#        else:
#           return self.find_coupons(self.categoriesMap.get(category_name))
# Complexity : O(n) where n is number of categories

class CategoriesClass:
    def __init__(self, coupons, categories):
        self.couponsMap = {}
        self.categoriesMap = {}

        for coupon in coupons:
            self.couponsMap[coupon["CategoryName"]] = coupon["CouponName"]

        for category in categories:
            self.categoriesMap[category["CategoryName"]] = category["CategoryParentName"]

    def find_coupons(self, category_name):
        if category_name is None:
            return None
        if category_name in self.couponsMap:
            return self.couponsMap.get(category_name)
        else:
            return self.find_coupons(self.categoriesMap.get(category_name))


if __name__ == "__main__":
    Coupons = [
        {"CategoryName": "Comforter Sets", "CouponName": "Comforters Sale"},
        {"CategoryName": "Bedding", "CouponName": "Savings on Bedding"},
        {"CategoryName": "Bed & Bath", "CouponName": "Low price for Bed & Bath"}
    ]

    Categories = [
        {"CategoryName": "Comforter Sets", "CategoryParentName": "Bedding"},
        {"CategoryName": "Bedding", "CategoryParentName": "Bed & Bath"},
        {"CategoryName": "Bed & Bath", "CategoryParentName": None},
        {"CategoryName": "Soap Dispensers", "CategoryParentName": "Bathroom Accessories"},
        {"CategoryName": "Bathroom Accessories", "CategoryParentName": "Bed & Bath"},
        {"CategoryName": "Toy Organizers", "CategoryParentName": "Baby And Kids"},
        {"CategoryName": "Baby And Kids", "CategoryParentName": None}
    ]

    cat = CategoriesClass(Coupons, Categories)
    print(cat.find_coupons("Comforter Sets"))
    print(cat.find_coupons("Bedding"))
    print(cat.find_coupons("Bathroom Accessories"))
    print(cat.find_coupons("Soap Dispensers"))
    print(cat.find_coupons("Toy Organizers"))
