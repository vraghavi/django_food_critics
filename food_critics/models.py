from django.db import models
from datetime import datetime
import copy

# Create your models here.

class Comments:
    def __init__(self, id, blog_id, date_commented, user_commented, description):
        self.id = id
        self.blog_id = blog_id
        self.date_commented = date_commented
        self.user_commented = user_commented
        self.description = description


class FoodBlog:
    def __init__(self, id, points, image, title, short_description, detail_description, no_of_comments, comments, date_posted, user_posted):
        self.id = id
        self.points = points
        self.image = image
        self.title = title
        self.short_description = short_description
        self.detail_description = detail_description
        self.no_of_comments = no_of_comments
        self.comments = comments
        self.date_posted = date_posted
        self.user_posted = user_posted


comment1 = Comments(1, 1, datetime.now(), "sarahkolie", "No fostermarshall. Only brunch special is reasonable")
comment2 = Comments(2, 1, datetime.now(), "fostermarshall", "I don’t know why, but I find it expensive")
comment3 = Comments(3, 1, datetime.now(), "pepperoni23", "Wait what!! How did I miss this?!")
comment4 = Comments(4, 1, datetime.now(), "hoveronfood", "Their food is yummy")
comment5 = Comments(5, 2, datetime.now(), "welcomefood", "Ok! Added one in bucket list")
comment6 = Comments(6, 2, datetime.now(), "hellopie", "Yummm, I like their food")
comment7 = Comments(7, 2, datetime.now(), "dessert87", "How is their dessert section?")
comment8 = Comments(8, 2, datetime.now(), "gobi65", "Do they serve Indian?")
comment9 = Comments(9, 3, datetime.now(), "unicorn123", "Next place visit")
comment10 = Comments(10, 3, datetime.now(), "hahacheese", "Wow!! Tag me in. I will join you")
comment11 = Comments(11, 3, datetime.now(), "happyfoodie", "Expensive, but okay.")
comment12 = Comments(12, 3, datetime.now(), "always_hangry", "Best place to go on a date")
comment13 = Comments(13, 4, datetime.now(), "onlysoups", "I love tacos and mexican food.")
comment14 = Comments(14, 4, datetime.now(), "yummthai", "Nothing can beat thai food.")


foodblog1 = FoodBlog(
    1,
    167,
    "gillies_inc.jpeg",
    "Gillie’s Inc brunch special is best and economical, Blacksburg",
    "Gillie's Cuisine was a delight! While looking for things to do in Blacksburg we discovered a lovely donut shop near the Virginia Tech campus. So utterly pleased were we with our discovery that we decided to cruise the area to see what else we could find.",
    "Gillie's Cuisine was a delight! While looking for things to do in Blacksburg we discovered alovely donut shop near the Virginia Tech campus. So utterly pleased were we with our discovery that we decided to cruise the area to see what else we could find.It was a lovely Saturday that we decided to cruise the area to see what else we could find.It was a lovely Saturday morning and to our amazing luck a farmers market was setting up shop for the day. Here we had the pleasure of speaking with a local police officer who was like a walking yelp app when it ame to great places to eat nearby. One particular place of interest was Gillies because of their rich menu of vegetarian/vegan/Gluten free items.I, like most good husbands, desire to please my bride. However, this is a tricky task when it comes to eating, since she eats more like a rabbit and I more like a T-REX. So places like this offering a better than average menu for her while also having items that please me is a truly treasured and sacred space! Add to that good fellowship amongst friends on a large outdoor sitting area well suited for the current Covid-19 pandemic and somehow all seems right with the universe again.THE FOODUNFORTUNATELY they ran out of grits, so I was not able to take advantage of the SHRIMP & GRITS special of the day. However, this caused me to order the SMOKED SALMON HASH and it did not disappoint(5 + stars). My son and I split this dish along with the BANANA WALNUT FRENCH TOAST(4.5 stars) while my wife and her bestie tried the HUEVOS NACHOS(4 stars). The hash was so enjoyable that I conceded the lions share to my son, who devoured every bite with joy. While it is satisfying to get what you want how you want it, for a parent it is even more satisfying to see your seedlings satisfaction as well.Overall it was a fantastic experience. The staff was great, the food was delicious, the morning weather was absolutely perfect to eat outdoors and the crowds were low. Couldn't have asked for a better visit except maybe to not run out of grits so early in the day!",
    48,
    [comment1, comment2, comment3, comment4],
    datetime.now(),
    "Kolhan")

