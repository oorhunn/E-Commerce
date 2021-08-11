import api_test
import iyzipay

payment_card = {
    'cardHolderName': 'John Doe',
    'cardNumber': '5528790000000008',
    'expireMonth': '12',
    'expireYear': '2030',
    'cvc': '123',
    'registerCard': '0'
}
buyer = {
    'id': 'BY789',
    'name': 'John',
    'surname': 'Doe',
    'gsmNumber': '+905350000000',
    'email': 'email@email.com',
    'identityNumber': '74300864791',
    'lastLoginDate': '2015-10-05 12:43:35',
    'registrationDate': '2013-04-21 15:12:09',
    'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'ip': '85.34.78.112',
    'city': 'Istanbul',
    'country': 'Turkey',
    'zipCode': '34732'
}
basket_items = [
    {
        'id': 'BI101',
        'name': 'Binocular',
        'category1': 'Collectibles',
        'category2': 'Accessories',
        'itemType': 'PHYSICAL',
        'price': '0.3'
    },
    {
        'id': 'BI102',
        'name': 'Game code',
        'category1': 'Game',
        'category2': 'Online Game Items',
        'itemType': 'VIRTUAL',
        'price': '0.5'
    },
    {
        'id': 'BI103',
        'name': 'Usb',
        'category1': 'Electronics',
        'category2': 'Usb / Cable',
        'itemType': 'PHYSICAL',
        'price': '0.2'
    }
]
address = {
    'contactName': 'Jane Doe',
    'city': 'Istanbul',
    'country': 'Turkey',
    'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'zipCode': '34732'
}


def create_payment(payment_card, buyer, address, basket_items):
    error = None
    options = {
        'api_key': iyzipay.api_key,
        'secret_key': iyzipay.secret_key,
        'base_url': iyzipay.base_url
    }
    if api_test.api_test() != 'success':
        error = 'Something went wrong with api test!!'
        return error
    totalPrice = 0.0
    for item in basket_items:
        totalPrice = totalPrice + float(item['price'])

    paidPrice = totalPrice + totalPrice*10/100
    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'price': totalPrice,
        'paidPrice': paidPrice,
        'currency': 'TRY',
        'installment': '1',
        'basketId': 'B67832',
        'paymentChannel': 'WEB',
        'paymentGroup': 'PRODUCT',
        'paymentCard': payment_card,
        'buyer': buyer,
        'shippingAddress': address,
        'billingAddress': address,
        'basketItems': basket_items
    }
    payment = iyzipay.Payment().create(request, options)
    return payment.read().decode('utf-8')


def cancel(): # not checked its functionality
    options = {
        'api_key': iyzipay.api_key,
        'secret_key': iyzipay.secret_key,
        'base_url': iyzipay.base_url
    }
    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'paymentId': '1',
        'ip': '85.34.78.112',
        'reason': 'other',
        'description': 'customer requested for default sample'
    }
    cancel = iyzipay.Cancel().create(request, options)

    return cancel.read().decode('utf-8')


def refund(): # not checked its functionality
    options = {
        'api_key': iyzipay.api_key,
        'secret_key': iyzipay.secret_key,
        'base_url': iyzipay.base_url
    }

    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'paymentTransactionId': '1',
        'price': '0.5',
        'currency': 'TRY',
        'ip': '85.34.78.112',
        'reason': 'other',
        'description': 'customer requested for default sample'
    }

    refunds = iyzipay.Refund().create(request, options)

    return refunds.read().decode('utf-8')
