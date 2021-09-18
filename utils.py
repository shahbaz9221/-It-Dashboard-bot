import csv

def write_agencytiles_into_csv(data):
    with open('Agencies.csv', mode='w') as csv_file:
        fieldnames = ['fiscalYear', 'agencycode', 'agencyName', 'totalSpendingCY']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for val in data['result']:
            writer.writerow({
                'fiscalYear': val['fiscalYear'],
                'agencycode': val['agencyCode'],
                'agencyName': val['agencyName'],
                'totalSpendingCY': val['totalSpendingCY']})


def write_individual_investment_into_csv(data):
    with open('Individual_investment.csv', mode='w') as csv_file:
        fieldnames = ['UII', 'agencycode', 'agencyAbbrev', 'bureauName','totalCySpending', 'InvestmentType',
                      'numberOfProjects', 'cioRating']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        writer.writeheader()
        for val in data['result']:
            writer.writerow({
                'UII': val['UII'],
                'agencycode': val['agencyCode'],
                'agencyAbbrev': val['agencyAbbrev'],
                'bureauName': val['bureauName'],
                'totalCySpending': val['totalCySpending'],
                'InvestmentType': val['investmentType'],
                'numberOfProjects': val['numberOfProjects'],
                'cioRating': val['cioRating']
                })
