# Copyright (c) 2020 Quidely
#
# All Rights Reserved.
# This file is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.

"""Test cases for factories."""

from django.test import TestCase

from quidely_eat import models
from seed import factories


#####################
# General
####################
class CreateUserTestCase(TestCase):

    def test_create(self):

        user = factories.UserFactory()
        self.assertTrue(isinstance(user, models.User))


class CreateCurrencyTestCase(TestCase):

    def test_create(self):

        currency = factories.CurrencyFactory()
        self.assertTrue(isinstance(currency, models.Currency))


class CreateLocationTestCase(TestCase):

    def test_create(self):

        location = factories.LocationFactory()
        self.assertTrue(isinstance(location, models.Location))


#####################
# Client related
####################
class CreateClientTestCase(TestCase):

    def test_create_simple(self):

        client = factories.ClientFactory()
        self.assertTrue(isinstance(client, models.Client))
        self.assertTrue(client.payment_method_set.count() > 0)

    # TODO(wilcoln): Add test with favorite restaurants
    # TODO(wilcoln): Add test with favorite menu items


class CreateLoyaltyBalanceTestCase(TestCase):

    def test_create(self):
        loyalty_balance = factories.LoyaltyBalanceFactory()
        self.assertTrue(isinstance(loyalty_balance, models.LoyaltyBalance))


class CreateLocationLabelTestCase(TestCase):

    def test_create(self):
        location_label = factories.LocationLabelFactory()
        self.assertTrue(isinstance(location_label, models.LocationLabel))


#####################
# Restaurant related
####################
class CreateRestaurantTestCase(TestCase):

    def setUp(self):
        self.tags = factories.RestaurantTagFactory.create_batch(10)

    def test_create_simple(self):
        restaurant = factories.RestaurantFactory()
        self.assertTrue(isinstance(restaurant, models.Restaurant))
        self.assertTrue(restaurant.payment_method_set.count() > 0)

    def test_create_with_tags(self):
        restaurant = factories.RestaurantFactory(tag_set=self.tags)
        self.assertTrue(isinstance(restaurant, models.Restaurant))
        self.assertEqual(restaurant.tag_set.count(), len(self.tags))
        self.assertTrue(restaurant.payment_method_set.count() > 0)


class CreateRestaurantTagTestCase(TestCase):

    def test_create(self):
        obj = factories.RestaurantTagFactory()
        self.assertTrue(isinstance(obj, models.RestaurantTag))


class CreateShowcaseImageTestCase(TestCase):

    def test_create(self):
        obj = factories.ShowcaseImageFactory()
        self.assertTrue(isinstance(obj, models.ShowcaseImage))


class CreateDeliveryPriceRangeTestCase(TestCase):

    def test_create(self):
        obj = factories.DeliveryPriceRangeFactory()
        self.assertTrue(isinstance(obj, models.DeliveryPriceRange))


class CreateOpeningTimeTestCase(TestCase):

    def setUp(self):
        self.hour_ranges = factories.HourRangeFactory.create_batch(3)

    def test_create_simple(self):
        obj = factories.OpeningTimeFactory()
        self.assertTrue(isinstance(obj, models.OpeningTime))


class CreateHourRangeTestCase(TestCase):

    def test_create(self):
        obj = factories.HourRangeFactory()
        self.assertTrue(isinstance(obj, models.HourRange))


class CreateMenuSectionTestCase(TestCase):

    def test_create(self):
        obj = factories.MenuSectionFactory()
        self.assertTrue(isinstance(obj, models.MenuSection))


class CreateMenuItemTestCase(TestCase):

    def test_create(self):
        obj = factories.MenuItemFactory()
        self.assertTrue(isinstance(obj, models.MenuItem))


class CreateDiscountTestCase(TestCase):

    def test_create(self):
        obj = factories.DiscountFactory()
        self.assertTrue(isinstance(obj, models.Discount))


class CreateCustomizationQuestionTestCase(TestCase):

    def test_create(self):
        obj = factories.CustomizationQuestionFactory()
        self.assertTrue(isinstance(obj, models.CustomizationQuestion))


class CreateCustomizationChoiceTestCase(TestCase):

    def test_create(self):
        obj = factories.CustomizationChoiceFactory()
        self.assertTrue(isinstance(obj, models.CustomizationChoice))


