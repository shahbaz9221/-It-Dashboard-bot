# +
import os
path = os.getcwd() + '\chrome_driver\chromedriver.exe'

start_url_of_Itdashboard = ['https://itdashboard.gov/']
it_dash_board_string_url = 'https://itdashboard.gov/'

start_url_of_individual_investment = ['https://itdashboard.gov/drupal/summary/005']
individual_investment_string_url = 'https://itdashboard.gov/drupal/summary/005'

chrome_driver_path = path

agency_tiles_url = 'https://itdashboard.gov/api/v1/ITDB2/visualization/govwide/agencyTiles'
Investment_table_url = 'https://itdashboard.gov/api/v1/ITDB2/visualization/agency/investmentsTable/agencyCode/005'


headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Cookie": "SSESS04ae24068a2b6b9bb1975f7ad3e4d1c2=6jlUkWTvKqGui1azMl8iQZw32XCryACAIvDn01u-MOM; has_js=1; wstact=d00da1a01ad1162f15f32f06bf9d82fff2a18cc966e10de10c52cc084f7cc3bf",
                "Referer": "https://itdashboard.gov/",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
}




# -


