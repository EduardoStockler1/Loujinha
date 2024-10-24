def checkStock(QuantityInStoke, MininumStoke, StokeInfo):
    if QuantityInStoke <= MininumStoke:
            StokeInfo = 1
            return StokeInfo
def demandForecast(nextDemand, lastDemand, infoActualItem ,seasonalFactor, periodsNumbers):
    nextDemand = (lastDemand + (infoActualItem / seasonalFactor))/periodsNumbers
    return nextDemand
def sells(product, productStoke, quantityBuyed):
    return productStoke-quantityBuyed
