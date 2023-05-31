import streamlit as st
import requests

country_codes = {
    "UAE Dirham": "AED",
    "Afghan Afghani": "AFN",
    "Albanian Lek": "ALL",
    "Armenian Dram": "AMD",
    "Netherlands Antillian Guilder": "ANG",
    "Angolan Kwanza": "AOA",
    "Argentine Peso": "ARS",
    "Australian Dollar": "AUD",
    "Aruban Florin": "AWG",
    "Azerbaijani Manat": "AZN",
    "Bosnia and Herzegovina Convertible Mark": "BAM",
    "Barbados Dollar": "BBD",
    "Bangladeshi Taka": "BDT",
    "Bulgarian Lev": "BGN",
    "Bahraini Dinar": "BHD",
    "Burundian Franc": "BIF",
    "Bermudian Dollar": "BMD",
    "Brunei Dollar": "BND",
    "Bolivian Boliviano": "BOB",
    "Brazilian Real": "BRL",
    "Bahamian Dollar": "BSD",
    "Bhutanese Ngultrum": "BTN",
    "Botswana Pula": "BWP",
    "Belarusian Ruble": "BYN",
    "Belize Dollar": "BZD",
    "Canadian Dollar": "CAD",
    "Congolese Franc": "CDF",
    "Swiss Franc": "CHF",
    "Chilean Peso": "CLP",
    "Chinese Renminbi": "CNY",
    "Colombian Peso": "COP",
    "Costa Rican Colon": "CRC",
    "Cuban Peso": "CUP",
    "Cape Verdean Escudo": "CVE",
    "Czech Koruna": "CZK",
    "Djiboutian Franc": "DJF",
    "Danish Krone": "DKK",
    "Dominican Peso": "DOP",
    "Algerian Dinar": "DZD",
    "Egyptian Pound": "EGP",
    "Eritrean Nakfa": "ERN",
    "Ethiopian Birr": "ETB",
    "Euro": "EUR",
    "Fiji Dollar": "FJD",
    "Falkland Islands Pound": "FKP",
    "Faroese Króna": "FOK",
    "Pound Sterling": "GBP",
    "Georgian Lari": "GEL",
    "Guernsey Pound": "GGP",
    "Ghanaian Cedi": "GHS",
    "Gibraltar Pound": "GIP",
    "Gambian Dalasi": "GMD",
    "Guinean Franc": "GNF",
    "Guatemalan Quetzal": "GTQ",
    "Guyanese Dollar": "GYD",
    "Hong Kong Dollar": "HKD",
    "Honduran Lempira": "HNL",
    "Croatian Kuna": "HRK",
    "Haitian Gourde": "HTG",
    "Hungarian Forint": "HUF",
    "Indonesian Rupiah": "IDR",
    "Israeli New Shekel": "ILS",
    "Manx Pound": "IMP",
    "Indian Rupee": "INR",
    "Iraqi Dinar": "IQD",
    "Iranian Rial": "IRR",
    "Icelandic Króna": "ISK",
    "Jersey Pound": "JEP",
    "Jamaican Dollar": "JMD",
    "Jordanian Dinar": "JOD",
    "Japanese Yen": "JPY",
    "Kenyan Shilling": "KES",
    "Kyrgyzstani Som": "KGS",
    "Cambodian Riel": "KHR",
    "Kiribati Dollar": "KID",
    "Comorian Franc": "KMF",
    "South Korean Won": "KRW",
    "Kuwaiti Dinar": "KWD",
    "Cayman Islands Dollar": "KYD",
    "Kazakhstani Tenge": "KZT",
    "Lao Kip": "LAK",
    "Lebanese Pound": "LBP",
    "Sri Lanka Rupee": "LKR",
    "Liberian Dollar": "LRD",
    "Lesotho Loti": "LSL",
    "Libyan Dinar": "LYD",
    "Moroccan Dirham": "MAD",
    "Moldovan Leu": "MDL",
    "Malagasy Ariary": "MGA",
    "Macedonian Denar": "MKD",
    "Burmese Kyat": "MMK",
    "Mongolian Tögrög": "MNT",
    "Macanese Pataca": "MOP",
    "Mauritanian Ouguiya": "MRU",
    "Mauritian Rupee": "MUR",
    "Maldivian Rufiyaa": "MVR",
    "Malawian Kwacha": "MWK",
    "Mexican Peso": "MXN",
    "Malaysian Ringgit": "MYR",
    "Mozambican Metical": "MZN",
    "Namibian Dollar": "NAD",
    "Nigerian Naira": "NGN",
    "Nicaraguan Córdoba": "NIO",
    "Norwegian Krone": "NOK",
    "Nepalese Rupee": "NPR",
    "New Zealand Dollar": "NZD",
    "Omani Rial": "OMR",
    "Panamanian Balboa": "PAB",
    "Peruvian Sol": "PEN",
    "Papua New Guinean Kina": "PGK",
    "Philippine Peso": "PHP",
    "Pakistani Rupee": "PKR",
    "Polish Złoty": "PLN",
    "Paraguayan Guaraní": "PYG",
    "Qatari Riyal": "QAR",
    "Romanian Leu": "RON",
    "Serbian Dinar": "RSD",
    "Russian Ruble": "RUB",
    "Rwandan Franc": "RWF",
    "Saudi Riyal": "SAR",
    "Solomon Islands Dollar": "SBD",
    "Seychellois Rupee": "SCR",
    "Sudanese Pound": "SDG",
    "Swedish Krona": "SEK",
    "Singapore Dollar": "SGD",
    "Saint Helena Pound": "SHP",
    "Sierra Leonean Leone": "SLL",
    "Somali Shilling": "SOS",
    "Surinamese Dollar": "SRD",
    "South Sudanese Pound": "SSP",
    "São Tomé and Príncipe Dobra": "STN",
    "Syrian Pound": "SYP",
    "Eswatini Lilangeni": "SZL",
    "Thai Baht": "THB",
    "Tajikistani Somoni": "TJS",
    "Turkmenistan Manat": "TMT",
    "Tunisian Dinar": "TND",
    "Tongan Paʻanga": "TOP",
    "Turkish Lira": "TRY",
    "Trinidad and Tobago Dollar": "TTD",
    "Tuvaluan Dollar": "TVD",
    "New Taiwan Dollar": "TWD",
    "Tanzanian Shilling": "TZS",
    "Ukrainian Hryvnia": "UAH",
    "Ugandan Shilling": "UGX",
    "United States Dollar": "USD",
    "Uruguayan Peso": "UYU",
    "Uzbekistani So'm": "UZS",
    "Venezuelan Bolívar Soberano": "VES",
    "Vietnamese Đồng": "VND",
    "Vanuatu Vatu": "VUV",
    "Samoan Tālā": "WST",
    "Central African CFA Franc": "XAF",
    "East Caribbean Dollar": "XCD",
    "Special Drawing Rights": "XDR",
    "West African CFA franc": "XOF",
    "CFP Franc": "XPF",
    "Yemeni Rial": "YER",
    "South African Rand": "ZAR",
    "Zambian Kwacha": "ZMW",
    "Zimbabwean Dollar": "ZWL",
}