class CreateOrderTestCase(TestCase):

    def test_create(self):
        obj = factories.OrderFactory()
        self.assertTrue(isinstance(obj, models.Order))


class CreateOrderItemTestCase(TestCase):

    def setUp(self):
        self.customization_choices = factories.CustomizationChoiceFactory.create_batch(10)

    def test_create_simple(self):
        obj = factories.OrderItemFactory()
        self.assertTrue(isinstance(obj, models.OrderItem))

    def test_create_with_customization_choices(self):
        obj = factories.OrderItemFactory(customization_choice_set=self.customization_choices)
        self.assertTrue(isinstance(obj, models.OrderItem))
        self.assertEqual(obj.customization_choice_set.count(), len(self.customization_choices))


class CreateDeliveryTestCase(TestCase):

    def test_create(self):
        obj = factories.DeliveryFactory()
        self.assertTrue(isinstance(obj, models.Delivery))


class CreateTakeAwayTestCase(TestCase):

    def test_create(self):
        obj = factories.TakeAwayFactory()
        self.assertTrue(isinstance(obj, models.TakeAway))


##########################
# Courier related
##########################
class CreateCourierTestCase(TestCase):

    def test_create(self):
        obj = factories.CourierFactory()
        self.assertTrue(isinstance(obj, models.Courier))


#################
# Social related
#################
class CreatePostTestCase(TestCase):

    def setUp(self):
        self.tags = factories.PostTagFactory.create_batch(10)

    def test_create_simple(self):
        obj = factories.PostFactory()
        self.assertTrue(isinstance(obj, models.Post))

    def test_create_with_tags(self):
        post = factories.PostFactory(tag_set=self.tags)
        self.assertTrue(isinstance(post, models.Post))
        self.assertEqual(post.tag_set.count(), len(self.tags))


class CreatePostTagTestCase(TestCase):

    def test_create(self):
        obj = factories.PostTagFactory()
        self.assertTrue(isinstance(obj, models.PostTag))


class CreatePostReactionTestCase(TestCase):

    def test_create(self):
        obj = factories.PostReactionFactory()
        self.assertTrue(isinstance(obj, models.PostReaction))


class CreateMenuItemReviewTestCase(TestCase):

    def test_create(self):
        obj = factories.MenuItemReviewFactory()
        self.assertTrue(isinstance(obj, models.MenuItemReview))

    def test_create_with_menu_item(self):
        menu_item = factories.MenuItemFactory()
        obj = factories.MenuItemReviewFactory(menu_item=menu_item)
        self.assertTrue(isinstance(obj, models.MenuItemReview))


class CreateRestaurantReviewTestCase(TestCase):

    def test_create(self):
        obj = factories.RestaurantReviewFactory()
        self.assertTrue(isinstance(obj, models.RestaurantReview))


class CreateCourierReviewTestCase(TestCase):

    def test_create(self):
        obj = factories.CourierReviewFactory()
        self.assertTrue(isinstance(obj, models.CourierReview))


class CreateCashPaymentMethodTestCase(TestCase):

    def test_create(self):
        obj = factories.CashPaymentMethodFactory()
        self.assertTrue(isinstance(obj, models.CashPaymentMethod))


class CreateOrangeMoneyPaymentMethodTestCase(TestCase):

    def test_create(self):
        obj = factories.OrangeMoneyPaymentMethodFactory()
        self.assertTrue(isinstance(obj, models.OrangeMoneyPaymentMethod))


class CreateMTNMoMoPaymentMethodTestCase(TestCase):

    def test_create(self):
        obj = factories.MTNMoMoPaymentMethodFactory()
        self.assertTrue(isinstance(obj, models.MTNMoMoPaymentMethod))


class CreateExpressionUnionPaymentMethodTestCase(TestCase):

    def test_create(self):
        obj = factories.ExpressUnionPaymentMethodFactory()
        self.assertTrue(isinstance(obj, models.ExpressUnionPaymentMethod))


class CreateInvoiceTestCase(TestCase):

    def test_create(self):
        obj = factories.InvoiceFactory()
        self.assertTrue(isinstance(obj, models.Invoice))
