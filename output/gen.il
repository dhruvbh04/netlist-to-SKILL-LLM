cv = dbOpenCellViewByType("genLib" "autoCell" "schematic" "" "w")
inst_M1 = dbCreateInst(cv "analogLib" "nmos" "symbol" 0:0 "R0")
inst_M1~>W = "1u"
inst_M1~>L = "180n"
inst_R1 = dbCreateInst(cv "analogLib" "res" "symbol" 10:0 "R0")
inst_R1~>resistance = "10k"
inst_C1 = dbCreateInst(cv "analogLib" "cap" "symbol" 20:0 "R0")
inst_C1~>capacitance = "2p"
net_0 = dbCreateNet(cv "0")
net_vdd = dbCreateNet(cv "vdd")
net_in = dbCreateNet(cv "in")
net_out = dbCreateNet(cv "out")
dbCreateInstTerm(inst_M1 net_out "D")
dbCreateInstTerm(inst_M1 net_in "G")
dbCreateInstTerm(inst_M1 net_0 "S")
dbCreateInstTerm(inst_M1 net_0 "B")
dbCreateInstTerm(inst_R1 net_vdd "PLUS")
dbCreateInstTerm(inst_R1 net_out "MINUS")
dbCreateInstTerm(inst_C1 net_out "PLUS")
dbCreateInstTerm(inst_C1 net_0 "MINUS")