foodblog2 = FoodBlog(
    2,
    119,
    "plaka_grill.jpeg",
    "My recommendations at Plaka Grill, Falls Church",
    "I don't understand how anyone in their right mind could give this place less than 5 Stars. Anyone giving Plaka Grill less than 5 stars should be flogged or maybe made to walk the plank. Do we still allow that? This super nice Greek restaurant is located in the City of Falls Church Virginia.",
    "I want to start by saying I absolutely love the food at Plaka Grill, Their Plaka Gyro is this probably the closest thing to an authentic gyro you would get in Greece. I use the frequent their location on W. Broad St. in Falls Church City quite often but since they have moved its just the little bit further to go to as often so when I do go it always feels like a treat except for the last 3 times I went. 1st Trip: I went during my lunch break and ordered a very small order for myself and a co-worker (2 soups, 1 app, 1 salad) when I arrived there was only one table sitting in the restaurant, they had clearly been there a while, I walked up ordered and paid and then waiting over 25 mins for my order to be prepared, I could see it waiting in the window while other staff members were having personal conversations in the back room ignoring the fact that the one staff person was now busy with other guests that walked in. When I arrived back at my office with my food they had completely forgotten one of our items.2nd Trip: Again for lunch this time we ate there, again a small order, (2 soups, 1 app, 1 gyro) We placed the order and had to ask the cashier twice to read it back to us, at which point again an item was missing from the order. After repeating the order for a 4th time is was corrected.3rd Trip: Went for carry out this past Sunday and knowing they closed at 9 I rushed over to grad dinner for my whole family and walked in at 8:42 just to be told that the kitchen had already closed, to say I was disappointed is an understatement. I understand that places are not that busy these days with COVID but if you are going to close your kitchen early then please just lock your doors as well so people cant come in expecting service up until your advertised hours of operation.All in all GREAT FOOD, but very disappointing staff & service.",
    23,
    [comment5, comment6, comment7, comment8],
    datetime.now(),
    "Jim@89")

foodblog3 = FoodBlog(
    3,
    90,
    "chauncey.jpeg",
    "Must try dishes at Chauncey’s Family Dining, Arlington",
    "I think that I've driven past Chauncey's a thousand times over the years and never knew what the scoop was. Well, we stopped in last week on the way to Manchester for lunch. I had looked at the menu before heading out and knew that I wanted to try the maple hot wings...so that order went in ASAP.",
    "I think that I've driven past Chauncey's a thousand times over the years and never knew what the scoop was. Well, we stopped in last week on the way to Manchester for lunch. I had looked at the menu before heading out and knew that I wanted to try the maple hot wings...so that order went in ASAP. We also ordered the homemade potato chips with ranch dip. The wings were very nice; there was a light coating on them (which I didn't expect), but the sauce was hot and sweet. Yum. The homemade potato chips were served warm...freshly fried! Crispy and not too greasy. Good ranch dressing, too. I decided to go for 'the babysitter'...grilled cheese sandwich with a side of sweet potato fries. Can't remember the last time I had a grilled cheese sandwich (asked for it to be served with tomato) - it was just right. The sweet potato fries were huge and clearly homemade. I tasted the cheeseburger (checkerboard - with 2 different kinds of cheese melted on a hand-packed patty) - this was a really, really good burger. There was a long list of dessert offerings, but we couldn't eat anything else. We did take an apple crisp home for momma...which she later told us was one of the best she's ever had. So, save room for dessert! Quick tip: when walking into Chauncy's, hang out by the bar area and don't make a b-line right to the dining room. The layout of the restaurant might cause you not to be seen by the staff. And...save room for dessert!!!",
    19,
    [comment9, comment10, comment11, comment12],
    datetime.now(),
    "ieatfood@arlington")

foodblog4 = FoodBlog(
    4,
    86,
    "birria_tacos.jpeg",
    "Do It for the Blog: Trying Birria Tacos and the Quesabirria",
    "If you’ve been on Instagram over the last few months, you’ve probably noticed a trendy new dish popping up in Mexican restaurants across the country. Birria tacos have been sweeping the nation, as food bloggers share photos and boomerangs of this popular entrée that’s actually been around for quite some time.",
    "If you’ve been on Instagram over the last few months, you’ve probably noticed a trendy new dish popping up in Mexican restaurants across the country. Birria tacos have been sweeping the nation, as food bloggers share photos and boomerangs of this popular entrée that’s actually been around for quite some time. Mexican restaurants across the Coastal Virginia/Hampton Roads region have joined in the birria food trend. The Virginian-Pilot covered the birria wave by focusing on the ooey, gooey quesabirria. I used this as my reference point to figure out which restaurant to go to. Taqueria La Patrona had been on my list to try for several months. I tried to order from them on Cinco De Mayo, but they were out of most dishes by the time I called to order. I knew then that this had to be a fantastic Mexican restaurant. Following the Pilot’s article, Taqueria La Patrona was overrun with orders for their birria dishes. Throughout the week, the restaurant has to update their Facebook page to let people know that they don’t have the ingredients to make anymore. Fortunately, I’ve found a sweet spot for ordering these birria dishes before they’re sold out. No, I won’t be spilling my secret time to order (unless you ask really nicely). However, I will tell you that they’re no longer selling the dish on Mondays and Wednesdays.  First, I tried Taqueria La Patrona’s Tacos de Birria con Consomé. Three crispy, but not crunchy, corn tortilla tacos, filled with shredded beef, cilantro and onion, are served with a flavorful consomé that’s mild in heat.",
    50,
    [comment13, comment14],
    datetime.now(),
    "mexicanfoodie@bb")

food_blogs = []
food_blogs.append(foodblog1)
food_blogs.append(foodblog2)
food_blogs.append(foodblog3)
food_blogs.append(foodblog4)
food_blogs_copy = copy.deepcopy(food_blogs)
regular_user = {"pid":"sarahkolie", "password":"hello"}
admin_user = {'pid':"admin", "password":"admin"}
