from django.urls import path 
from .views import SearchCustomer, account_profile, card_profile, edit_account,customer_profile,edit_customer, edit_card, edit_receipts, edit_transaction, edit_wallet, home_page, list_accounts, list_card, list_loan, list_receipts, list_reward, list_thirdparty, list_transaction, list_wallet, notification_list, receipt_profile, register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet,transaction_profile, wallet_profile

urlpatterns=[
    #deposit api


    path("",home_page,name='home'),
    # path("customers/",list_customers,name='all_customers'),
    path("customers_get/",SearchCustomer.as_view(),name='all_customers'),
    path("customers/<int:id>/",customer_profile,name="customerProfile"),
    path("customers/edit/<int:id>/",edit_customer,name="edit_customer"),
    # path('customers/<int:id>/',CustomerProfile.as_view(),name="edit_customer"),
    path("registercust/",register_customer,name='registration'),


    path("register_account/",register_account,name='account'),
    path("accounts/",list_accounts,name='all_accounts'),
    path("accounts/<int:id>/",account_profile,name="accountProfile"),
    path("accounts/edit/<int:id>/",edit_account,name="edit_account"),


    path("register_wallet/",register_wallet,name='wallet'),
    path("wallets/",list_wallet,name='all_wallets'),
    path("wallets/<int:id>/",wallet_profile,name="walletProfile"),
    path("wallets/edit/<int:id>/",edit_wallet,name="edit_wallet"),


    path("register_transaction/",register_transaction,name='Transaction'),
    path("transactions/",list_transaction,name='all_transactions'),
    path("transactions/<int:id>/",transaction_profile,name="transactionProfile"),
    path("transactions/edit/<int:id>/",edit_transaction,name="edit_transaction"),




    path('card/',register_card,name="card"),
    path("cards/",list_card,name='all_cards'),
    path("cards/<int:id>/",card_profile,name="cardProfile"),
    path("cards/edit/<int:id>/",edit_card,name="edit_card"),


    path('thirdp/',register_thirdparty,name='thirdparty'),
    path('thirdpartys/',list_thirdparty,name='all_thirdpartys'),

    path('notification/',register_notification,name='notification'),
    path('notifications/',notification_list,name='all_notifications'),



    path('loan/',register_loan,name='loan'),
    path('loans/',list_loan,name='all_loans'),

    path('receipt/',register_receipt,name='receipt'),
    path('receipts/',list_receipts,name='all_receipts'),
    path("receipts/<int:id>/",receipt_profile,name="receiptProfile"),
    path("receipts/edit/<int:id>/",edit_receipts,name="edit_receipt"),



    path('reward/',register_reward,name='reward'),
    path('rewards/',list_reward,name='all_rewards'),


    
        


    
]
