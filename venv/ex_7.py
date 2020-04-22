import json


with open('ex_7.txt','r') as f:
    companies_with_profit =[]
    average_profit = {}
    all_company_profit_info = 0
    how_much_comp_with_profit = 0
    for i in f:
        company_result = {}
        company_info_list = i.split('   ')

        if "\n" in company_info_list[3]:
            company_info_list[3] = company_info_list[3].replace("\n",'')

        if int(company_info_list[3]) > 0:
            profit_result = int(company_info_list[2]) - int(company_info_list[3])

        else:
            profit_result = int(company_info_list[2]) + int(company_info_list[3])

        if profit_result > 0:
            all_company_profit_info += profit_result

        company_result[company_info_list[0]] = profit_result
        if profit_result > 0:
            companies_with_profit.append(company_result)
            how_much_comp_with_profit += 1

    average_profit['average_profit'] = int(all_company_profit_info / how_much_comp_with_profit)
    companies_with_profit.append(average_profit)

with open('ex_7.json','w') as fi:
    data = json.dump(companies_with_profit,fi)

    print(companies_with_profit)