countryList = sorted(list(country_codes.keys()))


def converter():
    st.header('Currency Converter application')
    fromCode = st.selectbox('From : ', countryList)
    toCodesList = countryList.copy()
    toCodesList.remove(fromCode)

    toCode = st.selectbox('To :', toCodesList)
    amount = st.number_input('Enter amount in '+fromCode + ' :')

    if st.button('Convert'):
        # url = https://api.exchangerate-api.com/v4/latest/
        # url =  f'https://v6.exchangerate-api.com/v6/f999688a223170137c71e110/pair/{country_codes[fromCode]}/{country_codes[toCode]}/{amount}'
        url = f'https://api.exchangerate-api.com/v4/latest/{country_codes[fromCode]}'
        response = requests.get(url).json()
        rate = response['rates'][f'{country_codes[toCode]}']
        result = amount*round(rate, 2)
        st.header('Result:')
        st.header(f'{amount} {country_codes[fromCode]} = {result} {country_codes[toCode]}')


def predictor():
    st.write('predictor app is under processing.')
    pass


def main():
    st.sidebar.header('Currency Converter and Rate Predictor App')
    opt = st.sidebar.selectbox('Select an option: ', ['Converter', 'Prediction'])
    if opt == 'Converter':
        converter()
    elif opt == 'Prediction':
        predictor()
    else:
        st.write('please select an option from sidebar.')


# if __name__ == '__main__':
#     main()

main()
