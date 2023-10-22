from hotels.hotels import Hotels

try:
    with Hotels() as bot:
        bot.landFirstPage()
        bot.cancelCommercial()
        bot.changeCurrency()
        bot.destinationPlace()
        bot.tripDates()
        bot.numberOfTravelers()
        bot.searchButton()
        bot.hotelLevelFiltering()
        bot.filterPrice()
        hotel_data = bot.filterHotelDetails()
        bot.writeToExcel(hotel_data)




except Exception as e:
    print("Run failed",e)
