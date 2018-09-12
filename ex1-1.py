def cal_profit(visitor):
    #calculate cosr
    content_cost = 70_000
    labor_cost = 30_000
    server_cost = 50_000
    cost = centent_cost + labor_cost + server_cost
    #calculate revenue
    sub_number =int(visitor / 10)
    subcription_fee = 15 * sub_number
    ad_revenue = 0.8 * sub_number
    revenue = subcription_fee + ad_revenue
    #calculate profit
    profit = revenue - cost
    return profit