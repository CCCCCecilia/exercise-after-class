def cal_profit(visitor):
    #calculate cost
    content_cost = 70_000
    other_cost = 30_000
    server_cost = 50_000
    cost = content_cost + other_cost + server_cost
    #calculate revenue
    subscriber = int(visitor / 10)
    subcription_fee = 15 * subscriber
    ad_revenue = 0.8 * visitor
    revenue = subcription_fee + ad_revenue
    #calculate profit
    profit = revenue - cost
    return profit