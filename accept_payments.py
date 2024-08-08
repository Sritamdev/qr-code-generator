import qrcode
#taking upi id as a input
upi_id =input("enter ur upi id\n")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#defining the payment url based on the upi_id and the payment app 
#u can modify this urls based on the payment apps u want to support
phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr codes for each platform 
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#save the qr code to image file 
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#display the qr codes so u need to install the Pillow library
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show() 



