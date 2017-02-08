import csv
import os
try:
    import statistics
except:
    # error code instead
    import statistics_standin_for_py2 as statistics

from data_types import Purchase

def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    # print(data)
    query_data(data)


def print_header():
    print('-----------------------------')
    print('  REAL ESTATE DATA MINING APP')
    print('-----------------------------')
    print('')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder,'data','SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        return purchases
        # print(purchases[0].__dict__)
        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        # for row in reader:
        #     print (type(row), row)

def get_price(p):
    return p.price

def query_data(data):
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    high_purchase = data[-1]
    print("The most expensive house is ${:,} with {} beds and {} baths".format(high_purchase.price, high_purchase.beds, high_purchase.baths))
    # print(high_purchase.price)

    low_purchase = data[0]
    print("The least expensive house is ${:,} with {} beds and {} baths".format(low_purchase.price, low_purchase.beds, low_purchase.baths))
    # print(low_purchase.price)

    prices = [
        #projects or items
        p.price
            # the set to process
        for p in data
    ]
    ave_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(ave_price)))

    two_bed_homes = (
        p # projects or items
        for p in data
        if accounce(p,'2-bedrooms, found {}'.format(p.beds)) and p.beds == 2
        )
    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_price = statistics.mean((p.price for p in homes))
    ave_baths = statistics.mean((p.baths for p in homes))
    ave_sqft = statistics.mean((p.sq__ft for p in homes))
    print("The average price of a 2-bedroom home is ${:,}, baths={}, sq ft={:,}"
          .format(int(ave_price),round(ave_baths,1),round(ave_sqft,1)))


def accounce(item, msg):
    print("Pulling item {} for {}".format(item,msg))
    return item

if __name__ == '__main__':
    main()