import sys
args = sys.argv

totalfee = int(args[1])
border_fee =1000000

def sansyutsu (get):
    if get > border_fee :
        tax_fee_under_border = border_fee * 0.1
        fee_over_border = get - border_fee
        tax_fee_over_border = fee_over_border * 0.2
        total_tax = totalfee - tax_fee_under_border - tax_fee_over_border
        return int(total_tax)
    else:
        total_tax = totalfee * 0.9
        return int(total_tax)

tax = totalfee - sansyutsu(totalfee)
sikyu  =sansyutsu(totalfee)
print("支給額:"+ str(sikyu) + "、税額:" + str(tax) ,end="")

