def scrape(begin_date, end_date):
    """
    This function is called by the `scrape_then_merge.py` file
    Input: Beginning Date and End Date for range to get data for
    Output: None
    Description: saves creates csvs for the USGS water stations in the San Joaquin Delta region
    """
    import pandas as pd
    from datetime import datetime
    from bs4 import BeautifulSoup
    from selenium import webdriver


    driver = webdriver.Chrome()
    main_url = 'https://nwis.waterdata.usgs.gov/ca/nwis/uv?cb_00010=on&cb_00010=on&cb_00300=on&cb_00300=on&cb_00400=on&cb_00480=on&cb_32295=on&cb_32316=on&cb_99133=on&format=html&site_no=11337190&period=&begin_date='

    # begin_date = '2017-10-01'
    # end_date = '2017-10-10'
    # Uncomment these lines to test

    full_url = main_url + begin_date + '&end_date=' + end_date

    driver.get(full_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    #####################
    # Scraping bit here #
    #####################
    table = soup.find('table', class_='dataListWithSuperscript').find('tbody').find_all('tr', class_='ui-widget-content even')
    table_as_list = []

    for row in table:
        rowlist = []
        for item in row:
            item_as_str = item.text.strip()
            if len(item_as_str) > 0:
                if item_as_str[-1] == 'P':
                    # P is appended to the end of each entry if the data is 'provisional data subject to revision'
                    rowlist.append(item.text.strip()[:-1])
                else:
                    rowlist.append(item.text.strip())
        #date time has the timezone being stripped from it and puts out date + time
        rowlist[0] = datetime.strptime(rowlist[0][:10], '%m/%d/%Y') 
        table_as_list.append(rowlist)

    ###################
    # pandas df stuff #
    ###################
    columns = ['datetime','temp_c','PH','DO','nitrate_mg/l','chlorophyll','flourescence','salinity']
    df = pd.DataFrame(table_as_list, columns=columns)
    for column in list(df.columns)[1:]:
        df[column] = df[column].astype(float)

    ###################
    # saving the file #
    ###################
    filename = begin_date + '.csv'
    df.groupby(['datetime']).mean().to_csv(filename, index=True)
    print(f'saved file as {filename}')